# Design plan: Port St Lucie Tree Service

This plan covers Phase 2 only. No public pages will be written until it is approved.

The layout reference is `https://www.valdostafencecompany.com/`, reviewed on 12 October 2026 (homepage, a service page, a town page, the service-area page, about, contact, and the FAQ page). The content source is the audit in `SEO-AUDIT.md`.

The new site should feel like the same kind of local contractor website: a dark header, a full-bleed hero, an estimate card, service cards, plain content sections, a linked service area, questions, and a multi-column footer. It should not reuse that company’s colors, logo, photos, or sentences.

## What the reference layout does

Homepage, top to bottom:

1. A red utility bar with hours on the left and the phone on the right.
2. A dark sticky header: logo, primary links, a services dropdown, a service-area dropdown, and two actions (call, request an estimate). On a narrow screen those links collapse into a menu, and a call/estimate bar sticks to the bottom.
3. A full-bleed hero. The H1 is the service plus the city. The paragraph under it links the main services inline. Two buttons sit under the paragraph: request an estimate, and call.
4. A light estimate card overlaps the bottom of the hero. On this project the card is the shared Tally form, not a custom form. See “Enquiry form” below.
5. A service-card grid. Each card is a photo, a name, one sentence, and a link to the service.
6. A work/gallery band, then two columns for residential and commercial work.
7. A short “how to choose” list, a repair/related-service section, and a linked list of towns.
8. A review block. We will not build this. The Port St Lucie site publishes no reviews.
9. A short FAQ, then a closing call-to-action.
10. A dark footer with services, company links, hours, towns, phone, and email.

Inner service pages add a breadcrumb (`Home / Services / service name`), one H1, several H2 sections, a small FAQ, a “towns we serve” list, related links, and the same footer.

Town pages use one H1, a few local H2s, links to services, and links to the other towns.

Contact repeats the estimate form. About is a short company page with service area and hours, and it avoids claims the business cannot support.

## Original visual system

The current Port St Lucie site already uses Oswald for headings and Open Sans for body text. The reference uses Oswald for headings and Source Sans 3 for body text. We will keep that kind of hierarchy and not copy the reference brand.

| Role | Choice |
| --- | --- |
| Page background | Warm paper, `#f4f1ea` |
| Ink text | `#1c1915` |
| Header, hero, and footer | Deep green, `#1b3024` |
| Accent for buttons and the phone bar | Cypress, `#2f6b4f` |
| Card surface | `#fffcf7` |
| Borders | `#e4ddd2` |
| Headings | A condensed face in the same role as the current site’s Oswald. Self-hosted, `size-adjust` fallback to Arial Narrow. |
| Body | A plain sans, self-hosted or a system stack (`"Segoe UI", system-ui, sans-serif`) so the first paint does not wait on a font CDN. |
| Buttons | Solid accent, white label, about 8px radius. Focus ring visible. |
| Photos | Original or licensed tree-work photos. No Weebly uploads and no photos from the fence site. |

The phone-number PNG will not be the logo. The header will be a text wordmark, “Port St Lucie Tree Service”, linking to `/`. The phone stays in the utility bar, the hero, and the footer as `772-492-4436`.

Hours, a street address, an email, and a review score will be omitted until you supply them. The reference shows all four. This business’s site does not.

## Shared header and footer

Utility bar: “Port St. Lucie, Florida” on the left, phone on the right. No hours.

Header links, matching the live menu:

- Home → `/`
- Services, with the six existing children
- About → `/about.html`
- Contact → `/contact.html`
- Call button and “Request an estimate” (estimate scrolls to the form on the homepage and goes to `/contact.html` elsewhere)

Proposed addition, not on the live site: a “Service area” dropdown listing only the location URLs that already exist. This does not remove any current link. It is how the reference makes town pages crawlable from the header. Say if you want the menu left exactly as it is.

Footer columns:

- Services: the six service URLs
- Company: About, Contact, `/locations-port-st-lucie.html`, `/neighborhoods.html`
- Phone: `772-492-4436`
- Places: the existing location and neighborhood URLs

No privacy, terms, or login links. Those exist on the reference site and not here.

Mobile: the same links in a button-opened menu, plus a bottom bar with Call and Request an estimate. Skip-to-content link first in the page. Menu button has an accessible name.

## Homepage (Phase 3)

Phase 3 builds this page and the shared header and footer, and stops for a visual check.

1. Hero. H1 stays “Tree Service Port St Lucie”. The current hero H2, “Port St Lucie Tree service”, becomes the eyebrow above the H1 so the page has a single H1. Supporting sentence is the existing first paragraph. Inline links point at the six service pages (new links; the current hero only links to `/services.html` via “LEARN MORE”). Buttons: Request an estimate, and Call `772-492-4436`.
2. Estimate card overlapping the hero. It embeds the shared Tally form documented below, with `source` set to `Port St Lucie Tree Service`.
3. “Our Services”. Six cards. Each uses the existing homepage paragraph for that service, shortened only if the card needs one or two lines, with the full paragraph still available on the service page. Each card links to its service URL. Today those blocks are not linked.
4. About band using the existing “About Us” homepage copy, with a link to `/about.html`.
5. Two columns: residential care (from the tree-care and brush copy already on the homepage) and commercial work (from the existing commercial paragraph).
6. Service area. The 15 place names already listed on the site, linked where a page exists. North Palm Beach and Lake Park stay as text, because they have no URL. Carlton and SE Morningside are linked from this list as well, since those pages exist.
7. Questions. The live site has no FAQ. Proposed questions use only facts already written on the site:
   - Which tree services are offered? (the list on the homepage)
   - Can you remove a stump after a tree is already down? (stump paragraph)
   - Do you work on commercial property? (commercial paragraph)
   - What should I do after a storm? (storm paragraph)
   - How do I reach you? (phone and the form; no hours)
   Anything about price, licences, insurance, response time, or guarantees stays out.
8. Closing band: “Call Us Today” plus the existing closing paragraph and the phone.

Title, meta description, and keywords on this page stay as audited. Canonical, once you confirm the host, will be `https://www.portstlucietrees.com/`.

## Later page templates (Phase 4, after homepage approval)

Every file name stays exactly as it is now, including the misspellings.

**Service page** (`tree-removal.html`, `stump-removal.html`, `commercial-tree-service.html`, `tree-care-prevention.html`, `brush-cleaning.html`, `storm-damage-clean-up.html`, and `services.html`):

- Breadcrumb: Home / Services / page name. The live site has no breadcrumbs. This is a new, useful pattern from the reference.
- Existing H1 and existing body, including the current subsection titles promoted to real H2s.
- The existing in-content link stays, with the same anchor text.
- Related services and the place list, as links.
- The same estimate form as the homepage.
- Existing title, meta description, and keywords.

**About and contact:** existing H1 and paragraphs. Contact keeps the form and the phone. It will not gain an address or hours.

**Location page:** existing H2 text becomes the H1 only if you approve that change. Until then the visible heading text stays exact, and we add a visually hidden or matching H1 with the same words so the page has one H1. Body copy stays. The unlinked place list becomes real links to the matching URLs. North Palm Beach and Lake Park remain text. The beach-template pages are not rewritten in the first build. They are a duplicate-content problem, and rewriting them needs a separate pass that does not invent local facts.

**`/locations-port-st-lucie.html`:** keep the title and the same place list, and turn names into links where a page exists.

**`/neighborhoods.html`:** the page is almost empty. Keep the URL and the title “Neighborhoods”. The body can be a short index that links only to `/portstluciecarlton.html` and `/se-morningside-blvd.html`, using the headings those pages already have. No new neighborhood profiles.

**`/index.html`:** the file remains, byte-served, so the URL still resolves. Whether it is separately indexable is the decision below.

## Linking rules for the rebuild

Keep every current navigation item and every contextual pair in the audit.

Add, if you approve:

- Service cards and service-page cross links
- Place names in the repeated list linked to their existing URLs
- Header “Service area” menu
- Footer page links
- Breadcrumbs

Do not keep the outbound link from Royal Palm Beach to `concretecolumbusga.com`.

Do not add North Palm Beach or Lake Park URLs.

## Enquiry form

The quote form is the same Tally form already used on [Baltimore Fence Company](https://baltimorefencingpros.com/). Form id `xX6B0y`. Baltimore passes the hidden field `source` as `Baltimore Fence Company`. This site uses the same embed and changes only that value.

`source` for every embed on this project: `Port St Lucie Tree Service`.

```html
<iframe
  data-tally-src="https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1&source=Port+St+Lucie+Tree+Service"
  loading="lazy"
  width="100%"
  height="552"
  frameborder="0"
  marginheight="0"
  marginwidth="0"
  title="Port St Lucie Tree Service quote form"
></iframe>
<script>
  var d = document, w = "https://tally.so/widgets/embed.js", v = function () {
    if (typeof Tally !== "undefined") Tally.loadEmbeds();
    else d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach(function (e) { e.src = e.dataset.tallySrc; });
  };
  if (typeof Tally !== "undefined") v();
  else if (d.querySelector('script[src="' + w + '"]') == null) {
    var s = d.createElement("script");
    s.src = w;
    s.onload = v;
    s.onerror = v;
    d.body.appendChild(s);
  }
</script>
```

The iframe goes in the homepage hero card and on `/contact.html`. The loader script is included once per page. The card label above the iframe can say “Free Quote” and “Port St Lucie Tree Service”. The form fields themselves stay whatever that Tally form already asks. We will not rebuild them as a local form.

## Technical approach

Static HTML, one CSS file, and a small script for the menu and the FAQ disclosure buttons. The quote form is the Tally embed, loaded once per page. No framework and no Weebly assets.

Shared header and footer will be partials assembled by a small build script into the 27 HTML files. Cloudflare Pages will publish the built HTML. The script is only for authoring, so the deployed site is still plain files.

Images: compressed, width-capped, with width and height set and descriptive alt text. Existing alts that already describe the photo are the starting point. “Picture” will be replaced with a description of that image only when we have a replacement photo we can see. We will not hotlink `/uploads/1/3/0/7/130737278/`.

Forms: the shared Tally embed below. It does not post to Weebly, and it does not need an email address on this site.

`sitemap.xml` will list the canonical HTTPS `www` URLs. `robots.txt` will allow the 27 pages and point at that sitemap. The Weebly rules for `/ajax/`, `/apps/`, NerdyBot, and dotbot go away with the platform, unless you want `/confirmation.html` kept as a disallowed leftover. It is not one of the 27 pages.

New pages will include a canonical link, Open Graph title and description taken from the existing title and meta description, and `LocalBusiness` JSON-LD limited to the name and phone. Address, hours, geo, and `aggregateRating` stay out.

## Accessibility and speed

- One H1 per page.
- Contrast of green, paper, and white text checked against WCAG AA.
- Visible focus, labels on every field, and a menu button that exposes state.
- Buttons and links hit at least 44px on touch screens.
- CSS and the script small enough to ship without a bundler beyond the partials script.
- No render-blocking third-party widgets. No chat bubble, no review widget, no font CDN unless we later choose one.

## Decisions needed before Phase 3

1. Canonical host `https://www.portstlucietrees.com`, matching the live 301s.
2. Homepage URL: recommend a canonical on `/index.html` pointing at `/`, with both URLs still returning 200. The alternative is to leave them as duplicate indexable pages, which is what the live site does.
3. Approve the header service-area menu, footer links, breadcrumbs, and linking the existing place names. Current links stay either way.
4. Approve the five FAQ items written only from existing homepage copy.
5. Provide photos, or approve a first homepage that uses clearly temporary, licensed placeholders rather than the Weebly images.
6. Approve the green and paper palette above, or send brand colors.
7. Location copy stays as audited for Phase 4. A later pass can thin the duplicate beach template only with facts you confirm.

Phase 3, after approval, is the homepage plus the shared header and footer only.
