#!/usr/bin/env python3
"""The seventeen MaliHaus markets.

HARD RULES for everything in this file, because these pages are the ones
most likely to drift into invention:

  * NO local offices, employees, addresses, telephone numbers, Google
    Business Profiles or map listings. MaliHaus serves these markets, it
    is not physically located in them.
  * NO local transaction history, testimonials, closing statistics,
    property values, offer amounts or market statistics. Not even
    softened ones. If a sentence would need a citation, it is not here.
  * NO claims about local law, foreclosure procedure, probate rules,
    tax or code enforcement. Those differ by state and county and are
    not verified, so every page routes those questions to a local
    professional instead of answering them.
  * Copy is CONDITIONAL and owner-focused ("if your property has...")
    rather than assertive about the market ("this market has...").
  * Geographic statements are limited to common knowledge that does not
    move: which state a city is in, that the Kansas City metropolitan
    area spans a state line, that Greensboro and Winston-Salem sit in
    the same region of North Carolina.

KANSAS CITY IS UNRESOLVED. Michael did not say whether he means
Missouri, Kansas or the metro. The route and copy are deliberately
state neutral. Do not add a state until he confirms it.

Imagery (replaced 2026-09-03 on Michael's feedback that the old images
were repetitive and showed palm trees in markets where that is wrong):
every market now has its OWN image, generated for that market's regional
housing style. Sixteen distinct images, no repeats. Palms and South
Florida architecture appear ONLY in Broward and Miami-Dade. Jacksonville,
Tampa and Orlando are visibly different from each other and from South
Florida. Every northern market shows regional housing with deciduous
trees and no tropical planting.

The images are original AI-generated residential exteriors. They are
generic houses at no real address and are never captioned as MaliHaus
properties or as a specific street. Each is served as WebP at 640w and
1440w from img/markets/<slug>-<width>.webp.
"""

LOCATIONS = []


def _l(**kw):
    """Each market supplies its own `alt`. The image paths are derived from
    the slug, so a replacement image is a file swap with no code change."""
    kw["img"] = f"img/markets/{kw['slug']}"
    LOCATIONS.append(kw)


# --------------------------------------------------------------------------
# Florida markets
# --------------------------------------------------------------------------

_l(
    slug="broward-county-fl",
    alt='A single storey concrete block ranch house with a barrel tile roof, carport and palm trees, typical of everyday residential Broward County, Florida',
    name="Broward County",
    region="Florida Markets",
    area="Broward County, Florida",
    state="FL",
    h1="Need to sell a property in Broward County?",
    h1_em="in Broward County?",
    title="Sell a Property in Broward County, Florida | MaliHaus",
    meta="Need to sell a property in Broward County? MaliHaus reviews homes in their current condition and explains which of its three selling approaches may fit. No repairs required.",
    card="One of the markets MaliHaus knows best, covering everything from coastal condominium ownership to inland single family homes carrying deferred maintenance.",
    opening=[
        "Broward County covers a lot of very different property, from older single family neighbourhoods well inland to coastal blocks and association governed communities. What those owners have in common is rarely the property itself. It is usually a situation that makes an ordinary listing difficult.",
        "MaliHaus reviews properties across Broward County in their current condition. Whether the issue is a roof at the end of its life, an association that has become expensive, a tenant you would rather not manage or a family property nobody has decided about, the starting point is the same. Tell us about the property and we will tell you which of our three routes may apply.",
    ],
    how=[
        "We begin with an inspection to understand condition, repair requirements and the overall scope of the project. That is what determines which of the three approaches is realistic, and it is why we do not put a number in front of anyone before we have looked properly.",
        "From there, one of three things tends to happen. The property meets our purchasing criteria and we buy it with our own cash. Or the project is larger than we would take on alone, in which case we may complete select repairs ourselves, with your written approval, to bring in an investor partner. Or it suits wider exposure, and we present it to investors through our national network so they can compete for it.",
    ],
    sit_intro=("Owners in Broward County contact us about the whole range of situations below. Insurance and "
               "association costs, roof condition and long standing tenancies come up frequently in South "
               "Florida, though the situation that applies to you is the one that matters."),
    featured=["major-repairs-as-is", "tired-landlords", "inherited-property-probate",
              "foreclosure-missed-payments", "fire-water-storm-damage", "financial-hardship"],
    faqs=[
        ("Do you cover the whole of Broward County?",
         "Yes. Tell us the address and we will review it, wherever in the county it sits."),
        ("My property is in an association and the dues have gone up a lot.",
         "Mention that at the start, along with any special assessment you know about. Association obligations affect what a property is worth to a buyer, so it is far better raised early than discovered during a title search."),
        ("The roof is old and I cannot get it insured.",
         "That is one of the more common reasons owners here contact us. We look at properties with roofs at the end of their life and we do not ask you to replace one before we will assess the property."),
        ("Is MaliHaus based in Broward County?",
         "MaliHaus is based in Boca Raton and serves Broward County. We do not operate a separate office in every market we work in, and we would not claim to."),
        ("I have a question about Florida foreclosure or probate procedure.",
         "That is a question for a Florida attorney, and we would be doing you a disservice by answering it ourselves. We can tell you whether a sale is realistic, which is a different question and one we can answer."),
    ],
    related=["miami-dade-county-fl", "orlando-fl", "tampa-fl"],
)

_l(
    slug="palm-beach-county-fl",
    alt='A single storey stucco ranch house with a weathered barrel tile roof, a carport, a cracked concrete driveway, a clipped hedge and sabal palms on a patchy lawn, on an ordinary flat residential street in Palm Beach County, Florida',
    name="Palm Beach County",
    region="Florida Markets",
    area="Palm Beach County, Florida",
    state="FL",
    h1="Need to sell a property in Palm Beach County?",
    h1_em="in Palm Beach County?",
    title="Sell a Property in Palm Beach County, Florida | MaliHaus",
    meta="Need to sell a property in Palm Beach County? MaliHaus reviews homes in their current condition and explains which of its three selling approaches may fit. No repairs required.",
    card="The county MaliHaus works from, running from the coast out to the western communities, where a great deal of the housing is ordinary single family and association governed property rather than the waterfront the county is known for.",
    opening=[
        "Palm Beach County is far broader than the stretch of coast it takes its name from. Most of its housing is ordinary: single family homes on quiet streets, association governed communities inland, older properties that have been in the same family for years and condominium ownership of every age and condition. Owners in all of it run into the same thing, which is a situation that makes an ordinary listing awkward.",
        "MaliHaus is based in Boca Raton and reviews properties across Palm Beach County in the condition they are in now. Whether the difficulty is a roof at the end of its life, an association cost that has climbed, a special assessment, a tenant you would rather not manage or a family property nobody has decided about, the starting point does not change. Tell us about the property and we will tell you which of our three routes may apply.",
    ],
    how=[
        "We begin with an inspection to understand condition, repair requirements and the overall scope of the project. That is what determines which of the three approaches is realistic, and it is why we do not put a number in front of anyone before we have looked properly.",
        "From there, one of three things tends to happen. The property meets our purchasing criteria and we buy it with our own cash. Or the project is larger than we would take on alone, in which case we may complete select repairs ourselves, with your written approval, to bring in an investor partner. Or it suits wider exposure, and we present it to investors through our national network so they can compete for it.",
    ],
    sit_intro=("Owners in Palm Beach County contact us about the whole range of situations below. Roof "
               "condition, insurance difficulty and association costs come up frequently in South Florida, "
               "though the situation that applies to you is the one that matters."),
    featured=["major-repairs-as-is", "inherited-property-probate", "tired-landlords",
              "foreclosure-missed-payments", "downsizing-senior-transition", "fire-water-storm-damage"],
    faqs=[
        ("Do you cover the whole of Palm Beach County?",
         "Yes. Tell us the address and we will review it, wherever in the county it sits, from the coastal municipalities to the western communities."),
        ("MaliHaus is in Boca Raton. Does that mean you only buy nearby?",
         "No. Boca Raton is where MaliHaus is based, not the limit of what it looks at. Properties across the county are reviewed the same way, and so are the other markets listed on this site."),
        ("My association dues have gone up and there is a special assessment coming.",
         "Raise that at the start, along with the amount if you know it. Association obligations affect what a property is worth to a buyer, so it is far better mentioned early than discovered during a title search."),
        ("The roof is at the end of its life and insurance has become difficult.",
         "That is one of the more common reasons owners here contact us. We look at properties with roofs in that condition and we do not ask you to replace one before we will assess the property."),
        ("I have a question about Florida foreclosure or probate procedure.",
         "That is a question for a Florida attorney, and we would be doing you a disservice by answering it ourselves. We can tell you whether a sale is realistic, which is a different question and one we can answer."),
    ],
    related=["broward-county-fl", "miami-dade-county-fl", "orlando-fl"],
)

_l(
    slug="miami-dade-county-fl",
    alt='A mid century mint green stucco house with jalousie windows, a decorative breeze block screen and a chain link fence, typical of everyday residential Miami-Dade County, Florida',
    name="Miami-Dade County",
    region="Florida Markets",
    area="Miami-Dade County, Florida",
    state="FL",
    h1="Looking for a practical way to sell in Miami-Dade County?",
    h1_em="in Miami-Dade County?",
    title="Sell a Property in Miami-Dade County, Florida | MaliHaus",
    meta="Looking for a practical way to sell in Miami-Dade County? MaliHaus reviews properties in their current condition, including inherited homes and properties owned from abroad.",
    card="Complicated ownership is common here, from properties held across generations to homes owned by people who now live in another country.",
    opening=[
        "A good number of the properties we are asked about in Miami-Dade County come with an ownership story attached. A home that has passed through two or three generations of a family, a property held by relatives spread between several countries, or one that has been rented out for so long that nobody remembers what condition it is actually in.",
        "MaliHaus can review properties in Miami-Dade County as they stand, and can work with owners who are not in Florida or not in the United States. What we need first is the property and an honest account of the situation, including the parts that are unresolved.",
    ],
    how=[
        "Every property starts with an inspection so we understand its condition and what the project would actually involve. That assessment is what tells us which of our three routes is realistic for this particular property.",
        "If it meets our purchasing criteria we buy it with our own cash. If it carries more risk than we would take alone we may, with your written approval, complete select repairs while it is under contract so that an investor partner will join us. And where wider exposure would serve you better, we present it to investors nationally and let them compete.",
    ],
    sit_intro=("The situations below come up across Miami-Dade County. Inherited property, ownership held by "
               "several family members and owners managing a property from overseas are particularly common "
               "reasons people get in touch."),
    featured=["inherited-property-probate", "title-problems-multiple-owners", "out-of-state-owner",
              "tired-landlords", "major-repairs-as-is", "vacant-abandoned-property"],
    faqs=[
        ("The owners are family members living in different countries. Can you still work with us?",
         "Yes. We work with authorised owners wherever they are, and documents are handled electronically where the title company allows it. Where several people are on the title, all of them need to agree before a sale could complete."),
        ("Nobody is certain who legally owns it any more.",
         "That is more common than people expect and it does need resolving before anything could complete. A title search establishes what is actually recorded, and an attorney in Florida deals with the rest. We can tell you whether the property is worth pursuing before you spend anything on that."),
        ("Does anyone need to speak Spanish or Creole to deal with you?",
         "Tell us what would be easiest when you first get in touch and we will do our best to accommodate it."),
        ("Do you have an office in Miami?",
         "No. MaliHaus is based in Boca Raton and serves Miami-Dade County. We are not going to invent a local office to look bigger than we are."),
    ],
    related=["broward-county-fl", "orlando-fl", "tampa-fl"],
)

_l(
    slug="jacksonville-fl",
    alt='A red brick ranch house with a carport, set among tall pines and live oaks draped in Spanish moss, typical of everyday residential Jacksonville, Florida',
    name="Jacksonville",
    region="Florida Markets",
    area="Jacksonville, Florida",
    state="FL",
    h1="Need to sell a property in Jacksonville?",
    h1_em="in Jacksonville?",
    title="Sell a Property in Jacksonville, Florida | MaliHaus",
    meta="Need to sell a property in Jacksonville? MaliHaus reviews homes across the city in their current condition and explains which of its three selling approaches may fit.",
    card="A city large enough that two properties a few miles apart can present entirely differently. Each one is assessed on its own condition.",
    opening=[
        "Jacksonville covers an unusually large area for a single city, and that has a practical consequence for anyone selling. Two properties a short drive apart can be completely different propositions, and a general opinion about what things are worth in Jacksonville is not much use to any individual owner.",
        "MaliHaus assesses properties in Jacksonville individually, on their own condition and their own circumstances. Whether the property is occupied, tenanted, empty or in the middle of a repair nobody finished, we will review it as it stands.",
    ],
    how=[
        "We inspect the property first. Condition, the repairs it needs and the overall scope of the work are what determine which of our three routes is open, so that assessment comes before any figure is discussed.",
        "Depending on what we find we may purchase it directly with our own cash, or complete select repairs ourselves with your written approval to bring in an investor partner, or present it to investors across the country through our national network so they can compete for it.",
    ],
    sit_intro=("Owners get in touch about all of the situations below. Relocation, rental properties that have "
               "stopped being worth the effort and homes inherited by someone who lives elsewhere come up "
               "regularly in Jacksonville."),
    featured=["relocation", "tired-landlords", "inherited-property-probate",
              "out-of-state-owner", "major-repairs-as-is", "sell-house-fast"],
    faqs=[
        ("I am being relocated and have to be gone by a fixed date.",
         "Tell us the date at the start and we will work to it rather than around it. If you need to stay in the property for a period after closing, that is worth raising early because it is much easier to build in than to negotiate later."),
        ("Do you cover the whole city?",
         "Yes. Jacksonville is a large area and we assess each property individually rather than by neighbourhood reputation."),
        ("The property is rented and I live somewhere else.",
         "That is a common combination and it is not a problem. Tell us what the lease says and we will coordinate access with the tenant or the property manager rather than asking you to arrange it."),
        ("Will you need me to come to Jacksonville?",
         "Generally not. We can review the property remotely and handle documents electronically where the title company permits it."),
    ],
    related=["orlando-fl", "tampa-fl", "broward-county-fl"],
)

_l(
    slug="tampa-fl",
    alt='A 1920s craftsman bungalow with a deep front porch and tapered columns, shaded by a live oak, typical of the older residential neighbourhoods of Tampa, Florida',
    name="Tampa",
    region="Florida Markets",
    area="Tampa, Florida",
    state="FL",
    h1="Considering selling a property in Tampa?",
    h1_em="in Tampa?",
    title="Sell a Property in Tampa, Florida | MaliHaus",
    meta="Considering selling a property in Tampa? MaliHaus reviews properties in their current condition, including rentals and homes carrying years of deferred maintenance.",
    card="Older homes carrying deferred maintenance and rental properties that have stopped paying for the work they need are frequent reasons owners call.",
    opening=[
        "A property that has been held for a long time in Tampa often reaches a point where several things need doing at once. A roof, a system, a repair that was deferred through two or three tenancies, and an insurance renewal that has started asking questions about all of it.",
        "MaliHaus reviews properties in Tampa in whatever condition they are in. You are not expected to bring it up to standard first, and we would rather you spoke to us before spending money on it than afterwards.",
    ],
    how=[
        "The process starts with a full inspection so we understand the condition and the real scope of the work. Only then does it become clear which of our three approaches fits this particular property.",
        "If it meets our purchasing criteria we buy it outright with our own cash. If the project is heavier than we want to carry alone we may complete select repairs first, with your written approval and our own money, so an investor partner will come in with us. Or we present it to our national investor network and let qualified buyers compete for it.",
    ],
    sit_intro=("The situations below are the ones owners contact us about. Condition, long held rental "
               "properties and financial pressure from rising ownership costs come up often around Tampa."),
    featured=["major-repairs-as-is", "tired-landlords", "financial-hardship",
              "vacant-abandoned-property", "inherited-property-probate", "expired-listing"],
    faqs=[
        ("The house needs more work than I can afford to do.",
         "That is one of the main reasons owners contact us and it is not a reason for us to walk away. Tell us what you know is wrong with it, including the things you have been putting off."),
        ("I already had it listed and it did not sell.",
         "Tell us what happened, particularly whether it went under contract and then came back. A property failing repeatedly at the buyer's lender is a different problem from one that never attracted an offer, and the answers are different too."),
        ("My insurance renewal has become unaffordable.",
         "It is worth raising at the start, because it usually points at something about the property's condition that will matter to any buyer. We can factor it into the assessment."),
        ("Are you actually based in Tampa?",
         "No. MaliHaus is based in Boca Raton and serves Tampa. We do not claim local offices we do not have."),
    ],
    related=["orlando-fl", "jacksonville-fl", "broward-county-fl"],
)

_l(
    slug="orlando-fl",
    alt='A two storey stucco house with a barrel tile roof and attached garage on a planned subdivision street, typical of suburban Orlando, Florida',
    name="Orlando",
    region="Florida Markets",
    area="Orlando, Florida",
    state="FL",
    h1="Need another way to sell a property in Orlando?",
    h1_em="in Orlando?",
    title="Sell a Property in Orlando, Florida | MaliHaus",
    meta="Need another way to sell a property in Orlando? MaliHaus reviews properties in their current condition, including rentals and homes owned from out of state.",
    card="A market where a large share of owners live somewhere else, which makes repairs, tenants and paperwork harder to manage.",
    opening=[
        "A great many Orlando properties are owned by people who do not live in Orlando. That works perfectly well until something needs attention, and then every quote, every repair and every question about the property needs somebody physically there.",
        "MaliHaus works with owners at a distance as a matter of routine. We can review a property in Orlando without you travelling for it, coordinate access with a tenant or a property manager, and tell you which of our three routes may apply.",
    ],
    how=[
        "It begins with an inspection of the property, which we arrange. We are establishing its condition, what it would need and the scope of the project, because that is what decides which route is realistic.",
        "We may then buy it directly with our own cash if it meets our purchasing criteria. Where the project is larger, we may with your written approval complete select repairs ourselves in order to bring an investor partner in alongside us. Or we take it to our national investor network, where buyers across the country can compete for it.",
    ],
    sit_intro=("These are the situations Orlando owners raise with us. Distance ownership, rental properties "
               "and relocation are particularly common, though every one of the sixteen applies to somebody."),
    featured=["out-of-state-owner", "tired-landlords", "relocation",
              "vacant-abandoned-property", "major-repairs-as-is", "inherited-property-probate"],
    faqs=[
        ("I live in another state and have not seen the property in years.",
         "That is a normal starting point for us. Tell us what you do know, and we will arrange the inspection and coordinate access from our side."),
        ("It has been used as a short term rental. Does that change anything?",
         "Tell us how it has been used and what furniture and equipment is in it, along with any association or local registration requirements you are aware of. It is all relevant to the assessment."),
        ("Can everything be handled remotely?",
         "In most cases yes. Documents are handled electronically where the title company allows it, and remote notarisation is available in many situations. We will confirm what applies before anything needs signing."),
        ("The tenant will not let anyone in.",
         "Tell us at the start. Access is worth resolving before anything else, and your obligations to the tenant are set by the lease and by Florida law regardless of who the buyer is."),
    ],
    related=["tampa-fl", "jacksonville-fl", "miami-dade-county-fl"],
)

# --------------------------------------------------------------------------
# National markets
# --------------------------------------------------------------------------

_l(
    slug="cleveland-oh",
    alt='A white American Foursquare house with a full width front porch and a detached garage, bare autumn trees and a wet street, typical of everyday residential Cleveland, Ohio',
    name="Cleveland",
    region="National Markets",
    area="Cleveland, Ohio",
    state="OH",
    h1="Need to sell a property in Cleveland?",
    h1_em="in Cleveland?",
    title="Sell a Property in Cleveland, Ohio | MaliHaus",
    meta="Need to sell a property in Cleveland? MaliHaus reviews properties in their current condition, including vacant homes and rentals owned from out of state.",
    card="Vacant properties and rentals owned from elsewhere are two of the most common reasons owners here get in touch.",
    opening=[
        "Two situations come up again and again with Cleveland properties. One is a house standing empty, where the costs and the code letters have kept arriving long after anyone lived in it. The other is a rental bought from a distance that has turned out to need more attention than it returns.",
        "MaliHaus reviews properties in Cleveland in their current condition, including ones that have been empty for years. Nothing has to be repaired, cleared or made presentable before we will look at it, and the national investor network gives us a route for properties that suit wider exposure.",
    ],
    how=[
        "We inspect the property to establish its condition and the real scope of the work. That is the step that decides which of our three approaches is open, and it happens before any figure is put in front of you.",
        "The property may meet our purchasing criteria, in which case we buy it with our own cash. It may carry more risk than we would take alone, in which case we may complete select repairs ourselves with your written approval and bring in an investor partner. Or it may be best served by exposure to investors across the country, competing for it through our national network.",
    ],
    sit_intro=("Owners here contact us about the situations below. Vacancy, distance ownership and properties "
               "carrying code or tax issues are the ones that come up most in and around Cleveland."),
    featured=["vacant-abandoned-property", "out-of-state-owner", "tired-landlords",
              "tax-liens-code-violations", "inherited-property-probate", "major-repairs-as-is"],
    faqs=[
        ("The property has been vacant for several years and is in poor condition.",
         "That is one of the situations we look at most. Length of vacancy and condition are factors in the assessment, not reasons to stop the conversation."),
        ("I bought it as a rental from out of state and it has been nothing but trouble.",
         "A common story, and you do not need to travel to deal with it. We can arrange the inspection and coordinate access from our side."),
        ("There are code violations recorded against it.",
         "Tell us what you know at the start. Whether they can be addressed as part of a transaction depends on what they are and on local rules, and those questions have to be confirmed by the appropriate professionals in Ohio."),
        ("Do you have an office in Cleveland?",
         "No. MaliHaus serves Cleveland through its own purchasing capacity and its national investor network. We do not operate an office there and we will not pretend otherwise."),
        ("Winter has caused damage while it was empty.",
         "Tell us what happened, including anything you know about frozen pipes or water that got in. We assess properties with that kind of damage rather than requiring it to be repaired first."),
    ],
    related=["akron-oh", "dayton-oh", "cincinnati-oh"],
)

_l(
    slug="memphis-tn",
    alt='A single storey brick ranch house with a carport and a flowering crepe myrtle in the front yard, typical of everyday residential Memphis, Tennessee',
    name="Memphis",
    region="National Markets",
    area="Memphis, Tennessee",
    state="TN",
    h1="Considering selling a property in Memphis?",
    h1_em="in Memphis?",
    title="Sell a Property in Memphis, Tennessee | MaliHaus",
    meta="Considering selling a property in Memphis? MaliHaus reviews rentals, vacant homes and inherited properties in their current condition, including for owners living elsewhere.",
    card="A market where a large share of single family homes are owned as rentals, often by people who live a long way away.",
    opening=[
        "A lot of the Memphis properties we are asked about are single family homes bought as rentals, frequently by owners who have never stood in front of them. The arrangement works while the property is tenanted and quiet. It stops working when a tenancy ends badly, or when the repairs start outrunning the rent.",
        "MaliHaus reviews properties in Memphis as they stand, tenanted or empty. You do not need to end a tenancy, complete repairs or travel to the property before we will assess it.",
    ],
    how=[
        "An inspection comes first, because condition and the true scope of the repairs decide everything that follows. We arrange it, including coordinating access with a tenant or property manager where there is one.",
        "From there we may buy the property with our own cash if it meets our purchasing criteria. Where the project is heavier, we may with your written approval invest our own money in select repairs so an investor partner will join the purchase. Or we present it through our national investor network and let qualified buyers compete.",
    ],
    sit_intro=("These are the situations owners bring to us. Rental fatigue, distance ownership and inherited "
               "property are the most frequent around Memphis, though all sixteen apply to somebody."),
    featured=["tired-landlords", "out-of-state-owner", "inherited-property-probate",
              "vacant-abandoned-property", "major-repairs-as-is", "financial-hardship"],
    faqs=[
        ("The property still has a tenant in it. Can you review it?",
         "Yes, and in some cases a tenant in place makes it a stronger proposition for an investor rather than a weaker one. Have the lease to hand when we speak."),
        ("I own several properties there. Can they be looked at together?",
         "Yes. Tell us about the portfolio and we will assess them together rather than one at a time."),
        ("The last tenant left it in a poor state.",
         "Tell us what was left behind and what was damaged. We look at properties in that condition and we do not ask you to make good first."),
        ("I have never actually been to the property.",
         "That is not unusual with rentals bought at a distance, and it is not a problem. We arrange the inspection and report back on what is actually there."),
    ],
    related=["birmingham-al", "indianapolis-in", "kansas-city"],
)

_l(
    slug="birmingham-al",
    alt='A brick ranch house set above the road on a sloped wooded lot with steps up from the pavement and exposed red clay, typical of everyday residential Birmingham, Alabama',
    name="Birmingham",
    region="National Markets",
    area="Birmingham, Alabama",
    state="AL",
    h1="Need a practical way to sell a property in Birmingham?",
    h1_em="in Birmingham?",
    title="Sell a Property in Birmingham, Alabama | MaliHaus",
    meta="Need a practical way to sell a property in Birmingham? MaliHaus reviews inherited homes, rentals and properties with complicated ownership in their current condition.",
    card="Family property held for a long time, sometimes with ownership that was never formally sorted out, is a frequent starting point here.",
    opening=[
        "A recurring situation with Birmingham properties is a house that has been in one family for a long time. Sometimes ownership was never formally settled after somebody died, sometimes several relatives now hold a share, and often nobody has wanted to be the one to raise it.",
        "MaliHaus can review the property and identify what would need clarifying for a sale to be possible. That is usually a more useful first step than paying for professional advice before anyone knows whether the property is worth pursuing at all.",
    ],
    how=[
        "The starting point is an inspection to establish condition and the scope of any work. Alongside that, where ownership is unclear, a title search establishes what is actually recorded rather than what the family remembers.",
        "Depending on what both turn up, we may purchase the property with our own cash, or complete select repairs ourselves with your written approval to bring in an investor partner, or present it to investors across the country through our national network.",
    ],
    sit_intro=("The situations below are the ones owners raise with us. Inherited property and questions about "
               "who is entitled to sell come up particularly often in Birmingham."),
    featured=["inherited-property-probate", "title-problems-multiple-owners", "vacant-abandoned-property",
              "tired-landlords", "major-repairs-as-is", "financial-hardship"],
    faqs=[
        ("The house has been in the family for decades and we are not sure who owns it now.",
         "That has to be established before any sale could complete, and it is a question for an attorney in Alabama. A title search shows what is recorded, and we can tell you whether the property is worth pursuing before you commit to professional fees."),
        ("Several cousins have a share and one of them cannot be found.",
         "A sale needs everyone who is entitled to sign, so that does need resolving. It is not unusual and it is not automatically the end of the road, but it is legal work rather than something we can do."),
        ("Nobody has lived in it for years.",
         "We assess long vacant properties in whatever condition they are in. Tell us roughly how long it has been empty and whether the utilities are still connected."),
        ("Do you have staff in Birmingham?",
         "No. MaliHaus serves Birmingham through its own purchasing capacity and its national investor network, and does not operate a local office or employ local staff."),
    ],
    related=["memphis-tn", "charlotte-nc", "greensboro-nc"],
)

_l(
    slug="kansas-city",
    alt='A 1950s brick and siding ranch house with a low front stoop and a detached garage on a flat tree lined street, typical of everyday residential neighbourhoods in the Kansas City area',
    name="Kansas City",
    region="National Markets",
    area="the Kansas City area",
    state="",
    kc_unresolved=True,
    h1="Need to sell a property in the Kansas City area?",
    h1_em="in the Kansas City area?",
    title="Sell a Property in the Kansas City Area | MaliHaus",
    meta="Need to sell a property in the Kansas City area? MaliHaus reviews properties in their current condition, including rentals, vacant homes and inherited property.",
    card="The metropolitan area spans a state line, so the first thing worth establishing is exactly where a property sits.",
    opening=[
        "The Kansas City metropolitan area spans a state line, which matters more than it might sound. Which side of that line a property sits on affects the professionals you would need and the rules that apply to it, so establishing the exact location is the first practical step rather than a detail to sort out later.",
        "MaliHaus reviews properties across the Kansas City area in their current condition. Give us the address and the situation and we will tell you which of our three approaches may apply.",
    ],
    how=[
        "We inspect the property to understand its condition, the repairs it needs and the scope of the project. That assessment is what determines which of the three routes is realistic.",
        "We may buy it directly with our own cash where it meets our purchasing criteria. Where the project carries more risk, we may with your written approval complete select repairs ourselves in order to bring an investor partner in. Or we present it to investors nationwide, who can compete to purchase it.",
    ],
    sit_intro=("Owners in the Kansas City area contact us about the situations below. Rental properties, "
               "vacancy and inherited homes are among the most common."),
    featured=["tired-landlords", "vacant-abandoned-property", "inherited-property-probate",
              "out-of-state-owner", "major-repairs-as-is", "sell-house-fast"],
    faqs=[
        ("My property is on the Kansas side. Is that a problem?",
         "No. Tell us the full address at the start. Which state a property sits in affects the professionals involved and the procedures that apply, so it is worth being precise from the beginning."),
        ("Does it matter which side of the state line it is on?",
         "For the review itself, no. For the legal and title work that follows a decision to sell, yes, because those follow the law of the state the property is in. We will make sure the right professionals are involved."),
        ("The property is tenanted.",
         "That is fine and we will review it as it stands. Have the lease to hand, because your obligations to the tenant follow the law of the state the property is in."),
        ("Do you have an office in Kansas City?",
         "No. MaliHaus serves the Kansas City area through its own purchasing capacity and its national investor network. There is no local office and no local telephone number."),
    ],
    related=["indianapolis-in", "memphis-tn", "cincinnati-oh"],
)

_l(
    slug="indianapolis-in",
    alt='A 1920s brick bungalow with a covered front porch and a detached garage, mature shade trees along the street, typical of everyday residential Indianapolis, Indiana',
    name="Indianapolis",
    region="National Markets",
    area="Indianapolis, Indiana",
    state="IN",
    h1="Looking for another way to sell a property in Indianapolis?",
    h1_em="in Indianapolis?",
    title="Sell a Property in Indianapolis, Indiana | MaliHaus",
    meta="Looking for another way to sell a property in Indianapolis? MaliHaus reviews rentals, vacant properties and homes needing significant repair in their current condition.",
    card="Rental properties that have stopped justifying the work, and homes carrying repairs the owner does not want to take on.",
    opening=[
        "The Indianapolis properties we are asked about most are ones where the maths has quietly changed. A rental that needs more each year than it returns, or a house where the list of repairs has grown to the point that an ordinary sale has become difficult.",
        "MaliHaus reviews properties in Indianapolis in their current condition, tenanted or empty, and explains which of the three selling routes may fit. You are not asked to make repairs or end a tenancy first.",
    ],
    how=[
        "Everything starts with an inspection so we can see the condition for ourselves and understand the true scope of the work rather than working from a description.",
        "If the property meets our purchasing criteria we buy it with our own cash. If it is a heavier project we may, with your written approval, invest our own money in select repairs while it is under contract, which makes it a stronger proposition for an investor partner. Or we present it to our national investor network for qualified buyers to compete over.",
    ],
    sit_intro=("These are the situations owners bring to us. Rental fatigue, condition and vacancy are the "
               "ones raised most often in Indianapolis."),
    featured=["tired-landlords", "major-repairs-as-is", "vacant-abandoned-property",
              "out-of-state-owner", "inherited-property-probate", "expired-listing"],
    faqs=[
        ("The repairs needed are more than the property is likely worth.",
         "Tell us and we will be straight with you about it. If a sale would not put you in a better position, we would rather say so than take up weeks of your time."),
        ("I have a tenant who has stopped paying.",
         "Tell us at the start, because it affects what is realistic. Your options regarding the tenancy follow Indiana law and are a matter for a local attorney, separate from anything we would discuss."),
        ("It has been on the market for months with no offers.",
         "Worth telling us what feedback you had. Condition, price and the financing available to likely buyers are different problems with different answers."),
        ("Are you based in Indianapolis?",
         "No. MaliHaus serves Indianapolis through its own purchasing capacity and its national investor network, without a local office."),
    ],
    related=["cincinnati-oh", "dayton-oh", "kansas-city"],
)

_l(
    slug="cincinnati-oh",
    alt='A narrow two storey brick house standing above the street on a hillside lot, with a concrete retaining wall and steps climbing to the front door, typical of everyday residential Cincinnati, Ohio',
    name="Cincinnati",
    region="National Markets",
    area="Cincinnati, Ohio",
    state="OH",
    h1="Need to sell a property in Cincinnati?",
    h1_em="in Cincinnati?",
    title="Sell a Property in Cincinnati, Ohio | MaliHaus",
    meta="Need to sell a property in Cincinnati? MaliHaus reviews properties in their current condition, including older homes with structural, basement or water problems.",
    card="Older homes with structural, basement or water problems that make a conventionally financed sale difficult.",
    opening=[
        "Where a Cincinnati property has a problem that worries a mortgage lender, the ordinary sale route gets complicated quickly. Structural movement, a basement that takes water, or a system that has not been touched in decades will all give an incoming buyer's lender pause, however willing the buyer is.",
        "MaliHaus reviews properties with exactly those problems. We are not asking you to fix them first, and we would rather see the property honestly than have it tidied up for us.",
    ],
    how=[
        "The inspection comes first and it matters more than usual with this kind of property. We need to understand what is actually going on structurally and what the repair scope really is.",
        "Once we know, we may purchase the property with our own cash if it meets our criteria. If it is a bigger project than we would take alone, we may complete select repairs ourselves with your written approval to bring in an investor partner. Or we present it to investors across the country and let them compete for it.",
    ],
    sit_intro=("Owners contact us about the situations below. Condition, inherited property and vacancy are "
               "the most common around Cincinnati."),
    featured=["major-repairs-as-is", "inherited-property-probate", "vacant-abandoned-property",
              "fire-water-storm-damage", "tired-landlords", "tax-liens-code-violations"],
    faqs=[
        ("The basement takes water every time it rains.",
         "Tell us. It is exactly the sort of thing that stops a conventionally financed sale and exactly the sort of thing we expect to find when we inspect."),
        ("An engineer has told me there is structural movement.",
         "Share the report if you have one. It saves time and it means we are assessing the property on real information rather than on a guess."),
        ("Do I need to get repair quotes first?",
         "No. If you already have them they are useful, but obtaining them is not something we ask of you."),
        ("Is there a MaliHaus office in Cincinnati?",
         "No. MaliHaus serves Cincinnati through its own purchasing capacity and its national investor network. There is no local office and no separate local number."),
    ],
    related=["dayton-oh", "cleveland-oh", "indianapolis-in"],
)

_l(
    slug="charlotte-nc",
    alt='A brick ranch house with a carport, azaleas and a flowering dogwood among tall pines, typical of everyday residential Charlotte, North Carolina',
    name="Charlotte",
    region="National Markets",
    area="Charlotte, North Carolina",
    state="NC",
    h1="Considering selling a property in Charlotte?",
    h1_em="in Charlotte?",
    title="Sell a Property in Charlotte, North Carolina | MaliHaus",
    meta="Considering selling a property in Charlotte? MaliHaus reviews properties in their current condition, including relocations, expired listings and rentals.",
    card="Job moves and unsold listings are two of the most common reasons owners in this market get in touch.",
    opening=[
        "Two things bring Charlotte owners to us more than anything else. A job move with a date attached that a normal sale cannot comfortably meet, and a property that was listed properly and simply did not sell.",
        "MaliHaus can review the property, tell you honestly why it is likely not selling if that is the situation, and explain which of our three routes may apply. If the answer is that relisting would serve you better, we will say so.",
    ],
    how=[
        "An inspection establishes the property's condition and the scope of any work needed, which is what determines the route. With an unsold property it also tends to reveal why it stalled.",
        "We may then buy it with our own cash if it meets our purchasing criteria, or complete select repairs ourselves with your written approval so an investor partner will join us, or present it to our national investor network where buyers can compete for it.",
    ],
    sit_intro=("These are the situations owners raise. Relocation, expired listings and rental properties are "
               "the most frequent in Charlotte."),
    featured=["relocation", "expired-listing", "sell-house-fast",
              "tired-landlords", "major-repairs-as-is", "divorce-separation"],
    faqs=[
        ("My listing expired and I do not know why it did not sell.",
         "Tell us what feedback you had and whether it ever went under contract. A property that repeatedly fell through has a different problem from one that never attracted an offer."),
        ("My listing agreement is still running.",
         "Say so at the start. Depending on your agreement there may be obligations to your agent that need respecting first, and it is better to establish that before anything else."),
        ("I have to relocate for work by a fixed date.",
         "Tell us the date. Where we buy directly there is no lender on our side, which removes the most common cause of a sale slipping."),
        ("Do you have people in Charlotte?",
         "No. MaliHaus serves Charlotte through its own purchasing capacity and its national investor network. We do not operate a local office."),
    ],
    related=["greensboro-nc", "winston-salem-nc", "birmingham-al"],
)

_l(
    slug="dayton-oh",
    alt='A post war Cape Cod house with dormer windows and pale siding on a flat street with bare winter trees, typical of everyday residential Dayton, Ohio',
    name="Dayton",
    region="National Markets",
    area="Dayton, Ohio",
    state="OH",
    h1="Need a practical way to sell a property in Dayton?",
    h1_em="in Dayton?",
    title="Sell a Property in Dayton, Ohio | MaliHaus",
    meta="Need a practical way to sell a property in Dayton? MaliHaus reviews vacant homes, inherited properties and rentals in their current condition.",
    card="Empty properties and inherited homes that nobody has been able to make a decision about.",
    opening=[
        "The Dayton properties we hear about most are ones where a decision has been deferred. A house that was inherited and then left, or one that emptied out after a tenancy ended and never got dealt with. Meanwhile the taxes, the insurance and occasionally the letters from the city keep arriving.",
        "MaliHaus reviews properties in Dayton as they are, however long they have been sitting. Nothing needs to be repaired, cleared or made presentable before we will look.",
    ],
    how=[
        "We inspect the property to establish its condition and the real scope of what it would take. That decides which of the three routes is realistic.",
        "The property may meet our purchasing criteria, in which case we buy it with our own cash. It may need select repairs first, which we may complete ourselves with your written approval in order to bring in an investor partner. Or it may suit exposure to investors nationally, competing for it through our network.",
    ],
    sit_intro=("Owners contact us about the situations below. Vacancy, inherited property and accumulated code "
               "or tax issues are the ones raised most in Dayton."),
    featured=["vacant-abandoned-property", "inherited-property-probate", "tax-liens-code-violations",
              "tired-landlords", "major-repairs-as-is", "hoarder-house-cleanout"],
    faqs=[
        ("It has been empty for a long time and I have been ignoring it.",
         "That is a very common position and it is not a reason to keep ignoring it. Empty properties tend to get harder rather than easier, so a review now is worth more than a review later."),
        ("There are unpaid taxes on it.",
         "Tell us roughly how long. Where the process has reached matters a great deal to what remains possible, and it is confirmed through the county rather than assumed."),
        ("It is full of a relative's belongings.",
         "You do not need to clear it. Take what matters to the family and leave the rest, and please speak to us before paying for a clearance."),
        ("Is MaliHaus located in Dayton?",
         "No. MaliHaus serves Dayton through its own purchasing capacity and its national investor network, with no local office."),
    ],
    related=["cincinnati-oh", "akron-oh", "cleveland-oh"],
)

_l(
    slug="akron-oh",
    alt='A 1930s pale green wood sided bungalow with a covered front porch and a detached garage on a damp autumn street, typical of everyday residential Akron, Ohio',
    name="Akron",
    region="National Markets",
    area="Akron, Ohio",
    state="OH",
    h1="Looking for another way to sell a property in Akron?",
    h1_em="in Akron?",
    title="Sell a Property in Akron, Ohio | MaliHaus",
    meta="Looking for another way to sell a property in Akron? MaliHaus reviews rentals, vacant homes and properties needing significant repair in their current condition.",
    card="Rentals that have run out of road and older homes where the repair list has grown past what an ordinary buyer will take on.",
    opening=[
        "Akron properties reach us in two main states. Rentals that have quietly stopped being worth the management, and houses where the repair list has grown past the point an ordinary financed buyer will take on.",
        "MaliHaus reviews both, as they stand. There is no requirement to repair, empty or prepare the property, and we would rather assess it honestly than have it presented at its best.",
    ],
    how=[
        "The inspection is first, so we understand the condition and the genuine scope of the project rather than the version in the listing photographs.",
        "From there we may buy the property outright with our own cash, or invest our own money in select repairs with your written approval so that an investor partner joins the purchase, or present it to investors across the country through our national network.",
    ],
    sit_intro=("These are the situations owners bring to us. Rental fatigue, condition and vacancy are the most "
               "frequent around Akron."),
    featured=["tired-landlords", "major-repairs-as-is", "vacant-abandoned-property",
              "out-of-state-owner", "inherited-property-probate", "financial-hardship"],
    faqs=[
        ("I am done being a landlord. What do you need from me?",
         "The address, the condition as you understand it, and the lease if there is a tenant. That is enough to begin."),
        ("The property will not pass a lender's inspection.",
         "That is one of the more common reasons owners contact us, and it is precisely what the three routes exist to work around."),
        ("Can you review more than one property at a time?",
         "Yes. If you have several, tell us and we will look at them together."),
        ("Do you have an office in Akron?",
         "No. MaliHaus serves Akron through its own purchasing capacity and its national investor network, without a local office or a local number."),
    ],
    related=["cleveland-oh", "dayton-oh", "cincinnati-oh"],
)

_l(
    slug="greensboro-nc",
    alt='A red brick ranch house with a carport and a picture window, backed by tall loblolly pines, typical of everyday residential Greensboro, North Carolina',
    name="Greensboro",
    region="National Markets",
    area="Greensboro, North Carolina",
    state="NC",
    h1="Need to sell a property in Greensboro?",
    h1_em="in Greensboro?",
    title="Sell a Property in Greensboro, North Carolina | MaliHaus",
    meta="Need to sell a property in Greensboro? MaliHaus reviews inherited homes, rentals and properties needing repair in their current condition.",
    card="Inherited family homes and long held rentals, in a market MaliHaus covers alongside neighbouring Winston-Salem.",
    opening=[
        "Greensboro sits alongside Winston-Salem in the same part of North Carolina, and we treat the two as one working area. The properties owners ask us about are frequently family homes held for a long time, or rentals that have been kept well past the point they were enjoyable to own.",
        "MaliHaus reviews properties in Greensboro in their current condition, and can work with owners who live elsewhere. Repairs and clearances are not something you need to arrange first.",
    ],
    how=[
        "We start with an inspection to establish condition and the scope of the work, which is what determines which of our three routes applies.",
        "Depending on that, we may purchase the property with our own cash, complete select repairs ourselves with your written approval to bring an investor partner in, or present it to investors across the country through our national network so they can compete for it.",
    ],
    sit_intro=("The situations below are the ones owners raise. Inherited property, rentals and downsizing "
               "come up most often in Greensboro."),
    featured=["inherited-property-probate", "tired-landlords", "downsizing-senior-transition",
              "major-repairs-as-is", "out-of-state-owner", "vacant-abandoned-property"],
    faqs=[
        ("I inherited a house here but live in another state.",
         "A common combination and one we work with routinely. We arrange the inspection and coordinate everything locally so you do not have to travel for it."),
        ("My parents want to move somewhere smaller but the house needs updating.",
         "It is worth speaking to us before spending anything on it. Updating a home you are leaving is rarely money that comes back, and a period of occupancy after closing can often be arranged."),
        ("Do you cover Winston-Salem as well?",
         "Yes. Greensboro and Winston-Salem are both markets we serve and we treat them as a single working area."),
        ("Are you based in North Carolina?",
         "No. MaliHaus serves Greensboro through its own purchasing capacity and its national investor network. There is no local office."),
    ],
    related=["winston-salem-nc", "charlotte-nc", "birmingham-al"],
)

_l(
    slug="winston-salem-nc",
    alt='A two storey red brick colonial style house with black shutters and a low hedge on an established tree lined street, typical of everyday residential Winston-Salem, North Carolina',
    name="Winston-Salem",
    region="National Markets",
    area="Winston-Salem, North Carolina",
    state="NC",
    h1="Considering selling a property in Winston-Salem?",
    h1_em="in Winston-Salem?",
    title="Sell a Property in Winston-Salem, North Carolina | MaliHaus",
    meta="Considering selling a property in Winston-Salem? MaliHaus reviews properties in their current condition, including homes being sold as part of a downsizing or an estate.",
    card="Long held family homes, downsizing moves and estates, covered alongside neighbouring Greensboro.",
    opening=[
        "Winston-Salem sits in the same part of North Carolina as Greensboro and we cover the two together. A large share of the properties we are asked about here are homes somebody has lived in for a very long time, being sold as part of a downsizing, a move into care or an estate.",
        "Those sales are rarely urgent and they should not be rushed. MaliHaus reviews the property in its current condition and works to a realistic schedule, with family members and advisers involved wherever that helps.",
    ],
    how=[
        "The process begins with an inspection so we understand the property's condition and the scope of any work. That establishes which of the three approaches is realistic.",
        "We may buy the property directly with our own cash where it meets our purchasing criteria. Where more is needed, we may complete select repairs ourselves with your written approval so an investor partner will join the purchase. Or we take it to our national investor network for qualified buyers to compete over.",
    ],
    sit_intro=("Owners contact us about the situations below. Downsizing, inherited property and homes needing "
               "significant updating are the most common in Winston-Salem."),
    featured=["downsizing-senior-transition", "inherited-property-probate", "major-repairs-as-is",
              "hoarder-house-cleanout", "tired-landlords", "vacant-abandoned-property"],
    faqs=[
        ("My mother needs to move into assisted living and the house is full.",
         "You do not need to clear it. Take what the family wants and leave the rest, and please speak to us before paying for a clearance."),
        ("Can we stay in the house for a while after selling?",
         "Tell us what you need at the start. A period of occupancy after closing can often be arranged and is much easier to agree upfront than later."),
        ("I hold power of attorney for a parent.",
         "That may be sufficient and we would need to see the documentation. The title company confirms what is required before anything proceeds."),
        ("Do you cover Greensboro too?",
         "Yes. We treat Winston-Salem and Greensboro as one working area."),
    ],
    related=["greensboro-nc", "charlotte-nc", "cincinnati-oh"],
)

LOC_BY_SLUG = {l["slug"]: l for l in LOCATIONS}
FLORIDA = [l for l in LOCATIONS if l["region"] == "Florida Markets"]
NATIONAL = [l for l in LOCATIONS if l["region"] == "National Markets"]
