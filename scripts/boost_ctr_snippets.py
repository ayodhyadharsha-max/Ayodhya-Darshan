import os
import re

root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

ctr_upgrades = {
    "index.html": {
        "title": "<title>Ayodhya Darshan &amp; Ram Mandir Tour Packages (From ₹1,499)</title>",
        "desc": '<meta name="description" content="⭐ 4.9/5 Rated. Book Ayodhya Ram Mandir VIP Darshan &amp; Tour Packages from ₹1,499. AC Cabs, 3-Star Stays &amp; 24x7 Guide. Call +91 92352 22399 for free quotes!">'
    },
    "ayodhya-same-day-tour.html": {
        "title": "<title>Ayodhya Same Day Tour Package 2026 (Cabs @ ₹1,499)</title>",
        "desc": '<meta name="description" content="⭐ 4.9/5 Rated. Book 1-Day Ayodhya Ram Mandir Darshan Cabs from ₹1,499. Private AC Dzire/Ertiga with hotel pick-up &amp; Saryu Aarti. Book via WhatsApp!">'
    },
    "ayodhya-varanasi-tour-package.html": {
        "title": "<title>Varanasi Ayodhya Tour Package 2026 (4 Days @ ₹4,999)</title>",
        "desc": '<meta name="description" content="⭐ 4.9/5 Rated. Complete 4 Days Varanasi Kashi Vishwanath &amp; Ayodhya Ram Mandir Yatra package from ₹4,999. Includes Ganga Aarti boat &amp; AC cabs!">'
    },
    "mathura-vrindavan-tour-package.html": {
        "title": "<title>Mathura Vrindavan Tour Package 2026 (3 Days @ ₹3,999)</title>",
        "desc": '<meta name="description" content="⭐ 4.9/5 Rated. Book 3 Days Mathura Vrindavan Banke Bihari &amp; Prem Mandir tour package from ₹3,999. AC Cabs &amp; 3-Star Hotel stay included.">'
    },
    "blog-ram-mandir-vip-pass-booking-guide.html": {
        "title": "<title>Ram Mandir VIP Pass Booking Guide 2026 (100% Free Slots)</title>",
        "desc": '<meta name="description" content="⭐ Complete official guide to Ayodhya Ram Mandir VIP &amp; Sugam Darshan entry passes (100% Free). Timings, gate entry rules &amp; fast-track yatra cabs!">'
    }
}

for filename, meta_data in ctr_upgrades.items():
    filepath = os.path.join(root_dir, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Title
    old_title = re.search(r'<title>.*?</title>', content, re.DOTALL)
    if old_title:
        content = content.replace(old_title.group(0), meta_data["title"])

    # Replace Description
    old_desc = re.search(r'<meta\s+name="description"\s+content=".*?"', content, re.DOTALL)
    if old_desc:
        content = content.replace(old_desc.group(0), meta_data["desc"])

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"⚡ Upgraded High-CTR Title & Meta Description in {filename}!")

