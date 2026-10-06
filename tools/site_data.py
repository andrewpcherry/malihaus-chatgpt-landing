#!/usr/bin/env python3
"""All MaliHaus site copy, in one place.

Shared constants, the sixteen situations and the sixteen markets.
tools/build_site.py renders them. Nothing in here knows about HTML
beyond the odd inline emphasis, and the telephone number is deliberately
absent: site.js owns it.

Rules baked in and not to be broken:
  * No guarantees. Not to buy, not on price, not on timing, not on
    stopping a foreclosure, not on resolving a legal problem.
  * No fabricated local offices, employees, transaction history,
    testimonials, market statistics, property values or telephone numbers.
  * No unverified claims about local law, foreclosure procedure, probate
    rules or tax matters. Where a local legal question comes up the page
    sends the reader to a local professional instead of answering it.
  * Coverage language is the approved line below and nothing else.
"""

ROOT = "https://www.malihaus.com"

COVERAGE = "Serving homeowners across Florida and selected markets nationwide."
REVIEW_LINE = "Rated 4.8 stars by more than 400 MaliHaus clients"
REVIEW_URL = "https://www.experience.com/reviews/michael-mali"
# Michael asked on 2026-09-03 for the Google listing to sit alongside the
# Experience.com link wherever the review proof appears, not only on the
# home page. Both figures are his, from the 2026-09-02 build brief.
GOOGLE_URL = "https://www.google.com/search?q=Malihaus+Capital+Boca+Raton"
GOOGLE_SCORE = "5.0"
GOOGLE_LINE = "29 reviews on our Google listing"
EXPERIENCE_SCORE = "4.8"
EXPERIENCE_LINE = "Rated 4.8 stars by more than 400 MaliHaus clients"

NATIONAL_STRAP = "Local market knowledge supported by a national investor network."

# Michael's exact wording, supplied 2026-09-03. Do not reword or paraphrase.
NATIONAL_SUPPORT = ("Your property deserves more than a one-size-fits-all offer. We evaluate it first, "
                    "then determine the best path forward: a direct purchase, an improved property paired "
                    "with an investor partner, or competitive exposure to our nationwide investor network.")

# --------------------------------------------------------------------------
# The three selling pillars. Michael's wording, exactly as supplied.
# Do not reword. Do not reduce this to two.
# --------------------------------------------------------------------------

PILLARS_TITLE = "3 Ways to Sell"

PILLARS = [
    {
        "n": "01",
        "icon": "cash",
        "h": "We inspect it, then buy it ourselves",
        "p": ("We complete a full property inspection to evaluate its condition, repair requirements and "
              "overall project scope. If the property meets our purchasing criteria, we move forward using "
              "our own cash with no lender financing to fall through."),
        "when": ("Best when the property fits our direct-purchase criteria and you want a straightforward "
                 "cash sale."),
        "short": "A full inspection, then a purchase with our own cash if the property meets our criteria.",
    },
    {
        "n": "02",
        "icon": "build",
        "h": "We improve it, then bring in an investor partner",
        "p": ("If the project carries more risk than we want to take on alone, we may, with your written "
              "approval, complete select repairs while the property is under contract. By investing our own "
              "money first, we make the home more attractive to our investor partners and demonstrate that "
              "we have real skin in the game. That commitment gives our partners greater confidence to join "
              "the purchase and complete the project with us."),
        "when": ("Best when some upfront improvements can create a stronger and more dependable path to "
                 "closing."),
        "short": "Select repairs made with our own money, with your written approval, to bring in a partner.",
    },
    {
        "n": "03",
        "icon": "network",
        "h": "Our national investor network competes for it",
        "p": ("Through our partnership with a national real estate syndicate, we can present your property "
              "to investors across the country. Qualified buyers can review the opportunity and compete to "
              "purchase it, creating exposure beyond the local market."),
        "when": ("Best when broader exposure and competitive investor demand could produce a stronger "
                 "result."),
        "short": "Your property presented to investors nationwide, who can compete to purchase it.",
    },
]

# --------------------------------------------------------------------------
# The shared three step process. Michael's wording.
# --------------------------------------------------------------------------

STEPS = [
    ("Step 1", "Tell us about the property",
     "Share the address, condition of the property and the situation you are facing."),
    ("Step 2", "Let us evaluate the opportunity",
     "The MaliHaus team reviews the property, the repair requirements, the local market and the "
     "available purchase route."),
    ("Step 3", "Review your options",
     "MaliHaus explains which of the three selling approaches may fit the property. The owner decides "
     "whether the proposed solution works for them."),
]

CLOSING_H2 = "Not sure which situation applies?"
CLOSING_COPY = ("You do not need to diagnose the problem or choose the right page. Tell us about the "
                "property, your circumstances and the outcome you want. The MaliHaus team will review "
                "the information and let you know whether it may be able to help.")
CLOSING_BTN = "Start the Conversation"

# --------------------------------------------------------------------------
# Icons
# --------------------------------------------------------------------------

ICONS = {
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    "doc": '<path d="M14 3H7a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V7z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h4"/>',
    "key": '<circle cx="8" cy="13" r="4"/><path d="M11 11.5 20 4M17.5 6.5 19.5 8.5M15.5 8.5 17.5 10.5"/>',
    "keys": '<path d="M3 21h8V9l-4-3-4 3z"/><path d="M11 21h10V12l-5-3-5 3"/><path d="M6.5 13h1M15.5 16h1"/>',
    "empty": '<path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="m9 11 6 6M15 11l-6 6"/>',
    "tools": '<path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="m9.5 14.5 2 2M14 12l-4.5 4.5"/><path d="M15.5 10.2a2.2 2.2 0 1 0-2.6 3.4"/>',
    "flame": '<path d="M12 3c0 3-3 4-3 7a3 3 0 0 0 6 0c0-1-.6-2-.6-2"/><path d="M12 21a6 6 0 0 0 6-6c0-4-3-6-3-9"/><path d="M12 21a6 6 0 0 1-6-6c0-2 1-3.4 2-4.6"/>',
    "split": '<path d="M12 3v6"/><path d="M12 9 7 14v7M12 9l5 5v7"/><path d="M9.5 6.5 12 9l2.5-2.5"/>',
    "van": '<path d="M3 17V7h11v10"/><path d="M14 10h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "pin": '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
    "stamp": '<path d="M4 20h16"/><path d="M7 17h10l-1-5H8z"/><path d="M12 12V8a2.4 2.4 0 1 1 2.4-2.4"/>',
    "boxes": '<path d="M3 8h8v8H3zM13 4h8v6h-8zM13 12h8v8h-8z"/>',
    "sign": '<path d="M12 21V8"/><path d="M4 4h14l2.5 2.5L18 9H4z"/><path d="M9 21h6"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5.5a3 3 0 0 1 0 5M17 20a6 6 0 0 0-2-4.5"/>',
    "down": '<path d="M3 21h18M6 21V11l6-4.5 6 4.5v10"/><path d="M12 18v-5M9.5 15.5 12 18l2.5-2.5"/>',
    "coins": '<ellipse cx="12" cy="6.5" rx="7" ry="3"/><path d="M5 6.5v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5"/><path d="M5 11.5v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5"/>',
    "cash": '<rect x="2.5" y="6" width="19" height="12" rx="1.5"/><circle cx="12" cy="12" r="2.8"/><path d="M6 9.5v5M18 9.5v5"/>',
    "build": '<path d="M3 21h18"/><path d="M6 21V8l6-4 6 4v13"/><path d="M10 21v-5h4v5"/><path d="m14.5 9.5 2 2"/>',
    "network": '<circle cx="12" cy="5" r="2.4"/><circle cx="5" cy="18" r="2.4"/><circle cx="19" cy="18" r="2.4"/><path d="m10.4 6.9-3.8 8.8M13.6 6.9l3.8 8.8M7.4 18h9.2"/>',
    "map": '<path d="m3 6 6-2.5 6 2.5 6-2.5v15L15 21l-6-2.5L3 21z"/><path d="M9 3.5v15M15 6v15"/>',
}

# --------------------------------------------------------------------------
# The sixteen situations
# --------------------------------------------------------------------------

SITUATIONS = []


def _s(**kw):
    SITUATIONS.append(kw)


_s(
    slug="sell-house-fast",
    nav="Sell a House Fast",
    kicker="Selling quickly",
    icon="clock",
    title="Sell a House Fast | MaliHaus",
    meta="Need to sell a house quickly? MaliHaus reviews your property and timeline and explains whether a direct, as is sale could suit you. No repairs and no obligation.",
    h1="Need to sell your house quickly?",
    h1_em="quickly?",
    opening=[
        "Sometimes waiting months for a traditional sale is not practical. You may be relocating, facing a financial deadline or simply ready to move on from the property.",
        "MaliHaus can review your property, understand your preferred timeline and determine whether a direct, as is sale may be suitable. You remain in control of whether and when you proceed.",
    ],
    cta="Discuss Your Timeline",
    card="A deadline, a move or a change of plan means the traditional route is too slow. We look at the property and your timing together.",
    challenge_h="Why a traditional sale can be too slow",
    challenge=[
        "A conventional listing is built around finding the strongest possible buyer, and that takes time by design. The property is prepared, photographed and marketed, offers are gathered, and then the buyer's mortgage lender begins its own process. Each of those stages is reasonable on its own. Added together they can run for months.",
        "The part owners underestimate is that the timeline is not really theirs to control. A buyer's financing, an appraisal that comes in low or a renegotiation after inspection can all reset the clock when you are already most of the way through.",
    ],
    complications=[
        ("The date moves after you have committed", "People make plans around an expected closing date, then have to unpick them when the buyer's lender asks for one more document."),
        ("Repairs get requested late", "An inspection report arrives and suddenly the sale depends on work you had not budgeted for or arranged."),
        ("Carrying costs keep running", "The mortgage, insurance, taxes and utilities continue for every month the property has not sold."),
        ("Speed is often confused with a low price", "Owners assume a fast sale must mean a bad one, and never test whether that is actually true for their property."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "Where we buy directly, there is no lender in the middle of the transaction and therefore no financing that can fall through. That removes the single most common reason a sale slips.",
        "Tell us the date you are working towards and we will tell you honestly whether it is realistic. Sometimes the answer is that you have more time than you think and would do better listing. We would rather say that than take a property from someone who did not need to move quickly.",
    ],
    faqs=[
        ("How quickly can this actually move?",
         "Without a lender involved a purchase can move considerably faster than a financed sale, and title work usually sets the pace. We will not put a guaranteed number of days in front of you before we have seen the property and the title position, because that number would be a guess."),
        ("Do I have to accept a lower price to sell quickly?",
         "Not automatically. A direct sale removes commission, repair costs and months of carrying costs, and for some owners the net figure is closer to a listing than they expect. For others, listing genuinely pays more. We will show you the reasoning either way."),
        ("What if my timeline changes?",
         "Tell us. A later date is usually easier to accommodate than an earlier one, and there is no penalty for changing your mind about when, or about whether, you want to sell."),
        ("Do I need to tidy up or make repairs first?",
         "No. We look at properties in their current condition. Cleaning and repairing before we have seen it is money you may not need to spend."),
    ],
    related=["relocation", "financial-hardship", "expired-listing", "major-repairs-as-is"],
)

_s(
    slug="foreclosure-missed-payments",
    nav="Foreclosure or Missed Payments",
    kicker="Behind on payments",
    icon="doc",
    title="Behind on Mortgage Payments or Facing Foreclosure | MaliHaus",
    meta="Missed mortgage payments or received a foreclosure notice? MaliHaus can review the property and explain whether a sale may be an option. Not legal or financial advice.",
    h1="Falling behind on mortgage payments?",
    h1_em="mortgage payments?",
    opening=[
        "If you have missed payments or received a foreclosure notice, acting early can give you more time to understand your options.",
        "MaliHaus can review the property and determine whether a sale may help you resolve the situation before it progresses further. MaliHaus does not provide legal or financial advice, but the team can explain whether it may be able to purchase the property.",
    ],
    cta="Request a Confidential Property Review",
    card="Missed payments or a notice from the lender. Understanding the options early usually leaves more of them open.",
    challenge_h="What tends to happen, and why time matters",
    challenge=[
        "Missed payments rarely arrive on their own. They usually follow something else, a job ending, an illness, a business going quiet, and by the time the letters start the household is already dealing with the original problem.",
        "The instinct is often to wait until things improve before opening anything. That is understandable, but a foreclosure process follows its own schedule regardless of what is happening in the house, and the range of realistic options is generally widest early and narrowest late.",
    ],
    complications=[
        ("Nobody is sure how much time is left", "Owners frequently do not know which stage the process has reached or what the next date on the calendar actually is."),
        ("The arrears and the equity are separate questions", "A property can be well behind on payments and still hold real equity, or be current and hold very little. One does not tell you the other."),
        ("Advice arrives from every direction", "Letters, calls and offers pile up, and it becomes hard to tell which are legitimate."),
        ("Condition and access make listing harder", "Preparing a property for the open market is difficult when money is already tight."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "The useful first step is usually a real number rather than an estimate. Knowing what the property could sell for, and what is owed against it, is what turns an anxious situation into a decision you can actually make.",
        "We can review the property and tell you whether we may be in a position to purchase it. If a sale would not clear what is owed, we will say so plainly rather than let you spend weeks discovering it.",
    ],
    disclaimer=("MaliHaus is not a law firm, a tax adviser or a financial adviser, and nothing on this page "
                "is legal, tax or financial advice. We cannot stop a foreclosure and we do not promise any "
                "particular outcome. Foreclosure procedure and timing differ from state to state. For advice "
                "on the process itself, and before signing anything, speak to a qualified attorney in your "
                "state or a HUD approved housing counsellor."),
    faqs=[
        ("Is it too late once a foreclosure notice has arrived?",
         "Not necessarily, but where you stand depends on the stage the process has reached and on the rules that apply in your state, and those differ. That is a question for an attorney or a housing counsellor. What we can do is tell you quickly whether a sale is realistic, so you know whether it belongs on your list of options."),
        ("Will you contact my lender?",
         "Only if you ask us to and you authorise it. Nothing goes to your lender without your say so."),
        ("What if I owe more than the property is worth?",
         "Then a straight sale may not clear the balance, and you need to know that early. Tell us the approximate balance at the start and we will tell you honestly whether a purchase could work."),
        ("Is any of this on public record?",
         "A conversation with us is not. Court filings connected with a foreclosure may already be public where you live, which is separate from anything you discuss with us."),
        ("Does asking for a review commit me to selling?",
         "No. Asking what the property is worth is information gathering. Many people gather it and then take a different route entirely."),
    ],
    related=["financial-hardship", "sell-house-fast", "tax-liens-code-violations", "divorce-separation"],
)

_s(
    slug="inherited-property-probate",
    nav="Inherited Property and Probate",
    kicker="Inherited and probate",
    icon="key",
    title="Sell an Inherited or Probate Property | MaliHaus",
    meta="Inherited a property you do not want to keep? MaliHaus evaluates inherited homes in their current condition and works with the authorised owner or estate representative.",
    h1="Inherited a property you do not want to keep?",
    h1_em="you do not want to keep?",
    opening=[
        "An inherited property can bring repairs, maintenance, taxes and decisions involving multiple family members. Managing everything can be especially difficult when you live in another city or state.",
        "MaliHaus can evaluate inherited properties in their current condition and work with the authorized owner or estate representative. Owners should speak with MaliHaus before paying for repairs or a major cleanout.",
    ],
    cta="Discuss an Inherited Property",
    card="Repairs, taxes, a house full of belongings and family members who each want something different. Speak to us before you spend anything on it.",
    challenge_h="An inherited property is rarely just a property",
    challenge=[
        "Most inherited homes have been standing still for a while. The air conditioning has not run properly, the roof is whatever age it is, and the last serious work happened a long time ago. That is normal and it does not stop a sale.",
        "The harder part is usually everything around the house. Several people may have an interest in it, they may live in different states, and they are making decisions during a period when nobody particularly wants to be making decisions at all.",
    ],
    complications=[
        ("Authority is not always obvious", "Who can actually sign depends on how the estate was left and where probate has reached. That has to be established before anything can complete."),
        ("The costs keep running regardless", "Insurance, taxes, utilities and yard maintenance continue while the family works out what to do."),
        ("The contents are the part people dread", "Sorting a lifetime of belongings is often the thing that stalls everything else for months."),
        ("Distance makes everything slower", "Arranging quotes, access and contractors from another state turns small tasks into long ones."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We look at inherited properties as they stand, with the belongings still in them. Take what the family wants and leave the rest. Clearing the house is not a condition of us reviewing it or of us buying it.",
        "Before anyone spends money on a roof, a cleanout or a cosmetic refresh, it is worth knowing what the property is worth in its current state. Frequently that spending does not come back, and it is a great deal easier to decide once there is a real figure on the table for the family to look at.",
    ],
    disclaimer=("MaliHaus is not a law firm and nothing on this page is legal or tax advice. Probate rules "
                "differ from state to state. Whether a property can be sold during probate, and who is "
                "authorised to sign, is determined by the estate's representative, the relevant court and "
                "the estate's attorney. We work with the authorised owner or estate representative only."),
    faqs=[
        ("Can a property be sold before probate is finished?",
         "Sometimes a sale can be arranged while probate is still running, but whether it can complete depends on the court and on how the estate was left, and the rules differ by state. Your attorney decides that. What we can do is give you a figure to work with while it is being sorted out."),
        ("Do we have to empty the property first?",
         "No. Take what matters to the family and leave everything else. Clearing it out is not something we ask you to do before we will look at the property."),
        ("There is still a mortgage on it. Does that stop this?",
         "No. A mortgage is paid off out of the sale at closing in the normal way. If the balance is close to the property's value, tell us early, because that changes what is realistic."),
        ("Several of us inherited it and we do not agree. Can you still help?",
         "We can give you a figure, which is often the thing the disagreement is really about. We cannot make the decision for the family and we will not pressure anyone. When everyone is ready, we are ready."),
        ("Should we make repairs before speaking to you?",
         "We would suggest speaking to us first. Owners regularly spend money on an inherited property that does not increase what it sells for, and that is difficult to undo afterwards."),
    ],
    related=["hoarder-house-cleanout", "out-of-state-owner", "title-problems-multiple-owners", "vacant-abandoned-property"],
)

_s(
    slug="tired-landlords",
    nav="Tired Landlords",
    kicker="Rental property",
    icon="keys",
    title="Sell a Rental Property, Tenanted or Vacant | MaliHaus",
    meta="Ready to move on from a rental property? MaliHaus reviews tenant occupied and vacant rentals and explains whether a direct sale is practical.",
    h1="Ready to move on from a rental property?",
    h1_em="a rental property?",
    opening=[
        "Owning a rental property can become burdensome when you are dealing with repairs, vacancies, difficult tenants or declining returns.",
        "MaliHaus can review tenant occupied and vacant rental properties and determine whether a direct sale is practical. Tell the team about the property, the tenancy and the outcome you want.",
    ],
    cta="Review My Rental Property",
    card="Repairs, vacancies, difficult tenants or returns that no longer justify the work. Tenanted properties are reviewed as they are.",
    challenge_h="When the numbers stop justifying the work",
    challenge=[
        "Most landlords do not decide to sell because of one dramatic event. It accumulates. Insurance goes up, a roof needs doing, a turnover costs more than expected, and at some point the return stops matching the amount of attention the property demands.",
        "Selling on the open market brings its own friction. A property with a tenant in place is harder to show, a vacant one loses income while it sits, and owner occupier buyers often want it empty and refreshed before they will look at it seriously.",
    ],
    complications=[
        ("Showings are difficult with a tenant in place", "Access depends on cooperation, and a tenant with no reason to help usually does not."),
        ("Emptying it costs both ways", "Ending a tenancy to sell means losing the income while carrying the costs, with no certainty about how long the sale will take."),
        ("Deferred maintenance has built up", "Work put off across several tenancies tends to surface all at once during an inspection."),
        ("Owner occupier buyers want something different", "The features that make a property a decent rental are not always the ones that sell it to a family."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "A tenant in place is not a problem for us and in some cases it is an advantage, because to the right investor the property is an income stream rather than a project. You do not need to end a tenancy or leave a property empty to have a conversation with us.",
        "Tell us what the rent is, what the lease says and what condition the property is genuinely in. We can review it as it stands, tenant included, and explain which of the three routes may fit.",
    ],
    faqs=[
        ("Can you buy it with the tenant still living there?",
         "In many cases yes, and we will review the property on that basis. What the lease says matters, so have it to hand when we speak."),
        ("Do I have to tell the tenant we are talking?",
         "Not to have an initial conversation with us. Your obligations to the tenant are set by the lease and by the law where the property is, and those apply regardless of who is buying."),
        ("What about the security deposit and the rent that has been paid?",
         "Those are handled at closing in the normal way, the same as any other transaction involving a tenanted property."),
        ("The property needs work between tenancies. Does that matter?",
         "It is one of the more common reasons landlords contact us. We look at properties in their current condition and do not expect you to make it ready first."),
        ("I own several. Can they be looked at together?",
         "Yes. Tell us about the portfolio and we will review them together rather than one at a time."),
    ],
    related=["vacant-abandoned-property", "major-repairs-as-is", "out-of-state-owner", "financial-hardship"],
)

_s(
    slug="vacant-abandoned-property",
    nav="Vacant or Abandoned Property",
    kicker="Vacant and abandoned",
    icon="empty",
    title="Sell a Vacant or Abandoned Property | MaliHaus",
    meta="Is an empty property becoming a liability? MaliHaus assesses vacant and abandoned properties in their current condition without requiring the owner to restore the home first.",
    h1="Is an empty property becoming a liability?",
    h1_em="becoming a liability?",
    opening=[
        "Vacant homes can create ongoing costs, security concerns, maintenance problems and code issues. The longer the property remains empty, the more difficult it can become to manage.",
        "MaliHaus can assess vacant and abandoned properties in their current condition and discuss a possible sale without requiring the owner to restore the home first.",
    ],
    cta="Get a Property Review",
    card="Costs, security and code issues that grow the longer it sits. Reviewed in its current condition, with no restoration required first.",
    challenge_h="Empty properties get harder, not easier",
    challenge=[
        "A property that nobody is living in deteriorates faster than one that is occupied. Small problems that a resident would notice within a day, a leak, a failed unit, a broken window, go unseen for months and turn into much larger ones.",
        "There is an administrative side too. Insurers treat vacant properties differently and cover can lapse or narrow without the owner realising. Municipalities notice empty houses, and overgrown lots and unsecured openings tend to attract citations.",
    ],
    complications=[
        ("Insurance may not cover what you assume", "A standard policy can behave very differently once a property is classed as vacant."),
        ("Code enforcement compounds", "Citations for grass, debris or an unsecured structure can accumulate and attach to the property."),
        ("Security becomes a real cost", "Break ins, squatting and stripped copper are all more likely, and each makes the next problem worse."),
        ("Utilities being off makes assessment harder", "Without power or water, systems cannot be tested, which makes a conventional buyer nervous."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We assess vacant properties as they stand, including ones that have been empty for a long time and are not in a condition anyone would want to show to a retail buyer. Restoring it first is not a precondition of us looking at it.",
        "If there are outstanding citations or a lien has attached, tell us early. Those things do not automatically prevent a sale, but they do need to be identified at the start rather than discovered halfway through.",
    ],
    faqs=[
        ("It has been empty for years and is in poor condition. Is that a problem?",
         "It is one of the situations we see most. Length of vacancy and condition are things we take into account, not reasons to stop the conversation."),
        ("There are code violations against it. Does that stop a sale?",
         "Not necessarily. Whether they can be dealt with as part of a transaction depends on what they are and on local rules, and title and legal questions have to be confirmed by the appropriate professionals."),
        ("The utilities are switched off. Do I need to turn them back on?",
         "No. Tell us in advance so we know what can and cannot be tested when we look at the property."),
        ("Someone is living in it who should not be.",
         "Tell us at the outset. It changes what is realistic, and it is far better addressed at the start than discovered later."),
    ],
    related=["major-repairs-as-is", "tax-liens-code-violations", "inherited-property-probate", "out-of-state-owner"],
)

_s(
    slug="major-repairs-as-is",
    nav="Major Repairs and As-Is Properties",
    kicker="Condition and repairs",
    icon="tools",
    title="Sell a House As Is, Without Making Repairs | MaliHaus",
    meta="Sell without completing major repairs. MaliHaus considers properties in a wide range of conditions. Ask for a review before spending money on renovations.",
    h1="Sell without completing major repairs",
    h1_em="major repairs",
    opening=[
        "Roof problems, outdated systems, structural concerns and years of deferred maintenance can make a conventional sale difficult.",
        "MaliHaus considers properties in a wide range of conditions. Before spending money on renovations, property owners can ask the team to review the home and determine whether selling as is could provide a better option.",
    ],
    cta="Show Us the Property",
    card="Roof, systems, structure or years of deferred maintenance. Ask for a review before you spend anything on renovations.",
    challenge_h="Why condition complicates a traditional sale",
    challenge=[
        "A conventional sale usually depends on a buyer with a mortgage, and a mortgage depends on a lender being satisfied with the property. Where there are roof, structural, electrical or plumbing problems, that approval becomes uncertain no matter how willing the buyer is.",
        "This is why owners are so often told to fix things first. The difficulty is that major repairs are expensive, disruptive and slow, and there is no guarantee the money spent comes back in the sale price.",
    ],
    complications=[
        ("Work uncovers more work", "Opening up a roof or a wall regularly reveals something that was not in the quote."),
        ("Financing falls through late", "A property can go under contract and then fail at the lender's inspection, months into the process."),
        ("Insurance is harder to obtain", "Roof age and condition in particular can make cover difficult for an incoming owner to arrange."),
        ("Estimates vary enormously", "Owners commonly receive quotes for the same job that differ by a factor of several, with no clear way to judge them."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We look at properties in a wide range of conditions and we do not ask you to repair, clean or stage anything before we will assess it. What we are working out is what the property is worth as it stands today.",
        "Where the work needed is more than we would take on alone, the second route may apply: with your written approval we may complete select repairs ourselves while the property is under contract, which can make it a stronger proposition for an investor partner.",
    ],
    faqs=[
        ("Is there any condition you would not consider?",
         "We consider a wide range, but we do not buy every property and it would be wrong to suggest otherwise. Some properties do not meet our purchasing criteria, and when that is the case we say so quickly rather than leave you waiting."),
        ("Do I need an inspection or estimates first?",
         "No. If you already have a report or quotes, they are useful, but obtaining them is not something we ask of you."),
        ("The roof is at the end of its life. Should I replace it before selling?",
         "Speak to us before you do. It is a large amount of money that may not be recovered, and it is a decision worth making with a figure in front of you."),
        ("What does as is actually mean here?",
         "It means we are looking at the property in its current state, and we are not asking you to carry out work or to reduce the price later because of something an inspection turned up."),
        ("You mentioned you might do repairs yourselves. How does that work?",
         "That is our second route. If it applies we would explain exactly what we propose doing and you would approve it in writing before anything was touched. We invest our own money in that work."),
    ],
    related=["fire-water-storm-damage", "vacant-abandoned-property", "expired-listing", "sell-house-fast"],
)

_s(
    slug="fire-water-storm-damage",
    nav="Fire, Water or Storm Damage",
    kicker="Damaged property",
    icon="flame",
    title="Sell a Fire, Water or Storm Damaged Property | MaliHaus",
    meta="Dealing with a damaged property? MaliHaus reviews fire, flood, storm and water damaged homes in their current condition and explains whether a sale may be possible.",
    h1="Dealing with a damaged property?",
    h1_em="a damaged property?",
    opening=[
        "Fire, flooding, storms and water intrusion can leave an owner facing repairs, insurance questions and an uncertain timeline.",
        "MaliHaus can review damaged properties in their current condition. Depending on the circumstances, a direct sale may allow the owner to move forward without managing the complete restoration.",
    ],
    cta="Discuss a Damaged Property",
    card="Fire, flood, storm or water intrusion, with an insurance process attached. Reviewed as it stands.",
    challenge_h="Restoration is a project, and not everyone wants one",
    challenge=[
        "After serious damage the owner is handed a second job. There is an adjuster to deal with, a scope of works to agree, contractors to find and schedule, and a property that cannot be lived in or let while all of that happens.",
        "A severe storm makes it harder still, because it creates the same problem for a great many households at once. Contractors are booked, materials are slow, and the timeline stops being anything the owner controls.",
    ],
    complications=[
        ("The settlement and the repair cost may not match", "What is paid out and what the work actually costs are two different numbers, and the gap belongs to the owner."),
        ("Hidden damage appears later", "Water in particular travels, and what is visible on day one is frequently not the full extent."),
        ("Living costs run in parallel", "Somewhere else has to be paid for while the property is uninhabitable."),
        ("A damaged property is hard to list", "Retail buyers and their lenders are generally not willing to take on an unfinished restoration."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We can review a property in its damaged state, including one where the restoration has been started and stopped. Finishing the work is not something we require before looking at it.",
        "Where there is an open insurance claim, say so early. How a claim is treated in a sale depends on the policy and on where the claim has reached, and that is a question for your insurer and your own adviser rather than for us. What we can tell you is whether a purchase may be possible.",
    ],
    disclaimer=("MaliHaus is not an insurance adviser, a public adjuster or a law firm. Nothing here is "
                "advice about your policy, your claim or your rights under it. Questions about a claim, an "
                "assignment of benefits or a settlement should go to your insurer, your own adjuster or an "
                "attorney."),
    faqs=[
        ("Can you look at it while the insurance claim is still open?",
         "We can review the property, and the claim is a factor in what is realistic. How it is handled depends on your policy and the stage the claim has reached, which your insurer and your adviser will confirm."),
        ("Do I need to complete the repairs first?",
         "No. Owners contact us precisely because they do not want to manage a full restoration."),
        ("The work was started and then stopped. Does that matter?",
         "It is common and it does not prevent a review. Tell us what was done and what was left, and share any paperwork you have."),
        ("There is mould. Is that an automatic no?",
         "No. It is one of the things we take into account. Tell us what you know rather than trying to make the property presentable first."),
    ],
    related=["major-repairs-as-is", "vacant-abandoned-property", "financial-hardship", "sell-house-fast"],
)

_s(
    slug="divorce-separation",
    nav="Divorce or Separation",
    kicker="Divorce and separation",
    icon="split",
    title="Selling a Property During a Divorce or Separation | MaliHaus",
    meta="Selling property during a separation? When the authorised owners agree to explore a sale, MaliHaus can review the property and present a possible solution. Not legal advice.",
    h1="Selling property during a separation?",
    h1_em="during a separation?",
    opening=[
        "A shared property can become one of the largest practical decisions during a divorce or separation. Both parties may need a clear process and a realistic timeline.",
        "When the authorized owners agree to explore a sale, MaliHaus can review the property and present a possible solution. MaliHaus does not provide legal advice, and all ownership decisions remain with the parties and their advisers.",
    ],
    cta="Request a Property Review",
    card="A shared property, two households forming and a need for a clear process. Handled quietly, with both authorised owners.",
    challenge_h="The property is usually the largest single item",
    challenge=[
        "In most separations the home is the biggest asset and the hardest one to divide, because unlike a bank balance it cannot simply be split. It has to be kept by one party or converted into money, and both routes need a number everybody accepts.",
        "That is where it often stalls. Each side may have a different sense of what the property is worth, and without an agreed figure the conversation goes in circles while the mortgage, insurance and taxes carry on being due.",
    ],
    complications=[
        ("There is no agreed valuation", "Two opinions of value, neither tested, is a difficult basis for any decision."),
        ("Both signatures are needed", "Where both parties are on the title, neither can sell alone, however urgent it feels."),
        ("Showings mean strangers in the house", "An open market sale involves marketing and viewings at a time when privacy matters more than usual."),
        ("The costs keep running", "Payments continue while the decision is unresolved, often out of two households instead of one."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We can review the property and give both parties the same figure at the same time, which is frequently the thing that lets a decision get made. It is a straightforward, private process with no sign in the yard and no strangers walking through.",
        "We work only with the authorised owners, together. We do not take instructions from one party about a property owned by two, and we will not push either of you towards a decision.",
    ],
    disclaimer=("MaliHaus is not a law firm and nothing on this page is legal or financial advice. How a "
                "property is divided, what a court order requires and what each party is entitled to are "
                "matters for your attorneys, and the rules differ by state. Any sale needs the agreement of "
                "all authorised owners."),
    faqs=[
        ("Do both of us have to agree before we contact you?",
         "You can both ask what the property is worth without having agreed to sell. A sale itself needs the agreement of everyone on the title."),
        ("Can you work through our attorneys?",
         "Yes, and where there are attorneys involved that is often the simplest route for everyone."),
        ("Will this stay private?",
         "There is no listing, no yard sign and no marketing campaign. It is a conversation between us and the authorised owners."),
        ("One of us wants to keep the house. Is that still worth a call?",
         "Often yes, because knowing what it would sell for is exactly what makes a buy out negotiable rather than theoretical."),
        ("What if there is a court order about the property?",
         "Tell us at the start and involve your attorney. What the order requires takes precedence over anything we would otherwise discuss."),
    ],
    related=["title-problems-multiple-owners", "financial-hardship", "sell-house-fast", "foreclosure-missed-payments"],
)

_s(
    slug="relocation",
    nav="Relocation",
    kicker="Relocating",
    icon="van",
    title="Relocating and Need to Sell Your House | MaliHaus",
    meta="A new job or an unexpected move can make listing a property difficult. MaliHaus reviews the property and your moving schedule to see whether a direct sale fits.",
    h1="Relocating and need to sell?",
    h1_em="need to sell?",
    opening=[
        "A new job, family commitment or unexpected move can make preparing and listing a property difficult, especially when time is limited.",
        "MaliHaus can review the property and the owner's moving schedule to determine whether a direct sale may provide a more manageable path forward.",
    ],
    cta="Discuss Your Move",
    card="A job, a family commitment or an unexpected move, with a date attached. We work to your schedule rather than the market's.",
    challenge_h="Two properties, one household",
    challenge=[
        "A relocation usually comes with a date that is not negotiable. Around that date sits packing, a new home to arrange, possibly a new school, and a job that is already demanding attention.",
        "The problem is the overlap. If the move happens before the sale completes, the household is carrying two sets of costs, and the property being sold is now empty and several hundred miles away from the person responsible for it.",
    ],
    complications=[
        ("The dates rarely line up", "The new place is needed before the old one has sold, and the gap has to be funded."),
        ("Preparing a property while moving out of it", "Repairs, cleaning and photographs all have to happen in the same weeks as the packing."),
        ("Managing a sale from a distance", "Once you have gone, every showing, question and repair needs somebody local."),
        ("Employer timelines do not wait", "A start date is generally fixed regardless of what the property market is doing."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "Tell us the date you have to be gone and we will work to it rather than around it. Where we buy directly there is no lender on our side, so the timing has fewer moving parts than a financed sale.",
        "If you need to close before you move, or to stay in the property for a period after closing, say so at the start. It is a normal request and it is easier to build in from the beginning than to negotiate later.",
    ],
    faqs=[
        ("Can I close before I actually move out?",
         "Tell us what you need. Staying on for a short period after closing can often be arranged, and it is much simpler to agree upfront."),
        ("I have already moved. Can this be done remotely?",
         "Yes. We work with owners who are no longer in the state, and documents are handled electronically where the title company allows it."),
        ("Do I need to clear the house first?",
         "No. Anything you do not want to move can be left."),
        ("My employer is covering relocation costs. Does that change anything?",
         "It may affect what makes sense for you financially, so it is worth telling us. Some relocation packages include assistance with the property, which is worth checking before you decide anything."),
    ],
    related=["out-of-state-owner", "sell-house-fast", "vacant-abandoned-property", "expired-listing"],
)

_s(
    slug="out-of-state-owner",
    nav="Out-of-State Owners",
    kicker="Owning from a distance",
    icon="pin",
    title="Selling a Property You Own in Another State | MaliHaus",
    meta="Own a property in another state? MaliHaus works remotely with authorised owners and reviews the property without requiring repeated travel.",
    h1="Own a property in another state?",
    h1_em="in another state?",
    opening=[
        "Managing repairs, tenants, maintenance and paperwork from a distance can quickly become frustrating.",
        "MaliHaus can work remotely with authorized property owners and review the property without requiring repeated travel. The team will explain the process and the information needed at each stage.",
    ],
    cta="Review My Property",
    card="Repairs, tenants and paperwork handled from hundreds of miles away. Reviewed remotely, without repeated trips.",
    challenge_h="Distance turns small problems into slow ones",
    challenge=[
        "Owning a property in a state you do not live in is manageable while nothing goes wrong. The moment something does, every task requires somebody on the ground, and arranging that from elsewhere takes days rather than hours.",
        "Costs mount quietly as well. Flights and time off to deal with a property, contractors who cannot be supervised, and services that continue whether or not anyone is using them.",
    ],
    complications=[
        ("Nobody is there to let anyone in", "Every quote, inspection and repair needs access, and access needs a person."),
        ("Local rules are hard to keep up with", "Municipal requirements, permits and inspection regimes vary and are easy to fall foul of from a distance."),
        ("Trips cost more than they appear to", "Flights, hotels and time away add up, often to more than the problem being solved."),
        ("Seasonal risks need attention", "Storm season in the south and winter in the north both require a property to be prepared and checked, which is difficult remotely."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We can review a property without you flying in for it. Tell us what you know about the condition, and where there is a tenant or a property manager, we will coordinate access rather than asking you to arrange it.",
        "Documents are handled electronically wherever the title company allows, and remote notarisation is available in many cases. We will tell you at each stage exactly what is needed from you, so nothing arrives as a surprise.",
    ],
    faqs=[
        ("Do I have to travel to the property for this?",
         "Generally not. We can review it remotely and handle documents electronically where the title company permits it."),
        ("Can documents be signed remotely?",
         "In many cases yes. Requirements vary by state and by title company, and we will confirm what applies before anything needs signing."),
        ("Who inspects the property if I am not there?",
         "We arrange that. If there is a tenant or a property manager we coordinate with them directly."),
        ("I inherited it and have never seen it. Is that a problem?",
         "No, it is a common starting point. Tell us what you do know and we will work out the rest from our side."),
    ],
    related=["tired-landlords", "inherited-property-probate", "vacant-abandoned-property", "relocation"],
)

_s(
    slug="tax-liens-code-violations",
    nav="Tax Liens and Code Violations",
    kicker="Liens, taxes and code",
    icon="stamp",
    title="Selling a Property With Tax Liens or Code Violations | MaliHaus",
    meta="Unpaid taxes, municipal violations and liens complicate a sale but do not always prevent one. MaliHaus reviews the property and available information.",
    h1="Are property taxes, liens or code issues creating pressure?",
    h1_em="creating pressure?",
    opening=[
        "Unpaid taxes, municipal violations and property liens can complicate a traditional sale, but they do not always make a sale impossible.",
        "MaliHaus can review the property and available information to determine whether the issues may be addressed as part of a potential transaction. Title and legal questions must be confirmed by the appropriate professionals.",
    ],
    cta="Discuss the Property",
    card="Unpaid taxes, municipal violations or liens against the property. Complicated, but not automatically a dead end.",
    challenge_h="Why these stall a conventional sale",
    challenge=[
        "A sale transfers clear title, so anything recorded against the property has to be dealt with before it can complete. Unpaid taxes, a contractor's lien, a judgment or an accumulated set of code fines all sit in the way until they are resolved.",
        "What makes this difficult for owners is that the full picture is rarely visible from the kitchen table. Items can be recorded that the owner does not know about, and the totals frequently continue to grow while nothing is being done.",
    ],
    complications=[
        ("The real total is often unknown", "Interest, penalties and accruing fines mean the figure quoted last year is not the figure today."),
        ("There can be more than one claimant", "Different authorities and creditors may each have something recorded, with different rules."),
        ("Retail buyers walk away", "An ordinary buyer and their lender usually will not take on a property with unresolved recorded items."),
        ("Fines can keep accruing", "Some code enforcement penalties continue to run until the underlying issue is actually corrected."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "Tell us what you know, including the parts you are unsure about. A title search establishes what is actually recorded, and that is the point at which the situation stops being an unknown.",
        "Depending on what is found, some items can be dealt with as part of a transaction. Whether that applies to your property depends on the specifics and on local rules, and it has to be confirmed by the title company and the appropriate professionals rather than assumed.",
    ],
    disclaimer=("MaliHaus is not a law firm, a tax adviser or a title company. Nothing here is legal or tax "
                "advice, and nothing here is a promise that any lien, violation or tax debt can be resolved. "
                "Tax and code enforcement procedures differ by state and by municipality. Title and legal "
                "questions have to be confirmed by qualified professionals where the property is located."),
    faqs=[
        ("Can a property be sold with a lien recorded against it?",
         "Often a recorded item is settled out of the proceeds at closing, but whether that works depends on what it is and how much it is. A title search is what settles the question."),
        ("I do not know what is actually recorded against it.",
         "That is normal and it is exactly what a title search establishes. Tell us what you know and the search fills in the rest."),
        ("The code fines are larger than the property is worth.",
         "Then you need to know that before you spend any more energy on it. Some authorities will consider a reduction in connection with a sale that corrects the underlying problem, which is a conversation to have with them, not a promise we can make."),
        ("The property taxes have not been paid for years.",
         "Tell us how long. Where the process has reached matters a great deal to what is still possible, and it varies by state and by county."),
    ],
    related=["vacant-abandoned-property", "title-problems-multiple-owners", "financial-hardship", "foreclosure-missed-payments"],
)

_s(
    slug="hoarder-house-cleanout",
    nav="Hoarder Houses and Major Cleanouts",
    kicker="Contents and cleanouts",
    icon="boxes",
    title="Selling a Hoarder House or a Property Needing a Cleanout | MaliHaus",
    meta="Overwhelmed by the contents of a property? Speak to MaliHaus before paying for a complete cleanout. The property can be reviewed in its current condition.",
    h1="Overwhelmed by the contents of a property?",
    h1_em="the contents of a property?",
    opening=[
        "Some properties contain years of belongings, debris or accumulated materials. Emptying the home before exploring a sale may feel physically, emotionally and financially overwhelming.",
        "Property owners should speak with MaliHaus before paying for a complete cleanout. The team can review the property in its current condition and determine what may need to be removed, if anything.",
    ],
    cta="Request a Private Review",
    card="Years of belongings or accumulated materials. Speak to us before paying for a cleanout, because it may not be needed.",
    challenge_h="The cleanout is usually what stops everything",
    challenge=[
        "A full property is not really a logistics problem, it is the reason nothing else has happened. Owners and families often know exactly what they want to do and have simply not been able to face the first step.",
        "It is expensive as well as difficult. A full clearance can run into thousands of dollars, and it has to be paid before the property has sold and before anyone knows whether the spending will make any difference to the price.",
    ],
    complications=[
        ("Clearance costs are paid upfront", "The money goes out before the sale, and it does not necessarily come back in the price."),
        ("Things worth keeping are mixed in", "Documents, photographs and items of real value are usually somewhere in it, which makes a bulk clearance risky."),
        ("Access and assessment are limited", "It can be genuinely difficult to see the condition of the property underneath the contents."),
        ("It is not just a practical job", "Where the contents belonged to a parent, or where there is a hoarding disorder involved, the emotional weight is the hardest part."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We look at properties with the contents still in them. Take what matters to you and leave the rest. Clearing it is not a condition of us reviewing the property or of us buying it.",
        "This is handled privately and without judgement. It is far more common than most owners assume, and nobody is going to be walked through the property on a public viewing.",
    ],
    faqs=[
        ("Do I really not need to clear it out?",
         "Correct. Take the things you want and leave everything else. Please do speak to us before paying for a clearance."),
        ("Will people be walking through it?",
         "There is no listing and no public showings. Someone from our side needs to see the property, and that is the extent of it."),
        ("What if there is damage underneath the contents?",
         "That is normal in these properties and it is taken into account. We are not expecting to find it in perfect condition."),
        ("It belonged to a relative who has died.",
         "Then there may be probate considerations as well. Take a look at our page on inherited property and mention it when we speak."),
    ],
    related=["inherited-property-probate", "vacant-abandoned-property", "major-repairs-as-is", "downsizing-senior-transition"],
)

_s(
    slug="expired-listing",
    nav="Expired Listings",
    kicker="Unsold and expired",
    icon="sign",
    title="Your Listing Expired and the Property Did Not Sell | MaliHaus",
    meta="A property may remain unsold because of condition, price, financing problems or the limits of the traditional market. MaliHaus can provide another perspective.",
    h1="Has your property failed to sell?",
    h1_em="failed to sell?",
    opening=[
        "A property may remain unsold because of its condition, price, financing problems or the limitations of the traditional market.",
        "MaliHaus can provide another perspective and determine whether a direct sale may be available. There is no obligation to proceed simply because an owner requests a review.",
    ],
    cta="Explore Another Option",
    card="Months on the market, or a sale that collapsed at the last stage. Another perspective on why, and on what else is available.",
    challenge_h="Unsold usually means something specific",
    challenge=[
        "A property that has sat on the market is telling you something, and it is worth identifying what. Condition, price, photographs, access, the financing available to the likely buyer, or something particular about the property itself. Each has a different answer.",
        "There is also the category of properties that did sell, twice or three times, and then came back. That pattern usually points at the buyer's lender or the inspection rather than at anything about how the property was marketed.",
    ],
    complications=[
        ("Time on market becomes its own problem", "Buyers see a long listing history and assume something is wrong, whether or not it is."),
        ("Repeated fall throughs point at financing", "A property that keeps coming back is often failing at the lender's stage rather than at the buyer's."),
        ("Price reductions get chased downwards", "A sequence of cuts can end below where a properly targeted approach would have landed."),
        ("Another six months costs real money", "Mortgage, insurance, taxes and maintenance continue throughout the next attempt."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We can look at the property and give you a straight assessment of why it is likely not selling, and which of our three routes might apply. If the honest answer is that relisting properly would pay you more, we will say so.",
        "If your listing agreement is still running, tell us. There may be obligations to your agent that need to be respected first, and that is worth establishing before anything else is discussed.",
    ],
    faqs=[
        ("My listing agreement has not expired yet. Can we still talk?",
         "Tell us the position. Depending on your agreement there may be obligations to your agent, and those need respecting. Establishing that first is the right order to do this in."),
        ("It fell through three times. What is going on?",
         "That pattern usually points at the buyer's financing or at the inspection rather than at the marketing. It is one of the first things worth checking."),
        ("Will you just offer me less than the list price?",
         "We will give you a figure and the reasoning behind it. If it does not work for you, that is a perfectly reasonable answer and nothing is owed."),
        ("Should I reduce the price and try again instead?",
         "Sometimes that genuinely is the better route, and we will tell you if we think so. Knowing what a direct sale looks like gives you something to compare it against."),
    ],
    related=["major-repairs-as-is", "sell-house-fast", "vacant-abandoned-property", "relocation"],
)

_s(
    slug="title-problems-multiple-owners",
    nav="Title Problems and Multiple Owners",
    kicker="Title and ownership",
    icon="users",
    title="Title Problems and Properties With Multiple Owners | MaliHaus",
    meta="Inherited ownership, missing documentation and disagreements between owners can hold up a sale. MaliHaus reviews the circumstances and identifies what needs clarifying.",
    h1="Is complicated ownership delaying a sale?",
    h1_em="delaying a sale?",
    opening=[
        "Inherited ownership, missing documentation, unresolved liens and disagreements between owners can prevent an otherwise viable transaction from moving forward.",
        "MaliHaus can review the basic circumstances and identify what would need to be clarified before a purchase could proceed. Legal and title matters must be resolved through qualified professionals.",
    ],
    cta="Explain the Situation",
    card="Inherited ownership, missing paperwork or several owners who do not agree. We identify what needs clarifying first.",
    challenge_h="Ownership questions have to be settled first",
    challenge=[
        "A sale can only proceed once it is clear who owns the property and who is entitled to sell it. Where a property has passed through a family across generations, or where paperwork was never properly recorded, that is not always obvious.",
        "These situations tend to sit untouched for years, because there is no obvious first move and every route appears to need a professional and a fee before anyone knows whether it is worth it.",
    ],
    complications=[
        ("Ownership has fragmented over time", "A property inherited across two or three generations can end up with a long list of part owners, some hard to trace."),
        ("The paperwork was never recorded", "A deed that was signed but never filed, or an agreement that only ever existed verbally."),
        ("Owners cannot be located", "A sale that needs every owner's signature stalls entirely if one of them cannot be found."),
        ("Old items remain recorded", "A mortgage that was paid off decades ago can still show against the property if it was never released."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "Tell us the circumstances as you understand them and we will identify what would need clarifying for a purchase to be possible. Frequently the first useful step is simply a title search, so that everyone is working from what is actually recorded rather than from family memory.",
        "We cannot resolve legal or title matters, and we would be misleading you to suggest otherwise. What we can do is tell you whether the property is worth pursuing, which is what determines whether the professional fees are worth incurring at all.",
    ],
    disclaimer=("MaliHaus is not a law firm or a title company and nothing here is legal advice. Title "
                "defects, ownership disputes and heirship questions have to be resolved by a qualified "
                "attorney and a title professional in the state where the property is located, and the "
                "rules differ. We cannot promise that any title issue can be cleared."),
    faqs=[
        ("Several relatives own it and one cannot be found.",
         "That does need resolving before a sale could complete, and it is a question for an attorney in that state. A title search establishes who is actually recorded, which is the necessary starting point."),
        ("There is a deed but it was never filed.",
         "Tell us and mention it to a title professional. It is a common situation and it is not automatically fatal to a sale."),
        ("An old mortgage still shows against the property.",
         "If it was paid off but never released, that is usually resolvable, though it takes time. The title search will confirm what is recorded."),
        ("Is it worth paying for a title search before we know anything?",
         "That is exactly why it is worth speaking to us first. If the property is not worth pursuing, you have saved the fee. If it is, you know the search is justified."),
    ],
    related=["inherited-property-probate", "divorce-separation", "tax-liens-code-violations", "vacant-abandoned-property"],
)

_s(
    slug="downsizing-senior-transition",
    nav="Downsizing and Senior Transitions",
    kicker="Downsizing",
    icon="down",
    title="Downsizing or Moving to a Simpler Living Arrangement | MaliHaus",
    meta="Downsizing involves more than selling a house. MaliHaus reviews the property in its current condition and works around a realistic transition schedule.",
    h1="Ready for a smaller home or a simpler living arrangement?",
    h1_em="a simpler living arrangement?",
    opening=[
        "Downsizing can involve more than selling a house. It may also require sorting belongings, coordinating a move and making decisions around a lifetime of memories.",
        "MaliHaus can review the property in its current condition and work around a realistic transition schedule. Family members and professional advisers can be included where appropriate.",
    ],
    cta="Discuss Your Plans",
    card="A move to something smaller or to assisted living, with a lifetime of belongings attached. Unhurried, at a realistic pace.",
    challenge_h="Downsizing is a transition, not a transaction",
    challenge=[
        "The property is usually the least complicated part. There is somewhere new to arrange, decades of belongings to sort, and a set of decisions that are genuinely difficult to make quickly.",
        "Where the move is to assisted living or is prompted by health, the timing is often set by something other than the property market, and the family is coordinating several things at once.",
    ],
    complications=[
        ("The new place has to be secured first", "Most people are unwilling to commit to selling until they know where they are going."),
        ("The house needs updating for the open market", "A home lived in for thirty years is usually dated by current buyer expectations, and updating it during a move is a great deal to ask."),
        ("The contents take longer than anyone expects", "Sorting a lifetime of belongings is slow, and it should be."),
        ("Several people are involved", "Adult children, advisers and sometimes care providers all need to be part of the conversation."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "We can work to a realistic schedule rather than a hurried one, including where you need to remain in the property for a period after closing while the new arrangement is finalised. Say so at the start and it can be built in.",
        "The property is reviewed as it stands, with no expectation that it is updated or emptied first. Family members, an attorney or a financial adviser are welcome in the conversation, and where somebody holds power of attorney we will need to see it before anything proceeds.",
    ],
    disclaimer=("MaliHaus is not a financial adviser, a tax adviser or a law firm. Decisions about downsizing "
                "can have tax and benefits implications, and those should be discussed with a qualified "
                "professional. Where someone is acting under a power of attorney, we will need to see the "
                "documentation."),
    faqs=[
        ("Can I stay in the house for a while after it is sold?",
         "Tell us what you need. A period of occupancy after closing can often be arranged and is much simpler to agree at the start."),
        ("Do I need to update the house first?",
         "No. We look at properties as they are, and updating a home you are leaving is rarely money well spent."),
        ("Can my children be part of the conversation?",
         "Yes, and we would encourage it. Advisers and attorneys are equally welcome."),
        ("I hold power of attorney for a parent. Can I handle this?",
         "Potentially, and we will need to see the documentation. The title company will confirm what is required before anything proceeds."),
        ("What if the timing depends on a place becoming available?",
         "That is a common situation. Tell us and we will work around it rather than pressing for a date you cannot commit to."),
    ],
    related=["inherited-property-probate", "hoarder-house-cleanout", "relocation", "major-repairs-as-is"],
)

_s(
    slug="financial-hardship",
    nav="Financial Hardship",
    kicker="Financial pressure",
    icon="coins",
    title="Financial Hardship and a Property You Can No Longer Keep | MaliHaus",
    meta="Loss of income, medical costs or rising ownership costs can make a property difficult to keep. MaliHaus can confidentially review the property. Not legal or financial advice.",
    h1="Has an unexpected financial change made the property difficult to keep?",
    h1_em="difficult to keep?",
    opening=[
        "Loss of income, medical expenses, rising ownership costs or other life changes can place pressure on a homeowner.",
        "MaliHaus can confidentially review the property and determine whether a possible sale could provide a practical way forward. MaliHaus does not offer legal, tax, bankruptcy or financial advice.",
    ],
    cta="Request a Confidential Review",
    card="Lost income, medical costs or ownership costs that have outgrown the budget. Reviewed confidentially and without pressure.",
    challenge_h="The costs of owning have moved",
    challenge=[
        "For a lot of households the mortgage is not what changed. Insurance premiums, association dues, taxes and maintenance have all moved, and a payment that was comfortable a few years ago is no longer comfortable now.",
        "Add a change in income, a medical event or a business going quiet, and the property shifts from being the thing that provides security to being the thing generating the pressure.",
    ],
    complications=[
        ("Insurance and association costs keep rising", "These are outside the owner's control and can move sharply from one year to the next."),
        ("Maintenance gets deferred first", "It is the easiest thing to postpone, and postponing it makes the property harder to sell later."),
        ("Credit gets used to hold it together", "Covering ownership costs with credit cards or loans usually enlarges the problem rather than solving it."),
        ("Deciding gets put off", "The longer a decision waits, the fewer options tend to remain available."),
    ],
    help_h="How MaliHaus may be able to help",
    help=[
        "A confidential review costs you nothing and gives you a real figure. Whatever you decide afterwards, deciding with a number in front of you is better than deciding without one.",
        "If the honest answer is that selling would not improve your position, we will tell you that. And if there is a route that suits you better than selling to us, we would rather you took it.",
    ],
    disclaimer=("MaliHaus is not a law firm, a tax adviser, a credit counsellor or a financial adviser, and "
                "nothing here is legal, tax, bankruptcy or financial advice. If you are considering "
                "bankruptcy or negotiating with creditors, speak to a qualified professional or a HUD "
                "approved housing counsellor before making decisions."),
    faqs=[
        ("Will anyone find out I have contacted you?",
         "No. There is no listing, no sign and no marketing. It is a private conversation."),
        ("What if selling still would not fix things?",
         "Then we will say so. Knowing that is genuinely useful, because it means you can stop considering an option that would not have worked."),
        ("I am behind on payments as well.",
         "Then the foreclosure and missed payments page is worth reading too, and mention it when we speak so we understand the full position."),
        ("Am I obliged to sell if I ask for a review?",
         "No. Asking what a property is worth commits you to nothing at all."),
    ],
    related=["foreclosure-missed-payments", "sell-house-fast", "divorce-separation", "major-repairs-as-is"],
)

SIT_BY_SLUG = {s["slug"]: s for s in SITUATIONS}

HOME_FEATURED = ["sell-house-fast", "inherited-property-probate", "foreclosure-missed-payments",
                 "tired-landlords", "major-repairs-as-is", "vacant-abandoned-property",
                 "out-of-state-owner", "expired-listing"]

# --------------------------------------------------------------------------
# Which funnel branch each situation page opens the funnel on, so a visitor
# who clicked "Foreclosure or Missed Payments" does not get asked to pick a
# situation again. The funnel has six branches; the site has sixteen pages.
# --------------------------------------------------------------------------

SIT_BRANCH = {
    # Only preselect where the funnel card is genuinely TRUE of that page.
    # Anything inferred is left blank so the visitor picks it themselves.
    # Ticking "facing foreclosure" for someone who only said money is tight,
    # or "I own a rental" for an out-of-state owner, is a judgement about the
    # seller, and it also hides the options they actually needed.
    "foreclosure-missed-payments":   "deadline",     # card says exactly this
    "tax-liens-code-violations":     "deadline",     # branch asks about liens and city notices
    "inherited-property-probate":    "inherited",    # card says exactly this
    "tired-landlords":               "rental",       # card says exactly this
    "major-repairs-as-is":           "condition",    # card says exactly this
    "fire-water-storm-damage":       "condition",    # branch asks about fire and water damage
    "hoarder-house-cleanout":        "condition",    # branch asks about clutter and hoarding
    "relocation":                    "moving",       # branch asks about relocation
    "divorce-separation":            "moving",       # branch asks about divorce
    "downsizing-senior-transition":  "moving",       # branch asks about downsizing

    # Deliberately NOT preselected. Each of these would put words in the
    # seller's mouth, so they land on the clean picker instead.
    "sell-house-fast":               "",   # wanting speed is not "moving by a date"
    "financial-hardship":            "",   # money being tight is not "facing foreclosure"
    "expired-listing":               "",   # a failed listing is not "just curious"
    "out-of-state-owner":            "",   # owning at a distance is not owning a rental
    "vacant-abandoned-property":     "",   # empty does not mean it needs work
    "title-problems-multiple-owners":"",   # a title problem is not always an inheritance
}
