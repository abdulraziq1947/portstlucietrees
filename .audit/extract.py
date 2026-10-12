#!/usr/bin/env python3
"""Extract SEO structure from saved Weebly HTML."""
import os, re, json
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

DIR = os.path.join(os.path.dirname(__file__), "html")
BASE = "https://www.portstlucietrees.com/"

SKIP = {"script", "style", "noscript"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # list of (tag, flags)
        self.skip = 0
        self.in_title = False
        self.title = []
        self.metas = []
        self.canonical = None
        self.alternates = []
        self.headings = []
        self.hbuf = None
        self.links = []
        self.abuf = None
        self.images = []
        self.forms = []
        self.form = None
        self.regions = []  # current region names
        self.text_parts = []
        self.jsonld = []
        self.ld = False
        self.ldbuf = []
        self.paragraphs = []
        self.pbuf = None
        self.labels = []
        self.lbuf = None

    def _flags(self, tag, ad):
        cls = ad.get("class") or ""
        ident = ad.get("id") or ""
        flags = set()
        blob = f"{cls} {ident}"
        if ident == "wsite-content" or "wsite-header-elements" in cls:
            flags.add("header" if "header" in cls else "content")
        if ident == "wsite-content":
            flags.add("content")
        if "wsite-footer" in cls or "footer-wrap" in cls:
            flags.add("footer")
        if "topbar" in cls or ident == "topBar":
            flags.add("topbar")
        if tag == "nav" or "wsite-menu" in cls or "nav" in ident.lower():
            flags.add("nav")
        return flags

    def _region(self):
        regs = set()
        for _, flags in self.stack:
            regs |= flags
        return regs

    def handle_starttag(self, tag, attrs):
        ad = {k: (v or "") for k, v in attrs}
        if tag in SKIP:
            self.skip += 1
            if tag == "script" and "ld+json" in ad.get("type", "").lower():
                self.ld = True
                self.ldbuf = []
            self.stack.append((tag, set()))
            return
        flags = self._flags(tag, ad)
        self.stack.append((tag, flags))
        if tag == "title":
            self.in_title = True
            return
        if tag == "meta":
            name = (ad.get("name") or ad.get("property") or ad.get("http-equiv") or "").lower()
            self.metas.append({"name": name, "content": ad.get("content", "")})
            return
        if tag == "link":
            rel = ad.get("rel", "").lower().split()
            if "canonical" in rel:
                self.canonical = ad.get("href")
            if "alternate" in rel:
                self.alternates.append({"hreflang": ad.get("hreflang"), "href": ad.get("href")})
            return
        if tag == "img":
            self.images.append({
                "src": ad.get("src"),
                "alt": ad.get("alt"),
                "region": sorted(self._region()),
            })
            return
        if tag == "a":
            self.abuf = {"href": ad.get("href"), "text": [], "region": set(self._region())}
            return
        if tag in ("h1", "h2", "h3", "h4"):
            self.hbuf = {"tag": tag, "text": [], "region": set(self._region()), "class": ad.get("class", "")}
            return
        if tag == "form":
            self.form = {
                "action": ad.get("action"),
                "method": (ad.get("method") or "get").lower(),
                "id": ad.get("id"),
                "fields": [],
                "region": sorted(self._region()),
            }
            return
        if tag in ("input", "textarea", "select") and self.form is not None:
            self.form["fields"].append({
                "tag": tag,
                "type": ad.get("type"),
                "name": ad.get("name"),
                "placeholder": ad.get("placeholder"),
                "required": "required" in ad,
            })
        if tag == "label":
            self.lbuf = []
        if tag == "p" or (tag == "div" and "paragraph" in (ad.get("class") or "")):
            self.pbuf = []

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        elif self.stack:
            # pop until matching if present
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    self.stack = self.stack[:i]
                    break
        if tag in SKIP:
            if self.skip:
                self.skip -= 1
            if tag == "script" and self.ld:
                self.jsonld.append("".join(self.ldbuf).strip())
                self.ld = False
            return
        if tag == "title":
            self.in_title = False
        if tag == "a" and self.abuf is not None:
            text = re.sub(r"\s+", " ", "".join(self.abuf["text"])).strip()
            self.links.append({
                "href": self.abuf["href"],
                "text": text,
                "region": sorted(self.abuf["region"]),
            })
            self.abuf = None
        if tag in ("h1", "h2", "h3", "h4") and self.hbuf is not None:
            text = re.sub(r"\s+", " ", "".join(self.hbuf["text"])).strip()
            self.hbuf["text"] = text
            self.hbuf["region"] = sorted(self.hbuf["region"])
            self.headings.append(self.hbuf)
            self.hbuf = None
        if tag == "form" and self.form is not None:
            self.forms.append(self.form)
            self.form = None
        if tag == "label" and self.lbuf is not None:
            lab = re.sub(r"\s+", " ", "".join(self.lbuf)).strip()
            if lab:
                self.labels.append(lab)
            self.lbuf = None
        if tag in ("p", "div") and self.pbuf is not None:
            text = re.sub(r"\s+", " ", "".join(self.pbuf)).strip()
            if text and len(text) > 40:
                self.paragraphs.append(text)
            self.pbuf = None

    def handle_data(self, data):
        if self.skip:
            if self.ld:
                self.ldbuf.append(data)
            return
        if self.in_title:
            self.title.append(data)
        if self.hbuf is not None:
            self.hbuf["text"].append(data)
        if self.abuf is not None:
            self.abuf["text"].append(data)
        if self.lbuf is not None:
            self.lbuf.append(data)
        if self.pbuf is not None:
            self.pbuf.append(data)
        if data.strip():
            self.text_parts.append(data)


def norm_href(href):
    if not href:
        return None
    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:", "#")):
        return href
    absu = urljoin(BASE, href)
    p = urlparse(absu)
    host = (p.netloc or "").lower()
    if host in ("www.portstlucietrees.com", "portstlucietrees.com", ""):
        path = p.path or "/"
        if path != "/" and path.endswith("/"):
            path = path[:-1]
        return path + (("?" + p.query) if p.query else "")
    return absu


def main():
    out = {}
    for name in sorted(os.listdir(DIR)):
        if not name.endswith(".html"):
            continue
        raw = open(os.path.join(DIR, name), encoding="utf-8", errors="replace").read()
        p = Extractor()
        p.feed(raw)
        title = re.sub(r"\s+", " ", "".join(p.title)).strip()
        meta = {m["name"]: m["content"] for m in p.metas if m["name"] in ("description", "keywords", "robots")}
        og = {}
        for m in p.metas:
            if m["name"].startswith("og:"):
                og.setdefault(m["name"], []).append(m["content"])
        visible = re.sub(r"\s+", " ", " ".join(p.text_parts)).strip()
        words = re.findall(r"[A-Za-z0-9']+", visible)
        internal = []
        external = []
        special = []
        for link in p.links:
            n = norm_href(link["href"])
            rec = {"href": link["href"], "norm": n, "text": link["text"], "region": link["region"]}
            if not n:
                continue
            if n.startswith(("mailto:", "tel:", "#", "javascript:")):
                special.append(rec)
            elif n.startswith("http"):
                external.append(rec)
            else:
                internal.append(rec)
        phones = sorted(set(re.findall(r"(?:\+?1[\s.-]?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}", visible)))
        emails = sorted(set(re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", visible, re.I)))
        out[name] = {
            "title": title,
            "title_len": len(title),
            "description": meta.get("description"),
            "description_len": len(meta.get("description") or ""),
            "keywords": meta.get("keywords"),
            "robots": meta.get("robots"),
            "canonical": p.canonical,
            "alternates": p.alternates,
            "og": og,
            "jsonld": p.jsonld,
            "headings": p.headings,
            "images": [{"src": i["src"], "alt": i["alt"]} for i in p.images],
            "forms": p.forms,
            "labels": p.labels,
            "internal_links": internal,
            "external_links": external,
            "special_links": special,
            "paragraphs": p.paragraphs,
            "word_count": len(words),
            "phones": phones,
            "emails": emails,
        }
        print(f"{name}: title={title[:60]!r} words={len(words)} h={[h['tag']+':'+h['text'][:40] for h in p.headings]} links={len(internal)} imgs={len(p.images)} forms={len(p.forms)}")

    path = os.path.join(os.path.dirname(__file__), "seo.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", path)


if __name__ == "__main__":
    main()
