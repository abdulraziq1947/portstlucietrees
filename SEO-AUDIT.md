# SEO audit: portstlucietrees.com

Audit date: 12 October 2026.  
Source: live HTML fetched from `https://www.portstlucietrees.com`. Every required URL returned HTTP 200. None of the 27 pages were inaccessible.

The public site is a Weebly site (`cdn2.editmysite.com`, form posts to `weebly.com/weebly/apps/formSubmit.php`). This repository had no commits and no site files when the audit started. Nothing on the live site was changed.

Saved copies of the fetched HTML, `robots.txt`, and `sitemap.xml` are in `.audit/` for the later rebuild. Those files are a working archive, not the new website.

## Canonical host

There is no `rel="canonical"` on any page. There is no meta robots tag on any page. There is no JSON-LD or microdata.

The server’s redirect preference, measured without following redirects automatically, is HTTPS and `www`. Every hop below is a 301.

| Start URL | Hops | Final |
| --- | --- | --- |
| `http://portstlucietrees.com/` | 301 to `http://www.portstlucietrees.com/`, then 301 | `https://www.portstlucietrees.com/` 200 |
| `http://www.portstlucietrees.com/` | 301 | `https://www.portstlucietrees.com/` 200 |
| `https://portstlucietrees.com/` | 301 | `https://www.portstlucietrees.com/` 200 |
| `https://www.portstlucietrees.com/` | none | 200 |
| `http://portstlucietrees.com/index.html` | 301 to `http://www…/index.html`, then 301 | `https://www.portstlucietrees.com/index.html` 200 |
| `https://portstlucietrees.com/about.html` | 301 | `https://www.portstlucietrees.com/about.html` 200 |

`/` and `/index.html` both return 200 and the HTML is byte-identical (74,478 bytes).

Signals disagree about which URL is preferred:

- Redirects land on `https://www.portstlucietrees.com`.
- `og:url` on every page uses `http://www.portstlucietrees.com` plus the path. The homepage `og:url` is `http://www.portstlucietrees.com/` (the root, not `index.html`).
- `sitemap.xml` lists `http://www.portstlucietrees.com/index.html` and does not list `/`.
- `robots.txt` points its sitemap line at `http://www.portstlucietrees.com/sitemap.xml`.

Recommended canonical host for the rebuild, because it is where the 301s already end: `https://www.portstlucietrees.com`.

Homepage decision still needed before build: keep `/` and `/index.html` as two indexable copies, or give `/index.html` a canonical (or 301) to `/`. The live site does not specify a preference. See “Decisions needed” in `DESIGN-PLAN.md`.

## robots.txt and sitemap

Live `robots.txt`:

```
Sitemap: http://www.portstlucietrees.com/sitemap.xml

User-agent: NerdyBot
Disallow: /

User-agent: dotbot
Crawl-delay: 10

User-agent: *
Disallow: /ajax/
Disallow: /apps/
Disallow: /confirmation.html
```

None of the 27 required URLs are disallowed. They are all crawlable. No page sets `noindex`.

`sitemap.xml` is a single urlset. Every `<lastmod>` is `2026-08-22T17:01:00+00:00`. It lists the 26 `.html` paths, including `/index.html`, and omits `/`. Locations use `http://www`, which 301 to `https://www`.

`sitemap_index.xml` and `wp-sitemap.xml` return 404.

`/confirmation.html` is disallowed and is not one of the 27 required URLs. It was not audited as a content page.

## Sitewide facts found on the pages

Recorded only where the HTML states them.

| Item | What the site actually shows |
| --- | --- |
| Names used | “Port St Lucie Tree Service” in the footer and much of the body. Logo alt text is “Tree Service Port St Lucie”. |
| Phone | `772-492-4436`, linked as `tel:7724924436`. |
| Email | Not present. |
| Street address | Not present. |
| Hours | Mentioned only as “business hours” / “normal business hours”. No days or times. |
| Licence, insurance, certifications, awards | Not present. |
| Reviews | Copy refers to “a glowing review” and “ask around”. No review text, rating, or reviewer is published. |
| Language | `<html lang="en">`. |

The logo file is `/uploads/1/3/0/7/130737278/772-492-4436.png`. Its HTML link is `/`. A sitewide script then rewrites `.wsite-logo a` to `tel:7724924436`.

## Navigation, footer, and forms

Desktop and mobile menus are the same, and they appear on every page. There are no breadcrumbs.

- Home → `/`
- Services → `/services.html`
  - Tree Removal → `/tree-removal.html`
  - Stump Removal → `/stump-removal.html`
  - Commercial Tree Service → `/commercial-tree-service.html`
  - Tree Care Prevention → `/tree-care-prevention.html`
  - Brush Cleaning → `/brush-cleaning.html`
  - Storm Damage Clean Up → `/storm-damage-clean-up.html`
- About → `/about.html`
- Contact → `/contact.html`

The footer is the same on every page: the words “Port St Lucie Tree Service” and the phone link. It does not link to other pages.

Header search posts to `/apps/search`, which `robots.txt` disallows.

Enquiry forms post to `//www.weebly.com/weebly/apps/formSubmit.php`. Required fields are marked with an asterisk.

- Homepage, about, services, contact, and the six service pages: Name (first and last), Phone Number, Email, Comment.
- Location and neighborhood pages that have a form: Name (first and last), Email, Comment. No phone field.
- `neighborhoods.html` and `locations-port-st-lucie.html` have no enquiry form.

## Internal links that are easy to lose

Location names in “Locations we serve” are plain text. They are not links. No page in the HTML links to a location, neighborhood, or locations URL. Those URLs are reachable from the sitemap only.

Contextual links that do exist, and should be kept:

| Page | Anchor text | Target |
| --- | --- | --- |
| `/` and `/index.html` hero | LEARN MORE | `/services.html` |
| `/` and `/index.html` body | services | `/services.html` |
| `/services.html` | Tree Removal | `/tree-removal.html` |
| `/tree-removal.html` | stump | `/stump-removal.html` |
| `/stump-removal.html` | work | `/commercial-tree-service.html` |
| `/commercial-tree-service.html` | tree services | `/tree-care-prevention.html` |
| `/tree-care-prevention.html` | Another service | `/brush-cleaning.html` |
| `/brush-cleaning.html` | clean ups | `/storm-damage-clean-up.html` |
| `/storm-damage-clean-up.html` | our focus | `/about.html` |
| `/about.html` | let us be a part of | `/contact.html` |
| `/contact.html` | the services | `/` |
| Several location pages | Port St Lucie Tree Service | `/` |

Location pages whose body links “Port St Lucie Tree Service” to `/`: `hobo-sound-fl.html`, `jupiter-florida.html`, `mico-florida.html`, `palm-beach-gardens-florida.html`, `riviera-beach-fl.html`, `royal-palm-beach-florida.html`, `sebastian-florida.html`, `vero-beach-florida.html`.

`royal-palm-beach-florida.html` also wraps the letter “S” in “Stuart” with an outbound link to `http://www.concretecolumbusga.com/phenix-city-al.html`. That looks like a stray edit. It is recorded here and should not be treated as a real editorial link.

The six homepage service blocks (Tree Removal, Stump Removal, Commercial Tree Service, Tree Care Prevention, Brush Cleaning, Storm Damage Clean Up) are not linked to their service URLs. Only the word “services” in the intro links to `/services.html`.

## Shared technical gaps

- No canonical tag.
- No structured data.
- `og:url` and sitemap locations use `http://` even though that host 301s to `https://`.
- Many images use the alt text “Picture”. Meaningful alts that do exist are listed per page below.
- Location pages use an `h2` as the page heading and have no `h1`. `neighborhoods.html` and `locations-port-st-lucie.html` have no heading with text.
- Service subsections (“Pruning”, “Pulling Stumps”, and the others listed below) are styled text, not heading elements.
- `meta name="keywords"` appears only on some pages. `services.html` and `commercial-tree-service.html` include “Augusta Stump Removal”, which does not match this Florida site. It is recorded and should not be promoted.
- Several location titles and descriptions are missing, very short, or duplicated from the homepage sentence.

## Page inventory

Content words are words inside `#wsite-content` only, after scripts and styles are removed. They include the form labels on pages that have a form.

### Core pages

#### `/` and `/index.html`

Identical documents.

- Title (66): Tree Removal, Tree Care Services, Tree Services, Port St Lucie, FL
- Meta description (157): Tree removal, trimming and care is imperative to the safety of your property. If you have trees on your property, let us be the company to take care of them.
- Keywords: Tree Service Port St Lucie, Tree Removal Port St Lucie, Tree Trimming Service Port St Lucie, Tree Cutting Service Port St Lucie, Port St Lucie Fl Tree Removal, Tree Removal Port St Lucie Fl, Tree Pruning Port St Lucie Fl
- `og:url`: `http://www.portstlucietrees.com/`
- Headings: H2 “Port St Lucie Tree service” (hero). H1 “Tree Service Port St Lucie”. Then H2s: Our Services, Tree Removal, Stump Removal, Commercial Tree Service, Tree Care Prevention, Brush Cleaning, Storm Damage Clean Up, Call Us Today.
- Content words: about 1,031.
- Structure: hero with Learn More and Call Now; intro paragraph; About Us; enquiry form; six service summaries; closing call paragraph. The six summaries are the same ideas as the service-page openings.
- Image alts worth keeping: “Tree Service Port St Lucie” (logo), “tree care service logo”, “tree removal in progress”, “tree stump got removed”, “commercial tree service worker working”, “tree care service in progress”, “tree care worker working on brush cleaning”, “tree fallen on car after storm”. One image is alt “Picture”.

#### `/about.html`

- Title (62): Tree Care Company, Best Tree Care Companies, Port St Lucie, FL
- Meta description (80): We are committed to providing you with the best tree maintenance service around.
- Keywords: Tree Removal Service Port St Lucie Fl, Tree Cutting Service Port St Lucie Fl, Stump Grinding Port St Lucie Fl, Port St Lucie Tree Service, Stump Removal Port St Lucie Fl
- H1: About
- Content words: about 272. Two paragraphs: full-service tree care in Port St. Lucie, reputation, seasonal safety (summer debris and winter branches), then the form.
- Image alts: “Tree Service Port St Lucie”, “tree care expert during work”, “Picture”.

#### `/services.html`

- Title (71): Tree Care, Tree Services Provider, Tree Care Experts, Port St Lucie, FL
- Meta description (134): We try and provide as many tree related services as we can think of. We do this so that we can always say yes, when you need our help.
- Keywords: same list as commercial, including “Augusta Stump Removal”.
- H1: Services
- Styled subsection labels, not heading tags: Tree Removal, Stump Removal, Commercial Tree Service, Tree Care Prevention, Brush Cleaning, Storm Damage Clean Up.
- Content words: about 268. Only “Tree Removal” is a link (`/tree-removal.html`).
- Image alts: logo, plus “Picture”.

#### `/contact.html`

- Title (62): Tree Removal Service, Tree Trimming Service, Port St Lucie, FL
- Meta description (149): If you have read through our services above and think that we may be able to take care of your trees, then now is the time to reach out and say “hi”.
- Keywords: same list as brush cleaning / tree removal.
- H1: Contact
- Content words: about 274. Two paragraphs about calling or using the form. No address, email, or hours.
- In-content link: “the services” → `/`.
- Image alts: logo, “woman smiling taking phone call”, “Picture”.

#### `/tree-removal.html`

- Title (63): Tree Removal, Professional Tree Care Company, Port St Lucie, FL
- Meta description (102): If you have trees on your property that need to be removed, we can take care of that business for you.
- Keywords: Tree Trimming Port St Lucie Fl, Tree Removal Companies Port St Lucie Fl, Tree Company Port St Lucie Fl, Tree and Stump Removal Port St Lucie Fl, Tree Stump Removal Port St Lucie Florida, Stump Grinding Service Port St Lucie Fl
- H1: Tree Removal
- Subsections: Cutting/Pulling Roots, Green Removal, Dangers of Not Removing, Benefits
- Content words: about 524. In-content link: “stump” → `/stump-removal.html`.

#### `/stump-removal.html`

- Title (62): Stump Removal, Affordable Tree Care Company, Port St Lucie, FL
- Meta description (145): If you have already had trees cut down in the past, but you still have their stumps on your property, and want them removed, we have you covered.
- Keywords: same list as the homepage.
- H1: Stump Removal
- Subsections: Pulling Stumps, Digging Out, Benefits of Removal, Uses for Wood
- Content words: about 526. In-content link: “work” → `/commercial-tree-service.html`.

#### `/commercial-tree-service.html`

- Title (66): Commercial Tree Service, Reliable Tree Services, Port St Lucie, FL
- Meta description (107): If you happen to have a commercial property that needs tree or stump removal services, we can also do that.
- Keywords: includes “Augusta Stump Removal”.
- H1: Commercial Tree Service
- Subsections: Commercial Tree Removal, Commercial Stump Removal, Commercial Trimming, Commercial Root Removal
- Content words: about 521. In-content link: “tree services” → `/tree-care-prevention.html`.

#### `/tree-care-prevention.html`

- Title (65): Tree Care Prevention, Local Tree Care Services, Port St Lucie, FL
- Meta description (146): If you are letting trees, on your property, grow then preventative care is necessary. Pruning is one of the number one care options that we offer.
- Keywords: same list as tree removal.
- H1: Tree Care Prevention
- Subsections: Pruning, Branch Removal, Mulching, Small Tree Protection
- Content words: about 516. In-content link: “Another service” → `/brush-cleaning.html`.

#### `/brush-cleaning.html`

- Title (63): Brush Cleaning, Tree Removal Service Near Me, Port St Lucie, FL
- Meta description (158): When leaves and needles fall off of trees, they collect around the base of the tree. There is nowhere for this brush to go, it becomes a matted, tangled mess.
- Keywords: same list as tree removal.
- H1: Brush Cleaning
- Subsections: Controlled Burns, Brush Removal, Tree Care, Consequences of Not Removing
- Content words: about 522. In-content link: “clean ups” → `/storm-damage-clean-up.html`.

#### `/storm-damage-clean-up.html`

- Title (63): Storm Damage Clean Up, Top Tree Care Experts, Port St Lucie, FL
- Meta description (89): If a storm has come through, and blown debris everywhere, we can help pick it up for you.
- Keywords: same list as the homepage.
- H1: Storm Damage Clean Up
- Subsections: Fallen Limbs, Needle and Leaf Cleanup, Broken Trees, Other Debris
- Content words: about 521. In-content link: “our focus” → `/about.html`.

Service-page images follow one pattern: the phone-number logo, one job photo with a descriptive alt (“tree care expert during work”, “tree care expert working on brush cleaning”, and similar), and a black banner image with alt “Picture”.

### Location and area pages

Almost every location page repeats an unlinked list:

Port St Lucie, Stuart, Palm City, Fort Pierce, Florida Ridge, Hobe Sound, Vero Beach, Jupiter, Palm Beach Gardens, North Palm Beach, Sebastian, Lake Park, Riviera Beach, Royal Palm Beach, Mico.

North Palm Beach and Lake Park are named and have no page in this set. Carlton and SE Morningside are pages and are not in that list.

A near-duplicate template covers eight pages. The paragraph swaps the place name and then says the town has beautiful beaches, winter visitors, and that Port St Lucie Tree Service is the “#1” company for trimming, stump removal, brush cleaning, tree removal, and storm cleanup at a low price. Those pages are thin and overlap each other.

| URL | Title | Meta description | On-page heading | Content words | Notes |
| --- | --- | --- | --- | --- | --- |
| `/hobo-sound-fl.html` | Tree Service Hobo Sound FL | None. `og:description` is the beach paragraph. | H2 Tree Service Hobe Sound FL | ~190 | Filename and title say “Hobo”. Heading and body say “Hobe Sound”. Beach template. Links home. |
| `/jupiter-florida.html` | Tree Service Jupiter FL | None. og excerpt of the same template. | H2 Tree Service Jupiter FL | ~189 | Beach template. Links home. |
| `/mico-florida.html` | Tree Service | None. og excerpt. | H2 Tree Service Mico, FL | ~188 | Title does not name the city. Beach template. Links home. |
| `/palm-beach-gardens-florida.html` | Tree Service Palm Beach Gardens FL | None. og excerpt. | H2 Tree Service Palm Beach Gardens FL | ~192 | Beach template. Links home. |
| `/riviera-beach-fl.html` | Tree Service Riviera Beach FL | None. og excerpt. | H2 Tree Service Riviera Beach, FL | ~190 | Beach template. Links home. |
| `/royal-palm-beach-florida.html` | Tree Service Royal Palm Beach Fl | None. og excerpt. | H2 Tree Service Royal Palm Beach FL | ~194 | Beach template. Links home. Stray outbound link on “S”. Hero image filename is `tree-service-mico-fl_1.jpg`. |
| `/sebastian-florida.html` | Tree Service Sebastian Florida | None. og excerpt. | H2 Tree Service Sebastian FL | ~188 | Beach template. Links home. |
| `/vero-beach-florida.html` | Tree Service Vero Beach FL | None. og excerpt. | H2 Tree Service Vero Beach FL | ~190 | Beach template. Links home. |
| `/port-st-lucie-flordia.html` | Tree Service port st lucie | None. og excerpt is the Palm City paragraph. | H2 Tree Service Port St Lucie FL | ~194 | Filename spelling “flordia” must stay. Body is the beach template translated awkwardly and it describes Palm City, not Port St. Lucie. |

These pages have their own paragraphs, then the same unlinked location list and the same closing line, “The Port St Lucie area is an ever expanding space and we are the #1 tree service for all your tree removal needs!” Carlton and SE Morningside do not use that closing line or the location list.

| URL | Title | Meta description | On-page heading | Content words | What the body is about |
| --- | --- | --- | --- | --- | --- |
| `/florida-ridge-fl.html` | Tree Removal Service Florida Ridge FL | Homepage sentence plus “in Florida Ridge” | H2 Tree Service Florida Ridge FL | ~217 | Short civic description of the Florida Ridge / Sebastian / Vero Beach area, then the shared closer and location list. |
| `/fort-pierce-florida.html` | Tree Removal Service Fort Pierce FL | Homepage sentence plus “in Fort Pierce Florida.” | H2 Tree Service Fort Pierce FL | ~163 | Short civic history (founded 1901, about 41,000 people, about 29 square miles, downtown), then the shared closer and list. |
| `/palm-city-florida.html` | Tree service palm city florida | Homepage sentence plus “in Palm City Florida.” | H2 Tree Service Palm City FL | ~202 | Parks: Leighton Park, the Palm City Bridge, St. Lucie River, Spear Corporal Justin Wilson Memorial Park at 2050 SW Mapp Road. Keywords meta is present. |
| `/stuart-flordia.html` | Tree Service Stuart Fl | Homepage sentence plus “in Stuart FL” | H2 Tree Service Stuart FL | ~289 | Treasure Coast, Martin County, population figure 16,237, St. Lucie River, Indian River Lagoon, “America’s Happiest Seaside Town” (2016). Filename spelling “flordia” must stay. No in-content link. Image filename `concrete-contractors-stuart-fl_orig.jpg` does not match the page. Keywords meta is present. |
| `/portstluciecarlton.html` | Tree Service port st lucie- Carlton | None. og excerpt is the neighborhood paragraph. | H2 Port St Lucie - Carlton | ~249 | NeighborhoodScout-style notes: bike commuting 3.3%, child poverty comparison, retirement character. No location list. |
| `/se-morningside-blvd.html` | Tree Service port st lucie-PORT ST. LUCIE, FL (SE PORT SAINT LUCIE BLVD - SE MORNINGSIDE BLVD | None. og excerpt is the neighborhood paragraph. Title has no closing parenthesis. | H2 SE PORT ST LUCIE BLVD & SE MORNINGSIDE BLVD | ~240 | NeighborhoodScout-style waterfront / retiree description. No location list. |
| `/locations-port-st-lucie.html` | Port St Lucie Tree Service Locations | None. `og:description` is the city list. | None | ~57 | Only the unlinked city list. No form, no photo, no H1. |
| `/neighborhoods.html` | Neighborhoods | None. `og:description` is the footer line “Port St Lucie Tree Service” and the phone. | Empty H2 in a blank white hero | ~9 | No body copy, no form, no links to Carlton or SE Morningside. |

Location images are almost all alt “Picture”. Filenames sometimes name the city (`hobe-sound-fl-tree-service_orig.jpg`, `fort-pierce-fl-tree-service_orig.jpg`, and similar) and sometimes reuse `stuart-fl_*.jpg`.

## What must stay exactly

- Every filename in the required URL list, including `port-st-lucie-flordia.html`, `stuart-flordia.html`, `hobo-sound-fl.html`, and `portstluciecarlton.html`.
- The navigation and the contextual anchor/target pairs listed above.
- Existing titles, meta descriptions, H1s, and keyword metas, including awkward capitalization, unless a change is approved.
- The phone number `772-492-4436`.
- Page-specific copy on the core pages and the distinct location paragraphs. The beach-template pages should not be replaced with a new generic city essay during the first rebuild.

## What is missing and must not be invented

Address, email, hours, licence numbers, insurance, certifications, awards, star ratings, review quotes, project counts, and completed-job case studies. The Valdosta reference site publishes reviews and hours. This site does not.
