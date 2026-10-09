"""Builds the Hotel Saikrupa website.

site/      full pages for hosting (index.html, rooms.html, img/)
preview/   the same pages shaped for a claude.ai preview (index has no <html>/<head>)
"""
import html, json, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import *

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
E = html.escape
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mukta:wght@400;500;600;700&family=Rozha+One&display=swap">'
WA_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>'
WA_BASE = f"https://wa.me/{PHONE_INTL}?text="
import urllib.parse
def wa(msg): return WA_BASE + urllib.parse.quote(msg)
WA_HELLO = wa("Namaste, I would like to know room availability and the best price at Hotel Saikrupa, Shirdi.")

def rupees(n): return f"₹{n:,}"

def header(active=""):
    return f'''<header class="top"><div class="wrap">
<a class="brand" href="index.html" aria-label="Hotel Saikrupa home"><img src="img/emblem.png" alt="" width="44" height="44"><span><span class="word"><span class="h">Hotel</span> <span class="s">Saikrupa</span></span><small>Shirdi · since 1988</small></span></a>
<nav class="nav" aria-label="Main"><a href="index.html">Home</a><a href="rooms.html">Rooms</a><a href="index.html#aarti">Aarti timings</a><a href="index.html#reviews">Reviews</a><a href="index.html#reach">Reach us</a></nav>
<a class="btn btn-wa" href="{WA_HELLO}" target="_blank" rel="noopener">{WA_ICON}<span>WhatsApp {PHONE_DISPLAY}</span></a>
</div></header>'''

def footer():
    return f'''<div class="tag-band"><div class="wrap"><p>{TAGLINE}</p></div></div>
<footer><div class="wrap"><span>© Hotel Saikrupa, Shirdi · {E(ADDRESS)}</span><span><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram @hotel_saikrupa_shirdi</a></span></div></footer>
<a class="btn btn-wa sticky-wa" href="{WA_HELLO}" target="_blank" rel="noopener">{WA_ICON}<span>WhatsApp us</span></a>'''

def room_card(r):
    rid, name, ac, size, beds, guests, mx, photo, text = r
    p = PRICES.get(rid)
    price = f'<span><span class="muted">From</span> <b>{rupees(p)}</b> <span class="muted">/ night</span></span>' if p else '<span class="muted">Ask for today\'s rate</span>'
    msg = wa(f"Namaste, I would like to book a {name} ({ac}) at Hotel Saikrupa. Dates: __ . Guests: __ .")
    return f'''<article class="room"><img src="img/{photo}" alt="{E(name)}, {ac}" loading="lazy">
<div class="body"><span class="tag">{ac}</span><h3>{E(name)}</h3><p class="muted">{E(text)}</p>
<div class="facts"><span>{E(beds)}</span><span>Up to {E(mx)}</span></div>
<div class="price">{price}<a href="{msg}" target="_blank" rel="noopener">Book on WhatsApp</a></div></div></article>'''

FEATURED = ["deluxe-double", "deluxe-triple", "deluxe-family", "suite-ac", "standard-triple", "standard-double"]

def booking_box():
    opts = "".join(f'<option value="{r[0]}">{E(r[1])} ({r[2]})</option>' for r in ROOMS)
    return f"""<div class="enquire" id="book">
<h2>Check availability</h2>
<form class="form" id="enq" onsubmit="return false">
<label for="f-name">Your name<input id="f-name" type="text" autocomplete="name" placeholder="Name"></label>
<label for="f-city">Coming from<input id="f-city" type="text" placeholder="City"></label>
<label for="f-in">Check-in<input id="f-in" type="date" required></label>
<label for="f-n">Nights<select id="f-n"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></label>
<label for="f-a">Adults<select id="f-a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>8</option><option>10</option><option>15</option><option>20</option></select></label>
<label for="f-c">Children<select id="f-c"><option>0</option><option>1</option><option>2</option><option>3</option><option>4</option></select></label>
<label for="f-rn">Rooms<select id="f-rn"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6+</option></select></label>
<label for="f-r" class="wide">Room type<select id="f-r"><option value="">Any suitable room</option>{opts}</select></label>
<p class="est" id="f-est" aria-live="polite"></p>
<a class="btn btn-wa" id="f-go" href="{WA_HELLO}" target="_blank" rel="noopener">{WA_ICON}Ask on WhatsApp</a>
</form>
<p class="note">Best price guaranteed: our direct prices are always below booking sites. We reply on WhatsApp with availability for your dates. Or call {PHONE_DISPLAY}.<br><b>Advance payment by UPI after we confirm your room on WhatsApp.</b></p>
</div>"""

def room_js():
    d = {r[0]: {"n": f"{r[1]} ({r[2]})", "b": r[5], "ac": r[2] == "AC", "p": list(RATES[r[0]])} for r in ROOMS}
    return json.dumps(d, ensure_ascii=False)

def periods_js():
    return json.dumps({"fest": [[a, b] for _, a, b in FESTIVALS], "card": [[a, b] for _, a, b in CARD_PERIODS]})

JS = """<script>
(function(){
  var R=__ROOMS__, PER=__PERIODS__, PHONE='__PHONE__';
  var $=function(i){return document.getElementById(i)};
  var f={name:$('f-name'),city:$('f-city'),d:$('f-in'),n:$('f-n'),a:$('f-a'),c:$('f-c'),rn:$('f-rn'),r:$('f-r'),go:$('f-go'),est:$('f-est')};
  if(!f.go)return;
  var pad=function(x){return (x<10?'0':'')+x};
  var iso=function(x){return x.getFullYear()+'-'+pad(x.getMonth()+1)+'-'+pad(x.getDate())};
  var t=new Date(); t.setDate(t.getDate()+1);
  f.d.min=iso(new Date()); if(!f.d.value)f.d.value=iso(t);
  var ref='WEB-'+Math.random().toString(36).slice(2,6).toUpperCase();
  function parse(v){var p=v.split('-');return new Date(+p[0],+p[1]-1,+p[2]);}
  function nice(d){return d.toLocaleDateString('en-IN',{weekday:'short',day:'numeric',month:'short',year:'numeric'});}
  function inr(x){return '\\u20b9'+x.toLocaleString('en-IN');}
  function upd(){
    var nights=+f.n.value, adults=+f.a.value, kids=+f.c.value, rooms=parseInt(f.rn.value,10);
    var lines=['\\ud83d\\ude4f Namaste! Booking enquiry from the website','Ref: '+ref,''];
    if(f.name.value.trim())lines.push('Name: '+f.name.value.trim());
    if(f.city.value.trim())lines.push('Coming from: '+f.city.value.trim());
    var est='';
    if(f.d.value){
      var ci=parse(f.d.value), co=new Date(ci); co.setDate(co.getDate()+nights);
      lines.push('Check-in: '+nice(ci)+', 12 noon');
      lines.push('Check-out: '+nice(co)+', 11 am');
      lines.push('Nights: '+nights);
      lines.push('Guests: '+adults+' adult'+(adults>1?'s':'')+(kids?', '+kids+' child'+(kids>1?'ren':''):''));
      lines.push('Rooms: '+f.rn.value);
      function inP(s,L){for(var j=0;j<L.length;j++){if(s>=L[j][0]&&s<=L[j][1])return true;}return false;}
      function nightRate(room,d){var s=iso(d),dy=d.getDay();if(inP(s,PER.card))return room.p[4];if(inP(s,PER.fest))return room.p[3];if(dy===6)return room.p[2];if(dy===4||dy===5||dy===0)return room.p[1];return room.p[0];}
      function cost(room){var t=0,d=new Date(ci);for(var i=0;i<nights;i++){t+=nightRate(room,d);d.setDate(d.getDate()+1);}t*=rooms;var ex=Math.max(0,adults-room.b*rooms);return {t:t+ex*250*nights,ex:ex};}
      function fits(room){var a=Math.ceil(adults/rooms),k=Math.ceil(kids/rooms);if(room.b===2)return a+k<=3;if(room.b===3)return a<=4&&a+k<=5;return a<=6&&a+k<=6;}
      function exTxt(ex){return ex?' (incl. '+ex+' extra adult'+(ex>1?'s':'')+')':'';}
      var nn=nights+' night'+(nights>1?'s':'');
      var room=R[f.r.value];
      if(room){
        lines.push('Room type: '+room.n);
        var c=cost(room), gst=Math.round(c.t*0.05);
        est='Estimated: '+inr(c.t)+' + '+inr(gst)+' GST for '+nn+exTxt(c.ex)+'.';
        lines.push('Website estimate: '+inr(c.t)+' + GST for '+nn+exTxt(c.ex));
      } else {
        lines.push('Room type: Any suitable room');
        var best={}, k;
        for(k in R){var r=R[k];if(!fits(r))continue;var key=r.ac?'ac':'non';var c2=cost(r);if(!best[key]||c2.t<best[key].c.t)best[key]={r:r,c:c2};}
        var sug=[];
        if(best.non)sug.push(best.non.r.n+' '+inr(best.non.c.t)+exTxt(best.non.c.ex));
        if(best.ac)sug.push(best.ac.r.n+' '+inr(best.ac.c.t)+exTxt(best.ac.c.ex));
        if(sug.length){
          est='Suggested for your group, '+nn+': '+sug.join(' or ')+', plus 5% GST.';
          lines.push('Suggested: '+sug.join(' / ')+' + GST for '+nn);
        }
      }
      if(kids)est+=(est?' ':'')+'Children above 5 years are charged ₹250 per night.';
      if(est)est+=' Each night is priced by its day: Mon\u2013Wed lowest, festival dates higher. We confirm on WhatsApp.';
    }
    lines.push('','Please confirm availability and the best price.');
    f.est.textContent=est; f.est.hidden=!est;
    f.go.href='https://wa.me/'+PHONE+'?text='+encodeURIComponent(lines.join('\\n'));
  }
  ['name','city','d','n','a','c','rn','r'].forEach(function(k){f[k].addEventListener('change',upd);f[k].addEventListener('input',upd)});
  upd();
})();
</script>"""

def hours(h):  # 4.5 -> left %
    return (h - 4) / 19 * 100

def aarti():
    marks = [(4.5, "4:30 am", "Kakad Aarti", "Dawn aarti"), (12, "12:00 noon", "Madhyan Aarti", "Midday aarti"),
             (18.25, "At sunset", "Dhoop Aarti", "Evening aarti"), (22, "10:00 pm", "Shej Aarti", "Night aarti")]
    m = "".join(f'<div class="mark" style="left:{hours(h):.1f}%"><span class="t">{t}</span><i></i><b>{n}</b><span>{s}</span></div>' for h, t, n, s in marks)
    return f'''<section class="aarti" id="aarti"><div class="wrap">
<div class="section-head"><span class="eyebrow">Plan your darshan</span><h2>Aarti timings at the Samadhi Mandir</h2>
<p class="muted">Four aartis mark Shri Saibaba's day. From our door it is 350 m on foot, about 5 minutes, to Gate 5/6, so you can step out just before an aarti and be back to rest after.</p></div>
<div class="darshan">
<figure><img src="img/samadhi-face.jpg" alt="Shri Saibaba at the Samadhi Mandir, Shirdi" loading="lazy" width="600" height="898"></figure>
<figure><img src="img/samadhi-mandir.jpg" alt="Shri Saibaba Samadhi Mandir, Shirdi" loading="lazy" width="900" height="602"></figure>
<p class="credit">Photo courtesy: Shri Saibaba Sansthan Trust, Shirdi</p>
</div>
<div class="day"><div class="day-inner"><div class="day-bar"></div>{m}
<div class="day-scale"><span>4 am</span><span>8 am</span><span>12 noon</span><span>4 pm</span><span>8 pm</span><span>11 pm</span></div></div></div>
<p class="src muted">Timings are set by Shri Saibaba Sansthan Trust, Shirdi, and can change on festival days. Our reception will confirm them for your dates.</p>
</div></section>'''

def index_body():
    cards = "".join(room_card(r) for r in ROOMS if r[0] in FEATURED)
    revs = "".join(f'<blockquote><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><p>“{E(q)}”</p><cite>{E(n)} · Google review, {E(d)}</cite></blockquote>' for q, n, d in REVIEWS)
    route = '''<svg viewBox="0 0 220 40" role="img" aria-label="Walking route from Hotel Saikrupa to Gate 5/6, 350 metres">
<path d="M10 28 C 60 28, 70 12, 110 14 S 170 26, 210 12" fill="none" stroke="var(--marigold)" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/>
<circle cx="10" cy="28" r="6" fill="var(--blue)"/><circle cx="210" cy="12" r="6" fill="var(--red)"/></svg>'''
    return f'''{header()}
<main>
<section class="hero"><div class="wrap">
<div><span class="eyebrow">Shirdi · Kankuri Road · since 1988</span>
<h1>Five minutes' walk to <em>Shri Saibaba's</em> Samadhi Mandir</h1>
<p class="lead">A family-run, pure-vegetarian hotel in Shirdi with 38 AC and non-AC rooms, from budget doubles to family suites for six.</p>
<p class="tagline">{TAGLINE}</p>
<div class="ctas"><a class="btn btn-wa" href="#book">{WA_ICON}Check availability</a><a class="btn btn-line" href="rooms.html">See rooms and prices</a></div>
<p class="phone-line">Call or WhatsApp <b>{PHONE_DISPLAY}</b> · Landline {LANDLINES}</p></div>
<div class="hero-photo"><img src="img/facade-new-hero.jpg" alt="Hotel Saikrupa building on Kankuri Road, Shirdi" width="1600" height="1374">
<div class="route">{route}<div><strong>350 m · 5 min walk</strong><span class="lbl">to Samadhi Mandir, Gate 5/6</span></div></div></div>
</div></section>

<div class="wrap">{booking_box()}
<div class="proof">
<div><b>4.6 ★</b><span>on Google, from 1,160+ guest reviews</span></div>
<div><b>97%</b><span>of 2025–26 guests rated us 4 or 5 stars</span></div>
<div><b>38</b><span>rooms, including family rooms and suites for up to 6</span></div>
<div><b>24 × 7</b><span>hot water, Wi-Fi on every floor, ample parking</span></div>
</div></div>

<section id="rooms"><div class="wrap">
<div class="section-head"><span class="eyebrow">Rooms</span><h2>A room for every group, from two to six</h2>
<p class="muted">Every room has an attached bathroom, a 32-inch LED TV and 24-hour hot water. Lowest (Monday to Wednesday) prices shown, plus 5% GST. Our website and WhatsApp prices are always below booking sites.</p></div>
<div class="rooms">{cards}</div>
<p class="more"><a class="btn btn-line" href="rooms.html">All 9 room types, with beds and sizes</a></p>
</div></section>

{aarti()}

<section id="stay"><div class="wrap">
<div class="section-head"><span class="eyebrow">The hotel</span><h2>Simple, clean, and run by a family since 1988</h2><p class="muted" style="font-size:1.1rem">Founded in 1988 by Dr. Avinash Kotasthane, Hotel Saikrupa has been a second home to Shri Saibaba's devotees for 38 years.</p></div>
<div class="fac">
<figure class="f1"><img src="img/reception.jpg" alt="Reception with a portrait of Shri Saibaba" loading="lazy"><figcaption>Reception</figcaption></figure>
<figure class="f2"><img src="img/murti.jpg" alt="Shri Saibaba murti in the hotel lobby" loading="lazy"><figcaption>Shri Saibaba murti in the lobby</figcaption></figure>
<figure class="f3"><img src="img/lobby.jpg" alt="Hotel lobby" loading="lazy"><figcaption>Lobby</figcaption></figure>
<figure class="f4"><img src="img/since-1988.jpg" alt="Hotel Saikrupa signboard, established 1988" loading="lazy"><figcaption>स्थापना १९८८</figcaption></figure>
<figure class="f5"><img src="img/terrace.jpg" alt="Covered terrace garden on the first floor" loading="lazy"><figcaption>Terrace garden, first floor</figcaption></figure>
<figure class="f6"><img src="img/parking.jpg" alt="Hotel parking area" loading="lazy"><figcaption>Ample parking</figcaption></figure>
</div>
<ul class="amen">
<li>Pure vegetarian, alcohol-free, no smoking</li><li>24-hour hot water (central solar system)</li><li>High-speed Wi-Fi on all floors and in the lobby</li>
<li>32-inch LED TV in every room</li><li>Covered terrace garden restaurant, first floor</li><li>Breakfast from November 2026</li>
<li>Ample parking for cars and buses</li><li>Check-in 12 noon · Check-out 11 am</li><li>Children up to 5 years stay free</li>
</ul>
</div></section>

<section id="reviews" style="background:var(--paper-2)"><div class="wrap">
<div class="section-head"><span class="eyebrow">Reviews</span><h2>What our guests write</h2></div>
<div class="rv-top"><b>4.6 ★</b><span class="muted">Google rating from 1,160+ reviews · 4.88 average for reviews since 2025</span></div>
<div class="reviews">{revs}</div>
<div class="rv-cta"><a class="btn btn-line" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Read all reviews on Google</a>{('<a class="btn btn-line" href="'+GOOGLE_WRITE_REVIEW+'" target="_blank" rel="noopener">Stayed with us? Write a review</a>') if GOOGLE_WRITE_REVIEW else ''}</div>
</div></section>

<section id="faq" style="background:var(--paper-2)"><div class="wrap"><div class="section-head"><span class="eyebrow">Questions</span><h2>Staying near the Samadhi Mandir: common questions</h2></div><div class="faq"><details><summary>How far is Hotel Saikrupa from Shri Saibaba Samadhi Mandir?</summary><p>350 m on foot, about 5 minutes, to Gate 5/6 of the Samadhi Mandir. The hotel is behind the Shirdi Nagar Parishad office on Kankuri Road.</p></details><details><summary>Do you have family rooms for 4 to 6 people?</summary><p>Yes. We have family rooms with 2 double beds and family suites with 2 rooms behind one private entrance, each for up to 6 guests.</p></details><details><summary>Do you have AC and non-AC rooms?</summary><p>Yes. Doubles, triples and family rooms are available in both AC and non-AC.</p></details><details><summary>What are the check-in and check-out times?</summary><p>Check-in is at 12 noon and check-out at 11 am.</p></details><details><summary>Is parking available?</summary><p>Yes, there is ample parking for cars and buses at the hotel.</p></details><details><summary>How far is Sainagar Shirdi railway station and Shirdi Airport?</summary><p>Sainagar Shirdi railway station is about 3 km away and Shirdi Airport about 14 km. We can help arrange a taxi.</p></details><details><summary>How do I pay the advance?</summary><p>By UPI to the hotel's bank account, after we confirm your room on WhatsApp. Our staff share the payment details with you there.</p></details><details><summary>Do your prices go up at festivals?</summary><p>Festival nights (Dasara 16–20 Oct, Diwali 6–15 Nov, Makar Sankranti 14–16 Jan, Republic Day 23–26 Jan) use our festival price, and Christmas–New Year (23 Dec–4 Jan) our published tariff. Since 1988 we have never charged above our published tariff.</p></details><details><summary>How do I get the best price?</summary><p>Book directly on WhatsApp at 8262 800 200. Our direct prices are always below booking sites.</p></details></div></div></section>

<section id="policies"><div class="wrap info">
<div><div class="section-head"><span class="eyebrow">Good to know</span><h2>House rules</h2></div>
<dl class="dl"><dt>Check-in</dt><dd>12 noon</dd><dt>Check-out</dt><dd>11 am</dd>
<dt>ID</dt><dd>Valid photo ID for every guest. Foreign nationals: passport and valid visa.</dd>
<dt>Children</dt><dd>Free up to 5 years. Above 5 years, charged as an extra person (₹250 per night).</dd>
<dt>Food</dt><dd>Pure vegetarian premises. No alcohol, no smoking, no visitors in guest rooms.</dd>
<dt>Lift</dt><dd>No lift; rooms are on the ground, first and second floors. Ask for a ground-floor room if needed.<br><em>A modern hydraulic lift is being installed and will be ready by 15 December 2026.</em></dd>
<dt>Cancellation</dt><dd>Free up to 15 days before arrival. 50% from 15 days to 48 hours. No refund within 48 hours.</dd></dl></div>
<div><div class="section-head"><span class="eyebrow">Getting here</span><h2>Distances</h2></div>
<figure class="walkmap"><svg viewBox="0 0 600 380" role="img" aria-label="Walking route: Hotel Saikrupa to Gate 5/6 of Shri Saibaba Samadhi Mandir, 350 metres, about 5 minutes">
<rect x="0" y="0" width="600" height="380" rx="12" fill="var(--paper-2)"/>
<path d="M205 -10 L 255 160 L 300 270 L 335 390" fill="none" stroke="var(--line)" stroke-width="34" stroke-linecap="round"/>
<path d="M205 -10 L 255 160 L 300 270 L 335 390" fill="none" stroke="var(--card)" stroke-width="2" stroke-dasharray="10 10"/>
<path d="M330 165 L 610 135" fill="none" stroke="var(--line)" stroke-width="16"/>
<path d="M-10 296 L 292 268" fill="none" stroke="var(--line)" stroke-width="12"/>
<text x="300" y="318" font-size="13" font-weight="600" fill="var(--muted)" transform="rotate(70 300 318)">NH 160</text><text x="212" y="40" font-size="13" font-weight="600" fill="var(--muted)" transform="rotate(73 212 40)">NH 160</text>
<text x="470" y="128" font-size="13" fill="var(--muted)" text-anchor="middle" transform="rotate(-6 470 128)">Palkhi Road</text>
<rect x="430" y="30" width="140" height="80" rx="8" fill="var(--card)" stroke="var(--marigold)" stroke-width="2"/>
<text x="500" y="62" font-size="14" font-weight="600" fill="var(--ink)" text-anchor="middle">Shri Saibaba</text>
<text x="500" y="80" font-size="14" font-weight="600" fill="var(--ink)" text-anchor="middle">Samadhi Mandir</text>
<circle cx="345" cy="205" r="7" fill="var(--marigold)"/>
<text x="358" y="210" font-size="12" fill="var(--muted)">Shri Saibaba statue</text>
<path d="M120 300 L 150 297 L 278 284 L 262 230 L 255 190 L 300 170 L 360 160" fill="none" stroke="var(--red)" stroke-width="4" stroke-dasharray="2 8" stroke-linecap="round"/>
<rect x="180" y="304" width="104" height="38" rx="6" fill="var(--card)" stroke="var(--muted)" stroke-width="1.5"/><text x="232" y="320" font-size="11" font-weight="600" fill="var(--ink)" text-anchor="middle">Shirdi Nagar</text><text x="232" y="334" font-size="11" font-weight="600" fill="var(--ink)" text-anchor="middle">Parishad</text><text x="40" y="282" font-size="12.5" font-weight="600" fill="var(--muted)" transform="rotate(-5.3 40 282)">Kankuri Road</text><g transform="translate(10 282) scale(1.2)" aria-hidden="true">
<rect x="0" y="16" width="52" height="34" fill="#F3E7A6" stroke="#B9A75A" stroke-width="1"/>
<rect x="14" y="2" width="24" height="40" fill="#F4F6F8" stroke="#9AA3AD" stroke-width="1"/>
<rect x="11" y="0" width="30" height="3" fill="#E2B21C"/>
<rect x="0" y="14" width="52" height="2.5" fill="#E2B21C"/>
<rect x="17" y="5" width="2" height="6" fill="#2B4C9B"/>
<rect x="21" y="5.5" width="14" height="2" fill="#2B4C9B"/>
<rect x="21" y="8.5" width="14" height="3" fill="#C62828"/>
<rect x="18" y="14" width="16" height="18" fill="#2A3442"/>
<rect x="23" y="24" width="6" height="8" fill="#E8EDF1"/>
<rect x="-3" y="36" width="58" height="6" fill="#ECEFF1" stroke="#C62828" stroke-width="1"/>
<rect x="2" y="42" width="48" height="10" fill="#9E3B2B"/>
<rect x="5" y="44" width="16" height="7" fill="#F4F6F8"/><rect x="24" y="44" width="7" height="7" fill="#F4F6F8"/><rect x="34" y="44" width="13" height="7" fill="#F4F6F8"/>
</g><circle cx="120" cy="300" r="10" fill="var(--blue)"/>
<text x="84" y="334" font-size="14" font-weight="700" fill="var(--blue)">Hotel Saikrupa</text>
<circle cx="362" cy="160" r="10" fill="var(--red)"/>
<text x="378" y="186" font-size="14" font-weight="700" fill="var(--red)">Gate 5/6</text>
<text x="20" y="40" font-size="20" font-weight="700" fill="var(--ink)">350 m · 5 min walk</text>
<text x="20" y="362" font-size="11" fill="var(--muted)">Sketch, not to scale</text>
</svg></figure>
<dl class="dl"><dt>Samadhi Mandir, Gate 5/6</dt><dd>350 m on foot, about 5 minutes</dd>
<dt>Sainagar Shirdi railway station</dt><dd>about 3 km</dd>
<dt>Shirdi Airport</dt><dd>about 14 km</dd></dl>
<p class="muted" style="margin-top:14px">Arriving by train or flight? Tell us on WhatsApp and we will help arrange a taxi.</p></div>
</div></section>

<section class="reach" id="reach"><div class="wrap info">
<div><h2>Reach us</h2><p class="tagline" style="color:inherit;opacity:.9">{TAGLINE}</p>
<dl class="dl" style="margin-top:18px"><dt>Address</dt><dd>{E(ADDRESS)}</dd>
<dt>Call or WhatsApp</dt><dd>{PHONE_DISPLAY}</dd><dt>Landline</dt><dd>{LANDLINES}</dd><dt>Email</dt><dd>{EMAIL}</dd></dl>
<div class="ctas"><a class="btn btn-wa" href="{WA_HELLO}" target="_blank" rel="noopener">{WA_ICON}WhatsApp us</a><a class="btn btn-line" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></div></div>
<div><img src="img/facade-dusk.jpg" alt="Hotel Saikrupa lit up in the evening" loading="lazy" style="border-radius:var(--r)"></div>
</div></section>
</main>
{footer()}
{JS.replace("__ROOMS__", room_js()).replace("__PERIODS__", periods_js()).replace("__PHONE__", PHONE_INTL)}'''

def dmy(s):
    import datetime
    return datetime.date.fromisoformat(s).strftime("%-d %b")

def tariff_section():
    rows = "".join(f"<tr><td>{E(r[1])} ({r[2]})</td><td>{rupees(RATES[r[0]][4])}</td></tr>" for r in ROOMS)
    fest = "; ".join(f"{n} {dmy(a)}–{dmy(b)}" for n, a, b in FESTIVALS)
    card = "; ".join(f"{n} {dmy(a)}–{dmy(b)}" for n, a, b in CARD_PERIODS)
    return f'''<section class="tariff" id="tariff"><h2>Our published tariff</h2>
<p><b>Since 1988, we have never charged above our published tariff, even in the festival rush.</b> On most nights our price is well below it.</p>
<table><thead><tr><th>Room type</th><th>Published tariff per night</th></tr></thead><tbody>{rows}</tbody></table>
<p class="muted">Plus GST as applicable. Prices on this website are valid till {VALID_TILL}. Festival prices apply on: {fest}. Published tariff applies on: {card}. Extra person above 5 years ₹250 per night; children up to 5 stay free.</p></section>'''

def rooms_body():
    arts = ""
    for r in ROOMS:
        rid, name, ac, size, beds, guests, mx, photo, text = r
        mw, tfs, sat, fest, card = RATES[rid]
        price = f"Mon–Wed <b>{rupees(mw)}</b> · Thu, Fri, Sun {rupees(tfs)} · Sat {rupees(sat)} · Festivals {rupees(fest)}<br><span class='muted'>per night, plus 5% GST · published tariff {rupees(card)}</span>"
        msg = wa(f"Namaste, I would like to book a {name} ({ac}) at Hotel Saikrupa. Dates: __ . Guests: __ .")
        extra = "".join(f'<img class="extra" src="img/{x}" alt="{E(name)}, another view" loading="lazy">' for x in EXTRA_PHOTOS.get(rid, []))
        arts += f'''<article id="{rid}"><img src="img/{photo}" alt="{E(name)}, {ac}" loading="lazy">
<div class="body"><span class="eyebrow">{ac}</span><h2 style="font-size:1.7rem">{E(name)}</h2><p class="muted">{E(text)}</p>
<table><tr><th>Beds</th><td>{E(beds)}</td></tr><tr><th>Size</th><td>{E(size)} (sleeping area)</td></tr>
<tr><th>Standard</th><td>{guests} adults</td></tr><tr><th>Maximum</th><td>{E(mx)}</td></tr><tr><th>Price</th><td>{price}</td></tr></table>
<p><a class="btn btn-wa" href="{msg}" target="_blank" rel="noopener">{WA_ICON}Book on WhatsApp</a></p></div>{extra}</article>'''
    return f'''{header()}
<main><section style="padding-top:20px"><div class="wrap">
<a class="back" href="index.html">← Back to home</a>
<div class="section-head" style="margin-top:18px"><span class="eyebrow">Rooms and prices</span><h1 style="font-size:clamp(2rem,4.5vw,3rem)">9 room types, for two to six guests</h1>
<p class="muted">Every room has an attached bathroom with 24-hour hot water, a 32-inch LED TV and Wi-Fi. Extra person ₹250 per night; children up to 5 years stay free. Our website and WhatsApp prices are the lowest you will find, below booking sites.</p><p class="tagline">{TAGLINE}</p></div>
<div class="rp">{arts}</div>
{tariff_section()}
<p style="margin-top:28px"><a class="back" href="index.html">← Back to home</a></p></div></section></main>
{footer()}'''

FAQ = [('How far is Hotel Saikrupa from Shri Saibaba Samadhi Mandir?', '350 m on foot, about 5 minutes, to Gate 5/6 of the Samadhi Mandir. The hotel is behind the Shirdi Nagar Parishad office on Kankuri Road.'), ('Do you have family rooms for 4 to 6 people?', 'Yes. We have family rooms with 2 double beds and family suites with 2 rooms behind one private entrance, each for up to 6 guests.'), ('Do you have AC and non-AC rooms?', 'Yes. Doubles, triples and family rooms are available in both AC and non-AC.'), ('What are the check-in and check-out times?', 'Check-in is at 12 noon and check-out at 11 am.'), ('Is parking available?', 'Yes, there is ample parking for cars and buses at the hotel.'), ('How far is Sainagar Shirdi railway station and Shirdi Airport?', 'Sainagar Shirdi railway station is about 3 km away and Shirdi Airport about 14 km. We can help arrange a taxi.'), ('How do I pay the advance?', "By UPI to the hotel's bank account, after we confirm your room on WhatsApp. Our staff share the payment details with you there."), ('Do your prices go up at festivals?', 'Festival nights (Dasara 16–20 Oct, Diwali 6–15 Nov, Makar Sankranti 14–16 Jan, Republic Day 23–26 Jan) use our festival price, and Christmas–New Year (23 Dec–4 Jan) our published tariff. Since 1988 we have never charged above our published tariff.'), ('How do I get the best price?', 'Book directly on WhatsApp at 8262 800 200. Our direct prices are always below booking sites.')]

JSONLD = {
    "@context": "https://schema.org", "@type": "Hotel", "name": "Hotel Saikrupa",
    "url": "https://www.shirdihotelsaikrupa.com/", "telephone": "+91 82628 00200", "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "Behind Shirdi Nagar Parishad office, Kankuri Road",
                "addressLocality": "Shirdi", "postalCode": "423109", "addressRegion": "Maharashtra", "addressCountry": "IN"},
    "image": "https://www.shirdihotelsaikrupa.com/img/facade-new-hero.jpg", "numberOfRooms": 38,
    "checkinTime": "12:00", "checkoutTime": "11:00", "priceRange": "₹900–₹4,000",
    "description": "Family-run pure-vegetarian hotel in Shirdi since 1988, 350 m from Gate 5/6 of Shri Saibaba Samadhi Mandir.",
    "foundingDate": "1988", "sameAs": ["https://www.instagram.com/hotel_saikrupa_shirdi/"],
    "hasMap": "https://www.google.com/maps/search/?api=1&query=Hotel+Saikrupa+Shirdi",
    "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ["Free Wi-Fi", "Free parking", "24-hour hot water", "Restaurant", "Family rooms", "Air conditioning"]],
}
FAQLD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

# Google Analytics 4 (property "ShirdiHotelSaikrupa.com", account hotelsaikrupabooking@gmail.com).
# Counts only on the real domain, so local test pages are not counted.
# Also records WhatsApp and phone taps as events: whatsapp_click (where: booking_form or other) and call_click.
GA_ID = "G-56FJB5HJES"
GA = f'''<script>if(/(^|\\.)shirdihotelsaikrupa\\.com$/.test(location.hostname)){{var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id={GA_ID}';document.head.appendChild(s);}}
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('https://wa.me/')===0)gtag('event','whatsapp_click',{{where:a.closest('form')?'booking_form':'other',page:location.pathname}});
else if(h.indexOf('tel:')===0)gtag('event','call_click',{{page:location.pathname}});}},true);</script>'''

def full(title, desc, body, canonical, jsonld=False):
    ld = (f'<script type="application/ld+json">{json.dumps(JSONLD, ensure_ascii=False)}</script>'
          f'<script type="application/ld+json">{json.dumps(FAQLD, ensure_ascii=False)}</script>') if jsonld else ""
    return f'''<!doctype html>
<html lang="en"><head>{GA}<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}"><link rel="icon" href="img/emblem.png">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="https://www.shirdihotelsaikrupa.com/img/facade-new-hero.jpg"><meta property="og:type" content="website"><meta property="og:locale" content="en_IN"><meta property="og:site_name" content="Hotel Saikrupa Shirdi"><meta property="og:url" content="{canonical}"><meta name="twitter:card" content="summary_large_image">
<meta name="keywords" content="hotel in Shirdi, hotels near Sai Baba temple Shirdi, hotel near Shri Saibaba Samadhi Mandir, budget hotel Shirdi, family rooms Shirdi, AC rooms Shirdi, pure veg hotel Shirdi, Shirdi hotel with parking, Hotel Saikrupa Shirdi, Kankuri Road Shirdi"><meta name="geo.region" content="IN-MH"><meta name="geo.placename" content="Shirdi">
<meta name="theme-color" content="#1F3A6E">
{FONTS}<style>{CSS}</style>{ld}</head>
<body>{body}</body></html>'''

TITLE = "Hotel Saikrupa Shirdi | Family Hotel 5 Minutes from Shri Saibaba Samadhi Mandir"
DESC = "Family-run pure-veg hotel in Shirdi since 1988, 5 minutes' walk from Shri Saibaba Samadhi Mandir. AC and non-AC rooms, family suites for 6, parking. Book direct on WhatsApp 8262 800 200 for the best price."

def main():
    site = os.path.join(ROOT, "site"); prev = os.path.join(ROOT, "preview")
    os.makedirs(prev, exist_ok=True)
    open(os.path.join(site, "index.html"), "w", encoding="utf-8").write(full(TITLE, DESC, index_body(), "https://www.shirdihotelsaikrupa.com/", True))
    open(os.path.join(site, "rooms.html"), "w", encoding="utf-8").write(full("Rooms and Prices | Hotel Saikrupa Shirdi", "AC and non-AC rooms in Shirdi near Shri Saibaba Samadhi Mandir: doubles, triples, family rooms and suites for up to 6, with weekday, weekend and festival prices.", rooms_body(), "https://www.shirdihotelsaikrupa.com/rooms.html"))
    # preview: index without document wrapper; rooms as a full page
    open(os.path.join(prev, "index.html"), "w", encoding="utf-8").write(f"<title>{TITLE}</title>\n{FONTS}\n<style>{CSS}</style>\n{index_body()}")
    shutil.copy(os.path.join(site, "rooms.html"), os.path.join(prev, "rooms.html"))
    print("built")

if __name__ == "__main__":
    main()
