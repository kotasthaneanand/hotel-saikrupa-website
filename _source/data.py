# Content for the Hotel Saikrupa website. Edit here, then run build.py.

PHONE_DISPLAY = "8262 800 200"
PHONE_INTL = "918262800200"
LANDLINES = "02423 255018 / 02423 255019"
EMAIL = "hotelsaikrupabooking@gmail.com"
ADDRESS = "Behind Shirdi Nagar Parishad office, Kankuri Road, Shirdi 423109, Maharashtra"
MAPS = "https://www.google.com/maps/search/?api=1&query=Hotel+Saikrupa+Shirdi"
GOOGLE_REVIEWS = "https://maps.app.goo.gl/98SHnhePbwJummed7"
GOOGLE_WRITE_REVIEW = "https://g.page/r/CdEE9DBaz4zaEBM/review"
INSTAGRAM = "https://www.instagram.com/hotel_saikrupa_shirdi/"
TAGLINE = "🙏 Seva of Shri Saibaba's devotees is our dharma. Since 1988. 🙏"

# Prices valid till 31 Jan 2027 (staff guide V5, Anand, 12 Oct 2026). Rs per room per night, plus 5% GST.
# Direct price = tariff card minus 10%. Weekday = Sun to Fri nights; only Saturday night is the weekend.
# Per room: (Weekday, Weekday, Saturday, Festival, Published tariff card); the first two are equal since V5.
# The tariff card is the ceiling: since 1988 the hotel never charges above it.
RATES = {
    "standard-double": (1050, 1050, 1300, 1700, 2200),
    "deluxe-double":   (1200, 1200, 1550, 2150, 2800),
    "standard-triple": (1300, 1300, 1600, 2050, 2700),
    "compact-triple":  (1500, 1500, 1800, 2350, 3000),
    "deluxe-triple":   (1600, 1600, 2000, 2500, 3200),
    "standard-family": (2000, 2000, 2450, 2950, 3300),
    "suite-nonac":     (2250, 2250, 2700, 3150, 3500),
    "premium-triple":  (1950, 1950, 2350, 2850, 3550),
    "deluxe-family":   (2750, 2750, 3200, 3800, 4200),  # Premium Deluxe Family, room 210
    "suite-ac":        (2500, 2500, 2950, 3600, 4000),
}
PRICES = {k: v[0] for k, v in RATES.items()}  # lowest ("From") price
# Nights (first and last night, inclusive) priced at the Festival rate
FESTIVALS = [("Shri Saibaba Punyatithi (Dasara)", "2026-10-18", "2026-10-21"), ("Diwali", "2026-11-05", "2026-11-11"),
             ("Republic Day", "2027-01-23", "2027-01-25")]
# Nights priced at the Saturday rate whatever the day
SAT_PERIODS = [("Diwali holidays", "2026-11-12", "2026-11-15"), ("Makar Sankranti", "2027-01-13", "2027-01-15")]
# Nights priced at the published tariff card (no discount)
CARD_PERIODS = [("Christmas and New Year", "2026-12-23", "2027-01-04")]
VALID_TILL = "31 Jan 2027"

ROOMS = [
    # id, name, ac, size, beds, guests, max, photo, text
    ("deluxe-double", "Deluxe Double Room", "AC", "120–130 sq ft", "1 double bed", 2,
     "3 (1 extra adult or child)", "r-deluxe-double.jpg",
     "A comfortable air-conditioned room for two, with an attached bathroom. Suits couples and pairs of devotees."),
    ("deluxe-triple", "Deluxe Triple Room", "AC", "about 160 sq ft", "1 double + 1 single bed", 3,
     "4 adults, or 3 adults + 2 children", "r-deluxe-triple.jpg",
     "A spacious air-conditioned room for three adults, with an attached bathroom. Some rooms have a balcony."),
    ("premium-triple", "Premium Deluxe Triple Room", "AC", "about 160 sq ft", "1 double + 1 single bed", 3,
     "4 adults, or 3 adults + 2 children", "r-premium-triple.jpg",
     "Newly renovated in 2026: a double bed with storage drawers and a padded headboard, a matching single bed, a full-length mirror and a kettle with tea tray. Air-conditioned, with an attached bathroom."),
    ("compact-triple", "Compact Triple Room", "AC", "about 125 sq ft", "1 double + 1 single bed", 3,
     "4 adults, or 3 adults + 2 children", "r-compact-triple.jpg",
     "Smaller than our Deluxe Triple, air-conditioned, with an attached bathroom. Good value for a short darshan stay."),
    ("deluxe-family", "Premium Deluxe Family Room", "AC", "about 230 sq ft", "2 double beds", 4,
     "6 adults, or 4 adults + 2 children", "r-premium-family.jpg",
     "Newly renovated in 2026: two double beds with storage drawers, wall shelves and a large mirror. Our largest air-conditioned room, for families travelling together."),
    ("suite-ac", "Family Suite, 2 rooms", "AC", "240–325 sq ft", "Double bed in one room, 2 single beds in the other", 4,
     "6 adults, or 4 adults + 2 children", "r-suite-double.jpg",
     "Two air-conditioned rooms behind one private entrance, sharing a bathroom. The family stays together with a little more privacy."),
    ("standard-double", "Standard Double Room", "Non-AC", "about 120 sq ft", "1 double bed", 2,
     "3 (1 extra adult or child)", "r-standard-double.jpg",
     "A simple, clean non-AC room for two with an attached bathroom. Our best-value option."),
    ("standard-triple", "Standard Triple Room", "Non-AC", "about 160 sq ft", "1 double + 1 single bed", 3,
     "4 adults, or 3 adults + 2 children", "room-triple.jpg",
     "A spacious non-AC room for three adults, with an attached bathroom. Some rooms have a balcony."),
    ("standard-family", "Standard Family Room", "Non-AC", "about 230 sq ft", "2 double beds", 4,
     "6 adults, or 4 adults + 2 children", "room-family.jpg",
     "A large non-AC room for families and groups."),
    ("suite-nonac", "Family Suite, 2 rooms", "Non-AC", "about 325 sq ft", "Double + single bed in one room, 2 single beds in the other", 4,
     "6 adults, or 4 adults + 2 children", "r-suite-nonac-double.jpg",
     "Two non-AC rooms behind one private entrance, sharing a bathroom."),
]

# Google reviews, 5 stars, word for word (trimmed only). Credit: first name + last initial.
REVIEWS = [
    ("This is perfect hotel for us for 32 years … I come 2 to 3 times a year … this time you all have exceeded the expectations of cleanliness in room lobby corridors", "Ajay Kumar S.", "Sep 2026"),
    ("Safe for women, best room service, very close to sai temple. 24hrs hot water, tea and water bottles are been provided as per demand. Well cleaned washroom. Had a great stay here.", "Nupur G.", "Jun 2026"),
    ("The hotel is clean. The staff is very polite, professional. I will recommend to all family people for stay over here.", "Dhaval S.", "Dec 2025"),
    ("Great service and very close to the Mandir. Reasonable priced rooms and very helpful staff. Recommended. Complimentary water bottles also provided", "Hakim D.", "Sep 2026"),
    ("I've been staying at this hotel since 2006...needless to say I am extremely happy with their service.", "Shobha N.", "Jan 2022"),
    ("Good service, huge rooms overall a good experience", "Krish P.", "Mar 2025"),
]

# Reviews page (17 Oct 2026): 40 five-star Google reviews from the Quote Bank, word for word.
# Trimmed only (… marks a cut). Credit: first name + last initial.
REVIEW_GROUPS = [('near',
  "A few minutes' walk to the Mandir",
  'Guests most often mention how close we are: 350 m, about 5 minutes on foot, to Gate 5/6.',
  [('Best hotel Cleaning is best service is to very best and temple location is near 2 min walking distance complimentary water bottle and available', 'Gaurvesh S.', 'Sep 2026'),
   ('Hotel at 1 min walking from temple and rooms are clean and budget friendly.', 'Mayur B.', 'Mar 2025'),
   ('Hotel location is very near to saibaba mandir,. Room is very clean and reasonable. Staff is kindly handel to customer. It was recommended. Thanks.', 'Surendra K.', 'Mar 2026'),
   ('Great Experience ✅ Satisfied 🤟🏻 Service 👍🏼 Location - 2 min walk from Temple. Decent Room and the tariff was within the budget according to the hotels available nearby. Staff behaviour was very '
    'Good 👍🏼',
    'Aman J.',
    'Aug 2026'),
   ('One of the best hotel i ever seen …specifically ruksana mam and bramhane sir very co operative staff…and also 2 mins walk from saibaba temple…thank you so much for everything…',
    'Vinayak M.',
    'Aug 2025'),
   ('खुप छान सव्हीस विशेष म्हणजे पार्किग सोय उत्तम तसेच हॉटेल मंदिरपासून फक्त एकच मिनीटाच्या अंतरावर असल्यामुळे सतत मंदिर परिसरात नवे तर मंदिरातच असल्याचे समाधान . स्टाफ खुप अपुलकिने वागतो कारणास्तव '
    'आपल्याला चांगले समाधान वाटते . Very good service, especially the parking facility is good and since the hotel is just a minute away from the temple, it is always a pleasure to be in the temple '
    'area and even in the temple itself. The staff is very friendly and makes us feel very satisfied.',
    'Santosh P.',
    'Feb 2025')]),
 ('rooms',
  'Comfortable, spacious rooms',
  '38 rooms, from budget doubles to family suites for six, including Premium rooms renovated in 2026.',
  [('It was really a good hotel. Receptionist and servents are friendly in nature. Rooms were clean and spacious. Services were immediate if any needed. Room is very near to the temple & you will '
    'get it under your budget. 24/7 hot water is available. Overall experience was too good. I can strongly suggest the room to the other people.',
    'Preksha G.',
    'Aug 2026'),
   ('The facilities here is good...room is so cozy and comfortable.. location is near to mandir and we are enjoy stay here.', 'Khushi S.', 'Jun 2026'),
   ('I oftenly visit hotel saikrupa located in shirdi There service is best and i like the quality of rooms and the service provided was best I would recommend everyone to book this hotel for there '
    'stay',
    'Ansh S.',
    'Jul 2026'),
   ('Excellent hotel, nice servicing, clean room, 24 hours hot water with A.C.Room clear towels, clear bathrooms, We feel Royal International Hotel. We enjoy a lot.Thank you so much.',
    'Saburi R.',
    'Mar 2026'),
   ('It was a good experience all staffs are helpful and rooms and services are great.', 'Vishal N.', 'Mar 2026'),
   ('One of the best hotel experiences I’ve had! The staff went above and beyond to make my stay comfortable. From a smooth check-in to prompt room service, everything was handled with '
    'professionalism and a smile. The room was clean, spacious, and well-equipped. Special thanks to the housekeeping and front desk team for their warm hospitality. Highly recommend this hotel for '
    'anyone looking for great service and comfort.',
    'Naveen K.',
    'May 2025')]),
 ('clean',
  'Clean rooms, safe to stay',
  'Clean rooms, clean bathrooms and a safe place for women and elders.',
  [('Safe for women, best room service, very close to sai temple. 24hrs hot water, tea and water bottles are been provided as per demand. Well cleaned washroom. Had a great stay here.',
    'Nupur G.',
    'Jun 2026'),
   ('The hotel was so nice, nearest to the temple walkway, distance from Sai Mandir...hotel was clean and neat, staff approach was good and safe for family', 'Rajamanikandan S.', 'May 2026'),
   ('Very good hospitality and clean and safety for family Tq', 'Mohd M.', 'Apr 2025'),
   ('व्यवस्थापन अतिशय सुरक्षित v चांगले वाटले Management felt very safe and good.', 'Narendra P.', 'Apr 2025'),
   ('Hotel Saikrupa is located near Sai temple. The hotel service is very good, neat and clean and chipper also. The hot water is available 24 hrs. I am a regular customer. Enjoy your trip at hotel '
    'Saikrupa, Shirdi',
    'Chandrakant H.',
    'Aug 2026')]),
 ('family',
  'For families and devotees',
  'Many guests come with parents and children, for darshan at every hour.',
  [('The service was so good. The hospitality was also very nice. We had good experience. Very near to Shirdi Mandhir. Easy to reach the temple , even at midnight without fear. Om sairam.',
    'Bharathi K.',
    'Dec 2025'),
   ('It was the best experience, I was with my family we had a very pleasant stay , the management was very helpful and polite to us , they helped us in darshan also', 'Yeshwanth R.', 'May 2025'),
   ('The hotel is clean. The staff is very polite, professional. I will recommend to all family people for stay over here.', 'Dhaval S.', 'Dec 2025'),
   ("Premises is neat and clean. Ambiance is good and too near from the temple. I'll definitely suggest "
    'for the pilgrims to come and enjoy the stay. Have a happy day🙂',
    'Gaurav B.',
    'Mar 2026'),
   ('Few minutes from the temple. Nice ambiance. Ideal if you come with your family members.', 'Nilesh B.', 'Feb 2025')]),
 ('staff',
  'Staff who look after you',
  'Hot water at any hour, tea and water on request, and a team that knows many guests by name.',
  [('Great service Very near to Sai temple Sataff is co operative Very clean room Hot water 24 hours', 'Shailesh S.', 'Nov 2025'),
   ('Nice stay near temple neet and clean friendly staff received complementary tea and water bottle', 'Sanjay B.', 'Aug 2026'),
   ('Clean rooms and nice stay,Staff is very good in behaviour. Parking facility is also available👍🏻', 'Ayushi K.', 'Aug 2025'),
   ('Good Service . Hotel location is near to temple . Cleaning is good . 24hr Hot water Available . Must Visit !', 'Purva N.', 'Aug 2026'),
   ('Room and stay wad awesome. Hotel cleaning and room service is good. Complementary Tea was impressed. Hotel staffs are also good. Overall Will prefer this Hotel always.',
    'Chandra G.',
    'Jul 2026'),
   ('The hotel was very good cleanliness and staff was also very good.. Ruksana maam was was very good and helpful for us.. the stay is also located nearby to the temple..! 👍🏻',
    'Anmol B.',
    'Apr 2026'),
   ('I visited to shirdi temple for a vacation and this hotel makes my journey beautiful as it ambience is awesome … staff was very co operative, specially Mangesh is one the kind Night Manager who '
    'was there to assist u in every possible way. Overall experience was good.',
    'Rohit V.',
    'Dec 2025')]),
 ('value',
  'Fair prices',
  'Our published tariff has never been exceeded since 1988, even in the festival rush.',
  [('Great service and very close to the Mandir. Reasonable priced rooms and very helpful staff. Recommended. Complimentary water bottles also provided', 'Hakim D.', 'Sep 2026'),
   ('Hotel stay of saikrupa is very best stay cleaning is very nice room and staff is also good and room rate is very reasonable location is very best near to temple best hotel in shirdi and early '
    'check in. … I suggest all sai bhakt for visit saikrupa and stay here',
    'Joseph P.',
    'Jul 2026'),
   ('Good service and very good location. Neat maintenance and provided support for local site visit with reasonable price.', 'Omkar S.', 'Apr 2025'),
   ('Hotel is near the temple with reasonable rates and awesome service.', 'Mrunal P.', 'Sep 2025'),
   ('Good service, huge rooms overall a good experience', 'Krish P.', 'Mar 2025'),
   ('Nice stay ,comfiy room great place to stay , with u and your family,it was an extraordinary experience with in budget sai kripa hotel near nagar parishad', 'Subramanyama B.', 'Jun 2025')]),
 ('loyal',
  'Guests who come back, year after year',
  'Some families have stayed with us for 20 and 30 years.',
  [('This is perfect hotel for us for 32 years from doctor sahab till now I come 2 to 3 times a year … this time you all have exceeded the expectations of cleanliness in room lobby corridors upkeep '
    'has room amenities with kettel all are too good … your staff at reception Ms Ruksana is gem,Ratan Mama pratibha guru sir all are too good',
    'Ajay Kumar S.',
    'Sep 2026'),
   ('Best Service..I am staying in this hoteL Last 20/Years.. Supper Location and Best Service..Om Sai Ram..', 'Jatin S.', 'Mar 2025'),
   ("I've been staying at this hotel since 2006...needless to say I am extremely happy with their service. … Room is neat. Prompt service. Whatever I had asked for e.g arranging pickup from station. "
    'Every ask has been delivered.',
    'Shobha N.',
    'Jan 2022'),
   ('Rooms and Hospitality are very excellent and hot water available any time. Complementary Tea and Water bottle. Overall experience too good. I am regular customer thank you',
    'Dr. Prashant N.',
    'Aug 2026'),
   ('Nice hotel As we are coming in this hotel since Five Years Cheap and best RATES', 'Surendra J.', 'Feb 2025')])]

# Featured story on the reviews page: guest's silver chain returned (4 Aug 2026). Review word for word.
# Photo is a still from the hotel's video with the guest's face blurred until he agrees to the website showing it.
FEATURED_STORY = {
    "title": "A guest's silver chain, kept safe for a month",
    "photo": "chain-returned.jpg",
    "alt": "Hotel Saikrupa's reception manager handing back a silver chain to a guest at reception, guest's face blurred",
    "caption": "Returned by the Hotel Saikrupa Reception Manager, 4 Aug 2026. Guest's face blurred for privacy.",
    "quote": "Thanks giving my silver chain aftet 1months all staff are well maintain job for me thanks again all of one thank you🥰😍🙏🙏",
    "credit": "Sagar B.", "date": "Aug 2026",
}

# Photos shown with a review group: group id -> (file, alt text, caption). Faces of guests blurred until they agree.
GROUP_PHOTOS = {
    "loyal": ("guest-with-team.jpg", "A regular guest with the Hotel Saikrupa team at reception, guest's face blurred",
              "Prabhakar K., a regular guest, with the Hotel Saikrupa team at reception, Sep 2026. Guest's face blurred for privacy."),
}

# MakeMyTrip / Goibibo reviews for the reviews page. 4 and 5 stars only, word for word (trimmed only, … marks a cut).
# Text must be copied from MakeMyTrip Connect (not typed from screenshots). Each: (quote, credit, "MakeMyTrip" or "Goibibo", "Mon YYYY", stars).
# The section stays hidden while this list is empty.
OTA_REVIEWS = [
    ("I have been coming to Shirdi for more than 25 years, and I can genuinely say this has been my best hotel stay here. In my previous visits, I have seen some issue like cleanliness, hot water, bedbugs, or the attitude of the staff. This time, it was a completely different experience. The room was clean, and the service was outstanding. Every single person we interacted with was polite and helpful. Many times they came to us on their own just to ask if we needed anything, instead of waiting for us to call them. That small gesture was very good. It's rare to find such a hotel in Shirdi. Thank you for making our Shirdi trip so pleasant.", "Shailaja P.", "MakeMyTrip", "Aug 2026", 5),
    ("Hotel is good and food provided at restaurant is good and owner and staff so helpfull", "Nathu K.", "MakeMyTrip", "Apr 2023", 5),
    ("nice stay. good ambience. close to temple", "Arpan S.", "MakeMyTrip", "Dec 2022", 5),
    ("hotel is very good looking 👌 namaste", "Sunil S.", "MakeMyTrip", "Dec 2022", 5),
    ("Nice staff. Counter person and receptionist also gave proper guidance. Warm water was excellent and sufficient staff.", "Satish P.", "MakeMyTrip", "Nov 2018", 5),
    ("Very satisfying. … Walkable distance to temple. And transport facilities to other places also is very convenient. I will recommend this hotel to my friends also", "Chamarthy M.", "MakeMyTrip", "Sep 2017", 5),
    ("Rooms are clean, staff is good, have decent parking space and near to the temple is good advantage.", "Mitesh K.", "MakeMyTrip", "Aug 2026", 4),
    ("property location is very near to the temple and the service was also good Near to temple good and polite staff", "Krishna P.", "MakeMyTrip", "Aug 2025", 5),
    ("Service is very nice and staff is also nice and our family enjoyed very much and our kids feel very happy", "Poonam B.", "MakeMyTrip", "Dec 2024", 5),
]
OTA_COUNT = "120"  # ratings on MakeMyTrip (65) and Goibibo (55) together (MMT Connect, 17 Oct 2026)
OTA_RATING = ""    # not shown on purpose: MakeMyTrip 3.7/5, Goibibo 3.8/5 on 17 Oct 2026; Anand decided 17 Oct not to show them

# Photo gallery page (gallery.html), Anand's photos of 17 Oct 2026: (file, caption)
GALLERY = [  # (group heading, [(file, caption), ...])
    ("The hotel", [
        ("g-facade-day.jpg", "Hotel Saikrupa, Kankuri Road, Shirdi"),
        ("g-facade-lit.jpg", "Lit up for the festival season"),
        ("facade-dusk.jpg", "The hotel in the evening"),
        ("since-1988.jpg", "स्थापना १९८८: welcoming devotees since 1988"),
        ("parking.jpg", "Ample parking for cars and buses"),
        ("terrace.jpg", "Covered terrace garden, first floor"),
    ]),
    ("Reception and lobby", [
        ("g-entrance.jpg", "Our entrance, decorated with fresh flowers"),
        ("g-entrance-day.jpg", "Reception, renovated in 2026"),
        ("g-reception-desk.jpg", "Reception desk, with Shri Saibaba's portrait"),
        ("g-reception.jpg", "Reception and lobby seating"),
        ("g-lobby.jpg", "The lobby"),
        ("g-lobby-family.jpg", "Anjali Kotasthane, partner in Hotel Saikrupa, in the renovated lobby"),
        ("murti.jpg", "Shri Saibaba murti in the lobby"),
        ("g-brass-lamps.jpg", "Brass lamps in the lobby"),
        ("g-staircase.jpg", "Staircase to the rooms"),
    ]),
    ("Rooms", [
        ("r-premium-family.jpg", "Premium family room, renovated 2026"),
        ("r-premium-triple.jpg", "Premium triple room, renovated 2026"),
        ("r-deluxe-double.jpg", "Deluxe double room"),
        ("r-deluxe-family.jpg", "Deluxe family room"),
        ("r-suite-double.jpg", "Family Suite: double-bed room"),
        ("r-suite-twin.jpg", "Family Suite: twin-bed room"),
        ("r-suite-nonac-double.jpg", "Non-AC Family Suite: double-bed room"),
        ("g-room-double.jpg", "Double room, fresh towels and blankets"),
        ("g-bathroom.jpg", "Attached bathroom with western toilet and hot water"),
    ]),
    ("Sacred places and the view", [
        ("view-statue-day.jpg", "Shri Saibaba statue near the Samadhi Mandir, seen from the hotel"),
        ("view-statue-dusk.jpg", "The same view, lit up in the evening"),
        ("shrine-maulay-devi.jpg", "Maulay Devi Mandir, within our premises"),
        ("shrine-datta.jpg", "Shri Datta murti, within our premises"),
    ]),
]

# Extra photos shown on the rooms page under a room type
EXTRA_PHOTOS = {"premium-triple": ["r-premium-triple-2.jpg"], "deluxe-family": ["r-premium-family-2.jpg"],
                "suite-ac": ["r-suite-twin.jpg"], "suite-nonac": ["r-suite-nonac-double-2.jpg"]}  # Family Suite (AC) twin-bed room, original photo from Anand 17 Oct
