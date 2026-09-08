# ESL Games SEO Kit

Repo-ready SEO scaffolding for a plain HTML/CSS site targeting the ESL games
and teaching-resources market. Every keyword target and structural decision in
here traces back to the competitive research in the two market-research
workbooks — the reasoning is recorded in the last column of
`seo/keyword-map.csv` so you can argue with it.

---

## First, the honest framing

**SEO does not live in GitHub.** GitHub stores files and runs automation. What
search engines see is the HTML you publish — titles, headings, URL structure,
markup, internal links, and above all the content itself. If you are on GitHub
Pages then the repo *is* the site, so committing these files does put them live;
if you deploy elsewhere, these are still just the source files.

What genuinely belongs in the repo is the third thing in that list: **automation
that stops you shipping SEO mistakes.** That is what
`.github/workflows/seo-checks.yml` does. It cannot make you rank. It can stop
you pushing a page with a duplicate title, a missing canonical, three `<h1>`
tags, or broken schema — the errors that quietly cost rankings and that nobody
notices for months.

And the thing worth saying plainly: **none of this ranks a site on its own.**
Markup is a label on the box. The research found the incumbents win on content
depth and engagement, not tags — games4esl holds the head term "esl games" and
is still losing traffic at 19% a month because people leave after 52 seconds.
Tags are table stakes; the content is the actual work.

---

## What's in here

```
├── README.md                      this file
├── robots.txt                     → repo root, so it serves at /robots.txt
├── build_sitemap.py               generates sitemap.xml from your HTML files
├── .github/workflows/
│   └── seo-checks.yml             blocks bad SEO on push; rebuilds the sitemap
├── seo/
│   ├── keyword-map.csv            20 targets → URL, title, description, H1
│   └── page-checklist.md          run before every commit
└── templates/
    ├── head.html                  commented <head> block with all tokens
    ├── game-page.html             single game — LearningResource + HowTo schema
    └── collection-page.html       topic page — CollectionPage + ItemList schema
```

---

## Setup, in order

1. **Copy the files into your repo**, keeping the structure. `robots.txt` and
   `build_sitemap.py` go at the root.

2. **Find and replace two tokens everywhere**: `YOURDOMAIN.com` → your domain,
   `YOURBRAND` → your site name. Leave them in `templates/` — the Action
   deliberately ignores that folder so the templates stay reusable.

3. **Enable the Action.** Settings → Actions → General → Workflow permissions →
   *Read and write permissions*. Without this the sitemap commit step fails.

4. **Generate your first sitemap:**
   ```bash
   python build_sitemap.py --domain https://yourdomain.com
   ```

5. **Verify in Google Search Console** and submit `sitemap.xml`. Do this before
   writing a single page — nothing here matters until Google knows you exist.

---

## How to use the keyword map

`seo/keyword-map.csv` has 20 targets in four priority bands. Build them in order.

**Priority 1** is where to start. These are terms held by sites that are
measurably weak: eslgamesworld ranks for "esl games online" (a $1.99 CPC term)
while holding just 168 keywords at global rank #1.5 million. Its positions are
there for the taking.

**Priority 2** is unserved demand — "no prep esl games", "esl games for large
classes", "esl games for one to one classes". Not one of the 22 sites studied
targets class-size or teaching-context constraints, yet these are the problems
teachers actually search at 8am.

**Priority 3** is the deeper topic long tail, the pattern teach-this.com built a
paid membership on.

**Priority 4 is aspirational and labelled as such.** "esl games" is held by a
site with 1,800 ranking keywords and years of accumulated authority. Put it on
your homepage as a long-term target, expect 18+ months, and do not judge
progress by it.

### The one structural finding worth building around

Sites ranking for **game names** — "spelling bee", "hangman" — get around 5.1
pages per visit. Sites ranking for **ESL jargon** get 2.0–2.6 and bounce far
harder. People search for the game they want to play, not for "esl vocabulary
activity". Name pages after games, then let the collection pages catch the
grammar-topic searches. Those game-name terms also carry the higher bids
($2.62 for "spelling bee", $4.12 for "ducky race"), which tells you advertisers
value that traffic more too.

---

## Writing a page

1. Pick the next row in the keyword map.
2. Copy `templates/game-page.html` or `templates/collection-page.html`.
3. Fill in the title, description, canonical, H1 from the CSV row.
4. Write the content. This is the actual work; the rest is packaging.
5. Add two or three internal links out, and one link *in* from an existing page.
6. Run through `seo/page-checklist.md`.
7. Commit. The Action checks it and rebuilds the sitemap.

---

## What this kit deliberately does not do

- **No keyword volume data.** Real volumes need Ahrefs, Semrush or Google
  Keyword Planner. The CPCs quoted in the map come from Similarweb's public
  pages and are a rough proxy for commercial value, not for search volume.
  Validate before committing months of writing.
- **No backlink strategy.** Links remain the strongest off-page factor and none
  of it happens in a repo. Worth knowing from the research: Pinterest is the top
  social referrer for four of the studied sites, and italki refers traffic to
  eslkidsgames — a partnership channel nobody else is using.
- **No promise about timing.** A new domain targeting these terms should expect
  little movement for three to six months, then compounding if the content is
  genuinely better. Anyone quoting faster is selling something.
