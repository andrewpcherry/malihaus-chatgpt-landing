/* MaliHaus, the property enquiry funnel.

   This is a NATIVE MaliHaus page. It is not the REI demo funnel restyled.
   What was carried across is the LOGIC ONLY: the six situation branches and
   their questions, the combination intelligence, the shared qualifying
   questions, the A/B/C/X tiering and the lead payload. Everything the
   visitor sees is built from the site's own components (.mh-card, .btn,
   .wrap) and the site's own tokens, so it looks like the rest of MaliHaus
   and nothing like the demo it came from.

   The shape: pick your situation (one or more), then tap through
   qualification, then a short contact step. No dropdowns anywhere.

   Deal structures are deliberately never named. A sophisticated investor
   reads the deal type off the answers, and naming it would publish
   commercial terms MaliHaus has not approved. */

(function () {
  'use strict';

  var CFG = window.MALIHAUS || {};
  var MOUNT = document.getElementById('mhfunnel');
  if (!MOUNT) return;

  var MARKET = "Florida and selected markets nationwide";

  /* ------------------------------------------------------------------ *
   * DATA, carried across unchanged apart from dropping the old palette
   * ------------------------------------------------------------------ */

  var BRANCHES = {
  inherited:{
    icon:"key",
    label:"Inherited or estate", tag:"Estate",
    card:"I inherited a house, or I'm handling an estate",
    blurb:"A property that came to you through a death in the family, whether or not probate has started.",
    also:"Probate, executor or administrator, several heirs, a house full of belongings, a relative's house you have never lived in",
    headline:"An inherited property usually has more room in it than people expect.",
    intro:"Estate sales stall on three things: where probate stands, whether every heir agrees, and what happens to everything still inside. Those decide what is possible before price is even a conversation.",
    extra:{name:"heirNotes", label:"Anything about the estate we should know before we call? (optional)"},
    qs:[
      {id:"probate", key:true, q:"Where does the estate stand?", sub:"A rough answer is fine, this is the first thing we check anyway.",
       opts:["Probate is finished","It is in probate now","Probate has not started","No probate needed, it transferred directly","I am not sure"]},
      {id:"heirs", key:true, q:"Who else has a claim on the property?", sub:"This decides who has to sign at closing.",
       opts:["Just me","Me and one other person","Three or more heirs","I am not sure yet"]},
      {id:"agreed", q:"Are the other heirs agreed on selling?", sub:"An honest answer here saves everybody weeks.",
       when:function(a){return a.heirs==="Me and one other person"||a.heirs==="Three or more heirs";},
       opts:["Yes, everyone agrees","Mostly, we are close","No, we are not agreed","We have not discussed it"]},
      {id:"contents", q:"What is still inside the house?",
       opts:["It is cleared out","Some furniture and belongings","Completely full","I have not been inside","Something else"]}
    ]
  },
  deadline:{
    icon:"doc",
    label:"Foreclosure or a deadline", tag:"Time pressure",
    card:"I'm behind on payments or facing foreclosure",
    blurb:"Missed payments, a notice of default, an auction or hearing date, back taxes, or a lien.",
    also:"Pre-foreclosure, notice of default, auction date set, back property taxes, tax lien, HOA lien, code violations, a judgment against the property",
    headline:"With a date on the calendar, certainty matters more than the last few thousand.",
    intro:"The worst outcome here is finding out too late that you had more options than you thought. What you have told us is enough for the team to work out what is realistic against your timeline and come back with real numbers.",
    extra:{name:"deadlineNotes", label:"What date are you working against? (optional)"},
    qs:[
      {id:"pressure", key:true, q:"What is the pressure?",
       opts:["Behind on mortgage payments","A notice of default or foreclosure filing","Property taxes or a tax lien","A lien, code violation or city notice","A court or auction date is set","Payments are current, the deadline is personal",
             "Another reason not listed"]},
      {id:"dateset", key:true, q:"Has a date actually been set?", sub:"This is the single most useful thing you can tell us.",
       when:function(a){return a.pressure && a.pressure!=="Payments are current, the deadline is personal";},
       opts:["Yes, within 30 days","Yes, more than 30 days out","No date yet","I do not know"]},
      {id:"lender", q:"Have you spoken to the lender or the county?",
       opts:["Yes, we are working on something","I have tried, no progress","Not yet","I would rather they were not involved yet"]}
    ]
  },
  condition:{
    icon:"tools",
    label:"Needs work", tag:"Condition",
    card:"The house needs more work than I want to take on",
    blurb:"Repairs, damage, or years of deferred maintenance that make listing it feel impossible.",
    also:"Roof, foundation, plumbing or electrical, fire or water damage, mold, a hoarder property, a half-finished renovation, condemned or red-tagged",
    headline:"Condition is what decides who can actually buy it.",
    intro:"Repairs can affect financing and selling options. Tell us about the condition so the team can review the property. Any offer depends on that review and a written agreement.",
    extra:{name:"conditionNotes", label:"Briefly, what is wrong with it? (optional)"},
    qs:[
      {id:"issue", key:true, q:"What is the main problem?", sub:"Pick the biggest one.",
       opts:["The roof","Foundation or structural","Plumbing, electrical or HVAC","Fire, water or mold damage","Years of clutter or a hoarder situation","Dated throughout, nothing broken","Several of these","Something else not listed"]},
      {id:"quoted", q:"Have you had the work priced?",
       opts:["Yes, I have real numbers","I have a rough idea","No quotes yet","I would rather not guess"]},
      {id:"repairIntent", q:"How would you rather handle the work?", sub:"There is no wrong answer. It changes what we bring you.",
       opts:["Sell it as it stands, I am not doing the work","I would do some of it, not all",
             "I would consider doing it if selling as-is costs too much","Something else"]}
    ]
  },
  rental:{
    icon:"keys",
    label:"Rental property", tag:"Landlord",
    card:"I own a rental I'm done with",
    blurb:"Tenants, turnover, repairs stacking up, or a property you manage from too far away.",
    also:"Non-paying tenant, mid-eviction, squatters, a vacant rental, Section 8, a small portfolio, an out-of-state property you never see",
    headline:"A rental is a different proposition to an owner-occupied house.",
    intro:"The team can review occupied rental properties. Any sale remains subject to lease terms, tenant rights, applicable law and a written agreement.",
    extra:{name:"rentalNotes", label:"Addresses or unit count if it is more than one property (optional)"},
    qs:[
      {id:"tenants", key:true, q:"What is the tenant situation?",
       opts:["Occupied and paying","Occupied and behind on rent","Occupied, the lease is ending soon","It is vacant right now","We are mid-eviction","Someone is in it without a lease","Something else"]},
      {id:"units", q:"How much are we talking about?",
       opts:["One property","Two to four units","Five or more units","Several addresses","Something else"]},
      {id:"trigger", q:"What tipped you into selling?",
       opts:["Tired of managing it","It stopped cash flowing","Repairs keep stacking up","Rebalancing or cashing out","I am out of state and it is a hassle",
             "Another reason not listed"]}
    ]
  },
  moving:{
    icon:"van",
    label:"Moving by a date", tag:"Timeline",
    card:"I need to be out by a certain date",
    blurb:"A job, a separation, a downsize, or a purchase that depends on this one closing.",
    also:"Relocation, divorce or separation, downsizing, a health or care move, already under contract on the next house, moving in with family",
    headline:"Working backwards from your date, here is what holds.",
    intro:"When a date matters more than the last few thousand, the real risk is a buyer whose financing collapses in week five. Tell us the date and the team will tell you honestly whether it can be met.",
    extra:{name:"movingNotes", label:"What date are you working towards? (optional)"},
    qs:[
      {id:"driver", key:true, q:"What is driving the move?",
       opts:["A job or relocation","Downsizing or upsizing","Divorce or separation",
             "Health, age or family care","I am buying another place first",
             "Money is tight and the payments are the problem",
             "I am behind on payments or facing foreclosure",
             "Another reason not listed"]},
      {id:"bothagree", key:true, q:"Are both parties agreed on selling?",
       when:function(a){return a.driver==="Divorce or separation";},
       opts:["Yes, we both want to sell","Mostly, we are close","Not yet","The attorneys are handling it"]},
      {id:"priority", q:"Which matters more to you?",
       opts:["A closing date I can count on","The highest possible number","A balance of the two",
            "I am not sure yet"]},
      {id:"possession", q:"Do you need time in the house after closing?",
       opts:["Yes, a few weeks","Yes, a month or more","No, I can be out at closing","Not sure yet"]}
    ]
  },
  comparing:{
    icon:"sign",
    label:"Weighing it up", tag:"Comparing",
    exclusive:true,
    card:"None of these, I'm just working out what it's worth",
    blurb:"Nothing urgent and nothing wrong. You want the real numbers before you decide anything.",
    also:"Curious what it would fetch, comparing an offer you already have, thinking about it for next year",
    headline:"Here is what your answers tell us about the property.",
    intro:"Nothing here is urgent, so take it at your own pace. The team will put real numbers together against what you have told us, and discuss the available options.",
    extra:null,
    qs:[
      {id:"question", key:true, q:"What are you actually trying to work out?",
       opts:["What the house is genuinely worth","What I would net listing against selling as-is","Whether a direct offer is a fair number","Whether now is the right time to sell",
             "Something else not listed"]},
      {id:"stage", key:true, q:"How far along are you?",
       opts:["Ready to move if the numbers work","Deciding over the next few months","A year or so out","Just curious"]}
    ]
  }
};

  var COMBOS = {
  "deadline|inherited":{
    t:"An inherited property with a foreclosure clock on it",
    p:"This is the most time-critical combination there is, and it is more common than people think. The estate has to be able to convey title before anything can close, and a foreclosure date does not pause while probate runs. Whoever you talk to needs to be working both clocks at once. Tell us the date on the first call and we will tell you honestly whether it can be met."},
  "condition|deadline":{
    t:"A house that needs work, with a date attached",
    p:"A deadline and repair needs can affect your options. Tell us about both. A particular price or closing date cannot be guaranteed."},
  "condition|inherited":{
    t:"An inherited house that also needs work",
    p:"Estates rarely have the cash to fund repairs, and heirs almost never want to spend their own money fixing a house they are selling. That is normal. It means the routes that buy it as it stands are usually the ones worth pricing."},
  "deadline|rental":{
    t:"A rental with a payment problem",
    p:"A tenant in place and arrears on the loan is a combination most buyers walk away from, because it needs both problems solved at once. It is worth telling us the rent and the arrears together on the first call, because the two numbers read very differently side by side than they do apart."},
  "condition|rental":{
    t:"A rental that needs work with somebody living in it",
    p:"Access, repair needs and existing tenancies can affect a sale. The team will review the circumstances; tenant rights and lease obligations still apply."},
  "deadline|moving":{
    t:"A move with a payment problem behind it",
    p:"Two dates that do not care about each other: the one you have to be out by, and the one the lender or the court has set. The route you pick has to satisfy the earlier of the two, and that is usually not a listing."},
  "inherited|moving":{
    t:"An estate property and a move of your own",
    p:"You are running your own timeline and the estate's at the same time, and probate sets the pace whether you like it or not. Worth being clear on the first call about which of the two is actually driving you."},
  "condition|moving":{
    t:"A house that needs work and a date to be out by",
    p:"Repairs before a listing would eat the time you do not have. The routes that take the house as it stands are the ones that can hold your date."},
  "moving|rental":{
    t:"A rental to unwind while you are moving yourself",
    p:"You are handling a tenant, a lease, and your own move at once. The good news is that the rental does not have to be empty for it to sell, so it does not have to be one more thing on your list."},
  "inherited|rental":{
    t:"An inherited property with tenants in it",
    p:"The lease came with the house and it survives the inheritance. That is not a problem to solve before selling, it is a fact to price in, and in some structures the rent is what makes the numbers work."}
};

  var COMMON = [
  {id:"location", q:"Where is the property?", sub:"We buy across "+MARKET+". The exact address comes later.",
   opts:["Florida","Ohio","North Carolina","Tennessee","Alabama","Indiana","Kansas City area","Another state"]},
  {id:"propertyType", q:"What kind of property is it?",
   opts:["Single family home","Townhouse","Condominium","Duplex or multi family","Mobile or manufactured home","Vacant land","Something else"]},
  {id:"priceExpectation", q:"Roughly what do you think it is worth?",
   sub:"A rough band is fine. It just tells us whether we are in the same ballpark before we call.",
   opts:["Under $150,000","$150,000 to $250,000","$250,000 to $400,000","$400,000 to $600,000","Over $600,000","I would rather not say"]},
  {id:"title", q:"Are you the owner on the title?", sub:"We can only work with somebody who is able to sign.",
   opts:["Yes, I am the owner","Yes, one of several owners","I am the executor, or I hold power of attorney","No, I am family helping out","No, I rent here","It is complicated, the title needs sorting out"]},
  {id:"listed", q:"Is it listed with an agent right now?",
   when:function(a,prim){return prim!=="comparing";},
   opts:["No","It was listed, that agreement has ended","Yes, it is listed now","It is under contract",
            "Something else"]},
  {id:"occupancy", q:"Who is in the property right now?",
   when:function(a,prim,has){return !has("rental");},
   opts:["I live there","A tenant","It is vacant","Family, or somebody else","Something else"]},
  {id:"equity", q:"What is left on the mortgage compared to what the house is worth?",
   sub:"This is the single number that changes the answer most. A rough guess is genuinely fine.",
   opts:["It is paid off, no mortgage","I owe less than half of what it is worth","I owe about half","I owe close to what it is worth","I owe more than it is worth","I am not sure"]},
  {id:"rate", q:"Roughly what interest rate is that loan at?",
   sub:"Worth checking before we speak, because it changes what is realistic.",
   when:function(a){return a.equity && a.equity!=="It is paid off, no mortgage";},
   opts:["Under 4 percent","Between 4 and 6 percent","Over 6 percent","I would have to look it up"]},
  {id:"cashneed", q:"Do you need all of the money at closing?",
   sub:"This is the other half of it. Any payment arrangement needs its own written terms and appropriate professional review.",
   opts:["Yes, all of it at closing","Some now, the rest over time would be fine","Monthly payments would actually suit me better","I would need to understand it first"]},
  {id:"timeline", q:"How soon do you want this resolved?",
   when:function(a,prim,has){return !(has("deadline") && a.dateset && a.dateset.indexOf("Yes")===0);},
   opts:["As soon as possible","Within 30 days","Thirty to ninety days","More than 90 days","It depends on the numbers"]}
];

  /* ------------------------------------------------------------------ *
   * STATE
   * ------------------------------------------------------------------ */

  var S = { situations: [], primary: null, phase: 'pick', i: 0,
            answers: {}, history: [] };

  function esc(t){ return String(t==null?'':t)
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
  function val(id){ var e=document.getElementById(id); return e?String(e.value||'').trim():''; }


  function has(k){ return S.situations.indexOf(k)>=0; }

  function queue(){
  var out=[], seen={};
  if(!S || !S.primary) return out;   /* part of the public handoff API, must not throw */
  function push(bk,q){ if(seen[q.id]) return; if(q.when&&!q.when(S.answers,S.primary,has)) return; seen[q.id]=1; out.push({b:bk,q:q}); }
  BRANCHES[S.primary].qs.forEach(function(q){ push(S.primary,q); });
  S.situations.forEach(function(k){
    if(k===S.primary) return;
    BRANCHES[k].qs.forEach(function(q){ if(q.key) push(k,q); });
  });
  COMMON.forEach(function(q){ push("common",q); });
  return out;
}

  function activeCombos(){
  var out=[], s=S.situations.slice().sort();
  for(var i=0;i<s.length;i++) for(var j=i+1;j<s.length;j++){
    var c=COMBOS[s[i]+"|"+s[j]];
    if(c) out.push({c:c, prim:(s[i]===S.primary||s[j]===S.primary)?0:1});
  }
  out.sort(function(a,b){return a.prim-b.prim;});
  return out.slice(0,2).map(function(x){return x.c;});
}

  function routeOut(a){
  if(a.title==="No, I rent here") return "renter";
  if(a.listed==="Yes, it is listed now") return "listed";
  if(a.listed==="It is under contract") return "contract";
  return null;
}

  function tier(){
  var a=S.answers;
  if(routeOut(a)) return {t:"X",why:"routed out"};
  var soon=a.timeline==="As soon as possible"||a.timeline==="Within 30 days";
  var mid=a.timeline==="Thirty to ninety days"||a.timeline==="It depends on the numbers";
  var canSign=a.title==="Yes, I am the owner"||a.title==="I am the executor, or I hold power of attorney";
  var partial=a.title==="Yes, one of several owners"||a.title==="No, I am family helping out";
  if(has("deadline")&&a.dateset==="Yes, within 30 days") return {t:"A",why:"date inside 30 days"};
  if(S.situations.length>2) return {t:"A",why:"three or more situations stacked, high motivation"};
  if(has("comparing")) return (a.stage==="Ready to move if the numbers work"&&canSign&&soon)
    ? {t:"B",why:"researching but ready"} : {t:"C",why:"research stage"};
  if(has("condition")&&a.repairIntent==="I would consider doing it if selling as-is costs too much"
     &&S.situations.length===1) return {t:"C",why:"weighing repairs against selling"};
  if(has("inherited")&&(a.agreed==="No, we are not agreed"||a.agreed==="We have not discussed it")) return {t:"B",why:"heirs not aligned"};
  if(has("moving")&&a.bothagree==="Not yet") return {t:"B",why:"both parties not agreed"};
  if(canSign&&soon) return {t:"A",why:"can sign, inside 30 days"};
  if(canSign&&mid) return {t:"B",why:"can sign, 30 to 90 days"};
  if(partial&&(soon||mid)) return {t:"B",why:"second signature needed"};
  if(a.timeline==="More than 90 days") return {t:"C",why:"more than 90 days out"};
  return {t:"B",why:"no urgency signal"};
}

  /* US ZIP prefixes map to states deterministically, so the seller never
     picks a state from a list of fifty. It is shown back to them and can be
     corrected on the call, so an edge case cannot silently write a wrong
     state into the CRM. */
  var ZIP_STATE=[["AL",350,369],["AK",995,999],["AZ",850,865],["AR",716,729],["CA",900,961],
  ["CO",800,816],["CT",60,69],["DE",197,199],["DC",200,205],["FL",320,349],["GA",300,319],
  ["GA",398,399],["HI",967,968],["ID",832,838],["IL",600,629],["IN",460,479],["IA",500,528],
  ["KS",660,679],["KY",400,427],["LA",700,714],["ME",39,49],["MD",206,219],["MA",10,27],
  ["MI",480,499],["MN",550,567],["MS",386,397],["MO",630,658],["MT",590,599],["NE",680,693],
  ["NV",889,898],["NH",30,38],["NJ",70,89],["NM",870,884],["NY",100,149],["NC",270,289],
  ["ND",580,588],["OH",430,459],["OK",730,749],["OR",970,979],["PA",150,196],["RI",28,29],
  ["SC",290,299],["SD",570,577],["TN",370,385],["TX",750,799],["UT",840,847],["VT",50,59],
  ["VA",220,246],["WA",980,994],["WV",247,268],["WI",530,549],["WY",820,831]];

  function stateFromZip(z){
  var d=(z||"").replace(/\D/g,"");
  if(d.length<5) return "";
  var p=parseInt(d.slice(0,3),10);
  for(var i=0;i<ZIP_STATE.length;i++){
    if(p>=ZIP_STATE[i][1]&&p<=ZIP_STATE[i][2]) return ZIP_STATE[i][0];
  }
  return "";
}

  function leadSummary(t, lead){
  var a=S.answers, out=[];
  var who=(val("firstName")+" "+val("lastName")).trim();
  var where=[val("city"),(lead&&lead.contact?lead.contact.state:""),val("zip")]
    .filter(Boolean).join(", ");
  out.push(who+" enquired through the website funnel about "+(val("address")||"a property")+
           (where?", "+where:"")+".");
  if(S.situations.length){
    out.push("Situation: "+S.situations.map(function(k){return BRANCHES[k].label;}).join(", ")+".");
  }
  activeCombos().forEach(function(c){ out.push("Note: "+c.t+"."); });
  var facts=[];
  if(a.timeline)  facts.push("timeline "+a.timeline.toLowerCase());
  if(a.title)     facts.push("ownership: "+a.title.toLowerCase());
  if(a.occupancy) facts.push("occupancy: "+a.occupancy.toLowerCase());
  if(a.equity)    facts.push("mortgage: "+a.equity.toLowerCase());
  if(a.issue)     facts.push("condition: "+a.issue.toLowerCase());
  if(a.propertyType) facts.push("property type: "+a.propertyType.toLowerCase());
  if(a.listed)    facts.push("listing status: "+a.listed.toLowerCase());
  if(facts.length) out.push("They told us "+facts.join("; ")+".");
  if(a.priceExpectation) out.push("Price expectation: "+a.priceExpectation+".");
  out.push("Preferred contact: "+(val("contactPref")||"not stated")+
           ", best time "+(val("bestTime")||"not stated")+".");
  out.push("Lead tier "+t.t+" ("+t.why+").");
  if(val("mhfNotes")) out.push("Their notes: "+val("mhfNotes"));
  return out.join(" ");
}

  /* ------------------------------------------------------------------ *
   * RENDER. Built from the site's own components, not the demo's.
   * ------------------------------------------------------------------ */

  var ICONS = {
    key:'<circle cx="8" cy="13" r="4"/><path d="M11 11.5 20 4M17.5 6.5 19.5 8.5M15.5 8.5 17.5 10.5"/>',
    doc:'<path d="M14 3H7a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V7z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h4"/>',
    tools:'<path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="m9.5 14.5 2 2M14 12l-4.5 4.5"/><path d="M15.5 10.2a2.2 2.2 0 1 0-2.6 3.4"/>',
    keys:'<path d="M3 21h8V9l-4-3-4 3z"/><path d="M11 21h10V12l-5-3-5 3"/><path d="M6.5 13h1M15.5 16h1"/>',
    van:'<path d="M3 17V7h11v10"/><path d="M14 10h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    sign:'<path d="M12 21V8"/><path d="M4 4h14l2.5 2.5L18 9H4z"/><path d="M9 21h6"/>'
  };
  function icon(n){ return '<svg viewBox="0 0 24 24" aria-hidden="true">'+(ICONS[n]||ICONS.sign)+'</svg>'; }

  function progress(){
    if (S.phase === 'pick') return 0;
    if (S.phase === 'contact' || S.phase === 'done') return 100;
    var q = queue().length || 1;
    return Math.round(Math.min(S.i / q, 1) * 88) + 6;
  }

  function shell(inner, showBar){
    var h = '';
    if (showBar !== false) {
      h += '<div class="mhf-bar" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="'
         + progress() + '"><span style="width:' + progress() + '%"></span></div>';
    }
    return h + inner;
  }

  /* ---- Step 1: the situation cards ---- */
  function pickHtml(){
    var h = '<div class="mhf-step">'
      + '<p class="kicker">Step one</p>'
      + '<h1 class="mhf-h">What is going on with the property?</h1>'
      + '<p class="mhf-sub">Pick everything that applies. Your answers help us understand '
      + 'your enquiry.</p>'
      + (S.situations.length
          ? '<p class="mhf-preset">We have ticked ' + esc(BRANCHES[S.situations[0]].label.toLowerCase())
            + ' from the page you came from. Add anything else that is true, or untick it.</p>'
          : '')
      + '<div class="mh-cards mhf-cards">';
    /* The card is a DIV, not a button, because each one now carries its own
       Continue and a button cannot be nested inside a button. The body is
       still one big tap target that toggles; Continue takes this situation
       straight through so nobody has to scroll to the foot of the list. */
    Object.keys(BRANCHES).forEach(function(k){
      var b = BRANCHES[k], on = S.situations.indexOf(k) >= 0;
      h += '<div class="mh-card mh-gold mhf-card' + (on ? ' on' : '') + '">'
         + '<button type="button" class="mhf-card-hit" aria-pressed="' + on + '" '
         + 'onclick="MHF.toggle(\'' + k + '\')">'
         + '<span class="mh-card-fig"><span class="mh-card-ic">' + icon(b.icon) + '</span>'
         + '<span class="mhf-tick" aria-hidden="true">&#10003;</span></span>'
         + '<span class="mh-card-b"><span class="mhf-card-h">' + esc(b.card) + '</span>'
         + '<span class="mhf-card-p">' + esc(b.blurb) + '</span></span></button>'
         + '<div class="mhf-card-acts">'
         + '<button type="button" class="mhf-card-go" onclick="MHF.pickAndGo(\'' + k + '\')">'
         + 'Continue &rarr;</button>'
         + '<span class="mhf-card-or">' + (on ? 'Selected' : 'or tick to add more') + '</span>'
         + '</div></div>';
    });
    h += '</div><div class="mhf-nav"><button class="btn solid" id="mhf-go" '
       + (S.situations.length ? '' : 'disabled ') + 'onclick="MHF.confirm()">Continue</button>'
       + '<span class="mhf-hint">' + (S.situations.length
            ? S.situations.length + ' selected'
            : 'Choose at least one to carry on') + '</span></div></div>';
    return h;
  }

  /* ---- Step 2: one tapped question at a time ---- */
  function questionHtml(){
    var qq = queue();
    if (S.i >= qq.length) { S.phase = 'outcome'; return outcomeHtml(); }
    var it = qq[S.i], q = it.q;
    var ctx = (it.b !== 'common' && it.b !== S.primary) ? BRANCHES[it.b].label : null;
    var h = '<div class="mhf-step">'
      + '<p class="kicker">' + (ctx ? esc('About the ' + ctx.toLowerCase()) : 'Your situation') + '</p>'
      + '<h2 class="mhf-h">' + esc(q.q) + '</h2>'
      + (q.sub ? '<p class="mhf-sub">' + esc(q.sub) + '</p>' : '')
      + '<div class="mhf-opts">';
    q.opts.forEach(function(o){
      h += '<button type="button" class="mhf-opt" onclick="MHF.answer(\'' + q.id + '\','
         + JSON.stringify(o).replace(/"/g,'&quot;') + ',' + JSON.stringify(q.q).replace(/"/g,'&quot;') + ')">'
         + '<span class="mhf-dot"></span><span>' + esc(o) + '</span></button>';
    });
    h += '</div>' + backBar(S.situations.map(function(k){return BRANCHES[k].label;}).join(' + ')) + '</div>';
    return h;
  }

  function backBar(trail){
    return '<div class="mhf-back"><button type="button" class="mhf-backbtn" onclick="MHF.back()">Back</button>'
         + (trail ? '<span class="mhf-trail">' + esc(trail) + '</span>' : '') + '</div>';
  }

  /* ---- Step 3: what we understood, then the contact step ---- */
  function outcomeHtml(){
    var out = routeOut(S.answers), m = BRANCHES[S.primary];
    if (out) {
      return '<div class="mhf-step"><p class="kicker">Before we go further</p>'
        + '<h2 class="mhf-h">' + esc(ROUTES[out].title) + '</h2>'
        + '<p class="mhf-sub">' + esc(ROUTES[out].copy) + '</p>'
        + '<div class="mhf-nav"><a class="btn solid" href="https://www.malihaus.com/">Back to the site</a>'
        + '<button class="btn ghost" onclick="MHF.restart()">Start again</button></div></div>';
    }
    var h = '<div class="mhf-step"><p class="kicker">Based on what you told us</p>'
      + '<h2 class="mhf-h">' + esc(m.headline) + '</h2>'
      + '<p class="mhf-sub">' + esc(m.intro) + '</p>';
    if (S.situations.length > 1) {
      h += '<div class="mhf-tags">';
      S.situations.forEach(function(k){ h += '<span>' + esc(BRANCHES[k].label) + '</span>'; });
      h += '</div>';
    }
    activeCombos().forEach(function(c){
      h += '<div class="mhf-combo"><h3>' + esc(c.t) + '</h3><p>' + esc(c.p) + '</p></div>';
    });
    h += '<div class="mhf-nav"><button class="btn solid" onclick="MHF.toContact()">'
       + 'Get My Numbers</button><span class="mhf-hint">One short step left</span></div>'
       + backBar('') + '</div>';
    return h;
  }

  /* ---- Step 4: the shortest contact step we can get away with ---- */
  function contactHtml(){
    function f(label, id, type, ac, extra){
      return '<div class="mhf-f"><label for="' + id + '">' + esc(label) + '</label>'
        + '<input name="' + ({firstName:'first_name',lastName:'last_name',address:'address',zip:'postal_code'}[id] || id) + '" id="' + id + '" type="' + type + '" autocomplete="' + ac + '" '
        + (extra || '') + '></div>';
    }
    function pick(label, name, opts, def){
      var h = '<div class="mhf-f mhf-full"><label>' + esc(label) + '</label><div class="mhf-picks" id="'
            + name + '-picks">';
      opts.forEach(function(o){
        h += '<button type="button" class="mhf-pk' + (o === def ? ' on' : '') + '" '
           + 'onclick="MHF.pick(this,\'' + name + '\')">' + esc(o) + '</button>';
      });
      return h + '</div><input type="hidden" id="' + name + '" value="' + esc(def) + '"></div>';
    }
    return '<form id="malihaus-seller-enquiry" class="mhf-step" onsubmit="event.preventDefault()"><p class="kicker">Last step</p>'
      + '<h2 class="mhf-h">Where should we send the numbers?</h2>'
      + '<p class="mhf-sub">A real person goes through the property with you and what it would actually '
      + 'pay you. Nothing here commits you to selling.</p>'
      + '<div class="mhf-form">'
      + f('First name','firstName','text','given-name')
      + f('Last name','lastName','text','family-name')
      + f('Phone','phone','tel','tel')
      + f('Email','email','email','email')
      + '<div class="mhf-f mhf-full">' + f('Street Address','address','text','street-address').replace(/^<div class="mhf-f">|<\/div>$/g,'') + '</div>'
      + f('City','city','text','address-level2')
      + f('ZIP code','zip','text','postal-code','inputmode="numeric" maxlength="10" oninput="MHF.zip(this.value)"')
      + '<div class="mhf-f mhf-full mhf-ziphint" id="mhf-zipstate"></div>'
      + pick('Best time to call','bestTime',['Any time','Morning','Afternoon','Evening'],'Any time')
      + pick('Call or text first','contactPref',['A call is fine','Text me first','Email me','Either is fine'],'A call is fine')
      + '<div class="mhf-f mhf-full"><label for="mhfNotes">'
      + esc((BRANCHES[S.primary].extra && BRANCHES[S.primary].extra.label)
            || 'Anything else we should know? (optional)')
      + '</label><textarea id="mhfNotes" rows="3"></textarea></div>'
      + '</div>'
      + '<label class="mhf-consent"><input type="checkbox" id="consent">'
      + '<span>' + consentHtml() + '</span></label>'
      + '<label class="mhf-consent"><input type="checkbox" id="marketingConsent"><span>Optional marketing permission. <span class="mhf-disc">' + esc(CFG.marketingConsentDisclosure || '') + '</span></span></label>'
      + '<div id="mhf-err" class="mhf-err" role="alert"></div>'
      + '<div class="mhf-nav"><button type="button" id="mhf-send" class="btn solid" onclick="MHF.submit()">Send My Property Enquiry</button>'
      + '<span class="mhf-hint">No obligation. Not a listing agreement.</span></div>'
      + backBar('') + '</form>';
  }

  /* Michael's approved A2P wording, verbatim, same as everywhere else. */
  function consentHtml(){
    var t = esc(CFG.consentCheckboxLabel || 'I agree to the Terms & Conditions and Privacy Policy.');
    if (CFG.termsUrl) t = t.replace('Terms &amp; Conditions',
      '<a href="' + esc(CFG.termsUrl) + '" target="_blank" rel="noopener">Terms &amp; Conditions</a>');
    if (CFG.privacyUrl) t = t.replace('Privacy Policy',
      '<a href="' + esc(CFG.privacyUrl) + '" target="_blank" rel="noopener">Privacy Policy</a>');
    return t + ' <span class="mhf-disc">' + esc(CFG.consentDisclosure || '') + '</span>';
  }

  function doneHtml(){
    return '<div class="mhf-step mhf-done"><div class="mhf-tickbig">&#10003;</div>'
      + '<h2 class="mhf-h">Thank you. We have what we need.</h2>'
      + '<p class="mhf-sub">Someone from the MaliHaus team will review the property and the situation '
      + 'you described and come back to you the way you asked.</p>'
      + '<a class="mhf-tel" data-call data-loc="funnel_done" href="#"><span data-phone></span></a>'
      + '<div class="mhf-nav"><a class="btn ghost" href="https://www.malihaus.com/situations/">Situations we help with</a>'
      + '<a class="btn ghost" href="https://www.malihaus.com/locations/">Areas we serve</a></div></div>';
  }

  function render(){
    var h = S.phase === 'pick'     ? pickHtml()
          : S.phase === 'question' ? questionHtml()
          : S.phase === 'outcome'  ? outcomeHtml()
          : S.phase === 'contact'  ? contactHtml()
          : doneHtml();
    MOUNT.innerHTML = shell(h, S.phase !== 'done');
    var f = MOUNT.querySelector('h1,h2');
    if (f && S.phase !== 'pick') { f.setAttribute('tabindex','-1'); f.focus({preventScroll:true}); }
    if (window.mhTrack) window.mhTrack('funnel_step', { step: S.phase, index: S.i });
  }

  /* ------------------------------------------------------------------ *
   * ACTIONS
   * ------------------------------------------------------------------ */

  var ROUTES = {
    renter: { title:"It sounds like you rent the property",
      copy:"We can only work with somebody who is able to sign, so we are not the right people for this. If you are helping the owner, ask them to start it themselves and we will pick it up from there." },
    listed: { title:"It is listed with an agent right now",
      copy:"While a listing agreement is live we stay out of it, both out of courtesy and because depending on your contract it can create a problem for you. Come back to us if the listing ends." },
    contract:{ title:"It is already under contract",
      copy:"There is nothing useful we can do while it is under contract. If it falls through, come back and we will move quickly." }
  };

  var MHF = {
    toggle: function(k){
      if (BRANCHES[k].exclusive) { S.situations = S.situations.indexOf(k)>=0 ? [] : [k]; }
      else {
        S.situations = S.situations.filter(function(x){ return !BRANCHES[x].exclusive; });
        var i = S.situations.indexOf(k);
        if (i>=0) S.situations.splice(i,1); else S.situations.push(k);
      }
      render();
    },
    /* Continue straight from one card. Selects it if it is not already
       selected, keeping anything else the visitor has ticked, then goes.
       An exclusive situation still clears the others, same as toggle. */
    pickAndGo: function(k){
      if (BRANCHES[k].exclusive) S.situations = [k];
      else {
        /* keep everything else already ticked, drop any exclusive one, and
           put this card FIRST: confirm() reads the primary off the head of
           the list, so the card they pressed is the branch they get. */
        S.situations = [k].concat(S.situations.filter(function(x){
          return x !== k && !BRANCHES[x].exclusive;
        }));
      }
      MHF.confirm();
    },
    confirm: function(){
      if (!S.situations.length) return;
      S.primary = S.situations[0];
      S.phase = 'question'; S.i = 0;
      if (window.mhTrack) window.mhTrack('funnel_situations', { situations: S.situations.join(',') });
      render();
    },
    answer: function(id, v, q){
      S.answers[id] = v;
      S.history.push({ q: q, a: v });
      S.i++;
      render();
    },
    back: function(){
      if (S.phase === 'contact') { S.phase = 'outcome'; return render(); }
      if (S.phase === 'outcome') { S.phase = 'question'; S.i = Math.max(0, queue().length - 1); return render(); }
      if (S.i > 0) { S.i--; S.history.pop(); return render(); }
      S.phase = 'pick'; render();
    },
    toContact: function(){ S.phase = 'contact'; render(); },
    restart: function(){ S = { situations:[], primary:null, phase:'pick', i:0, answers:{}, history:[] }; render(); },
    pick: function(btn, name){
      var row = document.getElementById(name + '-picks');
      for (var i=0;i<row.children.length;i++) row.children[i].className = 'mhf-pk';
      btn.className = 'mhf-pk on';
      document.getElementById(name).value = btn.textContent;
    },
    zip: function(v){
      var el = document.getElementById('mhf-zipstate');
      if (!el) return;
      var st = stateFromZip(v);
      DERIVED_STATE = st;
      el.textContent = st ? 'State: ' + st + '. Tell us on the call if that is wrong.' : '';
    },
    submit: function(){
      var err = document.getElementById('mhf-err');
      var first=val('firstName'), last=val('lastName'), phone=val('phone'), email=val('email'),
          addr=val('address'), city=val('city'), zip=val('zip');
      var state = DERIVED_STATE || stateFromZip(zip);
      var consent = document.getElementById('consent');
      var marketing = document.getElementById('marketingConsent');
      var need = [];
      if (!first) need.push('your first name');
      if (!last) need.push('your last name');
      if (!phone && !email) need.push('a phone number or an email address');
      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) need.push('a valid email address');
      if (phone && !/^(1\d{10}|\d{10})$/.test(phone.replace(/\D/g,''))) need.push('a valid US phone number');
      if (!addr) need.push('the property address');
      if (!city) need.push('the city');
      if (!/^\d{5}(-\d{4})?$/.test(zip)) need.push('a valid ZIP code');
      if (!consent || !consent.checked) need.push('the tick box so we are allowed to contact you');
      if (marketing && marketing.checked && !phone) need.push('a phone number for optional marketing permission');
      if (need.length) { err.textContent = 'We still need ' + need.join(', ') + '.'; return; }
      err.textContent = '';

      var t = tier(), now = new Date().toISOString();
      var lead = {
        leadSource: 'Website Funnel',
        situations: S.situations,
        primarySituation: S.primary,
        combinations: activeCombos().map(function(c){ return c.t; }),
        leadTier: t.t,
        tierReason: t.why,
        tags: ['Website Funnel', 'Tier ' + t.t],
        answers: queue().filter(function(item){return S.answers[item.q.id] != null;})
          .map(function(item){return {q:item.q.q, a:S.answers[item.q.id]};}),
        contact: { firstName:first, lastName:last, fullName:(first+' '+last).trim(),
                   phone:phone, email:email, address:addr, city:city, state:state, zip:zip,
                   propertyType: S.answers.propertyType || '',
                   priceExpectation: S.answers.priceExpectation || '',
                   bestTime: val('bestTime'), contactPreference: phone ? val('contactPref') : 'Email me' },
        notes: val('mhfNotes'),
        consent: { given:true, at:now, page:location.origin + location.pathname, policyVersion:'2026-10-06', text:CFG.consentCheckboxLabel + ' ' + CFG.consentDisclosure, marketing:!!(marketing && marketing.checked), marketingAt:(marketing && marketing.checked) ? now : null, marketingText:CFG.marketingConsentDisclosure },
        submittedAt: now,
        attribution: attribution()
      };
      lead.summary = leadSummary(t, lead);

      if (window.mhTrack) window.mhTrack('property_enquiry_submit',
        { form_name:'funnel' });
      try { sessionStorage.removeItem('mh_last_lead'); } catch(e){}
      window.mhLastLead = lead;

      if (!window.MHSellerDelivery) {
        err.textContent = 'Online delivery is unavailable. Please call ' + (CFG.phoneDisplay || '') + '.';
        return;
      }
      window.MHSellerDelivery.send(lead, S.answers).then(function(){
        try { if (window.MHAds) window.MHAds.leadCreated(lead.submittedAt); } catch(e){}
        S.phase='done'; render();
      }).catch(function(error){
        err.textContent = error.message + ' Please call ' + (CFG.phoneDisplay || '') + ' if you need help.';
      });
    }
  };
  window.MHF = MHF;

  /* Attribution is owned by site.js. Read it rather than keeping a copy. */
  function attribution(){
    try { return JSON.parse(sessionStorage.getItem('mh_attr') || '{}'); } catch(e){ return {}; }
  }
  var DERIVED_STATE = '';

  /* A visitor who clicked a specific situation on the site arrives with ?s=
     already set, so we skip the picker and start qualifying immediately.
     That is the point of putting the start action on each card. */
  (function seed(){
    var m = /[?&]s=([a-z]+)/.exec(location.search);
    if (!m) return;
    var k = m[1];
    if (!BRANCHES[k]) return;
    /* PRESELECT, do not skip. Arriving from "Sell a House Fast" used to jump
       straight into one branch's questions, which meant a seller who was also
       behind on payments was never offered the chance to say so. The card is
       ticked for them and the picker still shows, so they can add whatever
       else is true. */
    S.situations = [k];
    if (window.mhTrack) window.mhTrack('funnel_seeded', { situation: k });
  })();

  render();

  /* Land people on the funnel itself, not the top of the page, when they
     arrive from a card. */
  if (/[?&]s=/.test(location.search) || location.hash === '#start') {
    var t = document.getElementById('mhfunnel');
    if (t) t.scrollIntoView({ block: 'start' });
  }
})();
