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
     "6 adults, or 4 adults + 2 children", "r-suite-combo.jpg",
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
     "6 adults, or 4 adults + 2 children", "r-suite-combo.jpg",
     "Two non-AC rooms behind one private entrance, sharing a bathroom."),
]

# Google reviews, 5 stars, word for word (trimmed only). Credit: first name + last initial.
REVIEWS = [
    ("This is perfect hotel for us for 32 years … I come 2 to 3 times a year … this time you all have exceeded the expectations of cleanliness in room lobby corridors", "Ajay Kumar S.", "Sep 2026"),
    ("Safe for women, best room service, very close to sai temple. 24hrs hot water, tea and water bottles are been provided as per demand. Well cleaned washroom. Had a great stay here.", "Nupur G.", "Jun 2026"),
    ("The hotel is clean. Very near to the holy place of sai baba mandir. The staff is very polite, professional. I will recommend to all family people for stay over here.", "Dhaval S.", "Dec 2025"),
    ("Great service and very close to the Mandir. Reasonable priced rooms and very helpful staff. Recommended. Complimentary water bottles also provided", "Hakim D.", "Sep 2026"),
    ("I've been staying at this hotel since 2006...needless to say I am extremely happy with their service.", "Shobha N.", "Jan 2022"),
    ("Nearest to the Shirdi Sai Baba temple. Good service, huge rooms overall a good experience", "Krish P.", "Mar 2025"),
]

# Reviews page (17 Oct 2026): 25 five-star Google reviews from the Quote Bank, word for word.
# Trimmed only (… marks a cut). Credit: first name + last initial.
REVIEW_GROUPS = [('near',
  "A few minutes' walk to the Mandir",
  'Guests most often mention how close we are: 350 m, about 5 minutes on foot, to Gate 5/6.',
  [('Hotel at 1 min walking from temple and rooms are clean and budget friendly.', 'Mayur B.', 'Mar 2025'),
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
 ('clean',
  'Clean rooms, safe for families',
  'What matters most when you travel with parents and children.',
  [('Safe for women, best room service, very close to sai temple. 24hrs hot water, tea and water bottles are been provided as per demand. Well cleaned washroom. Had a great stay here.',
    'Nupur G.',
    'Jun 2026'),
   ('The hotel was so nice, nearest to the temple walkway, distance from Sai Mandir...hotel was clean and neat, staff approach was good and safe for family', 'Rajamanikandan S.', 'May 2026'),
   ('The hotel is clean. Very near to the holy place of sai baba mandir. The staff is very polite, professional. I will recommend to all family people for stay over here.', 'Dhaval S.', 'Dec 2025'),
   ('Very good hospitality and clean and safety for family Tq', 'Mohd M.', 'Apr 2025'),
   ('व्यवस्थापन अतिशय सुरक्षित v चांगले वाटले Management felt very safe and good.', 'Narendra P.', 'Apr 2025'),
   ('Hotel Saikrupa is located near Sai temple. The hotel service is very good, neat and clean and chipper also. The hot water is available 24 hrs. I am a regular customer. Enjoy your trip at hotel '
    'Saikrupa, Shirdi',
    'Chandrakant H.',
    'Aug 2026')]),
 ('staff',
  'Staff who look after you',
  'Hot water at any hour, tea and water on request, and a team that knows many guests by name.',
  [('Great service Very near to Sai temple Sataff is co operative Very clean room Hot water 24 hours', 'Shailesh S.', 'Nov 2025'),
   ('Nice stay near temple neet and clean friendly staff received complementary tea and water bottle', 'Sanjay B.', 'Aug 2026'),
   ('Clean rooms and nice stay,Staff is very good in behaviour. Parking facility is also available👍🏻', 'Ayushi K.', 'Aug 2025'),
   ('Good Service . Hotel location is near to temple . Cleaning is good . 24hr Hot water Available . Must Visit !', 'Purva N.', 'Aug 2026'),
   ('Room and stay wad awesome. Hotel cleaning and room service is good. Complementary Tea was impressed. Hotel staffs are also good. Overall Will prefer this Hotel always.',
    'Chandra G.',
    'Jul 2026')]),
 ('value',
  'Fair prices',
  'Our published tariff has never been exceeded since 1988, even in the festival rush.',
  [('Great service and very close to the Mandir. Reasonable priced rooms and very helpful staff. Recommended. Complimentary water bottles also provided', 'Hakim D.', 'Sep 2026'),
   ('Good service and very good location. Neat maintenance and provided support for local site visit with reasonable price.', 'Omkar S.', 'Apr 2025'),
   ('Hotel is near the temple with reasonable rates and awesome service.', 'Mrunal P.', 'Sep 2025'),
   ('Nearest to the Shirdi Sai Baba temple. Good service, huge rooms overall a good experience', 'Krish P.', 'Mar 2025')]),
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

# MakeMyTrip / Goibibo reviews for the reviews page. 4 and 5 stars only, word for word (trimmed only, … marks a cut).
# Text must be copied from MakeMyTrip Connect (not typed from screenshots). Each: (quote, credit, "MakeMyTrip" or "Goibibo", "Mon YYYY").
# The section stays hidden while this list is empty.
OTA_REVIEWS = []
OTA_COUNT = "120"  # ratings on MakeMyTrip (65) and Goibibo (55) together (MMT Connect, 17 Oct 2026)
OTA_RATING = ""    # not shown on purpose: MakeMyTrip 3.7/5, Goibibo 3.8/5 on 17 Oct 2026 (Anand to decide)

# Extra photos shown on the rooms page under a room type
EXTRA_PHOTOS = {"premium-triple": ["r-premium-triple-2.jpg"], "deluxe-family": ["r-premium-family-2.jpg"]}
