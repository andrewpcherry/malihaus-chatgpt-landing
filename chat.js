/* MaliHaus conversational demo. Type anything, it copes.
   Shared by the concept home page and the receptionist page. */
(function(){
var $=function(id){return document.getElementById(id);};
var wid=$('wid'), body=$('wbody'), chips=$('chips'), launch=$('launch'),
    nudge=$('nudge'), input=$('winput'), sendBtn=$('wsend'), closeBtn=$('wclose');
if(!wid||!body) return;
var wait=function(ms){return new Promise(function(r){setTimeout(r,ms);});};
var busy=false, started=false;

var S={addr:null,city:null,situation:null,occupancy:null,condition:null,
       timeline:null,price:null,contact:null,booked:false,turns:0};

function el(cls,txt){var d=document.createElement('div');d.className=cls;d.textContent=txt;
  body.appendChild(d);body.scrollTop=body.scrollHeight;return d;}
function me(t){el('wb u',t);}
async function bot(lines){
  busy=true; setChips([]);
  for(var i=0;i<lines.length;i++){
    var t=document.createElement('div');t.className='wtyp';
    t.innerHTML='<i></i><i></i><i></i>';body.appendChild(t);body.scrollTop=body.scrollHeight;
    await wait(Math.min(1500,460+lines[i].length*7));
    t.remove(); el('wb a',lines[i]); await wait(260);
  }
  busy=false;
}
function setChips(list){
  chips.innerHTML='';
  list.forEach(function(c){
    var b=document.createElement('button');b.className='chip';b.textContent=c;
    b.addEventListener('click',function(){ if(busy)return; handle(c); });
    chips.appendChild(b);
  });
}

/* ---------- extraction ---------- */
/* City recognition for the demo receptionist. Covers the Florida cities the
   team hears most plus every national market MaliHaus now serves. */
var CITY=/(delray|boca raton|boca|lake worth|boynton|west palm|palm beach|coral springs|deerfield|pompano|fort lauderdale|ft lauderdale|lauderdale|miami|hollywood|jupiter|wellington|greenacres|riviera|hialeah|davie|plantation|sunrise|margate|tamarac|coconut creek|parkland|stuart|port st lucie|jacksonville|orlando|tampa|kissimmee|ocala|cleveland|memphis|birmingham|kansas city|indianapolis|cincinnati|charlotte|dayton|akron|greensboro|winston.?salem)/i;
var ADDR=/\d{1,6}\s+[\w'.-]+(\s+[\w'.-]+){0,3}\s*(st|street|ave|avenue|rd|road|dr|drive|ln|lane|ct|court|blvd|boulevard|way|ter|terrace|pl|place|cir|circle|hwy|pkwy|trail|trl)\b/i;
var PHONE=/(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})/;

/* ---------- what the seller might say ---------- */
var SIT=[
 {re:/inherit|probate|passed|mother|father|\bmom\b|\bdad\b|died|death|estate|grandmother|grandfather|aunt|uncle/i,
  v:'Inherited property',
  ack:"I am sorry, that is a hard reason to be selling. Inherited property is one of the things we deal with most, and we can work with you while probate is still open."},
 {re:/foreclos|behind|default|arrears|late on|missed payment|bank letter|lis pendens|auction date|catch up/i,
  v:'Behind on payments',
  ack:"That is far more common than people think, and it is usually not as late as it feels. Being behind does not stop you selling."},
 {re:/tenant|renter|rental|landlord|lease|section 8|squatter|eviction/i,
  v:'Rental property',
  ack:"A tenant in place is not a problem for us. In some cases it is worth more that way, because it becomes an income property rather than a fixer."},
 {re:/divorce|separat|split up|ex.?wife|ex.?husband|spouse/i,
  v:'Divorce',
  ack:"Understood, and we keep those quiet and straightforward. There is no sign in the yard and no strangers walking through."},
 {re:/relocat|moving|move out of state|new job|transferr|job offer|military|orders/i,
  v:'Relocating',
  ack:"That usually means a date you cannot move, which is exactly the situation a straight purchase suits."},
 {re:/hoard|full of stuff|junk|clutter|belongings|everything still in/i,
  v:'Property full of belongings',
  ack:"You can leave anything you do not want. We clear it. People are often more embarrassed about that than they need to be."},
 {re:/fire|flood|mold|mould|storm|hurricane|water damage|sinkhole/i,
  v:'Damage',
  ack:"Damage does not put us off and it does not need repairing before a sale. It just changes which route pays you most."},
 {re:/lien|back taxes|owe taxes|code violation|hoa|association|judgment/i,
  v:'Liens or violations',
  ack:"Liens, back taxes and code violations get settled at closing out of the proceeds. They rarely stop a sale, they just need to be known about."},
 {re:/listed|realtor|agent|mls|expired|didn.t sell|no offers/i,
  v:'Listed and did not sell',
  ack:"If it sat on the market without the right offer, that tells us something useful about the price and the condition rather than about the house."},
 {re:/vacant|empty|nobody living|sitting there|unoccupied/i,
  v:'Vacant',
  ack:"Vacant is straightforward, and it usually means we can move faster than you expect."},
 {re:/sick|illness|medical|nursing home|assisted living|care home|hospital/i,
  v:'Health or care move',
  ack:"I am sorry to hear that. Those sales usually need to be quick and quiet, and we can work to whatever timing the family needs."},
 {re:/tired|done with|fed up|had enough|stress/i,
  v:'Wants out',
  ack:"Understood. Sometimes the reason is simply that you have had enough of it, and that is a perfectly good reason."}
];

var QA=[
 {re:/how much|what.*worth|price|offer|number|value|ballpark|lowball|pay me|give me for/i,
  a:["I cannot put a number on it in a chat window and I would not trust anyone who did.",
     "What happens is that we inspect the property properly, then work out which of our three approaches fits it. We may buy it ourselves with our own cash, we may complete some repairs first and bring in an investor partner, or we may present it to our national investor network so investors compete for it."]},
 {re:/fee|commission|cost|charge|pay\s+(you\s+)?anything|owe\s+(you\s+)?anything|do i pay|what.s the catch|catch\b|hidden|free\b/i,
  a:["Nothing. No fees, no commission, and we cover the closing costs. You do not spend a dollar to sell to us and you owe nothing if you walk away."]},
 {re:/repair|fix|clean|paint|roof|renovat|condition|as is|inspection|tidy/i,
  a:["Nothing needs fixing, cleaning or painting. We buy it exactly as it stands, and there is no inspection contingency to fall through."]},
 {re:/how fast|how quick|how long|when could|timeline|close by|days|week/i,
  a:["Two to three weeks is typical because there is no lender involved. If you need longer, you pick the date instead, and if you need to stay on for a few weeks after closing that can usually be arranged."]},
 {re:/who are you|are you real|legit|scam|trust|bbb|review|how do i know|are you a company|is this real/i,
  a:["Fair question. We are MaliHaus Capital, based in Boca Raton, and we have been buying in Florida for over ten years.",
     "We close at a local title company every time, never in a kitchen, so there is an independent third party holding the money."]},
 {re:/agent|realtor|list it|listing|do i need an agent/i,
  a:["You do not need one for this. We are the buyer, not a middleman, so there is no listing agreement and nobody takes a percentage."]},
 {re:/proof of funds|cash|financ|mortgage.*you|where.*money|bank/i,
  a:["We use our own capital, so there is no loan approval to wait on. We are happy to show proof of funds before you commit to anything."]},
 {re:/obligat|commit|sign|contract|binding|pressure|back out|change my mind/i,
  a:["None at all. You can hear the number and say no. Nothing is signed until you decide you want to go ahead."]},
 {re:/still owe|mortgage|payoff|underwater|negative equity|owe more/i,
  a:["That is fine and it is very common. The mortgage gets paid off out of the sale at closing. If the numbers are tight we will tell you straight rather than waste your time."]},
 {re:/showing|open house|strangers|people walking|photos|sign in the yard/i,
  a:["None of that. No listing photos, no open house, no sign, and nobody walking through except one person having a quick look."]},
 {re:/tenant.*rights|do they have to leave|evict|kick out/i,
  a:["You do not have to remove anyone. Buyers holding for income would generally rather the tenant stayed."]},
 {re:/multiple|other buyer|competing|shop around|another offer/i,
  a:["Please do compare. It is the reason we assess every property against all three of our approaches instead of one, so you can see what each is actually worth to you."]}
];

var ASK={
 addr:"What is the address of the property?",
 situation:"What is going on with it, in your own words?",
 occupancy:"Is anyone living in it at the moment?",
 condition:"Is there anything you already know it needs?",
 timeline:"Roughly when would you want this done by?",
 contact:"Last thing, what is the best number to reach you on?"
};
var ORDER=['addr','situation','occupancy','condition','timeline','contact'];

var CHIPS={
 addr:["I would rather not say yet","How much can you pay?","Are there any fees?"],
 situation:["I inherited it","I am behind on payments","I am done being a landlord","Something else"],
 occupancy:["It is empty","A tenant is in it","I still live there"],
 condition:["The roof is old","It is dated inside","Nothing major","I have not been inside"],
 timeline:["As soon as possible","A month or two","No rush","Depends on the number"],
 contact:["I will give it on the call","How much can you pay?"],
 done:["What happens next?","Are there any fees?","Who are you exactly?"]
};

function nextSlot(){
  for(var i=0;i<ORDER.length;i++){ if(!S[ORDER[i]]) return ORDER[i]; }
  return null;
}

function extract(t){
  var learned=[];
  var m=t.match(ADDR);
  if(m && !S.addr){ S.addr=m[0]; learned.push('addr'); }
  var c=t.match(CITY);
  if(c && !S.city){ S.city=c[0]; if(!S.addr){ S.addr=c[0]; learned.push('city'); } }
  var p=t.match(PHONE);
  if(p && !S.contact){ S.contact=p[0]; learned.push('contact'); }
  if(!S.situation){
    for(var i=0;i<SIT.length;i++){ if(SIT[i].re.test(t)){ S.situation=SIT[i].v; learned.push('situation:'+i); break; } }
  }
  if(!S.occupancy){
    if(/\b(empty|vacant|nobody|no one|unoccupied)\b/i.test(t)){S.occupancy='Vacant';learned.push('occ');}
    else if(/\btenant|renter|rented|leased\b/i.test(t)){S.occupancy='Tenant in place';learned.push('occ');}
    else if(/\bi live|we live|still in it|living there|my home\b/i.test(t)){S.occupancy='Owner occupied';learned.push('occ');}
  }
  if(!S.condition){
    if(/\broof|kitchen|bath|dated|old|needs|damage|mold|mould|leak|ac\b|air condition|plumb|electric|foundation\b/i.test(t)){
      S.condition=t.slice(0,90); learned.push('cond');
    } else if(/\bnothing major|good shape|fine|tidy|nothing wrong|nothing really\b/i.test(t)){
      S.condition='Nothing major'; learned.push('cond');
    }
  }
  if(!S.timeline){
    if(/\basap|as soon|straight away|right away|quickly|urgent|this month|30 days\b/i.test(t)){S.timeline='As soon as possible';learned.push('time');}
    else if(/\bno rush|not in a hurry|whenever|no hurry|sometime\b/i.test(t)){S.timeline='No particular rush';learned.push('time');}
    else if(/\bmonth|weeks|spring|summer|fall|autumn|winter|next year|by [a-z]+\b/i.test(t)){S.timeline=t.slice(0,60);learned.push('time');}
  }
  return learned;
}

function sitAck(){
  for(var i=0;i<SIT.length;i++){ if(SIT[i].v===S.situation) return SIT[i].ack; }
  return null;
}

async function handle(text){
  if(window.mhTrack){
    if(!handle._started){ handle._started=true;
      window.mhTrack('chat_conversation_started',{chat_name:'website_receptionist'}); }
    handle._turns=(handle._turns||0)+1;
    window.mhTrack('chat_message',{chat_name:'website_receptionist',turn:handle._turns});
  }
  if(busy) return;
  text=(text||'').trim(); if(!text) return;
  me(text); if(input) input.value='';
  S.turns++;

  var before={situation:S.situation, addr:S.addr};
  var learned=extract(text);
  var lines=[];

  /* a direct question gets a direct answer first */
  var answered=false;
  for(var i=0;i<QA.length;i++){
    if(QA[i].re.test(text)){ lines=lines.concat(QA[i].a); answered=true; break; }
  }

  /* acknowledge a newly understood situation */
  if(!before.situation && S.situation){ var a=sitAck(); if(a) lines.unshift(a); }
  else if(!before.addr && S.addr && !answered){
    lines.push("Thank you. I have got " + S.addr + ".");
  }

  if(/\b(rather not|not yet|prefer not|later|no thanks|skip)\b/i.test(text)){
    if(!S.addr){ S.addr='Not given yet'; lines.push("That is fine, we can leave the address until you are ready."); }
  }

  if(!lines.length){
    if(text.length<4){ lines.push("Understood."); }
    else if(/\?\s*$/.test(text) || /^(what|how|when|why|who|where|can|could|do|does|is|are|will|would|should)\b/i.test(text)){
      lines.push("That is a fair question, and I would rather you got a straight answer on the call than a vague one from me here. I have flagged it so it gets covered.");
    } else {
      lines.push("Thank you, that is noted and it will be in front of whoever calls you.");
    }
  }

  var slot=nextSlot();

  if(!slot && !S.booked){
    S.booked=true;
    lines.push("That is everything I need. Someone will call you with a figure and the recent sales it is based on, and you will not be asked anything you have already told me.");
    lines.push("Would the morning or the afternoon suit you better?");
    await bot(lines); setChips(["Morning","Afternoon","Either is fine"]); return;
  }
  if(S.booked && /morning|afternoon|either|evening|any/i.test(text)){
    await bot(["Booked in. You will get a text confirming it shortly. Thanks for your time, and I am sorry again about the circumstances."]);
    setChips([]); if(input) input.placeholder='Ask anything else…';
    return;
  }
  if(slot){ lines.push(ASK[slot]); }

  await bot(lines);
  setChips(CHIPS[slot] || CHIPS.done);
}

/* ---------- open / close ---------- */
async function begin(){
  if(started) return; started=true;
  await bot(["Hello, you are through to MaliHaus. I am the MaliHaus AI receptionist, so you are talking to an assistant rather than a person, and I can pass you to the team whenever you want.",
             "I can help with anything about selling a property, at any hour. What is going on with the house?"]);
  setChips(["I inherited a house","I am behind on payments","I am done being a landlord","How much can you pay?"]);
  if(input) input.focus();
}
function open_(){
  if(!wid.classList.contains('open') && window.mhTrack)
    window.mhTrack('chat_open',{chat_name:'website_receptionist'});
  wid.classList.add('open');
  if(nudge) nudge.classList.remove('on');
  if(launch){ launch.style.opacity='0'; launch.style.pointerEvents='none'; }
  begin();
}
if(launch) launch.addEventListener('click',open_);
if(nudge) nudge.addEventListener('click',open_);
if(closeBtn) closeBtn.addEventListener('click',function(){
  wid.classList.remove('open');
  if(launch){ launch.style.opacity='1'; launch.style.pointerEvents='auto'; }
});
if(input){
  input.addEventListener('keydown',function(e){
    if(e.key==='Enter'){ e.preventDefault(); handle(input.value); }
  });
}
if(sendBtn) sendBtn.addEventListener('click',function(){ handle(input?input.value:''); });

if(nudge){
  setTimeout(function(){ if(!wid.classList.contains('open')) nudge.classList.add('on'); },4200);
  setTimeout(function(){ nudge.classList.remove('on'); },14000);
}
window.__maliOpenChat=open_;
})();
