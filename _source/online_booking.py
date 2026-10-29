"""Online advance booking: Steps 1 to 4 of the website payment workflow (Anand, 29 Oct 2026).

Step 1: choose a room and how to continue (pay online, or send details on WhatsApp).
Step 2: guest details.
Step 3: price summary with GST, cancellation policy, and Modify or Proceed.
Step 4: pay the advance (Paytm link for the tier), upload the screenshot, get the reference code.

Bookings are accepted only for stays that end on or before LAST_STAY (end of the price period).
"""
import html, json

LAST_STAY = "2027-01-31"

def _section(room_options, links, script_url, phone, room_json, periods_json):
    js = JS_TEMPLATE
    for k, v in {
        "__ROOMS__": room_json,
        "__PERIODS__": periods_json,
        "__LINKS__": json.dumps({str(a): u for a, u in links}),
        "__SCRIPT_URL__": script_url,
        "__PHONE__": phone,
        "__LAST_STAY__": LAST_STAY,
    }.items():
        js = js.replace(k, v)
    return f"""<section id="book-online" class="online"><div class="wrap">
<div class="enquire online-box">
<h2>Book online and pay your advance</h2>
<p class="online-note">Your advance is part of your total bill, which includes GST. Stays must end by 31 Jan 2027, when our current prices end.</p>
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
<label>Nights<select id="ob-nights">{''.join(f'<option>{n}</option>' for n in range(1, 11))}</select></label>
<label>Adults<select id="ob-adults">{''.join(f'<option>{n}</option>' for n in range(1, 13))}</select></label>
<label>Children up to 5 (free)<select id="ob-kids-small">{''.join(f'<option>{n}</option>' for n in range(0, 6))}</select></label>
<label>Children above 5 (Rs 250 a night)<select id="ob-kids-big">{''.join(f'<option>{n}</option>' for n in range(0, 6))}</select></label>
<label>Rooms<select id="ob-rooms">{''.join(f'<option>{n}</option>' for n in range(1, 7))}</select></label>
<label>Aadhaar, last 4 digits (optional)<input id="ob-aadhaar" type="text" inputmode="numeric" maxlength="4" placeholder="1234"></label>
</div>
<p class="ob-small">We use these details only to confirm your booking. The Aadhaar digits are optional and are kept only for our records.</p>
<p class="ob-error" id="ob-err2" hidden></p>
<div class="ob-actions"><button type="button" class="btn btn-line ob-back" data-go="1">Back</button><button type="button" class="btn btn-line ob-next" data-go="3">Next</button></div>
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
var R=__ROOMS__, PER=__PERIODS__, LINKS=__LINKS__, SCRIPT_URL='__SCRIPT_URL__', PHONE='__PHONE__', LAST='__LAST_STAY__';
var $=function(i){return document.getElementById(i)};
var box=$('ob-steps'); if(!box)return;
var steps=box.querySelectorAll('.ob-step');
var ref='';
function pad(x){return (x<10?'0':'')+x}
function iso(d){return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())}
function parse(v){var p=v.split('-');return new Date(+p[0],+p[1]-1,+p[2])}
function inP(s,L){for(var j=0;j<L.length;j++){if(s>=L[j][0]&&s<=L[j][1])return true}return false}
function nightRate(room,d){var s=iso(d),dy=d.getDay();if(inP(s,PER.card))return room.p[4];if(inP(s,PER.fest))return room.p[3];if(dy===6||inP(s,PER.sat))return room.p[2];return room.p[0]}
function rs(x){return 'Rs '+Math.round(x).toLocaleString('en-IN')}
function show(n){for(var i=0;i<steps.length;i++){steps[i].hidden=(+steps[i].getAttribute('data-step')!==n)}
  var top=box.getBoundingClientRect().top+window.pageYOffset-80; if(n>1)window.scrollTo({top:top,behavior:'smooth'});}
function err(id,msg){var e=$(id);e.textContent=msg;e.hidden=!msg}
function tier(total){return total<=1500?500:(total<=3000?1000:1500)}
function quote(room,ci,nights,adults,big,rooms){
  var t=0,d=new Date(ci);
  for(var i=0;i<nights;i++){t+=nightRate(room,d);d.setDate(d.getDate()+1)}
  t*=rooms;
  var extra=Math.max(0,adults+big-room.b*rooms);
  var sub=t+extra*250*nights;
  var gst=Math.round(sub*0.05);
  return {sub:sub,gst:gst,total:sub+gst,extra:extra,rooms:rooms};
}
function read(){
  var roomId=$('ob-room').value, room=R[roomId];
  var d={room:room,roomId:roomId,name:$('ob-name').value.trim(),mobile:$('ob-mobile').value.replace(/\s+/g,''),
    city:$('ob-city').value.trim(),checkin:$('ob-in').value,nights:+$('ob-nights').value,
    adults:+$('ob-adults').value,small:+$('ob-kids-small').value,big:+$('ob-kids-big').value,
    rooms:+$('ob-rooms').value,aadhaar:$('ob-aadhaar').value.trim()};
  return d;
}
function checkDetails(d){
  if(!d.room)return 'Please choose a room on Step 1.';
  if(d.name.length<2)return 'Please enter your name.';
  if(!/^[0-9]{10}$/.test(d.mobile))return 'Please enter a 10-digit mobile number.';
  if(!d.checkin)return 'Please choose a check-in date.';
  var ci=parse(d.checkin), today=new Date(); today.setHours(0,0,0,0);
  if(ci<today)return 'Check-in cannot be in the past.';
  var co=new Date(ci); co.setDate(co.getDate()+d.nights);
  if(iso(co)>LAST)return 'Online booking is open for stays ending by 31 Jan 2027. Please WhatsApp us for later dates.';
  if(d.aadhaar&&!/^[0-9]{4}$/.test(d.aadhaar))return 'Aadhaar: enter the last 4 digits, or leave it blank.';
  return '';
}
function summaryHtml(d,q,ci,co){
  var rows=[
    ['Room',d.room.n+' × '+d.rooms],['Check-in',ci.toDateString()+', 12 noon'],['Check-out',co.toDateString()+', 11 am'],
    ['Nights',d.nights],['Guests',d.adults+' adult'+(d.adults>1?'s':'')+(d.small?', '+d.small+' child up to 5':'')+(d.big?', '+d.big+' child above 5':'')],
    ['Extra persons',q.extra?q.extra+' × Rs 250 a night':'None'],
    ['Room charge',rs(q.sub)+' before GST'],['GST (5%)',rs(q.gst)],['Total bill',rs(q.total)],['Advance to pay now',rs(tier(q.total))+' (the rest at the hotel)']
  ];
  var s='<dl>';for(var i=0;i<rows.length;i++){s+='<dt>'+rows[i][0]+'</dt><dd>'+rows[i][1]+'</dd>'}
  return s+'</dl>';
}
var cur=null;
function fillSummary(){
  var d=read(); var m=checkDetails(d); if(m){err('ob-err2',m);show(2);return false}
  err('ob-err2','');
  var ci=parse(d.checkin), co=new Date(ci); co.setDate(co.getDate()+d.nights);
  var q=quote(d.room,ci,d.nights,d.adults,d.big,d.rooms);
  cur={d:d,q:q,ci:ci,co:co};
  $('ob-summary').innerHTML=summaryHtml(d,q,ci,co);
  var msg=waText();
  $('ob-wa').href='https://wa.me/'+PHONE+'?text='+encodeURIComponent(msg);
  var pathWa=$('ob-path').value==='wa';
  $('ob-proceed').hidden=pathWa; $('ob-wa').hidden=!pathWa;
  return true;
}
function waText(){
  var d=cur.d,q=cur.q,L=['Namaste! Online booking request from the website'+(ref?' (ref '+ref+')':''),''];
  L.push('Name: '+d.name+(d.city?' ('+d.city+')':''),'Mobile: '+d.mobile,'Check-in: '+cur.ci.toDateString()+', Nights: '+d.nights,
    'Guests: '+d.adults+' adult(s), '+d.small+' child(ren) up to 5, '+d.big+' child(ren) above 5','Room: '+d.room.n+' x '+d.rooms,
    'Total incl. GST: '+rs(q.total)+'  Advance: '+rs(tier(q.total)));
  if(d.aadhaar)L.push('Aadhaar last 4: '+d.aadhaar);
  L.push('','Please confirm availability and the booking.');
  return L.join('\n');
}
function payLink(){
  var t=tier(cur.q.total);
  $('ob-amount').textContent='Advance to pay: '+rs(t)+' (part of your total bill of '+rs(cur.q.total)+' incl. GST).';
  $('ob-paylink').href=LINKS[String(t)]||'#';
}
document.addEventListener('click',function(e){
  var b=e.target.closest?e.target.closest('[data-go]'):null; if(!b)return;
  var n=+b.getAttribute('data-go');
  if(n===3){ if(!fillSummary())return; }
  show(n);
});
$('ob-proceed').addEventListener('click',function(){ payLink(); show(4); });
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
    var payload={website:'',name:d.name,city:d.city,mobile:d.mobile,checkin:d.checkin,checkout:iso(cur.co),nights:d.nights,
      adults:d.adults,children:d.small+d.big,roomType:d.room.n,rooms:d.rooms,advance:tier(q.total),total:q.total,
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
// Room chosen from a room card: index.html?room=ID#book-online
var q=(location.search||'').match(/room=([a-z\-]+)/);
if(q&&R[q[1]]){$('ob-room').value=q[1]}
})();"""

def online_booking_section(room_options, links, script_url, phone, room_json, periods_json):
    return _section(room_options, links, script_url, phone, room_json, periods_json)
