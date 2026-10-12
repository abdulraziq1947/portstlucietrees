#!/usr/bin/env python3
"""Build the static Port St Lucie Tree Service site from the audited HTML."""

import json
import re
from html import escape, unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / ".audit" / "html"
SEO = json.loads((ROOT / ".audit" / "seo.json").read_text())

BASE = "https://www.portstlucietrees.com"
PHONE = "772-492-4436"
TEL = "tel:7724924436"
BUSINESS = "Port St Lucie Tree Service"
SITE_NAME = "Tree Service Port St Lucie"

SERVICES = [
    ("tree-removal.html", "Tree Removal"),
    ("stump-removal.html", "Stump Removal"),
    ("commercial-tree-service.html", "Commercial Tree Service"),
    ("tree-care-prevention.html", "Tree Care Prevention"),
    ("brush-cleaning.html", "Brush Cleaning"),
    ("storm-damage-clean-up.html", "Storm Damage Clean Up"),
]
SERVICE_URL = {name: href for href, name in SERVICES}

PLACES = [
    ("port-st-lucie-flordia.html", "Port St Lucie, FL"),
    ("stuart-flordia.html", "Stuart, FL"),
    ("palm-city-florida.html", "Palm City, FL"),
    ("fort-pierce-florida.html", "Fort Pierce, FL"),
    ("florida-ridge-fl.html", "Florida Ridge, FL"),
    ("hobo-sound-fl.html", "Hobe Sound, FL"),
    ("vero-beach-florida.html", "Vero Beach, FL"),
    ("jupiter-florida.html", "Jupiter, FL"),
    ("palm-beach-gardens-florida.html", "Palm Beach Gardens, FL"),
    (None, "North Palm Beach, FL"),
    ("sebastian-florida.html", "Sebastian, FL"),
    (None, "Lake Park, FL"),
    ("riviera-beach-fl.html", "Riviera Beach, FL"),
    ("royal-palm-beach-florida.html", "Royal Palm Beach, FL"),
    ("mico-florida.html", "Mico, FL"),
]
PLACE_LOOKUP = {re.sub(r"\s+", " ", name).strip().lower(): href for href, name in PLACES}

NEIGHBORHOODS = [
    ("portstluciecarlton.html", "Port St Lucie - Carlton"),
    ("se-morningside-blvd.html", "SE PORT ST LUCIE BLVD & SE MORNINGSIDE BLVD"),
]

PAGES = [
    "index.html",
    "about.html",
    "services.html",
    "contact.html",
    "tree-removal.html",
    "stump-removal.html",
    "commercial-tree-service.html",
    "tree-care-prevention.html",
    "brush-cleaning.html",
    "storm-damage-clean-up.html",
    "locations-port-st-lucie.html",
    "neighborhoods.html",
    "royal-palm-beach-florida.html",
    "fort-pierce-florida.html",
    "palm-city-florida.html",
    "riviera-beach-fl.html",
    "se-morningside-blvd.html",
    "port-st-lucie-flordia.html",
    "florida-ridge-fl.html",
    "portstluciecarlton.html",
    "mico-florida.html",
    "stuart-flordia.html",
    "vero-beach-florida.html",
    "sebastian-florida.html",
    "jupiter-florida.html",
    "hobo-sound-fl.html",
    "palm-beach-gardens-florida.html",
]

JUNK = {
    "* indicates required field",
    "name *",
    "first",
    "last",
    "phone number *",
    "email *",
    "comment *",
    "submit",
}

# Photos downloaded from the live site. Alt text matches the live page
# except the quote graphic, whose live alt was the generic word "Picture".
LOGO = (
    "/images/live/editor/tree-removal-pros-port-st-lucie-home.jpg",
    "tree care service logo",
    298,
    340,
)
HERO_PHOTO = "/images/live/background-images/209300239.jpg"
TREES_PHOTO = "/images/live/background-images/1436807259.jpg"
HOME_PHOTOS = {
    "Tree Removal": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-removal-1_orig.jpg",
        "tree removal in progress",
        1067,
        800,
    ),
    "Stump Removal": (
        "/images/live/tree-removal-pros-port-st-lucie-stump-removal-1_orig.jpg",
        "tree stump got removed",
        1100,
        733,
    ),
    "Commercial Tree Service": (
        "/images/live/tree-removal-pros-port-st-lucie-commercial-tree-service-1_orig.jpg",
        "commercial tree service worker working",
        1059,
        800,
    ),
    "Tree Care Prevention": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-care-prevention-1_orig.jpg",
        "tree care service in progress",
        1100,
        733,
    ),
    "Brush Cleaning": (
        "/images/live/tree-removal-pros-port-st-lucie-brush-cleaning-1_orig.jpg",
        "tree care worker working on brush cleaning",
        1100,
        728,
    ),
    "Storm Damage Clean Up": (
        "/images/live/tree-removal-pros-port-st-lucie-storm-damage-clean-up-1_orig.jpg",
        "tree fallen on car after storm",
        1100,
        733,
    ),
}
PAGE_PHOTOS = {
    "about.html": (
        "/images/live/tree-removal-pros-port-st-lucie-about_orig.jpg",
        "tree care expert during work",
        1100,
        734,
    ),
    "services.html": (
        "/images/live/tree-removal-pros-port-st-lucie-services_orig.jpg",
        "tree logs after removal",
        1100,
        733,
    ),
    "contact.html": (
        "/images/live/tree-removal-pros-port-st-lucie-contact_orig.jpg",
        "woman smiling taking phone call",
        1100,
        733,
    ),
    "tree-removal.html": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-removal-2_orig.jpg",
        "tree removal in progress",
        1100,
        731,
    ),
    "stump-removal.html": (
        "/images/live/tree-removal-pros-port-st-lucie-stump-removal-2_orig.jpg",
        "stump left behind after tree got removed",
        1067,
        800,
    ),
    "commercial-tree-service.html": (
        "/images/live/tree-removal-pros-port-st-lucie-commercial-tree-service-2_orig.jpg",
        "tree care expert during work",
        1057,
        800,
    ),
    "tree-care-prevention.html": (
        "/images/live/tree-removal-pros-port-st-lucie-tree-care-prevention-2_orig.jpg",
        "tree care expert working on planting tree",
        1100,
        733,
    ),
    "brush-cleaning.html": (
        "/images/live/tree-removal-pros-port-st-lucie-brush-cleaning-2_orig.jpg",
        "tree care expert working on brush cleaning",
        1011,
        800,
    ),
    "storm-damage-clean-up.html": (
        "/images/live/tree-removal-pros-port-st-lucie-storm-damage-clean-up-2_orig.jpg",
        "tree damaged after storm",
        1100,
        736,
    ),
    "florida-ridge-fl.html": ("/images/live/flordia-ridge-tree-service_orig.jpg", "Picture", 331, 359),
    "fort-pierce-florida.html": ("/images/live/fort-pierce-fl-tree-service_orig.jpg", "Picture", 278, 326),
    "hobo-sound-fl.html": ("/images/live/hobe-sound-fl-tree-service_orig.jpg", "Picture", 310, 448),
    "jupiter-florida.html": ("/images/live/tree-service-jupiter-fl_orig.jpg", "Picture", 281, 285),
    "mico-florida.html": ("/images/live/tree-service-mico-fl_orig.jpg", "Picture", 258, 340),
    "palm-beach-gardens-florida.html": ("/images/live/palm-beach-gardens-tree-service_orig.jpg", "Picture", 265, 206),
    "palm-city-florida.html": ("/images/live/published/palm-city-fl-tree-service.jpg", "Picture", 413, 394),
    "port-st-lucie-flordia.html": ("/images/live/port-st-lucie_orig.jpg", "Picture", 300, 368),
    "riviera-beach-fl.html": ("/images/live/published/riviera-beach-fl-tree-service.jpg", "Picture", 252, 339),
    "royal-palm-beach-florida.html": ("/images/live/tree-service-mico-fl_1.jpg", "Picture", 258, 340),
    "sebastian-florida.html": ("/images/live/tree-service-sebastian-fl_orig.jpg", "Picture", 324, 484),
    "stuart-flordia.html": ("/images/live/concrete-contractors-stuart-fl_orig.jpg", "Picture", 305, 498),
    "vero-beach-florida.html": ("/images/live/published/tree-service-vero-beach-fl.jpg", "Picture", 296, 250),
}


def clean_text(fragment):
    fragment = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = unescape(fragment).replace("\xa0", " ")
    return re.sub(r"\s+", " ", fragment).strip()


def is_junk(text):
    lowered = text.lower().strip()
    return lowered in JUNK or lowered.startswith("* indicates required")


def inline_html(fragment):
    holders = []

    def repl(match):
        href = unescape(match.group(1)).strip()
        text = clean_text(match.group(2))
        if not text:
            return ""
        internal = href.startswith("/") and "://" not in href
        if href.startswith("tel:") or internal:
            if href in ("/index.html", "/"):
                href = "/"
            token = f"\x00A{len(holders)}\x00"
            holders.append(f'<a href="{escape(href, quote=True)}">{escape(text)}</a>')
            return token
        return text

    fragment = re.sub(
        r'<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        repl,
        fragment,
        flags=re.S | re.I,
    )
    fragment = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = unescape(fragment).replace("\xa0", " ")
    fragment = re.sub(r"[ \t]+", " ", fragment)
    fragment = re.sub(r"\s+", " ", fragment).strip()
    for index, html in enumerate(holders):
        fragment = fragment.replace(f"\x00A{index}\x00", html)
    return fragment


def paragraph_blocks(inner):
    blocks = []
    parts = re.split(r"(<ul[\s\S]*?</ul>)", inner, flags=re.I)
    for part in parts:
        if part.lower().startswith("<ul"):
            items = []
            for item in re.findall(r"<li[^>]*>(.*?)</li>", part, flags=re.S | re.I):
                text = clean_text(item)
                if text:
                    items.append(text)
            if items:
                blocks.append(("ul", items))
            continue
        pieces = re.split(r"<strong>(.*?)</strong>", part, flags=re.S | re.I)
        for index, piece in enumerate(pieces):
            if index % 2 == 1:
                title = clean_text(piece)
                if title and not is_junk(title):
                    blocks.append(("h2", title))
                continue
            html = inline_html(piece)
            plain = re.sub(r"<[^>]+>", "", html).strip()
            if html and not is_junk(plain):
                blocks.append(("p", html))
    return blocks


def extract(filename):
    raw = (AUDIT / filename).read_text(encoding="utf-8", errors="replace")
    match = re.search(r'id="wsite-content"(.*?)(?=<div class="footer-wrap">)', raw, re.S)
    if not match:
        raise SystemExit(f"No content region in {filename}")
    chunk = re.sub(r"<script[\s\S]*?</script>", "", match.group(1), flags=re.I)
    chunk = re.sub(r"<style[\s\S]*?</style>", "", chunk, flags=re.I)
    h1 = None
    blocks = []
    pattern = re.compile(
        r"<h1[^>]*>(.*?)</h1>|<h2[^>]*>(.*?)</h2>|<div class=\"paragraph\"[^>]*>(.*?)</div>",
        re.S | re.I,
    )
    for found in pattern.finditer(chunk):
        if found.group(1) is not None:
            h1 = clean_text(found.group(1)) or h1
        elif found.group(2) is not None:
            title = clean_text(found.group(2))
            if title:
                blocks.append(("h2", title))
        else:
            blocks.extend(paragraph_blocks(found.group(3)))
    if not h1:
        for index, (kind, value) in enumerate(blocks):
            if kind == "h2":
                h1 = value
                del blocks[index]
                break
    return {"h1": h1, "blocks": blocks}


def render_ul(items):
    lis = []
    for item in items:
        key = re.sub(r"\s+", " ", item).strip().lower()
        href = PLACE_LOOKUP.get(key)
        if href:
            lis.append(f'<li><a href="/{href}">{escape(item)}</a></li>')
        else:
            lis.append(f"<li>{escape(item)}</li>")
    return '<ul class="place-list">' + "".join(lis) + "</ul>"


def render_blocks(blocks):
    html = []
    for kind, value in blocks:
        if kind == "h2":
            html.append(f"<h2>{escape(value)}</h2>")
        elif kind == "p":
            html.append(f"<p>{value}</p>")
        elif kind == "ul":
            html.append(render_ul(value))
    return "\n".join(html)


def canon(filename):
    if filename == "index.html":
        return BASE + "/"
    return f"{BASE}/{filename}"


def description_for(filename, extracted):
    seo = SEO[filename]
    if seo.get("description"):
        return re.sub(r"\s+", " ", seo["description"]).strip()
    for kind, value in extracted["blocks"]:
        if kind == "p":
            plain = re.sub(r"<[^>]+>", "", value)
            plain = re.sub(r"\s+", " ", plain).strip()
            if len(plain) <= 165:
                return plain
            cut = plain[:157]
            if " " in cut:
                cut = cut.rsplit(" ", 1)[0]
            return cut.rstrip(".,;:") + "."
    og = (seo.get("og") or {}).get("og:description") or [None]
    return og[0]


def picture(src, alt, width, height, lazy=True, cls=""):
    loading = "lazy" if lazy else "eager"
    class_attr = f' class="{cls}"' if cls else ""
    return (
        f'<img src="{src}" alt="{escape(alt, quote=True)}" width="{width}" height="{height}"'
        f'{class_attr} loading="{loading}" decoding="async">'
    )


def page_figure(filename):
    photo = PAGE_PHOTOS.get(filename)
    if not photo:
        return ""
    src, alt, width, height = photo
    return f'<figure class="page-photo">{picture(src, alt, width, height)}</figure>'


def tally():
    src = (
        "https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1"
        "&transparentBackground=1&dynamicHeight=1&source=Port+St+Lucie+Tree+Service"
    )
    return f"""
    <div class="quote-card" id="quote">
      <small>Get a tree estimate</small>
      <p>{escape(BUSINESS)}</p>
      <iframe data-tally-src="{src}" loading="lazy" width="100%" height="552" frameborder="0" marginheight="0" marginwidth="0" title="Port St Lucie Tree Service quote form"></iframe>
    </div>"""


def tally_script():
    return """
<script>
var d=document,w="https://tally.so/widgets/embed.js",v=function(){if(typeof Tally!=="undefined"){Tally.loadEmbeds();}else{d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach(function(e){e.src=e.dataset.tallySrc;});}};if(typeof Tally!=="undefined"){v();}else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w;s.onload=v;s.onerror=v;d.body.appendChild(s);}
</script>"""


def here(filename, href):
    path = href[1:] if href.startswith("/") else href
    if href == "/" and filename == "index.html":
        return ' aria-current="page"'
    if path == filename:
        return ' aria-current="page"'
    return ""


def nav(filename):
    service_links = "\n".join(
        f'<li><a href="/{href}"{here(filename, "/" + href)}>{escape(label)}</a></li>'
        for href, label in SERVICES
    )
    place_links = "\n".join(
        f'<li><a href="/{href}"{here(filename, "/" + href)}>{escape(label)}</a></li>'
        if href
        else f"<li><span>{escape(label)}</span></li>"
        for href, label in PLACES
    )
    neighborhood_links = "\n".join(
        f'<li><a href="/{href}"{here(filename, "/" + href)}>{escape(label)}</a></li>'
        for href, label in NEIGHBORHOODS
    )
    services_current = filename in {href for href, _ in SERVICES} or filename == "services.html"
    places_current = filename in {href for href, _ in PLACES if href} or filename in {
        "locations-port-st-lucie.html",
        "neighborhoods.html",
        "portstluciecarlton.html",
        "se-morningside-blvd.html",
    }
    estimate = "/#quote" if filename == "index.html" else "/contact.html#quote"
    return f"""
    <nav class="site-nav" id="site-nav" aria-label="Primary">
      <ul>
        <li><a href="/"{here(filename, "/")}>Home</a></li>
        <li class="has-sub">
          <a class="nav-parent" href="/services.html"{' aria-current="page"' if services_current else ""}>Services</a>
          <ul class="sub">
            <li><a href="/services.html"{here(filename, "/services.html")}>All services</a></li>
            {service_links}
          </ul>
        </li>
        <li class="has-sub">
          <a class="nav-parent" href="/locations-port-st-lucie.html"{' aria-current="page"' if places_current else ""}>Service area</a>
          <ul class="sub places-menu">
            <li><a href="/locations-port-st-lucie.html"{here(filename, "/locations-port-st-lucie.html")}>All locations</a></li>
            {place_links}
            <li><a href="/neighborhoods.html"{here(filename, "/neighborhoods.html")}>Neighborhoods</a></li>
            {neighborhood_links}
          </ul>
        </li>
        <li><a href="/about.html"{here(filename, "/about.html")}>About</a></li>
        <li><a href="/contact.html"{here(filename, "/contact.html")}>Contact</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>
      <a class="btn btn-solid" href="{estimate}">Request an estimate</a>
    </div>"""


def footer():
    services = "\n".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' for href, label in SERVICES
    )
    places = "\n".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' if href else f"<li>{escape(label)}</li>"
        for href, label in PLACES
    )
    neighborhoods = "\n".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' for href, label in NEIGHBORHOODS
    )
    return f"""
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <h2>{escape(BUSINESS)}</h2>
        <p>Tree removal, stump removal, brush cleaning, and storm cleanup in Port St. Lucie, Florida.</p>
        <p><a href="{TEL}">{PHONE}</a></p>
      </div>
      <div>
        <h2>Services</h2>
        <ul>{services}</ul>
      </div>
      <div>
        <h2>Company</h2>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about.html">About</a></li>
          <li><a href="/services.html">Services</a></li>
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="/locations-port-st-lucie.html">Locations</a></li>
          <li><a href="/neighborhoods.html">Neighborhoods</a></li>
        </ul>
      </div>
      <div>
        <h2>Service area</h2>
        <ul>{places}{neighborhoods}</ul>
      </div>
    </div>
    <div class="wrap legal">
      <p>{escape(BUSINESS)}. Port St. Lucie, Florida. <a href="{TEL}">{PHONE}</a></p>
    </div>
  </footer>
  <div class="mobile-bar">
    <a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>
    <a class="btn btn-solid" href="/contact.html#quote">Request estimate</a>
  </div>"""


def crumbs(items):
    parts = []
    for href, label in items:
        if href:
            parts.append(f'<li><a href="{escape(href, quote=True)}">{escape(label)}</a></li>')
        else:
            parts.append(f"<li>{escape(label)}</li>")
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{"".join(parts)}</ol></nav>'


def json_ld():
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BUSINESS,
        "telephone": "+1-772-492-4436",
        "url": BASE + "/",
    }
    return json.dumps(data, ensure_ascii=False)


def shell(filename, extracted, main, crumbs_html="", with_tally=False):
    seo = SEO[filename]
    title = seo["title"]
    description = description_for(filename, extracted)
    keywords = seo.get("keywords")
    canonical = canon(filename)
    keyword_tag = f'\n<meta name="keywords" content="{escape(keywords, quote=True)}">' if keywords else ""
    desc_tag = f'\n<meta name="description" content="{escape(description, quote=True)}">' if description else ""
    og_desc = f'\n<meta property="og:description" content="{escape(description, quote=True)}">' if description else ""
    if filename in PAGE_PHOTOS:
        share = PAGE_PHOTOS[filename][0]
    elif filename == "index.html":
        share = HERO_PHOTO
    else:
        share = TREES_PHOTO
    og_image = f'\n<meta property="og:image" content="{BASE}{share}">'
    tally_js = tally_script() if with_tally else ""
    logo_src, logo_alt, logo_w, logo_h = LOGO
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>{desc_tag}{keyword_tag}
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="{escape(SITE_NAME, quote=True)}">
<meta property="og:title" content="{escape(title, quote=True)}">{og_desc}
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">{og_image}
<meta name="theme-color" content="#1b3024">
<link rel="icon" href="{LOGO[0]}" type="image/jpeg">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{json_ld()}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="utility">
  <div class="wrap utility-inner">
    <span>Port St. Lucie, Florida</span>
    <a href="{TEL}">{PHONE}</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">
      {picture(logo_src, logo_alt, logo_w, logo_h, lazy=False)}
      <span>Port St Lucie<small>Tree Service</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    {nav(filename)}
  </div>
</header>
{main}
{footer()}
<script src="/js/site.js"></script>
{tally_js}
</body>
</html>
"""


def place_section():
    return f"""
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Service area</p>
          <h2>Locations we serve</h2>
        </div>
        {render_ul([name for _, name in PLACES])}
        <p><a href="/neighborhoods.html">Neighborhoods</a></p>
      </div>
    </section>"""


def related_services(filename):
    links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>'
        for href, label in SERVICES
        if href != filename
    )
    return f"""
    <section class="section">
      <div class="wrap">
        <h2>Services</h2>
        <ul class="related">{links}</ul>
      </div>
    </section>"""


MAP_SRC = (
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d131340.077642477"
    "!2d-80.3924825!3d27.290052!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2"
    "!1s0x88deebae10c38979%3A0x34a1ee4d9dd96ba5!2sPort%20St%20Lucie%20Tree%20Service"
    "!5e1!3m2!1sen!2suk!4v1791843374669!5m2!1sen!2suk"
)


def map_embed():
    return f"""
    <div class="map-frame">
      <iframe src="{MAP_SRC}" width="600" height="450" style="border:0;" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="Port St Lucie Tree Service on Google Maps"></iframe>
    </div>"""


def map_section():
    return f"""
    <section class="section map-section">
      <div class="wrap">
        {map_embed()}
      </div>
    </section>"""


def cta_band(intro="", heading="Call us today"):
    extra = f"<p>{intro}</p>" if intro else ""
    return f"""
    <section class="band">
      <div class="wrap band-inner">
        <div class="band-copy">
          <h2>{escape(heading)}</h2>
          {extra}
        </div>
        <div class="band-panel">
          <a class="band-phone" href="{TEL}">{PHONE}</a>
          <div class="cta-actions">
            <a class="btn btn-solid" href="{TEL}">CLICK TO CALL</a>
            <a class="btn btn-ghost" href="/contact.html#quote">Request an estimate</a>
          </div>
        </div>
      </div>
    </section>"""


def render_home(extracted):
    lede = about = intro = closing = None
    services = []
    mode = None
    current = None
    for kind, value in extracted["blocks"]:
        if kind == "h2" and value == "About Us":
            mode = "about"
        elif kind == "h2" and value == "Our Services":
            mode = "intro"
        elif kind == "h2" and value in SERVICE_URL:
            mode = "service"
            current = value
        elif kind == "h2" and value == "Call Us Today":
            mode = "close"
        elif kind == "p":
            if mode is None and lede is None:
                lede = value
            elif mode == "about" and about is None:
                about = value
            elif mode == "intro" and intro is None:
                intro = value
            elif mode == "service" and current:
                services.append((current, value))
                current = None
            elif mode == "close" and closing is None:
                closing = value
    by_name = dict(services)
    cards = []
    for name, paragraph in services:
        href = SERVICE_URL[name]
        src, alt, width, height = HOME_PHOTOS[name]
        cards.append(
            f"""<article class="service-card">
              {picture(src, alt, width, height)}
              <div>
                <h2><a href="/{href}">{escape(name)}</a></h2>
                <p>{paragraph}</p>
                <p><a class="details" href="/{href}">Details</a></p>
              </div>
            </article>"""
        )
    about_src, about_alt, about_w, about_h = PAGE_PHOTOS["about.html"]
    commercial_src, commercial_alt, commercial_w, commercial_h = PAGE_PHOTOS["commercial-tree-service.html"]
    main = f"""
<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Port St Lucie Tree service</p>
        <h1>{escape(extracted["h1"])}</h1>
        <p class="lede">{lede}</p>
        <div class="hero-actions">
          <a class="btn btn-solid" href="#quote">Request an estimate</a>
          <a class="btn btn-ghost" href="{TEL}">CALL NOW</a>
        </div>
        <p class="hero-more"><a href="/services.html">LEARN MORE</a></p>
      </div>
      {tally()}
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Our services</p>
        <h2>Our Services</h2>
        <p>{intro}</p>
      </div>
      <div class="service-list">
        {"".join(cards)}
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="wrap feature-grid">
      <article class="feature">
        {picture(about_src, about_alt, about_w, about_h)}
        <div>
          <p class="kicker">About us</p>
          <h2>About Us</h2>
          <p>{about}</p>
          <p><a class="details" href="/about.html">About</a></p>
        </div>
      </article>
      <article class="feature">
        {picture(commercial_src, commercial_alt, commercial_w, commercial_h)}
        <div>
          <p class="kicker">Commercial</p>
          <h2>Commercial Tree Service</h2>
          <p>{by_name["Commercial Tree Service"]}</p>
          <p><a class="details" href="/commercial-tree-service.html">Details</a></p>
        </div>
      </article>
    </div>
  </section>
  {place_section()}
  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Questions</p>
        <h2>Questions before you call</h2>
      </div>
      <div class="faq">
        <details>
          <summary>Which tree services are offered?</summary>
          <p>{intro}</p>
        </details>
        <details>
          <summary>Can you remove a stump after a tree is already down?</summary>
          <p>{services[1][1]}</p>
        </details>
        <details>
          <summary>Do you work on commercial property?</summary>
          <p>{services[2][1]}</p>
        </details>
        <details>
          <summary>What should I do after a storm?</summary>
          <p>{services[5][1]}</p>
        </details>
        <details>
          <summary>How do I reach you?</summary>
          <p>{closing} <a href="{TEL}">{PHONE}</a></p>
        </details>
      </div>
    </div>
  </section>
  {map_section()}
  {cta_band(closing, "Call Us Today")}
</main>"""
    return shell("index.html", extracted, main, with_tally=True)


def crumb_for(filename, h1):
    if filename in {href for href, _ in SERVICES} or filename == "services.html":
        return crumbs([("/", "Home"), ("/services.html", "Services"), (None, h1)])
    if filename in {href for href, _ in NEIGHBORHOODS}:
        return crumbs([("/", "Home"), ("/neighborhoods.html", "Neighborhoods"), (None, h1)])
    if filename in {href for href, _ in PLACES if href}:
        return crumbs([("/", "Home"), ("/locations-port-st-lucie.html", "Locations"), (None, h1)])
    if filename == "locations-port-st-lucie.html":
        return crumbs([("/", "Home"), (None, "Locations")])
    if filename == "neighborhoods.html":
        return crumbs([("/", "Home"), (None, "Neighborhoods")])
    if filename == "about.html":
        return crumbs([("/", "Home"), (None, "About")])
    if filename == "contact.html":
        return crumbs([("/", "Home"), (None, "Contact")])
    return crumbs([("/", "Home"), (None, h1)])


def render_neighborhoods(extracted):
    links = "".join(
        f'<li><a href="/{href}">{escape(label)}</a></li>' for href, label in NEIGHBORHOODS
    )
    h1 = "Neighborhoods"
    main = f"""
<main id="main">
  <div class="page-hero photo-trees"><div class="wrap">{crumb_for("neighborhoods.html", h1)}<h1>{h1}</h1></div></div>
  <section class="section">
    <div class="wrap prose">
      <p>Neighborhood pages on this site:</p>
      <ul class="place-list">{links}</ul>
    </div>
  </section>
  {related_services("neighborhoods.html")}
  {map_section()}
  {cta_band()}
</main>"""
    extracted = {"h1": h1, "blocks": [("p", "Neighborhood pages on this site.")]}
    return shell("neighborhoods.html", extracted, main)


def render_page(filename, extracted):
    h1 = extracted["h1"] or SEO[filename]["title"]
    body = render_blocks(extracted["blocks"])
    extra = ""
    if filename in {href for href, _ in SERVICES} or filename == "services.html":
        extra = place_section() + related_services(filename)
    elif filename != "contact.html":
        extra = related_services(filename)
    figure = page_figure(filename)
    place_pages = {href for href, _ in PLACES if href} | {href for href, _ in NEIGHBORHOODS} | {
        "locations-port-st-lucie.html",
        "neighborhoods.html",
    }
    hero_class = "page-hero photo-trees" if filename in place_pages else "page-hero photo-work"
    if filename == "contact.html":
        content = f'<div class="contact-grid"><div>{figure}<div class="prose">{body}</div></div>{tally()}</div>'
    elif figure:
        content = f'<div class="story">{figure}<div class="prose">{body}</div></div>'
    else:
        content = f'<div class="prose">{body}</div>'
    main = f"""
<main id="main">
  <div class="{hero_class}"><div class="wrap">{crumb_for(filename, h1)}<h1>{escape(h1)}</h1></div></div>
  <section class="section"><div class="wrap">{content}</div></section>
  {extra}
  {map_section()}
  {"" if filename == "contact.html" else cta_band()}
</main>"""
    return shell(filename, extracted, main, with_tally=filename == "contact.html")


def write_sitemap():
    urls = [BASE + "/"] + [f"{BASE}/{name}" for name in PAGES if name != "index.html"]
    body = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        body.append("  <url>")
        body.append(f"    <loc>{url}</loc>")
        body.append("  </url>")
    body.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8")


def write_robots():
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://www.portstlucietrees.com/sitemap.xml\n",
        encoding="utf-8",
    )


def validate():
    missing = [name for name in PAGES if not (ROOT / name).exists()]
    if missing:
        raise SystemExit(f"Missing pages: {missing}")
    problems = []
    for name in PAGES:
        text = (ROOT / name).read_text(encoding="utf-8")
        if SEO[name]["title"] not in text:
            problems.append(f"{name} title mismatch")
        if f'rel="canonical" href="{canon(name)}"' not in text:
            problems.append(f"{name} canonical mismatch")
        if "concretecolumbusga.com" in text:
            problems.append(f"{name} stray outbound link")
        if "weebly.com" in text:
            problems.append(f"{name} weebly reference")
        for href in re.findall(r'href="(/[^"]*)"', text):
            path = href.split("#", 1)[0]
            if path in ("/", ""):
                continue
            target = ROOT / path.lstrip("/")
            if not target.exists():
                problems.append(f"{name} broken {href}")
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    contact = (ROOT / "contact.html").read_text(encoding="utf-8")
    if "source=Port+St+Lucie+Tree+Service" not in index or "source=Port+St+Lucie+Tree+Service" not in contact:
        problems.append("Tally source missing")
    checks = {
        "index.html": ["/services.html"],
        "services.html": ["/tree-removal.html"],
        "tree-removal.html": ["/stump-removal.html"],
        "stump-removal.html": ["/commercial-tree-service.html"],
        "commercial-tree-service.html": ["/tree-care-prevention.html"],
        "tree-care-prevention.html": ["/brush-cleaning.html"],
        "brush-cleaning.html": ["/storm-damage-clean-up.html"],
        "storm-damage-clean-up.html": ["/about.html"],
        "about.html": ["/contact.html"],
        "contact.html": ["/"],
    }
    for name, hrefs in checks.items():
        text = (ROOT / name).read_text(encoding="utf-8")
        for href in hrefs:
            if f'href="{href}"' not in text:
                problems.append(f"{name} missing link {href}")
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Built {len(PAGES)} pages")


def main():
    extracted = {name: extract(name) for name in PAGES}
    (ROOT / "index.html").write_text(render_home(extracted["index.html"]), encoding="utf-8")
    (ROOT / "neighborhoods.html").write_text(render_neighborhoods(extracted["neighborhoods.html"]), encoding="utf-8")
    for name in PAGES:
        if name in ("index.html", "neighborhoods.html"):
            continue
        (ROOT / name).write_text(render_page(name, extracted[name]), encoding="utf-8")
    write_sitemap()
    write_robots()
    validate()


if __name__ == "__main__":
    main()
