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
    comparing:{icon:'sign',label:'Property enquiry',tag:'Property',card:'I am considering selling a property',blurb:'Share the property details and your preferred selling timeframe.',exclusive:true,headline:'Tell us how to contact you about the property.',intro:'The MaliHaus team can review your enquiry. Any offer depends on property review and a separate written agreement.',extra:null,qs:[]},
    condition:{icon:'tools',label:'Property condition',tag:'Condition',card:'The property needs repairs',blurb:'Tell us about its current condition.',headline:'Tell us how to contact you about the property.',intro:'The MaliHaus team can review the condition you describe. No price or closing date is guaranteed.',extra:null,qs:[{id:'issue',q:'How would you describe the property condition?',opts:['Needs minor repairs','Needs major repairs','Renovation in progress','I am not sure']}]},
    rental:{icon:'keys',label:'Rental property',tag:'Property',card:'I am considering selling a rental property',blurb:'Share the property and occupancy details.',headline:'Tell us how to contact you about the property.',intro:'The MaliHaus team can review your property enquiry. Any sale requires a separate written agreement.',extra:null,qs:[]}
  };
  var COMBOS = {};
  var COMMON = [
    {id:'location',q:'Where is the property?',opts:['Florida','Ohio','North Carolina','Tennessee','Alabama','Indiana','Kansas City area','Another state']},
    {id:'propertyType',q:'What kind of property is it?',opts:['Single family home','Townhouse','Condominium','Duplex or multi family','Mobile or manufactured home','Vacant land','Something else']},
    {id:'title',q:'What is your relationship to the property?',opts:['Yes, I am the owner','Yes, one of several owners','I am an authorized representative','No, I am family helping out','No, I rent here']},
    {id:'occupancy',q:'Who occupies the property?',opts:['Owner occupied','Tenant occupied','Vacant','Other','I would rather not say']},
    {id:'timeline',q:'What is your preferred selling timeframe?',opts:['Within 30 days','Thirty to ninety days','More than 90 days','I am exploring options']}
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
    if(routeOut(a)) return {t:'X',why:'not the property owner or representative'};
    if(a.title==='Yes, I am the owner' && a.timeline==='Within 30 days') return {t:'A',why:'owner, preferred timeframe within 30 days'};
    return {t:'B',why:'property enquiry for review'};
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
      + '<h1 class="mhf-h">Tell us about your property</h1>'
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
        + '<div class="mhf-nav"><a class="btn solid" href="./">Back to the site</a>'
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
       + 'Continue to Contact Details</button><span class="mhf-hint">One short step left</span></div>'
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
      + '<h2 class="mhf-h">How should we contact you?</h2>'
      + '<p class="mhf-sub">Share your contact details so the team can respond to your property enquiry. Submitting does not commit you to selling.</p>'
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

  /* Separate enquiry acknowledgement and optional marketing consent. */
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
      + '<a class="mhf-tel" data-call data-loc="funnel_done" href="tel:+1' + esc(CFG.phoneDigits || '4079173347') + '"><span data-phone>' + esc(CFG.phoneDisplay || '407-917-3347') + '</span></a>'
      + '<div class="mhf-nav"><a class="btn ghost" href="/privacy-policy/">Privacy Policy</a>'
      + '<a class="btn ghost" href="./">Back to MaliHaus</a></div></div>';
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
      window.MHSellerDelivery.send(lead, S.answers).then(function(delivery){
        try { if (delivery && delivery.created === true && window.MHAds) window.MHAds.leadCreated(lead.submittedAt); } catch(e){}
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
