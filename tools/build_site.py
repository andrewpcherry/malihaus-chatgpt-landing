#!/usr/bin/env python3
"""Render the MaliHaus situation and location pages.

    python3 tools/build_site.py        # run from the repo root

Builds:
    situations/index.html                 the situations hub
    situations/<slug>/index.html          16 situation pages
    situations/<old>.html                 6 redirect stubs for the old URLs
    locations/index.html                  the locations hub
    locations/<slug>/index.html           16 location pages
    sitemap.xml                           every URL above
    .home-cards.html, .home-*.html        blocks pasted into index.html

Directory routes with an index.html load directly on GitHub Pages, so
/situations/sell-house-fast/ and /locations/tampa-fl/ resolve without a
404 and without a trailing-slash redirect.
"""

import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from site_data import (ROOT, COVERAGE, REVIEW_LINE, REVIEW_URL, GOOGLE_URL, GOOGLE_SCORE,
                       GOOGLE_LINE, EXPERIENCE_SCORE, EXPERIENCE_LINE,
                       NATIONAL_STRAP, NATIONAL_SUPPORT,
                       PILLARS_TITLE, PILLARS, STEPS, CLOSING_H2, CLOSING_COPY, CLOSING_BTN,
                       ICONS, SITUATIONS, SIT_BY_SLUG, HOME_FEATURED)
from locations_data import LOCATIONS, LOC_BY_SLUG, FLORIDA, NATIONAL
from site_data import SIT_BRANCH

DATE = "2026-09-03"

# One asset version for the whole site, so a bump can never half-apply.
ASSET_V = 20


def e(t):
    return html.escape(str(t), quote=True)


def j(t):
    return str(t).replace("\\", "\\\\").replace('"', '\\"')


def icon(name):
    return '<svg viewBox="0 0 24 24" aria-hidden="true">' + ICONS[name] + "</svg>"


def emphasise(h1, em):
    if em and h1.endswith(em):
        return e(h1[: -len(em)]) + "<i>" + e(em) + "</i>"
    return e(h1)


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------

NAV = [
    ("3 Ways to Sell", "{r}index.html#ways"),
    ("Situations We Help With", "{r}situations/"),
    ("Areas We Serve", "{r}locations/"),
    ("Reviews", "{r}index.html#reviews"),
]


def head(title, meta, canonical, r, og_image=None):
    og_image = og_image or f"{ROOT}/img/hero-everyday.jpg"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(meta)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MaliHaus">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(meta)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{r}img/cropped-Untitled-1-270x270.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Karla:wght@300;400;500;600&display=swap">
<link rel="stylesheet" href="{r}site.css">
<link rel="stylesheet" href="{r}components.css?v={ASSET_V}">
</head>
"""


def nav(r, active=""):
    links = "".join(
        f'    <a href="{l[1].format(r=r)}"' + (' aria-current="page"' if l[0] == active else "")
        + f">{e(l[0])}</a>\n" for l in NAV)
    drawer = "".join(f'    <a class="mh-dl" href="{l[1].format(r=r)}">{e(l[0])}</a>\n' for l in NAV)
    return f"""<div class="navbar"><div class="wrap"><nav>
  <a href="{r}index.html" aria-label="MaliHaus home"><img class="logo" src="{r}img/logo-copper.png" alt="MaliHaus"></a>
  <div class="navlinks">
{links}  </div>
  <div class="navr">
    <a class="navtel" data-call data-loc="nav" href="#"><span data-phone></span></a>
    <a class="btn solid" data-cta data-loc="nav" href="#enquiry">Tell Us About Your Property</a>
    <button class="mh-burger" id="mhburger" aria-label="Open menu" aria-expanded="false" aria-controls="mhdrawer">
      <svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</nav></div></div>

<div class="mh-drawer" id="mhdrawer" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mh-drawer-bg"></div>
  <div class="mh-drawer-p">
    <div class="mh-drawer-top">
      <img src="{r}img/logo-copper.png" alt="MaliHaus">
      <button class="mh-drawer-x" aria-label="Close menu">&times;</button>
    </div>
{drawer}    <a class="mh-drawer-tel" data-call data-loc="mobile_menu" href="#"><span data-phone></span></a>
    <a class="btn solid mh-drawer-cta" data-cta data-loc="mobile_menu" href="#enquiry">Tell Us About Your Property</a>
  </div>
</div>
"""


def footer(r):
    fl = "".join(f'      <a href="{r}locations/{l["slug"]}/">{e(l["name"])}</a>\n' for l in FLORIDA)
    nat = "".join(f'      <a href="{r}locations/{l["slug"]}/">{e(l["name"])}</a>\n' for l in NATIONAL)
    sits = "".join(f'      <a href="{r}situations/{s["slug"]}/">{e(s["nav"])}</a>\n' for s in SITUATIONS)
    return f"""<footer>
  <div class="wrap">
    <div class="mh-foot-cols">
      <div class="mh-foot-c mh-foot-wide">
        <img class="mh-foot-logo" src="{r}img/logo-copper.png" alt="MaliHaus">
        <p>{e(NATIONAL_STRAP)}</p>
        <p class="mh-foot-cov">{e(COVERAGE)}</p>
        <a class="mh-foot-tel" data-call data-loc="footer" href="#"><span data-phone></span></a>
      </div>
      <div class="mh-foot-c">
        <h2>Florida Markets</h2>
{fl}      </div>
      <div class="mh-foot-c">
        <h2>National Markets</h2>
{nat}      </div>
      <div class="mh-foot-c">
        <h2>Situations We Help With</h2>
{sits}      </div>
    </div>
    <div class="mh-foot-base">
      <span>MaliHaus &nbsp;&middot;&nbsp; 1515 S Federal Hwy Ste 156, Boca Raton, FL 33432</span>
      <span>The markets listed above are areas MaliHaus serves. They are not separate MaliHaus offices.</span>
      <span><a href="https://www.malihaus.com/privacy-policy/" target="_blank" rel="noopener">Privacy Policy</a>
        &nbsp;&middot;&nbsp;
        <a href="https://www.malihaus.com/terms-of-use/" target="_blank" rel="noopener">Terms &amp; Conditions</a></span>
    </div>
  </div>
</footer>

<div class="callbar">
  <a data-call data-loc="mobile_bar" href="#">Call now</a>
  <a data-sms data-loc="mobile_bar" href="#">Text us</a>
</div>
<div class="mh-chat-safe" aria-hidden="true"></div>
"""


def scripts(r):
    return f'<script src="{r}site.js?v={ASSET_V}"></script>\n'


# --------------------------------------------------------------------------
# Shared blocks
# --------------------------------------------------------------------------


def pillars_block(condensed=False):
    """Michael's three selling pillars. The condensed form shortens the
    supporting sentence for space, but never changes the meaning and
    never drops a pillar."""
    out = f'  <h2 class="lead">{e(PILLARS_TITLE)}</h2>\n'
    out += ('  <p class="sub">Every property is assessed against all three before anyone quotes a number. '
            'Which one applies depends on the property, its condition and the scope of the work.</p>\n')
    out += '  <div class="mh-pillars">\n'
    for p in PILLARS:
        body = p["short"] if condensed else p["p"]
        out += f"""    <div class="mh-pillar mh-gold">
      <div class="mh-pillar-top"><span class="mh-pillar-n">{p['n']}</span><span class="mh-pillar-ic">{icon(p['icon'])}</span></div>
      <h3>{e(p['h'])}</h3>
      <p>{e(body)}</p>
      <div class="mh-when">{e(p['when'])}</div>
    </div>
"""
    out += "  </div>\n"
    return out


def steps_block():
    out = '  <div class="mh-steps">\n'
    for n, h, p in STEPS:
        out += (f'    <div class="mh-step"><div class="mh-sn">{e(n)}</div>'
                f"<h3>{e(h)}</h3><p>{e(p)}</p></div>\n")
    out += "  </div>\n"
    return out


def proof_block():
    """Both public review records, side by side. Michael asked on 2026-09-03
    for the Google listing to appear wherever the Experience.com link does,
    not only on the home page. The Google mark keeps its own brand colours."""
    google_mark = ('<svg viewBox="0 0 48 48" aria-label="Google">'
      '<path fill="#4285F4" d="M45.1 24.5c0-1.6-.1-2.8-.4-4H24v7.3h12.1c-.2 1.9-1.6 4.8-4.5 6.7l-.1.3 6.5 5 .5.1c4.1-3.8 6.6-9.4 6.6-15.4z"/>'
      '<path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-6.9-5.4c-1.9 1.3-4.4 2.2-7.6 2.2-5.8 0-10.7-3.8-12.5-9.1l-.3.02-6.8 5.2-.1.3C7.9 41.1 15.4 46 24 46z"/>'
      '<path fill="#FBBC05" d="M11.5 28.4c-.5-1.4-.7-2.9-.7-4.4s.3-3 .7-4.4v-.3l-6.9-5.3-.2.1A22 22 0 0 0 2 24c0 3.5.9 6.9 2.4 9.9l7.1-5.5z"/>'
      '<path fill="#EA4335" d="M24 10.5c4.1 0 6.9 1.8 8.5 3.3l6.2-6C34.9 4.3 29.9 2 24 2 15.4 2 7.9 6.9 4.4 14.1l7.1 5.5z"/></svg>')
    star_mark = ('<svg viewBox="0 0 24 24" fill="none" stroke="#C68C4E" stroke-width="1.4" aria-hidden="true">'
      '<circle cx="12" cy="12" r="9"/>'
      '<path d="m12 7.4 1.35 2.9 3.15.42-2.3 2.16.58 3.12L12 14.53l-2.78 1.47.58-3.12-2.3-2.16 3.15-.42z"/></svg>')

    def card(href, mark, score, line):
        return f"""    <a class="mh-proof mh-gold" href="{href}" target="_blank" rel="noopener">
      {mark}
      <div class="mh-proof-t">
        <div class="mh-proof-r"><span class="mh-st">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <b>{e(score)}</b></div>
        <div class="mh-proof-n">{e(line)}</div>
      </div>
      <span class="mh-proof-a">Read them &rarr;</span>
    </a>
"""

    return ('  <div class="mh-proofs">\n'
            + card(GOOGLE_URL, google_mark, GOOGLE_SCORE, GOOGLE_LINE)
            + card(REVIEW_URL, star_mark, EXPERIENCE_SCORE, EXPERIENCE_LINE)
            + '  </div>\n')


def closing_block(r=""):
    return f"""  <div class="mh-notsure">
    <h2>{e(CLOSING_H2)}</h2>
    <p>{e(CLOSING_COPY)}</p>
    <div class="mh-b">
      <a class="btn solid" data-cta data-loc="closing" href="{r}get-offer/#start">{e(CLOSING_BTN)}</a>
      <a class="btn ghost" data-call data-loc="closing" href="#">Call <span data-phone></span></a>
    </div>
  </div>
"""


def form_block(r, situation="", heading="Tell Us About Your Property", intro=None):
    """The handoff to the funnel. Takes `r` directly rather than a placeholder
    the caller has to substitute: the old {R} trick escaped wrong in the
    f-string and shipped literal {e(heading)} to 34 live pages."""
    intro = intro or ("Start with the situation you are in, not a form. It takes about two minutes, "
                      "you tap rather than type, and nothing here commits you to selling.")
    q = f"?s={situation}" if situation else ""
    return f"""  <div class="mh-handoff">
    <h2>{e(heading)}</h2>
    <p>{e(intro)}</p>
    <div class="mh-b">
      <a class="btn solid" data-cta data-loc="funnel_handoff" href="{r}get-offer/{q}#start">Start With Your Situation</a>
      <a class="btn ghost" data-call data-loc="funnel_handoff" href="#">Call <span data-phone></span></a>
    </div>
  </div>
"""


def sit_card(s, r):
    """Two actions per card: read the page, or start the funnel already seeded
    with this situation. The start action is ON the card so a visitor never has
    to scroll to a block at the foot of the page to begin."""
    branch = SIT_BRANCH.get(s["slug"], "")
    q = f"?s={branch}" if branch else ""
    return f"""      <div class="mh-card mh-gold">
        <div class="mh-card-fig"><div class="mh-card-ic">{icon(s['icon'])}</div></div>
        <div class="mh-card-b">
          <h3><a class="mh-card-link" data-situation-link="{s['slug']}" href="{r}situations/{s['slug']}/">{e(s['nav'])}</a></h3>
          <p>{e(s['card'])}</p>
          <div class="mh-card-acts">
            <a class="mh-card-start" data-cta data-loc="situation_card" href="{r}get-offer/{q}#start">Start here &rarr;</a>
            <a class="mh-card-read" data-situation-link="{s['slug']}" href="{r}situations/{s['slug']}/">Read more</a>
          </div>
        </div>
      </div>
"""


def loc_card(l, r):
    """Market card: the local imagery stays prominent and full bleed at the
    top, the content panel below carries the gold contrast treatment.
    width/height are set so the card reserves its space and nothing shifts."""
    b = r + l["img"]
    return f"""      <div class="mh-loccard">
        <div class="mh-loccard-fig"><img
          src="{b}-640.webp"
          srcset="{b}-640.webp 640w, {b}-1440.webp 1440w"
          sizes="(max-width:640px) 100vw, (max-width:1000px) 50vw, 33vw"
          alt="{e(l['alt'])}" loading="lazy" decoding="async" width="640" height="360"></div>
        <div class="mh-loccard-b mh-gold">
          <h3>{e(l['name'])}</h3>
          <p>{e(l['card'])}</p>
          <a class="btn ghost" data-cta data-loc="location_card" href="{r}locations/{l['slug']}/">Explore This Market</a>
        </div>
      </div>
"""


def sit_links(slugs, r):
    out = '  <div class="mh-cards">\n'
    for sl in slugs:
        out += sit_card(SIT_BY_SLUG[sl], r)
    out += "  </div>\n"
    return out


# --------------------------------------------------------------------------
# Situations hub
# --------------------------------------------------------------------------


def build_situations_hub():
    r = "../"
    canonical = f"{ROOT}/situations/"
    title = "Situations We Help With | Sell Your Property | MaliHaus"
    meta = ("Explore the property situations MaliHaus can help with, including inherited homes, repairs, "
            "foreclosure, difficult tenants, vacant properties and urgent sales.")
    cards = "".join(sit_card(s, r) for s in SITUATIONS)
    items = ",\n".join(
        f'        {{ "@type": "ListItem", "position": {i+1}, "name": "{j(s["nav"])}", '
        f'"url": "{ROOT}/situations/{s["slug"]}/" }}' for i, s in enumerate(SITUATIONS))

    out = head(title, meta, canonical, r)
    out += '<body data-page-type="situations_hub">\n\n' + nav(r, "Situations We Help With")
    out += f"""
<div class="wrap">
  <div class="crumb"><a href="{r}index.html">Home</a><span>/</span>Situations We Help With</div>
</div>

<header class="phead"><div class="wrap">
  <p class="kicker">Situations we help with</p>
  <h1>Whatever the situation, <i>there may be a simpler way to sell</i></h1>
  <p class="standfirst">Selling a property is not always a straightforward decision. You may be dealing with repairs, tenants, an inheritance, financial pressure or a deadline that makes a traditional sale difficult.</p>
  <p class="standfirst">MaliHaus helps property owners understand their available options and determine whether a direct sale may provide a practical solution. Tell us about the property and your situation. We will review the information and explain what the next step could look like.</p>

  <div class="act">
    <a class="btn solid" data-cta data-loc="hub_head" href="#enquiry">Tell Us About Your Property</a>
    <a class="btn ghost" data-call data-loc="hub_head" href="#">Call <span data-phone></span></a>
  </div>

  <div class="tline">
    <span><span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span> {e(REVIEW_LINE)}</span>
    <span>{e(COVERAGE)}</span>
  </div>
</div></header>

<section><div class="wrap">
  <h2 class="lead">Sixteen situations, one starting point.</h2>
  <p class="sub">Pick whichever is closest to yours. None of them changes what we need from you to begin, which is the property and a rough idea of what is going on.</p>
  <div class="mh-cards">
{cards}  </div>
</div></section>

<section class="rule" id="ways"><div class="wrap">
{pillars_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">How it works, in three steps.</h2>
  <p class="sub">The same process whichever situation brought you here.</p>
{steps_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Areas we serve.</h2>
  <p class="sub">{e(COVERAGE)} Every situation on this page applies across each of the markets we work in.</p>
  <div class="mh-b" style="margin-top:34px">
    <a class="btn solid" data-cta data-loc="hub_areas" href="{r}locations/">See all the markets we serve</a>
  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">What MaliHaus clients say.</h2>
{proof_block()}</div></section>

<section class="rule" id="enquiry"><div class="wrap">
{form_block(r)}
{closing_block(r)}</div></section>

{footer(r)}
{scripts(r)}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{ROOT}/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Situations We Help With", "item": "{canonical}" }}
      ]
    }},
    {{
      "@type": "CollectionPage",
      "@id": "{canonical}",
      "url": "{canonical}",
      "name": "{j(title)}",
      "description": "{j(meta)}",
      "isPartOf": {{ "@id": "{ROOT}/#website" }},
      "about": {{ "@id": "{ROOT}/#business" }}
    }},
    {{
      "@type": "ItemList",
      "name": "Situations MaliHaus helps with",
      "itemListElement": [
{items}
      ]
    }}
  ]
}}
</script>

</body>
</html>
"""
    os.makedirs("situations", exist_ok=True)
    open("situations/index.html", "w").write(out)


# --------------------------------------------------------------------------
# A situation page
# --------------------------------------------------------------------------


def build_situation(s):
    r = "../../"
    canonical = f"{ROOT}/situations/{s['slug']}/"

    opening = "".join(f'  <p class="standfirst">{e(p)}</p>\n' for p in s["opening"])
    challenge = "".join(f"    <p>{e(p)}</p>\n" for p in s["challenge"])
    helps = "".join(f"    <p>{e(p)}</p>\n" for p in s["help"])
    comps = "".join(
        '    <div class="ck"><svg viewBox="0 0 24 24" fill="none" stroke="#C68C4E" stroke-width="1.6">'
        '<circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5M12 16.4v.3"/></svg>'
        f"<div><b>{e(t)}</b><span>{e(d)}</span></div></div>\n" for t, d in s["complications"])
    faqs = "".join(f'    <div class="qa"><h3>{e(q)}</h3><p>{e(a)}</p></div>\n' for q, a in s["faqs"])

    disclaimer = ""
    if s.get("disclaimer"):
        disclaimer = ('  <div class="mh-legal">\n'
                      f'    <p><b>Important.</b> {e(s["disclaimer"])}</p>\n  </div>\n')

    related = "".join(
        f'    <a class="sit" data-situation-link="{rs}" href="../{rs}/">'
        f'<span class="q">{e(SIT_BY_SLUG[rs]["card"].split(".")[0])}</span>'
        f'<span class="a">{e(SIT_BY_SLUG[rs]["nav"])} &rarr;</span></a>\n' for rs in s["related"])

    fl = "".join(f'      <a href="{r}locations/{l["slug"]}/">{e(l["name"])}</a>\n' for l in FLORIDA)
    nat = "".join(f'      <a href="{r}locations/{l["slug"]}/">{e(l["name"])}</a>\n' for l in NATIONAL)

    faq_json = ",\n".join(
        f"""        {{
          "@type": "Question",
          "name": "{j(q)}",
          "acceptedAnswer": {{ "@type": "Answer", "text": "{j(a)}" }}
        }}""" for q, a in s["faqs"])

    out = head(s["title"], s["meta"], canonical, r)
    out += '<body data-page-type="situation">\n\n' + nav(r, "Situations We Help With")
    out += f"""
<div class="wrap">
  <div class="crumb"><a href="{r}index.html">Home</a><span>/</span><a href="{r}situations/">Situations We Help With</a><span>/</span>{e(s['nav'])}</div>
</div>

<header class="phead"><div class="wrap">
  <p class="kicker">{e(s['kicker'])}</p>
  <h1>{emphasise(s['h1'], s.get('h1_em', ''))}</h1>
{opening}
  <div class="act">
    <a class="btn solid" data-cta data-loc="page_head" href="{r}get-offer/{('?s=' + SIT_BRANCH[s['slug']]) if SIT_BRANCH.get(s['slug']) else ''}#start">{e(s['cta'])}</a>
    <a class="btn ghost" data-call data-loc="page_head" href="#">Call <span data-phone></span></a>
  </div>

  <div class="tline">
    <span><span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span> {e(REVIEW_LINE)}</span>
    <span>{e(COVERAGE)}</span>
  </div>
</div></header>

<section><div class="wrap">
  <h2 class="lead">{e(s['challenge_h'])}</h2>
  <div class="prose">
{challenge}  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">What tends to complicate it.</h2>
  <p class="sub">Not everything below will apply to you. Most owners in this situation recognise at least one of them.</p>
  <div class="checks">
{comps}  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">{e(s['help_h'])}</h2>
  <div class="prose">
{helps}  </div>
{disclaimer}</div></section>

<section class="rule" id="ways"><div class="wrap">
{pillars_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">How it works, in three steps.</h2>
{steps_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Questions people in this situation ask.</h2>
  <div class="faq">
{faqs}  </div>
</div></section>

<section class="rule" id="enquiry"><div class="wrap">
{form_block(r, situation=SIT_BRANCH.get(s['slug'], ''), heading=s['cta'])}
{proof_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Areas we serve.</h2>
  <p class="sub">{e(COVERAGE)} This situation is one we look at across every market below.</p>
  <div class="mh-marketcols">
    <div class="mh-marketc">
      <h3>Florida Markets</h3>
{fl}    </div>
    <div class="mh-marketc">
      <h3>National Markets</h3>
{nat}    </div>
  </div>
  <div class="mh-b" style="margin-top:36px">
    <a class="btn ghost" data-cta data-loc="sit_areas" href="{r}locations/">See the full locations hub</a>
  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Related situations.</h2>
  <p class="sub">Several of these often overlap. If more than one applies, mention it when we speak.</p>
  <div class="sits">
{related}  </div>
{closing_block(r)}</div></section>

{footer(r)}
{scripts(r)}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{ROOT}/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Situations We Help With", "item": "{ROOT}/situations/" }},
        {{ "@type": "ListItem", "position": 3, "name": "{j(s['nav'])}", "item": "{canonical}" }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "@id": "{canonical}#faq",
      "mainEntity": [
{faq_json}
      ]
    }},
    {{
      "@type": "WebPage",
      "@id": "{canonical}",
      "url": "{canonical}",
      "name": "{j(s['title'])}",
      "description": "{j(s['meta'])}",
      "isPartOf": {{ "@id": "{ROOT}/#website" }},
      "about": {{ "@id": "{ROOT}/#business" }},
      "primaryImageOfPage": "{ROOT}/img/hero-everyday.jpg"
    }}
  ]
}}
</script>

</body>
</html>
"""
    d = os.path.join("situations", s["slug"])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(out)


# --------------------------------------------------------------------------
# Locations hub
# --------------------------------------------------------------------------


def build_locations_hub():
    r = "../"
    canonical = f"{ROOT}/locations/"
    title = "Areas We Serve | Sell Your Property | MaliHaus"
    meta = ("Explore the Florida and national markets served by MaliHaus and learn how we help property "
            "owners facing repairs, inherited ownership, tenants, financial pressure and other difficult "
            "situations.")

    fl_cards = "".join(loc_card(l, r) for l in FLORIDA)
    nat_cards = "".join(loc_card(l, r) for l in NATIONAL)
    items = ",\n".join(
        f'        {{ "@type": "ListItem", "position": {i+1}, "name": "{j(l["name"])}", '
        f'"url": "{ROOT}/locations/{l["slug"]}/" }}' for i, l in enumerate(LOCATIONS))
    areas = ",\n".join(
        f'        {{ "@type": "{"AdministrativeArea" if "County" in l["name"] else "City"}", '
        f'"name": "{j(l["area"])}" }}' for l in LOCATIONS)

    out = head(title, meta, canonical, r)
    out += '<body data-page-type="locations_hub">\n\n' + nav(r, "Areas We Serve")
    out += f"""
<div class="wrap">
  <div class="crumb"><a href="{r}index.html">Home</a><span>/</span>Areas We Serve</div>
</div>

<header class="phead"><div class="wrap">
  <p class="kicker">Areas we serve</p>
  <h1>Property solutions across Florida <i>and selected markets nationwide</i></h1>
  <p class="standfirst">MaliHaus works with property owners across South Florida, Central Florida, North Florida and selected markets nationwide. Whether you are dealing with repairs, tenants, an inheritance, financial pressure or another complicated situation, our team can review the property and help you understand the available next step.</p>

  <div class="act">
    <a class="btn solid" data-cta data-loc="loc_hub_head" href="#enquiry">Tell Us About Your Property</a>
    <a class="btn ghost" data-call data-loc="loc_hub_head" href="#">Call <span data-phone></span></a>
  </div>

  <div class="tline">
    <span><span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span> {e(REVIEW_LINE)}</span>
    <span>{e(NATIONAL_STRAP)}</span>
  </div>
</div></header>

<section><div class="wrap">
  <h2 class="lead">Florida Markets</h2>
  <p class="sub">The markets MaliHaus has worked in longest, from South Florida up through Central and North Florida.</p>
  <div class="mh-loccards">
{fl_cards}  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">National Markets</h2>
  <p class="sub">Markets we serve through our own purchasing capacity and our national investor network. These are areas we work in, not separate MaliHaus offices.</p>
  <div class="mh-loccards">
{nat_cards}  </div>
</div></section>

<section class="rule" id="ways"><div class="wrap">
{pillars_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">How it works, in three steps.</h2>
{steps_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Situations we help with.</h2>
  <p class="sub">Every situation below applies across every market we serve.</p>
{sit_links(HOME_FEATURED, r)}  <div class="mh-b" style="margin-top:34px">
    <a class="btn ghost" data-cta data-loc="loc_hub_sits" href="{r}situations/">See All Situations We Help With</a>
  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">What MaliHaus clients say.</h2>
{proof_block()}</div></section>

<section class="rule" id="enquiry"><div class="wrap">
{form_block(r)}
{closing_block(r)}</div></section>

{footer(r)}
{scripts(r)}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{ROOT}/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Areas We Serve", "item": "{canonical}" }}
      ]
    }},
    {{
      "@type": "CollectionPage",
      "@id": "{canonical}",
      "url": "{canonical}",
      "name": "{j(title)}",
      "description": "{j(meta)}",
      "isPartOf": {{ "@id": "{ROOT}/#website" }},
      "about": {{ "@id": "{ROOT}/#business" }}
    }},
    {{
      "@type": "ItemList",
      "name": "Markets served by MaliHaus",
      "itemListElement": [
{items}
      ]
    }},
    {{
      "@type": "Organization",
      "@id": "{ROOT}/#org-areas",
      "name": "MaliHaus",
      "url": "{ROOT}/",
      "telephone": "+14079173347",
      "areaServed": [
{areas}
      ]
    }}
  ]
}}
</script>

</body>
</html>
"""
    os.makedirs("locations", exist_ok=True)
    open("locations/index.html", "w").write(out)


# --------------------------------------------------------------------------
# A location page
# --------------------------------------------------------------------------


def build_location(l):
    r = "../../"
    canonical = f"{ROOT}/locations/{l['slug']}/"
    img = r + l["img"]

    opening = "".join(f'  <p class="standfirst">{e(p)}</p>\n' for p in l["opening"])
    how = "".join(f"    <p>{e(p)}</p>\n" for p in l["how"])
    faqs = "".join(f'    <div class="qa"><h3>{e(q)}</h3><p>{e(a)}</p></div>\n' for q, a in l["faqs"])
    related = "".join(
        f'    <a class="sit" href="../{rl}/"><span class="q">{e(LOC_BY_SLUG[rl]["name"])}</span>'
        f'<span class="a">Explore this market &rarr;</span></a>\n' for rl in l["related"])

    kc_note = ""
    if l.get("kc_unresolved"):
        kc_note = ('  <div class="mh-legal">\n    <p><b>Note.</b> MaliHaus serves the Kansas City '
                   'metropolitan area, which spans a state line. Give us the full property address so the '
                   'correct state professionals are involved from the beginning.</p>\n  </div>\n')

    faq_json = ",\n".join(
        f"""        {{
          "@type": "Question",
          "name": "{j(q)}",
          "acceptedAnswer": {{ "@type": "Answer", "text": "{j(a)}" }}
        }}""" for q, a in l["faqs"])

    area_type = "AdministrativeArea" if "County" in l["name"] else "City"

    out = head(l["title"], l["meta"], canonical, r, og_image=f"{ROOT}/{l['img']}-1440.webp")
    out += '<body data-page-type="location">\n\n' + nav(r, "Areas We Serve")
    out += f"""
<div class="wrap">
  <div class="crumb"><a href="{r}index.html">Home</a><span>/</span><a href="{r}locations/">Areas We Serve</a><span>/</span>{e(l['name'])}</div>
</div>

<header class="mh-lochero">
  <div class="mh-lochero-bg"><img
    src="{img}-1440.webp"
    srcset="{img}-640.webp 640w, {img}-1440.webp 1440w"
    sizes="100vw"
    alt="{e(l['alt'])}" fetchpriority="high" decoding="async" width="1440" height="810"></div>
  <div class="mh-lochero-scrim"></div>
  <div class="wrap mh-lochero-in">
    <p class="kicker">{e(l['name'])}</p>
    <h1>{emphasise(l['h1'], l.get('h1_em', ''))}</h1>
{opening}
    <div class="act">
      <a class="btn solid" data-cta data-loc="loc_head" href="#enquiry">Tell Us About Your Property</a>
      <a class="btn ghost" data-call data-loc="loc_head" href="#">Call <span data-phone></span></a>
    </div>

    <div class="tline">
      <span><span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span> {e(REVIEW_LINE)}</span>
      <span>{e(NATIONAL_STRAP)}</span>
    </div>
  </div>
</header>

<section><div class="wrap">
  <h2 class="lead">How MaliHaus works with owners in {e(l['name'])}.</h2>
  <div class="prose">
{how}  </div>
{kc_note}</div></section>

<section class="rule" id="ways"><div class="wrap">
{pillars_block(condensed=True)}  <div class="mh-b" style="margin-top:40px">
    <a class="btn ghost" data-cta data-loc="loc_ways" href="{r}index.html#ways">See the three approaches in full</a>
  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">How it works, in three steps.</h2>
{steps_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Situations we help with in {e(l['name'])}.</h2>
  <p class="sub">{e(l['sit_intro'])}</p>
{sit_links(l['featured'], r)}  <div class="mh-b" style="margin-top:34px">
    <a class="btn ghost" data-cta data-loc="loc_sits" href="{r}situations/">See All Situations We Help With</a>
  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">{e(NATIONAL_STRAP)}</h2>
  <div class="prose">
    <p>{e(NATIONAL_SUPPORT)}</p>
  </div>
</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Questions owners in {e(l['name'])} ask.</h2>
  <div class="faq">
{faqs}  </div>
</div></section>

<section class="rule" id="enquiry"><div class="wrap">
{form_block(r)}
{proof_block()}</div></section>

<section class="rule"><div class="wrap">
  <h2 class="lead">Related markets.</h2>
  <p class="sub">{e(COVERAGE)}</p>
  <div class="sits">
{related}  </div>
  <div class="mh-b" style="margin-top:36px">
    <a class="btn ghost" data-cta data-loc="loc_related" href="{r}locations/">See every market we serve</a>
  </div>

  <div class="mh-notsure">
    <h2>Ready to talk about a property in {e(l['name'])}?</h2>
    <p>Tell us the address, the condition of the property and the situation you are facing. The MaliHaus team will review it and explain which of the three approaches may fit.</p>
    <div class="mh-b">
      <a class="btn solid" data-cta data-loc="loc_closing" href="#enquiry">Tell Us About Your Property</a>
      <a class="btn ghost" data-call data-loc="loc_closing" href="#">Call <span data-phone></span></a>
    </div>
  </div>
</div></section>

{footer(r)}
{scripts(r)}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{ROOT}/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Areas We Serve", "item": "{ROOT}/locations/" }},
        {{ "@type": "ListItem", "position": 3, "name": "{j(l['name'])}", "item": "{canonical}" }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "@id": "{canonical}#faq",
      "mainEntity": [
{faq_json}
      ]
    }},
    {{
      "@type": "WebPage",
      "@id": "{canonical}",
      "url": "{canonical}",
      "name": "{j(l['title'])}",
      "description": "{j(l['meta'])}",
      "isPartOf": {{ "@id": "{ROOT}/#website" }},
      "about": {{ "@id": "{ROOT}/#business" }},
      "primaryImageOfPage": "{ROOT}/{l['img']}-1440.webp"
    }},
    {{
      "@type": "Service",
      "name": "Property purchase and investor placement in {j(l['name'])}",
      "provider": {{ "@id": "{ROOT}/#business" }},
      "areaServed": {{ "@type": "{area_type}", "name": "{j(l['area'])}" }},
      "description": "{j(l['meta'])}"
    }}
  ]
}}
</script>

</body>
</html>
"""
    d = os.path.join("locations", l["slug"])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(out)


# --------------------------------------------------------------------------
# Redirect stubs for the six original situation URLs
# --------------------------------------------------------------------------

REDIRECTS = {
    "inherited-property.html": "inherited-property-probate",
    "pre-foreclosure.html": "foreclosure-missed-payments",
    "tired-landlord.html": "tired-landlords",
    "divorce.html": "divorce-separation",
    "house-needs-repairs.html": "major-repairs-as-is",
    "relocating.html": "relocation",
}


def build_redirects():
    for old, slug in REDIRECTS.items():
        open(os.path.join("situations", old), "w").write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, follow">
<title>Moved | MaliHaus</title>
<link rel="canonical" href="{ROOT}/situations/{slug}/">
<meta http-equiv="refresh" content="0; url={slug}/">
<script>location.replace("{slug}/" + location.search + location.hash);</script>
</head>
<body>
<p>This page has moved to <a href="{slug}/">{e(SIT_BY_SLUG[slug]['nav'])}</a>.</p>
</body>
</html>
""")


# --------------------------------------------------------------------------
# Sitemap and the home page blocks
# --------------------------------------------------------------------------


def build_sitemap():
    urls = [(f"{ROOT}/", "1.0"),
            (f"{ROOT}/situations/", "0.9"),
            (f"{ROOT}/locations/", "0.9"),
            (f"{ROOT}/get-offer/", "0.9")]
    urls += [(f"{ROOT}/situations/{s['slug']}/", "0.8") for s in SITUATIONS]
    urls += [(f"{ROOT}/locations/{l['slug']}/", "0.8") for l in LOCATIONS]
    urls += [(f"{ROOT}/how-it-works.html", "0.3")]
    body = "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{DATE}</lastmod>\n"
                   f"    <priority>{p}</priority>\n  </url>\n" for u, p in urls)
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n'
                                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                   + body + "</urlset>\n")
    return len(urls)


def build_home_blocks():
    open(".home-cards.html", "w").write("".join(sit_card(SIT_BY_SLUG[k], "") for k in HOME_FEATURED))
    open(".home-pillars.html", "w").write(pillars_block())
    open(".home-steps.html", "w").write(steps_block())
    open(".home-nav.html", "w").write(nav(""))
    open(".home-footer.html", "w").write(footer(""))
    open(".home-form.html", "w").write(form_block(""))


if __name__ == "__main__":
    assert len(SITUATIONS) == 16, f"expected 16 situations, found {len(SITUATIONS)}"
    assert len(LOCATIONS) == 17, f"expected 17 locations, found {len(LOCATIONS)}"
    assert len({s["slug"] for s in SITUATIONS}) == 16
    assert len({l["slug"] for l in LOCATIONS}) == 17
    for s in SITUATIONS:
        for x in s["related"]:
            assert x in SIT_BY_SLUG and x != s["slug"], f"{s['slug']} -> {x}"
    for l in LOCATIONS:
        for x in l["related"]:
            assert x in LOC_BY_SLUG and x != l["slug"], f"{l['slug']} -> {x}"
        for x in l["featured"]:
            assert x in SIT_BY_SLUG, f"{l['slug']} -> {x}"
        assert len(l["faqs"]) >= 3

    build_situations_hub()
    for s in SITUATIONS:
        build_situation(s)
    build_redirects()
    build_locations_hub()
    for l in LOCATIONS:
        build_location(l)
    n = build_sitemap()
    build_home_blocks()
    print(f"built {len(SITUATIONS)} situation pages + hub, {len(LOCATIONS)} location pages + hub, "
          f"{len(REDIRECTS)} redirects, sitemap with {n} URLs")
