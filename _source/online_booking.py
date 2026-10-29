"""Online advance booking: Steps 1 to 4 of the website payment workflow (Anand, 29 Oct 2026).

Step 1: choose a room type and how to continue (pay online, or send details on WhatsApp).
Step 2: guest details. Add more room types if the family needs them (mixing is allowed).
Step 3: price summary per room, GST, cancellation policy, Modify or Proceed.
Step 4: pay the advance (Paytm link for the tier), upload the screenshot, get the reference code.

Occupancy rules: the first 2 children up to 5 are free and not counted. Every other person
(adults, children above 5, and children up to 5 beyond the first 2) counts. Each room has a
maximum total and a maximum of adults. Extra persons beyond a room's base cost Rs 250 a night.
Bookings are accepted only for stays that end on or before LAST_STAY.
"""
import json

LAST_STAY = "2027-01-31"
MAX_ROOMS = 4
FREE_CHILDREN_UP_TO_5 = 2

# Maximum people per room (rooms page): total, and adults only.
ROOM_MAX = {
    "deluxe-double": (3, 3), "standard-double": (3, 3),
    "deluxe-triple": (5, 4), "premium-triple": (5, 4), "compact-triple": (5, 4), "standard-triple": (5, 4),
    "deluxe-family": (6, 6), "suite-ac": (6, 6), "standard-family": (6, 6), "suite-nonac": (6, 6),
}

def _select(name, values, default=None):
    return "".join(f'<option{" selected" if v == default else ""}>{v}</option>' for v in values)

def _section(room_options, links, script_url, phone, room_json, periods_json):
    rooms = json.loads(room_json)
    for rid, r in rooms.items():
        r["mt"], r["ma"] = ROOM_MAX[rid]
    js = JS_TEMPLATE
    for k, v in {
        "__ROOMS__": json.dumps(rooms, ensure_ascii=False),
        "__PERIODS__": periods_json,
        "__LINKS__": json.dumps({str(a): u for a, u in links}),
        "__SCRIPT_URL__": script_url,
        "__PHONE__": phone,
        "__LAST_STAY__": LAST_STAY,
        "__MAX_ROOMS__": str(MAX_ROOMS),
        "__FREE__": str(FREE_CHILDREN_UP_TO_5),
    }.items():
        js = js.replace(k, v)
    nights = _select("n", range(1, 11))
    adults = _select("a", range(1, 25), 2)
    small = _select("s", range(0, 6))
    big = _select("b", range(0, 6))
    return f"""<section id="book-online" class="online"><div class="wrap">
<div class="enquire online-box">
<h2>Book online and pay your advance</h2>
<p class="online-note">Your advance is part of your total bill, which includes GST. Stays must end by 31-01-2027, when our current prices end.</p>
<div id="ob-steps" class="ob-steps" aria-live="polite">

<div class="ob-step" data-step="1">
<p class="ob-title">Step 1 of 4: choose your room</p>
<div class="form ob-grid">
<label class="wide">Room type<select id="ob-room"><option value="">Choose a room</option>{room_options}</select></label>
<label>How do you want to continue?<select id="ob-path"><option value="pay">Pay the advance online now</option><option value="wa">Send my details on WhatsApp</option></select></label>
</div>
<div class="ob-actions"><button type="button" class="btn btn-line ob-next" data-go="2">Next</button></div>
</div>

<div class="ob-step" data-step="2" hidden>
<p class="ob-title">Step 2 of 4: your details</p>
<div class="form ob-grid">
<label>Name<input id="ob-name" type="text" autocomplete="name" placeholder="Full name" required></label>
<label>Mobile<input id="ob-mobile" type="tel" inputmode="numeric" maxlength="10" placeholder="10 digits" required></label>
<label>Coming from<input id="ob-city" type="text" placeholder="City"></label>
<label>Check-in<input id="ob-in" type="date" required></label>
<label>Nights<select id="ob-nights">{nights}</select></label>
<label>Adults<select id="ob-adults">{adults}</select></label>
<label>Children up to 5 (first 2 free)<select id="ob-kids-small">{small}</select></label>
<label>Children above 5 (Rs 250 a night)<select id="ob-kids-big">{big}</select></label>
<label>Aadhaar, last 4 digits (optional)<input id="ob-aadhaar" type="text" inputmode="numeric" maxlength="4" placeholder="1234"></label>
</div>
<p class="ob-small">We use these details only to confirm your booking. The Aadhaar digits are optional and are kept only for our records.</p>
<p class="ob-error" id="ob-err2" hidden></p>
<div class="ob-actions"><button type="button" class="btn btn-line ob-back" data-go="1">Back</button><button type="button" class="btn btn-line ob-next" data-go="2.5">Next</button></div>
</div>

<div class="ob-step" data-step="2.5" hidden>
<p class="ob-title">Step 2 of 4: choose your rooms</p>
<p id="ob-people" class="ob-small"></p>
<div id="ob-suggest" class="ob-suggest"></div>
<p class="ob-title">Or choose your rooms (up to 4)</p>
<div id="ob-rooms-pick" class="ob-pick"></div>
<div class="ob-actions"><button type="button" class="btn btn-line" id="ob-add-room">Add a room</button><button type="button" class="btn btn-line" id="ob-del-room">Remove last room</button></div>
<p class="ob-error" id="ob-err25" hidden></p>
<div class="ob-actions"><button type="button" class="btn btn-line ob-back" data-go="2">Back</button><button type="button" class="btn btn-line ob-next" id="ob-rooms-next">Next</button></div>
</div>

<div class="ob-step" data-step="3" hidden>
<p class="ob-title">Step 3 of 4: check your booking</p>
<div id="ob-summary" class="ob-summary"></div>
<p class="ob-small">Cancellation: free until 12 noon, one day before check-in, with a full refund of your advance or 6 months' credit. On festival dates, free until 7 days before check-in. After that, the first night is charged.</p>
<div class="ob-actions">
<button type="button" class="btn btn-line ob-back" data-go="2">Modify details</button>
<button type="button" class="btn btn-line ob-next" id="ob-proceed">Proceed</button>
<a class="btn btn-wa" id="ob-wa" href="#" target="_blank" rel="noopener" hidden>Send details on WhatsApp</a>
</div>
</div>

<div class="ob-step" data-step="4" hidden>
<p class="ob-title">Step 4 of 4: pay your advance</p>
<p id="ob-amount" class="ob-amount"></p>
<p class="ob-small">Pay by UPI or card on Paytm, then upload the screenshot of the payment here.</p>
<div class="ob-actions"><a class="btn btn-line" id="ob-paylink" href="#" target="_blank" rel="noopener">Open the Paytm payment link</a></div>
<label class="ob-file">Payment screenshot (JPG or PNG, up to 3 MB)<input id="ob-shot" type="file" accept="image/jpeg,image/png"></label>
<label class="ob-check"><input id="ob-consent" type="checkbox"> I agree that Hotel Saikrupa may keep these booking details to confirm and manage my stay.</label>
<p class="ob-error" id="ob-err4" hidden></p>
<div class="ob-actions"><button type="button" class="btn btn-line ob-back" data-go="3">Back</button><button type="button" class="btn btn-wa" id="ob-submit">Send for confirmation</button></div>
</div>

<div class="ob-step" data-step="5" hidden>
<p class="ob-title">Your advance is received for checking</p>
<p id="ob-done" class="ob-summary"></p>
<div class="ob-actions"><a class="btn btn-wa" id="ob-done-wa" href="#" target="_blank" rel="noopener">Send the screenshot and reference code on WhatsApp</a></div>
</div>

</div>
</div>
</div></section>
<script>
{js}
</script>"""

JS_TEMPLATE = r"""(function(){
var R=__ROOMS__, PER=__PERIODS__, LINKS=__LINKS__, SCRIPT_URL='__SCRIPT_URL__', PHONE='__PHONE__', LAST='__LAST_STAY__', MAXR=__MAX_ROOMS__, FREE=__FREE__;
var $=function(i){return document.getElementById(i)};
var box=$('ob-steps'); if(!box)return;
var steps=box.querySelectorAll('.ob-step');
var ROOM_OPTS=$('ob-room').innerHTML;
var IDS=Object.keys(R);
var ref='', cur=null, picked=[];
function pad(x){return (x<10?'0':'')+x}
var WD=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
function dmy(d){return pad(d.getDate())+'-'+pad(d.getMonth()+1)+'-'+d.getFullYear()}
function dmyDay(d){return WD[d.getDay()]+' '+dmy(d)}
function dmyStr(s){var p=s.split('-');return p[2]+'-'+p[1]+'-'+p[0]}
function iso(d){return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())}
function parse(v){var p=v.split('-');return new Date(+p[0],+p[1]-1,+p[2])}
function inP(s,L){for(var j=0;j<L.length;j++){if(s>=L[j][0]&&s<=L[j][1])return true}return false}
function nightRate(room,d){var s=iso(d),dy=d.getDay();if(inP(s,PER.card))return room.p[4];if(inP(s,PER.fest))return room.p[3];if(dy===6||inP(s,PER.sat))return room.p[2];return room.p[0]}
function rs(x){return 'Rs '+Math.round(x).toLocaleString('en-IN')}
function tier(total){return total<=1500?500:(total<=3000?1000:1500)}
function show(n){for(var i=0;i<steps.length;i++){steps[i].hidden=(+steps[i].getAttribute('data-step')!==n)}
  if(n>1){var top=box.getBoundingClientRect().top+window.pageYOffset-80; window.scrollTo({top:top,behavior:'smooth'});}}
function err(id,msg){var e=$(id);e.textContent=msg;e.hidden=!msg}
// ---- enquiry logging: every WhatsApp hand-off is logged first (within 4 seconds), then WhatsApp opens ----
var ENQ_TIMEOUT=4000;
function genRef(prefix){var now=new Date();return prefix+'-'+dmy(now)+'-'+('000'+Math.floor(Math.random()*10000)).slice(-4)}
function logEnquiry(payload){
  if(SCRIPT_URL.indexOf('PASTE_')===0)return Promise.resolve(null);
  var call=fetch(SCRIPT_URL,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(payload)})
    .then(function(r){return r.json()}).catch(function(){return null});
  var wait=new Promise(function(res){setTimeout(function(){res(null)},ENQ_TIMEOUT)});
  return Promise.race([call,wait]);
}
function goWa(href,payload){ logEnquiry(payload).then(function(){window.location.href=href}); }
function appendRef(href,ref){return href+encodeURIComponent('\nRef: '+ref)}

// ---- guests and rooms ----
function people(d){ // counted persons: adults, children above 5, children up to 5 beyond the free ones
  return {adults:d.adults, kids:Math.max(0,d.small-FREE)+d.big};
}
// Place people in the given rooms: base occupancy first, then extra up to each room's maximum.
function allocate(list,adults,kids){
  var rooms=list.map(function(id){var r=R[id];return {b:r.b,mt:r.mt,ma:r.ma,ad:0,kd:0,p:0}});
  var ad=adults,kd=kids,i,a,k;
  for(i=0;i<rooms.length;i++){var r=rooms[i];
    a=Math.min(ad,r.b,r.ma); ad-=a; r.ad+=a; r.p+=a;
    k=Math.min(kd,r.b-r.p); kd-=k; r.kd+=k; r.p+=k;}
  for(i=0;i<rooms.length;i++){var q=rooms[i];
    a=Math.min(ad,q.ma-q.ad,q.mt-q.p); ad-=a; q.ad+=a; q.p+=a;
    k=Math.min(kd,q.mt-q.p); kd-=k; q.kd+=k; q.p+=k;}
  return ad===0&&kd===0?rooms:null;
}
// Price a list of rooms for the stay. Returns null if the guests do not fit.
function priceList(list,d){
  var g=people(d), placed=allocate(list,g.adults,g.kids);
  if(!placed)return null;
  var ci=parse(d.checkin), nights=d.nights, lines=[], sub=0;
  for(var m=0;m<list.length;m++){
    var room=R[list[m]], dt=new Date(ci), t=0;
    for(var i=0;i<nights;i++){t+=nightRate(room,dt);dt.setDate(dt.getDate()+1)}
    var extra=Math.max(0,placed[m].p-room.b), ec=extra*250*nights;
    lines.push({n:room.n,persons:placed[m].p,base:room.b,room:t,extra:extra,extraCost:ec,sum:t+ec});
    sub+=t+ec;
  }
  var gst=Math.round(sub*0.05);
  return {lines:lines,sub:sub,gst:gst,total:sub+gst};
}
// Cheapest room combinations of 1 to 4 rooms that fit the guests
function suggestions(d){
  var found=[], n, a, b, c, e;
  function consider(list){var q=priceList(list,d); if(q)found.push({list:list,q:q});}
  for(a=0;a<IDS.length;a++){
    consider([IDS[a]]);
    for(b=a;b<IDS.length;b++){
      consider([IDS[a],IDS[b]]);
      for(c=b;c<IDS.length;c++){
        consider([IDS[a],IDS[b],IDS[c]]);
        for(e=c;e<IDS.length;e++){consider([IDS[a],IDS[b],IDS[c],IDS[e]]);}
      }
    }
  }
  found.sort(function(x,y){return x.q.total-y.q.total});
  var out=[], seen={};
  for(var i=0;i<found.length&&out.length<3;i++){
    var key=found[i].list.slice().sort().join('|');
    if(seen[key])continue; seen[key]=1; out.push(found[i]);
  }
  return out;
}
function setPick(list){
  var wrap=$('ob-rooms-pick'); wrap.innerHTML='';
  var rows=Math.max(1,list.length);
  for(var i=0;i<rows;i++){addPickRow(list[i]||'')}
  syncAddButtons();
}
function addPickRow(val){
  var n=document.querySelectorAll('#ob-rooms-pick select').length+1;
  var lab=document.createElement('label');
  lab.innerHTML='Room #'+n+'<select class="ob-pick-sel"><option value="">Choose a room</option>'+ROOM_OPTS+'</select>';
  $('ob-rooms-pick').appendChild(lab);
  if(val)lab.querySelector('select').value=val;
}
function syncAddButtons(){
  var c=document.querySelectorAll('#ob-rooms-pick select').length;
  $('ob-add-room').disabled=c>=MAXR; $('ob-del-room').disabled=c<=1;
}
$('ob-add-room').addEventListener('click',function(){addPickRow('');syncAddButtons()});
$('ob-del-room').addEventListener('click',function(){
  var rows=$('ob-rooms-pick').querySelectorAll('label'); if(rows.length>1){rows[rows.length-1].remove()} syncAddButtons();
});
function pickedIds(){
  var out=[], s=document.querySelectorAll('.ob-pick-sel');
  for(var i=0;i<s.length;i++){if(s[i].value)out.push(s[i].value)}
  return out;
}
function renderSuggestions(d){
  var people_=people(d), total=people_.adults+people_.kids;
  $('ob-people').textContent='For '+d.adults+' adult'+(d.adults>1?'s':'')+(d.big?' and '+d.big+' child'+(d.big>1?'ren':'')+' above 5':'')+(d.small>FREE?' and '+(d.small-FREE)+' child'+((d.small-FREE)>1?'ren':'')+' up to 5 (the first '+FREE+' are free)':'')+' we suggest these rooms:';
  var sug=suggestions(d), box2=$('ob-suggest'); box2.innerHTML='';
  if(!sug.length){
    var now=new Date(), gref=genRef('GRP');
    var gl=['Group Booking Enquiry + Ref ID: '+gref,'',
      'Name: '+d.name+(d.city?' ('+d.city+')':''),'Mobile: '+d.mobile,
      'Check-in: '+dmyDay(parse(d.checkin))+', Nights: '+d.nights,
      'Guests: '+d.adults+' adult(s), '+d.small+' child(ren) up to 5, '+d.big+' child(ren) above 5',
      'Rooms: more than '+MAXR+' rooms needed','','Please share the best offers and group discount.'];
    box2.innerHTML='<div class="ob-option group"><p><b>Connect with our Reservation Team for best offers and group discount.</b><br>Your group needs more than '+MAXR+' rooms, so we will arrange it for you on WhatsApp.</p><p class="ob-small">Reference: <b>'+gref+'</b></p><a class="btn btn-wa ob-group-wa" target="_blank" rel="noopener" href="https://wa.me/'+PHONE+'?text='+encodeURIComponent(gl.join('\n'))+'">Send group enquiry on WhatsApp</a></div>';
    var gb=box2.querySelector('.ob-group-wa');
    gb.addEventListener('click',function(e){e.preventDefault();
      goWa(this.href,{type:'group',ref:gref,name:d.name,mobile:d.mobile,city:d.city,checkin:dmyStr(d.checkin),nights:d.nights,
        adults:d.adults,small:d.small,big:d.big,rooms:'More than '+MAXR+' rooms',source:'Group enquiry (above '+MAXR+' rooms)',notes:''});});
    return;
  }
  sug.forEach(function(x,i){
    var names=x.list.map(function(id){return R[id].n}).join(' + ');
    var div=document.createElement('div'); div.className='ob-option';
    div.innerHTML='<p><b>Option '+(i+1)+': '+x.list.length+' room'+(x.list.length>1?'s':'')+'</b> ('+names+')<br>'+rs(x.q.total)+' in total including GST, for '+d.nights+' night'+(d.nights>1?'s':'')+'</p>';
    var btn=document.createElement('button'); btn.type='button'; btn.className='btn btn-line'; btn.textContent='Use this option';
    btn.addEventListener('click',function(){setPick(x.list)});
    div.appendChild(btn); box2.appendChild(div);
  });
}
function details(){
  return {name:$('ob-name').value.trim(),mobile:$('ob-mobile').value.replace(/\s+/g,''),
    city:$('ob-city').value.trim(),checkin:$('ob-in').value,nights:+$('ob-nights').value,
    adults:+$('ob-adults').value,small:+$('ob-kids-small').value,big:+$('ob-kids-big').value,
    aadhaar:$('ob-aadhaar').value.trim()};
}
function checkDetails(d){
  if(d.name.length<2)return 'Please enter your name.';
  if(!/^[0-9]{10}$/.test(d.mobile))return 'Please enter a 10-digit mobile number.';
  if(!d.checkin)return 'Please choose a check-in date.';
  var ci=parse(d.checkin), today=new Date(); today.setHours(0,0,0,0);
  if(ci<today)return 'Check-in cannot be in the past.';
  var co=new Date(ci); co.setDate(co.getDate()+d.nights);
  if(iso(co)>LAST)return 'Online booking is open for stays ending by 31-01-2027. Please WhatsApp us for later dates.';
  if(d.aadhaar&&!/^[0-9]{4}$/.test(d.aadhaar))return 'Aadhaar: enter the last 4 digits, or leave it blank.';
  return '';
}
function summaryHtml(d,q,ci,co){
  var s='<dl><dt>Check-in</dt><dd>'+dmyDay(ci)+', 12 noon</dd><dt>Check-out</dt><dd>'+dmyDay(co)+', 11 am</dd><dt>Nights</dt><dd>'+d.nights+'</dd>';
  s+='<dt>Guests</dt><dd>'+d.adults+' adult'+(d.adults>1?'s':'')+(d.small?', '+d.small+' child'+(d.small>1?'ren':'')+' up to 5'+(d.small>FREE?' ('+FREE+' free)':' (free)'):'')+(d.big?', '+d.big+' child'+(d.big>1?'ren':'')+' above 5':'')+'</dd>';
  for(var i=0;i<q.lines.length;i++){var L=q.lines[i];
    s+='<dt>Room '+(i+1)+'</dt><dd>'+L.n+': '+L.persons+' people'+(L.extra?', '+L.extra+' extra × Rs 250 a night':'')+'<br>'+rs(L.sum)+' before GST, for the stay</dd>';}
  s+='<dt>Room charge</dt><dd>'+rs(q.sub)+' before GST</dd><dt>GST (5%)</dt><dd>'+rs(q.gst)+'</dd><dt>Total bill</dt><dd>'+rs(q.total)+'</dd><dt>Advance to pay now</dt><dd>'+rs(tier(q.total))+' (the rest at the hotel)</dd></dl>';
  return s;
}
function roomNames(){return cur.q.lines.map(function(L){return L.n+' ('+L.persons+')'}).join(', ')}
function waText(){
  var d=cur.d,q=cur.q,L=['Namaste! Online booking request from the website'+(ref?' (ref '+ref+')':''),''];
  L.push('Name: '+d.name+(d.city?' ('+d.city+')':''),'Mobile: '+d.mobile,'Check-in: '+dmyDay(cur.ci)+', Nights: '+d.nights,
    'Guests: '+d.adults+' adult(s), '+d.small+' child(ren) up to 5, '+d.big+' child(ren) above 5',
    'Rooms: '+roomNames(),'Total incl. GST: '+rs(q.total)+'  Advance: '+rs(tier(q.total)));
  if(d.aadhaar)L.push('Aadhaar last 4: '+d.aadhaar);
  L.push('','Please confirm availability and the booking.');
  return L.join('\n');
}
function fillSummary(){
  var d=details(); d.roomList=picked; var ci=parse(d.checkin), co=new Date(ci); co.setDate(co.getDate()+d.nights);
  var q=priceList(d.roomList,d);
  cur={d:d,q:q,ci:ci,co:co};
  $('ob-summary').innerHTML=summaryHtml(d,q,ci,co);
  $('ob-wa').href='https://wa.me/'+PHONE+'?text='+encodeURIComponent(waText());
  var pathWa=$('ob-path').value==='wa';
  $('ob-proceed').hidden=pathWa; $('ob-wa').hidden=!pathWa;
}
function payLink(){
  var t=tier(cur.q.total);
  $('ob-amount').textContent='Advance to pay: '+rs(t)+' (part of your total bill of '+rs(cur.q.total)+' incl. GST).';
  $('ob-paylink').href=LINKS[String(t)]||'#';
}
document.addEventListener('click',function(e){
  var b=e.target.closest?e.target.closest('[data-go]'):null; if(!b)return;
  var n=+b.getAttribute('data-go');
  if(n===2.5){
    var d=details(), mm=checkDetails(d);
    if(mm){err('ob-err2',mm);show(2);return}
    err('ob-err2','');
    renderSuggestions(d);
    var first=$('ob-room').value, sugList=suggestions(d);
    var start=(first&&priceList([first],d))?[first]:(sugList.length?sugList[0].list:(first?[first]:[]));
    setPick(start);
    err('ob-err25','');
  }
  show(n);
});
$('ob-rooms-next').addEventListener('click',function(){
  var d=details(); var list=pickedIds();
  if(!list.length){err('ob-err25','Please choose at least one room.');return}
  if(list.length>MAXR){err('ob-err25','You can book up to '+MAXR+' rooms online.');return}
  if(!priceList(list,d)){err('ob-err25','These rooms do not fit these guests. Choose one of the options above, or add a room.');return}
  err('ob-err25',''); picked=list; fillSummary(); show(3);
});
$('ob-proceed').addEventListener('click',function(){ payLink(); show(4); });
$('ob-wa').addEventListener('click',function(e){ e.preventDefault();
  var d=cur.d, ref=genRef('ENQ');
  goWa(appendRef(this.href,ref),{type:'details',ref:ref,name:d.name,mobile:d.mobile,city:d.city,checkin:dmy(cur.ci),
    nights:d.nights,adults:d.adults,small:d.small,big:d.big,rooms:roomNames(),source:'Online booking: details sent on WhatsApp',notes:'Total incl. GST '+rs(cur.q.total)});
});
// Check availability form (on the home page): log, then open WhatsApp
var fgo=$('f-go');
if(fgo){ fgo.addEventListener('click',function(e){ e.preventDefault();
  var m=decodeURIComponent(this.href).match(/Ref: (WEB-[A-Z0-9]+)/), ref=m?m[1]:genRef('ENQ');
  var kids=$('f-c').value, rt=$('f-r').options[$('f-r').selectedIndex].text;
  goWa(this.href,{type:'availability',ref:ref,name:$('f-name').value.trim(),mobile:'',city:$('f-city').value.trim(),
    checkin:dmyStr($('f-in').value),nights:$('f-n').value,adults:$('f-a').value,small:0,big:0,rooms:$('f-rn').value+' room(s), '+rt,
    source:'Check availability form',notes:'Children: '+kids+' (ages not asked)'});
}); }
$('ob-submit').addEventListener('click',function(){
  err('ob-err4','');
  if(!$('ob-consent').checked){err('ob-err4','Please tick the consent box to continue.');return}
  var f=$('ob-shot').files[0];
  if(!f){err('ob-err4','Please upload the payment screenshot.');return}
  if(!/^image\/(jpeg|png)$/.test(f.type)){err('ob-err4','Please upload a JPG or PNG file.');return}
  if(f.size>3*1024*1024){err('ob-err4','Screenshot is too large (max 3 MB).');return}
  if(SCRIPT_URL.indexOf('PASTE_')===0){err('ob-err4','Online booking is not active yet. Please use WhatsApp on '+PHONE+'.');return}
  var reader=new FileReader();
  reader.onload=function(){
    var b64=String(reader.result).split(',')[1];
    var d=cur.d,q=cur.q;
    var payload={website:'',name:d.name,city:d.city,mobile:d.mobile,checkin:dmyStr(d.checkin),checkout:dmy(cur.co),nights:d.nights,
      adults:d.adults,children:d.small+d.big,roomType:roomNames(),rooms:q.lines.length,advance:tier(q.total),total:q.total,
      aadhaar4:d.aadhaar,consent:true,screenshot:b64,screenshotType:f.type};
    $('ob-submit').disabled=true;
    fetch(SCRIPT_URL,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(payload)})
      .then(function(r){return r.json()})
      .then(function(j){
        if(!j.ok){throw new Error(j.error||'Could not send')}
        ref=j.code;
        $('ob-done').innerHTML='Reference code: <b>'+ref+'</b><br>Please save this code. We will check your payment and send the official advance receipt on WhatsApp.';
        $('ob-done-wa').href='https://wa.me/'+PHONE+'?text='+encodeURIComponent('Payment screenshot for reference '+ref+'. '+cur.d.name);
        show(5);
      })
      .catch(function(){ $('ob-submit').disabled=false; err('ob-err4','We could not send this just now. Please try again, or WhatsApp us on '+PHONE+'.'); });
  };
  reader.readAsDataURL(f);
});
var qs=(location.search||'').match(/room=([a-z\-]+)/);
if(qs&&R[qs[1]]){$('ob-room').value=qs[1]}
})();"""

def online_booking_section(room_options, links, script_url, phone, room_json, periods_json):
    return _section(room_options, links, script_url, phone, room_json, periods_json)
