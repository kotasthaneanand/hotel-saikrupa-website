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

PRICES = {  # weekday Mon-Thu, from-price per night, plus 5% GST
    "standard-double": 1150, "deluxe-double": 1350, "standard-triple": 1450, "compact-triple": 1650,
    "deluxe-triple": 1800, "standard-family": 2200, "suite-nonac": 2500, "deluxe-family": 2600, "suite-ac": 2800,
}
WEEKEND = {"standard-double": 1450, "deluxe-double": 1700, "standard-triple": 1800, "compact-triple": 2000,
    "deluxe-triple": 2200, "standard-family": 2700, "suite-nonac": 3000, "deluxe-family": 3100, "suite-ac": 3300}
PEAK = {"standard-double": 1900, "deluxe-double": 2400, "standard-triple": 2300, "compact-triple": 2600,
    "deluxe-triple": 2800, "standard-family": 3300, "suite-nonac": 3600, "deluxe-family": 3800, "suite-ac": 4000}

ROOMS = [
    # id, name, ac, size, beds, guests, max, photo, text
    ("deluxe-double", "Deluxe Double Room", "AC", "120–130 sq ft", "1 double bed", 2,
     "3 (1 extra adult or child)", "r-deluxe-double.jpg",
     "A comfortable air-conditioned room for two, with an attached bathroom. Suits couples and pairs of devotees."),
    ("deluxe-triple", "Deluxe Triple Room", "AC", "about 160 sq ft", "1 double + 1 single bed", 3,
     "4 adults, or 3 adults + 2 children", "r-deluxe-triple.jpg",
     "A spacious air-conditioned room for three adults, with an attached bathroom. Some rooms have a balcony."),
    ("compact-triple", "Compact Triple Room", "AC", "about 125 sq ft", "1 double + 1 single bed", 3,
     "4 adults, or 3 adults + 2 children", "r-compact-triple.jpg",
     "Smaller than our Deluxe Triple, air-conditioned, with an attached bathroom. Good value for a short darshan stay."),
    ("deluxe-family", "Deluxe Family Room", "AC", "about 230 sq ft", "2 double beds", 4,
     "6 adults, or 4 adults + 2 children", "r-deluxe-family-wide.jpg",
     "Our largest room, air-conditioned, for families travelling together."),
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

# Extra photos shown on the rooms page under a room type
EXTRA_PHOTOS = {"deluxe-family": ["r-deluxe-family-2.jpg"]}
