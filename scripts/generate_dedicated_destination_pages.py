import os

pages_data = [
    {
        "filename": "prayagraj-tour-package.html",
        "city": "Prayagraj",
        "title": "Prayagraj Tour Package 2026: Triveni Sangam, Bade Hanuman & Kumbh Yatra",
        "meta_desc": "Book Prayagraj Tour Package 2026. Private boat to Triveni Sangam snan, Bade Hanumanji darshan, Akshayavat, Anand Bhawan & Kumbh Mela arrangements. (From ₹1,499)",
        "keywords": "prayagraj tour package, triveni sangam boat booking, prayagraj same day tour, sangam snan package, prayagraj kumbh yatra",
        "h1": "Prayagraj Tour Package — Triveni Sangam & Tirtharaj Yatra",
        "lead": "Experience the divine energy of Tirtharaj Prayagraj. Enjoy a private boat ride to Triveni Sangam for holy snan, VIP darshan at Bade Hanuman Temple & Akshayavat, and seamless local AC cab transfers.",
        "image": "assets/destinations/triveni-sangam.webp",
        "highlights": [
            "Private boat ride to Triveni Sangam for holy bath",
            "Darshan at the legendary Bade Hanuman Mandir",
            "Sacred Akshayavat & Patalpuri Temple tour",
            "Anand Bhawan & historic Swaraj Bhawan visit",
            "Doorstep pickup from Prayagraj Junction or Airport"
        ],
        "itinerary": [
            ("07:00 AM", "Pick-up & Sangam Ghat Transfer", "Our AC cab picks you up from Prayagraj Junction (PRYJ) or your hotel and takes you to VIP Sangam Ghat."),
            ("08:00 AM", "Triveni Sangam Holy Snan & Boat Ride", "Board a private wooden motorboat for the holy confluence of Ganga, Yamuna & Saraswati. Perform snan and ritual prayers."),
            ("10:30 AM", "Bade Hanuman & Akshayavat Darshan", "Visit the reclining Bade Hanumanji temple, followed by Akshayavat tree and Patalpuri Mandir inside Prayagraj Fort complex."),
            ("01:30 PM", "Traditional Sattvic Lunch Break", "Enjoy authentic pure sattvic North Indian lunch at top-rated local dining partners."),
            ("03:00 PM", "Anand Bhawan & Alopi Devi Shakti Peeth", "Explore the historic Nehrus' ancestral home Anand Bhawan and pay homage at Alopi Devi Shakti Peeth."),
            ("06:00 PM", "Evening Yamuna Aarti & Drop", "Witness calm evening Yamuna Aarti before dropping off at Prayagraj station or your onward destination.")
        ],
        "faqs": [
            ("What is included in the Prayagraj Tour Package?", "The package includes private AC vehicle transport, a reserved boat for Triveni Sangam snan, dedicated local guide, temple VIP assistance, and station/hotel pickup and drop."),
            ("How long does the Triveni Sangam boat trip take?", "The Sangam boat trip and holy snan take approximately 1.5 to 2 hours, including boat travel time to the exact confluence point."),
            ("Can we combine Prayagraj with Ayodhya and Varanasi?", "Yes! We specialize in combined Ayodhya-Prayagraj-Varanasi circuits. Contact our 24x7 desk at +91 92352 22399 for custom combined packages.")
        ]
    },
    {
        "filename": "chitrakoot-tour-package.html",
        "city": "Chitrakoot",
        "title": "Chitrakoot Tour Package 2026: Kamadgiri, Ramghat & Gupt Godavari Yatra",
        "meta_desc": "Book Chitrakoot Tour Package 2026. Explore Kamadgiri Parikrama, Ramghat Mandakini Aarti, Sphatik Shila, Gupt Godavari & Hanuman Dhara. (From ₹1,899)",
        "keywords": "chitrakoot tour package, chitrakoot sightseeing package, ramghat aarti chitrakoot, kamadgiri parikrama tour, gupt godavari caves chitrakoot",
        "h1": "Chitrakoot Tour Package — Land of Ram's 11-Year Exile",
        "lead": "Step into the tranquil forests of Chitrakoot where Lord Ram, Sita Ji, and Lakshman spent 11 years of exile. Perform Kamadgiri Parikrama, experience Mandakini Aarti at Ramghat, and visit ancient sacred caves.",
        "image": "assets/destinations/mandakini-river.webp",
        "highlights": [
            "Sacred Kamadgiri Parikrama & Kamtanath Mandir darshan",
            "Ramghat Mandakini River boat ride & evening Aarti",
            "Mystical Gupt Godavari stream caves tour",
            "Sphatik Shila & Hanuman Dhara hilltop shrine",
            "Private AC car transfers from Karwi / Satna / Prayagraj"
        ],
        "itinerary": [
            ("07:00 AM", "Pickup & Arrival at Sacred Ramghat", "Pick up from Chitrakoot Dham Karwi Station or hotel. Begin with holy dip at Ramghat on Mandakini river."),
            ("08:30 AM", "Kamadgiri Parikrama & Temple Visit", "Embark on the 5 km holy Kamadgiri Parikrama path, visiting Kamtanath Temple and surrounding ancient shrines."),
            ("11:30 AM", "Gupt Godavari Caves Exploration", "Visit the natural pair of caves where underground Mandakini stream flows silently through carved rock formations."),
            ("02:00 PM", "Lunch & Sphatik Shila Visit", "Enjoy traditional local lunch, followed by visit to Sphatik Shila where Lord Ram & Sita Ji sat together."),
            ("04:30 PM", "Hanuman Dhara & Sita Rasoi", "Ascend to Hanuman Dhara where natural mountain spring cools Lord Hanuman's shrine."),
            ("06:30 PM", "Grand Mandakini Aarti at Ramghat", "Witness evening illumination and floating oil lamp Aarti along Ramghat before transfer to station/hotel.")
        ],
        "faqs": [
            ("Where is Chitrakoot located and how to reach?", "Chitrakoot is located on the UP-MP border, ~130 km from Prayagraj. The nearest railhead is Chitrakoot Dham Karwi (CKTD) or Satna (STA)."),
            ("Is Kamadgiri Parikrama accessible for senior citizens?", "Yes, the 5 km Parikrama pathway is fully paved, shaded, and battery e-rickshaws or palanquins (doli) are available for elderly pilgrims."),
            ("What is the best time to visit Chitrakoot?", "October to March offers pleasant weather for temple visits and outdoor parikrama.")
        ]
    },
    {
        "filename": "naimisharanya-tour-package.html",
        "city": "Naimisharanya",
        "title": "Naimisharanya Tour Package 2026: Chakra Tirth, Maa Lalita Devi & Vyas Gaddi",
        "meta_desc": "Book Naimisharanya Tour Package 2026. Visit holy Chakra Tirth, Maa Lalita Devi Shakti Peeth, Vyas Gaddi & Hanuman Garhi with AC cab transfers. (From ₹1,799)",
        "keywords": "naimisharanya tour package, chakra tirth holy bath, maa lalita devi shakti peeth, vyas gaddi naimisharanya, lucknow to naimisharanya tour",
        "h1": "Naimisharanya Tour Package — Sacred Forest of 88,000 Rishis",
        "lead": "Journey to the holy forest of Naimisharanya (Neemsar) where Sage Ved Vyas compiled the 18 Puranas. Take a sacred dip in round Chakra Tirth and seek blessings at Maa Lalita Devi Shakti Peeth.",
        "image": "assets/reviews/ayodhya-night.jpg",
        "highlights": [
            "Chakra Tirth holy bath & solar ritual prayers",
            "Maa Lalita Devi Shakti Peeth VIP darshan",
            "Vyas Gaddi where 18 Puranas were narrated",
            "Hanuman Garhi & historic Banyan tree site",
            "Private AC cab pick & drop from Lucknow or Sitapur"
        ],
        "itinerary": [
            ("07:00 AM", "Lucknow / Sitapur Pickup & Drive to Neemsar", "Early morning AC vehicle pickup from Lucknow Airport/Station or Sitapur for scenic drive to Naimisharanya."),
            ("09:00 AM", "Chakra Tirth Holy Bath", "Arrive at the circular Chakra Tirth water body, created by Lord Vishnu's Manomaya Chakra. Take holy dip."),
            ("10:30 AM", "Maa Lalita Devi Shakti Peeth Darshan", "Seek divine blessings at Maa Lalita Devi Mandir, one of the prominent 51 Shakti Peethas."),
            ("01:00 PM", "Vyas Gaddi & Hanuman Garhi", "Visit Vyas Gaddi under the ancient banyan tree where Maharshi Ved Vyas wrote Mahabharat & Puranas."),
            ("03:30 PM", "Sut Gaddi & Pandav Kila", "Explore Sut Gaddi and historic Pandav Kila along Gomti river banks."),
            ("06:00 PM", "Return Transfer to Lucknow / Sitapur", "Comfortable evening return transfer to Lucknow Junction or hotel.")
        ],
        "faqs": [
            ("How far is Naimisharanya from Lucknow?", "Naimisharanya is approximately 85 km from Lucknow (2 hours drive via Sitapur road)."),
            ("What makes Naimisharanya spiritually significant?", "It is the sacred land where Srimad Bhagavatam was recited by Rishi Suta to 88,000 rishis, and home to Chakra Tirth & Maa Lalita Devi Shakti Peeth."),
            ("Can Naimisharanya be covered in a 1-day trip from Lucknow?", "Yes, a 1-day trip from Lucknow is ideal and comfortable with our private AC cab transfers.")
        ]
    },
    {
        "filename": "vindhyachal-tour-package.html",
        "city": "Vindhyachal",
        "title": "Vindhyachal Tour Package 2026: Maa Vindhyavasini Darshan & Trikon Parikrama",
        "meta_desc": "Book Vindhyachal Tour Package 2026. Seek blessings at Maa Vindhyavasini Shakti Peeth, Ashtabhuja & Kali Khoh Trikon Parikrama. (From ₹1,699)",
        "keywords": "vindhyachal tour package, vindhyavasini devi darshan, trikon parikrama vindhyachal, ashtabhuja temple mirzapur, varanasi to vindhyachal tour",
        "h1": "Vindhyachal Tour Package — Maa Vindhyavasini Shakti Peeth Yatra",
        "lead": "Immerse yourself in Divine Shakti energy at Vindhyachal Dham. Perform the complete Trikon Parikrama visiting Maa Vindhyavasini, Ashtabhuja Devi, and Kali Khoh with guided VIP assistance.",
        "image": "assets/vindhyachal.webp",
        "highlights": [
            "Maa Vindhyavasini Devi Mandir VIP Darshan",
            "Complete Trikon Parikrama (Vindhyavasini - Kali Khoh - Ashtabhuja)",
            "Ganga Snan at Vindhyachal Pucca Ghat",
            "Ropeway experience to Ashtabhuja hill temple",
            "Private AC transfers from Varanasi or Mirzapur"
        ],
        "itinerary": [
            ("07:00 AM", "Varanasi / Mirzapur Pickup", "Morning pick-up in private AC cab from Varanasi (65 km) or Mirzapur Station (8 km)."),
            ("08:30 AM", "Ganga Snan & Vindhyavasini Darshan", "Arrive at Pucca Ghat for holy Ganga bath, followed by priority darshan at Maa Vindhyavasini Temple."),
            ("11:00 AM", "Kali Khoh Temple Visit", "Proceed on Trikon Parikrama circuit to Kali Khoh, hidden in mountain cave dedicated to Maa Kali."),
            ("01:00 PM", "Ashtabhuja Devi Temple & Ropeway", "Ascend via scenic ropeway or stairs to Ashtabhuja Devi temple atop Vindhya hill."),
            ("03:00 PM", "Sattvic Lunch & Shivpur Temple Visit", "Enjoy traditional prasadam lunch and visit nearby Shivpur Rameshwaram temple."),
            ("05:30 PM", "Return Transfer to Varanasi", "Drive back smoothly to Varanasi hotel, station, or airport.")
        ],
        "faqs": [
            ("How far is Vindhyachal from Varanasi?", "Vindhyachal is just 65 km (1.5 hours drive) from Varanasi, making it an ideal day excursion."),
            ("What is Trikon Parikrama?", "Trikon Parikrama is the holy triangular circuit connecting three manifestation temples: Maa Vindhyavasini, Maa Kali (Kali Khoh), and Maa Saraswati (Ashtabhuja)."),
            ("Is ropeway facility available at Ashtabhuja Devi?", "Yes, modern electric ropeway car facility is available for effortless hilltop access.")
        ]
    },
    {
        "filename": "mathura-tour-package.html",
        "city": "Mathura",
        "title": "Mathura Tour Package 2026: Shri Krishna Janmabhoomi & Vishram Ghat Yatra",
        "meta_desc": "Book Mathura Tour Package 2026. Private guided tour of Shri Krishna Janmabhoomi, Dwarkadhish Temple, Vishram Ghat & Yamuna Aarti. (From ₹1,499)",
        "keywords": "mathura tour package, krishna janmabhoomi tour, mathura same day package, vishram ghat yamuna aarti, delhi to mathura tour",
        "h1": "Mathura Tour Package — Birthplace of Lord Shri Krishna",
        "lead": "Step onto the holy soil of Braj Dham. Visit Shri Krishna Janmabhoomi temple complex, experience evening Yamuna Aarti at Vishram Ghat, and taste famous Mathura Peda.",
        "image": "assets/destinations/vishram-ghat.webp",
        "highlights": [
            "Shri Krishna Janmabhoomi Temple & Garbha Griha darshan",
            "Ancient Dwarkadhish Mandir morning Aarti",
            "Vishram Ghat Yamuna snan & boat ride",
            "Evening Yamuna Aarti with burning camphor lamps",
            "Private AC vehicle pickup from Delhi/NCR or Mathura Junction"
        ],
        "itinerary": [
            ("07:00 AM", "Pickup from Delhi / Mathura Junction", "Morning pickup in AC sedan/SUV from Delhi, Agra, or Mathura Junction (MTJ)."),
            ("09:30 AM", "Shri Krishna Janmabhoomi Darshan", "Visit the grand Janmabhoomi temple complex, prison cell (Garbha Griha), and Bhagvat Bhavan."),
            ("12:00 PM", "Dwarkadhish Temple & Local Bazaars", "Take darshan at historic Dwarkadhish Temple along Yamuna bank and sample authentic Mathura Pedas."),
            ("02:00 PM", "Pure Veg Braj Thali Lunch", "Enjoy traditional Braj thali featuring kadhi, bedmi poori, and lassi."),
            ("04:00 PM", "Gita Mandir & Potara Kund", "Visit Birla Gita Mandir with 18 chapters inscribed on walls and holy Potara Kund."),
            ("06:30 PM", "Grand Yamuna Aarti at Vishram Ghat", "Witness mesmerizing sunset Yamuna Aarti at Vishram Ghat before transfer.")
        ],
        "faqs": [
            ("How far is Mathura from Delhi?", "Mathura is 150 km from Delhi via Yamuna Expressway (approx. 2.5 hours drive)."),
            ("What are the main temples covered in Mathura?", "Shri Krishna Janmabhoomi, Dwarkadhish Temple, Vishram Ghat, Gita Mandir, and Potara Kund."),
            ("Can we combine Mathura with Vrindavan?", "Yes! We offer both Mathura single-city packages and combined Mathura-Vrindavan 1-day or 2-day packages.")
        ]
    },
    {
        "filename": "vrindavan-tour-package.html",
        "city": "Vrindavan",
        "title": "Vrindavan Tour Package 2026: Banke Bihari, Prem Mandir & Nidhivan Yatra",
        "meta_desc": "Book Vrindavan Tour Package 2026. VIP Banke Bihari darshan, Prem Mandir light show, ISKCON temple & Nidhivan guided tour. (From ₹1,499)",
        "keywords": "vrindavan tour package, banke bihari temple tour, prem mandir vrindavan, nidhivan tour, delhi to vrindavan package",
        "h1": "Vrindavan Tour Package — Sacred Land of Radha-Krishna Leela",
        "lead": "Lose yourself in divine Braj Ras and Krishna Bhakti. Experience soul-stirring darshan at Shri Banke Bihari Ji, marvel at marble carvings of Prem Mandir, and visit mystical Nidhivan.",
        "image": "assets/destinations/prem-mandir.webp",
        "highlights": [
            "Shri Banke Bihari Ji Mandir VIP guided darshan",
            "Mystical Nidhivan & Radha Raman temple tour",
            "ISKCON Vrindavan (Krishna Balaram Mandir) kirtan",
            "Grand Prem Mandir illuminated evening light show",
            "Private AC cab pickup from Delhi, Mathura, or Agra"
        ],
        "itinerary": [
            ("08:00 AM", "Arrival & ISKCON Temple Kirtan", "Arrive in Vrindavan. Begin at ISKCON Vrindavan temple amidst ecstatic Hare Krishna kirtan."),
            ("09:30 AM", "Shri Banke Bihari Temple Darshan", "Proceed to heart of Vrindavan for darshan of Lord Banke Bihari Ji with local assistance."),
            ("11:30 AM", "Radha Raman & Nidhivan Tour", "Explore ancient Radha Raman temple and mystical Nidhivan grove where Raas Leela takes place."),
            ("01:30 PM", "Braj Special Lunch", "Enjoy traditional sattvic Braj meal and famous Vrindavan rabri."),
            ("03:30 PM", "Vaishno Devi Dham & ISKCON Vrindavan", "Visit giant 141ft Maa Vaishno Devi shrine and Seva Kunj."),
            ("06:30 PM", "Prem Mandir Musical Fountain & Lighting", "Conclude with magnificent evening musical fountain & marble illumination display at Prem Mandir.")
        ],
        "faqs": [
            ("What are Banke Bihari temple timings?", "Morning: 7:45 AM - 12:00 PM; Evening: 5:30 PM - 9:30 PM. (Timings vary slightly between Summer & Winter)."),
            ("Is Prem Mandir light show free for tourists?", "Yes, the grand musical fountain and exterior architectural illumination show at Prem Mandir is free for all visitors every evening."),
            ("Are battery e-rickshaws available in Vrindavan narrow lanes?", "Yes, private AC cabs park at designated plazas and e-rickshaws seamlessly shuttle pilgrims through temple narrow lanes.")
        ]
    }
]

template_code = """<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval';">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="permissions-policy" content="geolocation=(), microphone=(), camera=()">
<link rel="alternate" hreflang="en-IN" href="https://www.ayodhyadharshan.com/{filename}">
<link rel="alternate" hreflang="hi-IN" href="https://www.ayodhyadharshan.com/{filename}">
<link rel="alternate" hreflang="x-default" href="https://www.ayodhyadharshan.com/{filename}">

<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
<link rel="icon" href="favicon.png" type="image/png" sizes="192x192">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.ayodhyadharshan.com/{filename}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ayodhya Dharshan">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://www.ayodhyadharshan.com/{filename}">
<meta property="og:image" content="https://www.ayodhyadharshan.com/{image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Mukta:wght@300;400;500;600;700&display=optional" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">

<!-- WebSite Schema -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{title}",
  "description": "{meta_desc}",
  "url": "https://www.ayodhyadharshan.com/{filename}"
}}
</script>

<!-- Product Schema -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{h1}",
  "description": "{meta_desc}",
  "brand": {{
    "@type": "Brand",
    "name": "Ayodhya Dharshan"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "142"
  }},
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "INR",
    "price": "1499",
    "availability": "https://schema.org/InStock"
  }}
}}
</script>

  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7513283731802791"
       crossorigin="anonymous"></script>
</head>
<body>

<nav class="site-nav">
  <div class="nav-inner">
    <a class="brand" href="index.html" aria-label="Ayodhya Dharshan home">
      <img width="500" height="500" src="assets/logo.webp" alt="Ayodhya Dharshan Logo" class="brand-mark" fetchpriority="high">
      <span class="brand-name">Ayodhya Dharshan<small>Teerth Yatra</small></span>
    </a>
    <div class="nav-links" id="navLinks">
      <a href="index.html">Home</a>
      <a href="destinations.html">Destinations</a>
      <a href="services.html">Services</a>
      <a href="yatra-cost-calculator.html">Calculator</a>
      <a href="about.html">About</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html">Contact</a>
    </div>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary" aria-label="Plan Your Yatra"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 2C7 9 7 13 12 22 17 13 17 9 12 2Z"/></svg><span class="btn-text">Plan Your Yatra</span></a>
      <button class="nav-toggle" id="navToggle" aria-label="Menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
</nav>

<section class="page-hero">
  <div class="container">
    <p class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; <a href="destinations.html">Destinations</a> &nbsp;/&nbsp; {city}</p>
    <p class="eyebrow">Dedicated {city} Tour Package 2026</p>
    <h1 class="display" style="font-size:clamp(2.4rem,5vw,4.2rem);">{h1}</h1>
    <p class="lead">{lead}</p>
    <div style="margin-top:24px; display:flex; gap:16px; flex-wrap:wrap;">
      <a href="contact.html" class="btn btn-primary">Book {city} Yatra Now</a>
      <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20the%20{city}%20Tour%20Package." target="_blank" rel="noopener" class="btn btn-ghost" style="border-color:var(--saffron);">💬 WhatsApp Enquiry</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="display:grid; grid-template-columns:1fr 340px; gap:48px;">
    <div>
      <h2 style="color:var(--maroon); margin-bottom:16px;">Key Highlights of {city} Tour</h2>
      <ul class="highlights" style="margin-bottom:36px;">
        {highlights_html}
      </ul>

      <h2 style="color:var(--maroon); margin-bottom:24px;">Detailed Tour Itinerary</h2>
      <div style="display:flex; flex-direction:column; gap:20px; margin-bottom:48px;">
        {itinerary_html}
      </div>

      <h2 style="color:var(--maroon); margin-bottom:20px;">Frequently Asked Questions ({city})</h2>
      <div style="display:flex; flex-direction:column; gap:16px;">
        {faqs_html}
      </div>
    </div>

    <!-- Sidebar Widget -->
    <div>
      <div style="position:sticky; top:100px; background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:28px;">
        <h3 style="color:var(--maroon); margin-bottom:12px;">Package Pricing & Summary</h3>
        <p style="font-size:0.95rem; color:var(--ink-2); margin-bottom:18px;">All-inclusive pricing with private AC car, guide, and temple assistance.</p>

        <div style="border-bottom:1px solid var(--line); padding-bottom:14px; margin-bottom:14px;">
          <div style="font-weight:600; color:var(--saffron-deep);">Standard Cab & Guide</div>
          <div style="font-size:1.4rem; font-weight:700; color:var(--ink);">From ₹1,499 <small style="font-size:0.8rem; font-weight:400; color:var(--ink-3);">/ person</small></div>
        </div>

        <div style="border-bottom:1px solid var(--line); padding-bottom:14px; margin-bottom:14px;">
          <div style="font-weight:600; color:var(--saffron-deep);">Deluxe AC Hotel + Cab</div>
          <div style="font-size:1.4rem; font-weight:700; color:var(--ink);">From ₹3,499 <small style="font-size:0.8rem; font-weight:400; color:var(--ink-3);">/ person</small></div>
        </div>

        <div style="margin-bottom:24px;">
          <div style="font-weight:600; color:var(--saffron-deep);">VIP Executive Package</div>
          <div style="font-size:1.4rem; font-weight:700; color:var(--ink);">From ₹5,999 <small style="font-size:0.8rem; font-weight:400; color:var(--ink-3);">/ person</small></div>
        </div>

        <a href="contact.html" class="btn btn-primary" style="width:100%; text-align:center; margin-bottom:12px;">Get Custom Quote</a>
        <a href="tel:+919235222399" class="btn btn-ghost" style="width:100%; text-align:center;">📞 Call +91 92352 22399</a>
      </div>
    </div>
  </div>
</section>

<footer class="site-foot">
  <div class="container foot-grid">
    <div class="foot-brand">
      <div class="brand" style="margin-bottom:16px;">
        <img width="500" height="500" src="assets/logo.webp" alt="Ayodhya Dharshan Logo" class="brand-mark" fetchpriority="high">
        <span class="brand-name" style="color:#FCEFD9;">Ayodhya Dharshan<small>Teerth Yatra</small></span>
      </div>
      <p>Soulful, fully-managed pilgrimages across the holiest cities of Uttar Pradesh — guided with reverence and care.</p>
    </div>
    <div><h4>Explore</h4>
      <a href="destinations.html">Destinations</a>
      <a href="services.html">Services</a>
      <a href="yatra-cost-calculator.html">Calculator</a>
      <a href="about.html">About Us</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html">Contact</a>
    </div>
    <div><h4>Cities</h4>
      <a href="ayodhya-dharshan-tour-package.html">Ayodhya</a>
      <a href="varanasi-same-day-tour-package.html">Varanasi</a>
      <a href="prayagraj-tour-package.html">Prayagraj</a>
      <a href="chitrakoot-tour-package.html">Chitrakoot</a>
      <a href="naimisharanya-tour-package.html">Naimisharanya</a>
      <a href="vindhyachal-tour-package.html">Vindhyachal</a>
      <a href="mathura-tour-package.html">Mathura</a>
      <a href="vrindavan-tour-package.html">Vrindavan</a>
    </div>
    <div><h4>Reach Us</h4>
      <a href="tel:+919235222399">+91 92352 22399</a>
      <a href="mailto:yatra@ayodhyadharshan.com">yatra@ayodhyadharshan.com</a>
      <a href="contact.html">RTO Office, Ayodhya</a>
      <a href="https://share.google/Q6wXLDvNd2VDOzNUp" target="_blank" rel="noopener">Find us on Google Maps</a>
      <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20{city}%20tour%20package." target="_blank" rel="noopener">WhatsApp · 24×7</a>
    </div>
  </div>
  <div class="container foot-bottom">
    <span>© 2026 Ayodhya Dharshan · Teerth Yatra Seva</span>
    <span>॥ श्री राम जय राम जय जय राम ॥</span>
  </div>
</footer>

<script>
const navToggle=document.getElementById('navToggle'), navLinks=document.getElementById('navLinks');
navToggle?.addEventListener('click',()=>navLinks.classList.toggle('open'));
</script>

</body>
</html>"""

for item in pages_data:
    highlights_html = "\n        ".join([f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>{h}</li>' for h in item["highlights"]])
    
    itinerary_html = "\n        ".join([
        f'<div style="background:var(--bg-card); border-left:4px solid var(--saffron); padding:16px 20px; border-radius:0 var(--r-sm) var(--r-sm) 0; border:1px solid var(--line); border-left-width:4px;">'
        f'<div style="font-weight:700; color:var(--saffron-deep); font-size:0.95rem;">{t}</div>'
        f'<h3 style="font-size:1.15rem; color:var(--maroon); margin:4px 0 6px;">{head}</h3>'
        f'<p style="margin:0; font-size:0.95rem; color:var(--ink-2);">{desc}</p>'
        f'</div>'
        for t, head, desc in item["itinerary"]
    ])
    
    faqs_html = "\n        ".join([
        f'<details style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-sm); padding:14px 18px;">'
        f'<summary style="font-weight:600; color:var(--maroon); cursor:pointer;">{q}</summary>'
        f'<p style="margin-top:10px; margin-bottom:0; font-size:0.95rem; color:var(--ink-2);">{a}</p>'
        f'</details>'
        for q, a in item["faqs"]
    ])
    
    code = template_code.format(
        filename=item["filename"],
        city=item["city"],
        title=item["title"],
        meta_desc=item["meta_desc"],
        keywords=item["keywords"],
        h1=item["h1"],
        lead=item["lead"],
        image=item["image"],
        highlights_html=highlights_html,
        itinerary_html=itinerary_html,
        faqs_html=faqs_html
    )
    
    file_path = os.path.join("/Users/rishabhjaiswal/ayodhya-darshan", item["filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Created dedicated destination page: {item['filename']}")

print("All 6 dedicated single-city destination pages generated!")
