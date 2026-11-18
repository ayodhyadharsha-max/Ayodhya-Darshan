#!/usr/bin/env python3
import os
import re

def update_index_html():
    file_path = "index.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title Tag
    old_title = "<title>Ayodhya Ram Mandir & Darshan Tour Packages 2026</title>"
    new_title = "<title>Ayodhya Darshan &amp; Ayodhya Tour Packages 2026 | Ram Mandir VIP Yatra</title>"
    if old_title in content:
        content = content.replace(old_title, new_title)
        print("✅ Updated index.html Title tag")
    else:
        # Fallback regex replace for title
        content = re.sub(r"<title>.*?</title>", new_title, content, count=1)
        print("✅ Updated index.html Title tag (via regex)")

    # 2. Update Meta Description
    old_desc_snippet = '<meta name="description" content="⭐ 4.9/5 Rated. Book Ayodhya Ram Mandir VIP Darshan &amp; Tour Packages from ₹1,499. AC Cabs, 3-Star Stays &amp; 24x7 Guide. Call +91 92352 22399 for free quotes!">'
    new_desc = '<meta name="description" content="⭐ 4.9/5 Rated. Book Ayodhya Darshan &amp; Ayodhya Tour Packages from ₹1,499. Ram Mandir VIP Sugam Darshan assistance, temple timings, AC cabs, 3★ hotels &amp; 24x7 local guide. Call +91 92352 22399 for free quotes!">'
    if old_desc_snippet in content:
        content = content.replace(old_desc_snippet, new_desc)
        print("✅ Updated index.html Meta Description")
    else:
        content = re.sub(r'<meta name="description" content="[^"]*">', new_desc, content, count=1)
        print("✅ Updated index.html Meta Description (via regex)")

    # 3. Update Meta Keywords
    old_kw_snippet = '<meta name="keywords" content="Ayodhya tour packages, Ayodhya darshan tour, Ram Mandir Ayodhya yatra, Varanasi Ayodhya tour package, Prayagraj Ayodhya tour, UP pilgrimage packages, Ayodhya cab booking">'
    new_kw = '<meta name="keywords" content="Ayodhya Darshan, Ayodhya Tour Packages, Ayodhya tour package, Ayodhya darshan booking, Ram Mandir darshan timings, Ayodhya darshan online, Ayodhya tour package with hotel, Ayodhya same day tour, Ayodhya cab booking, Ram Mandir VIP darshan, Varanasi Ayodhya tour package, Ayodhya yatra 2026">'
    if old_kw_snippet in content:
        content = content.replace(old_kw_snippet, new_kw)
        print("✅ Updated index.html Meta Keywords")

    # 4. Update OpenGraph & Twitter tags
    content = content.replace(
        '<meta property="og:title" content="Ayodhya Dharshan Tour Package | Varanasi Prayagraj Ayod...">',
        '<meta property="og:title" content="Ayodhya Darshan &amp; Ayodhya Tour Packages 2026 | Ram Mandir VIP Yatra">'
    )
    content = content.replace(
        '<meta name="twitter:title" content="Ayodhya Dharshan Tour Package | Varanasi Prayagraj Ayodhya Yatra">',
        '<meta name="twitter:title" content="Ayodhya Darshan &amp; Ayodhya Tour Packages 2026 | Ram Mandir VIP Yatra">'
    )

    # 5. Update Hero Section H1 and Lead
    old_hero_h1 = """      <h1 class="display">
        <span style="display:block;">Ayodhya Darshan &amp; Ram Mandir</span>
        <span style="display:block; font-size:clamp(1.4rem,2.6vw,2.35rem); color:var(--saffron-deep); font-weight:600; margin-top:4px;">Tour Packages 2026</span>
      </h1>"""
    
    new_hero_h1 = """      <h1 class="display">
        <span style="display:block;">Ayodhya Darshan &amp; Ayodhya Tour Packages</span>
        <span style="display:block; font-size:clamp(1.4rem,2.6vw,2.35rem); color:var(--saffron-deep); font-weight:600; margin-top:4px;">Ram Mandir VIP Yatra &amp; Cabs 2026</span>
      </h1>"""
    
    if old_hero_h1 in content:
        content = content.replace(old_hero_h1, new_hero_h1)
        print("✅ Updated index.html Hero H1")

    old_hero_lead = """      <p class="lead">From Shri Ram's Ayodhya &amp; Kashi Vishwanath in Varanasi to Banke Bihari &amp; Prem Mandir in Vrindavan — we organize custom, VIP-guided family yatras across all sacred destinations of Uttar Pradesh with 24/7 care and private AC cabs.</p>"""
    new_hero_lead = """      <p class="lead">Plan your holy <strong>Ayodhya Darshan</strong> and book all-inclusive <strong>Ayodhya tour packages</strong> with Ram Mandir VIP Sugam darshan assistance, comfortable 3★/4★ hotel stays, private AC cabs, and 24/7 on-ground yatra care across Ayodhya, Varanasi (Kashi), and Prayagraj.</p>"""
    if old_hero_lead in content:
        content = content.replace(old_hero_lead, new_hero_lead)
        print("✅ Updated index.html Hero Lead")

    # 6. Add High-Value Dedicated Section: "Ayodhya Darshan 2026: Official Timings, Route & Complete Yatra Guide"
    # Place right before <!-- ===== POPULAR PACKAGES ===== -->
    darshan_guide_section = """<!-- ===== COMPLETE AYODHYA DARSHAN & TOUR PACKAGES GUIDE ===== -->
<section class="section" id="ayodhya-darshan-guide" style="background:#fff; border-top:1px solid var(--line-soft); border-bottom:1px solid var(--line-soft); padding:64px 0;">
  <div class="container">
    <div class="center" style="max-width:760px; margin:0 auto 40px;">
      <p class="eyebrow center" style="color:var(--saffron-deep); font-weight:700;">Complete Pilgrimage &amp; Booking Guide</p>
      <h2 style="font-size:clamp(1.8rem, 2.8vw, 2.5rem); margin-bottom:14px; color:var(--maroon); font-family:var(--font-display);">Ayodhya Darshan: Ram Mandir Timings, Aarti &amp; Tour Packages 2026</h2>
      <p class="lead" style="font-size:1.05rem; color:var(--ink-2); line-height:1.7;">
        Planning your sacred <strong>Ayodhya Darshan</strong>? Here is the complete verified guide to <strong>Shri Ram Janmabhoomi Mandir timings</strong>, daily Aarti schedules, recommended darshan sequences, and custom <strong>Ayodhya tour packages</strong> with private AC cabs and trusted local pandit guides.
      </p>
    </div>

    <!-- Timings & Aarti Schedule Cards Grid -->
    <div class="grid cols-2" style="gap:24px; margin-bottom:40px;">
      <div class="card" style="padding:28px; border:1px solid var(--line); border-radius:12px; background:var(--bg-panel); box-shadow:0 4px 16px rgba(0,0,0,0.03);">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <span style="font-size:1.8rem;">⏰</span>
          <h3 style="margin:0; font-size:1.3rem; color:var(--maroon);">Ram Mandir Darshan Timings 2026</h3>
        </div>
        <p style="font-size:0.92rem; color:var(--ink-2); margin-bottom:14px;">Shri Ram Janmabhoomi Teerth Kshetra allows general darshan daily in two extended shifts:</p>
        <div style="background:#fff; border-radius:8px; border:1px solid var(--line); overflow:hidden;">
          <div style="display:flex; justify-content:space-between; padding:10px 14px; border-bottom:1px solid var(--line-soft); font-size:0.9rem;">
            <strong>🌅 Morning Darshan:</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">07:00 AM – 11:30 AM</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:10px 14px; border-bottom:1px solid var(--line-soft); font-size:0.9rem; background:#FFFDF8;">
            <strong>⏸️ Temple Closed (Bhog/Rest):</strong>
            <span style="color:var(--ink-muted);">11:30 AM – 01:35 PM</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:10px 14px; border-bottom:1px solid var(--line-soft); font-size:0.9rem;">
            <strong>☀️ Afternoon / Evening:</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">01:35 PM – 07:00 PM</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:10px 14px; font-size:0.9rem; background:#FFFDF8;">
            <strong>🌙 Night Darshan (Close):</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">07:00 PM – 09:30 PM (Gates close 10 PM)</span>
          </div>
        </div>
      </div>

      <div class="card" style="padding:28px; border:1px solid var(--line); border-radius:12px; background:var(--bg-panel); box-shadow:0 4px 16px rgba(0,0,0,0.03);">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <span style="font-size:1.8rem;">🪔</span>
          <h3 style="margin:0; font-size:1.3rem; color:var(--maroon);">Daily Ram Lalla Aarti Schedule</h3>
        </div>
        <p style="font-size:0.92rem; color:var(--ink-2); margin-bottom:14px;">Devotees can attend holy aartis with pre-booked passes issued by the Temple Trust:</p>
        <div style="background:#fff; border-radius:8px; border:1px solid var(--line); overflow:hidden;">
          <div style="display:flex; justify-content:space-between; padding:10px 14px; border-bottom:1px solid var(--line-soft); font-size:0.9rem;">
            <strong>✨ Mangala Aarti (Morning):</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">04:30 AM (Pass Required)</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:10px 14px; border-bottom:1px solid var(--line-soft); font-size:0.9rem; background:#FFFDF8;">
            <strong>🌸 Shringar Aarti (Morning):</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">06:30 AM (Pass Required)</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:10px 14px; border-bottom:1px solid var(--line-soft); font-size:0.9rem;">
            <strong>🍱 Bhog Aarti (Midday):</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">12:00 PM (No Pass Needed)</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:10px 14px; font-size:0.9rem; background:#FFFDF8;">
            <strong>🌺 Shayan Aarti (Night):</strong>
            <span style="color:var(--saffron-deep); font-weight:700;">09:30 PM (Pass Required)</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Step-by-Step Darshan Process & Itinerary -->
    <div style="background:var(--cream); border:1px solid var(--line-soft); border-radius:12px; padding:32px; margin-bottom:36px;">
      <h3 style="color:var(--maroon); font-size:1.4rem; margin-bottom:16px; font-family:var(--font-display);">Recommended Step-by-Step Ayodhya Darshan Sequence</h3>
      <p style="font-size:0.95rem; color:var(--ink-2); margin-bottom:20px; line-height:1.7;">
        According to centuries of Sanatan traditions, every Ayodhya pilgrimage follows a sacred sequence to maximize spiritual blessings and avoid unnecessary walking:
      </p>
      <div class="grid cols-4" style="gap:16px;">
        <div style="background:#fff; padding:18px; border-radius:8px; border:1px solid var(--line); border-top:3px solid var(--saffron);">
          <strong style="color:var(--saffron-deep); display:block; margin-bottom:6px;">Step 1: Saryu Snan</strong>
          <span style="font-size:0.88rem; color:var(--ink-2);">Holy dip or achaman at Ram ki Paidi / Naya Ghat before starting temple visits.</span>
        </div>
        <div style="background:#fff; padding:18px; border-radius:8px; border:1px solid var(--line); border-top:3px solid var(--saffron);">
          <strong style="color:var(--saffron-deep); display:block; margin-bottom:6px;">Step 2: Hanuman Garhi</strong>
          <span style="font-size:0.88rem; color:var(--ink-2);">Seek permission from Lord Hanuman (Ayodhya Kotwal) before visiting Shri Ram's abode.</span>
        </div>
        <div style="background:#fff; padding:18px; border-radius:8px; border:1px solid var(--line); border-top:3px solid var(--saffron);">
          <strong style="color:var(--saffron-deep); display:block; margin-bottom:6px;">Step 3: Ram Janmabhoomi</strong>
          <span style="font-size:0.88rem; color:var(--ink-2);">Bhavya Ram Mandir darshan of Ram Lalla, Ram Darbar, and Kuber Tila.</span>
        </div>
        <div style="background:#fff; padding:18px; border-radius:8px; border:1px solid var(--line); border-top:3px solid var(--saffron);">
          <strong style="color:var(--saffron-deep); display:block; margin-bottom:6px;">Step 4: Kanak Bhawan &amp; Aarti</strong>
          <span style="font-size:0.88rem; color:var(--ink-2);">Visit Sita-Ram palace (Kanak Bhawan) and attend the grand evening Saryu Maha Aarti at 6:30 PM.</span>
        </div>
      </div>
    </div>

    <!-- Booking Assistance Banner -->
    <div style="background:linear-gradient(135deg, #7A1C1C 0%, #9A3415 100%); color:#fff; border-radius:12px; padding:28px 32px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px; box-shadow:0 8px 24px rgba(122,28,28,0.2);">
      <div>
        <h4 style="font-size:1.35rem; margin-bottom:6px; color:#FFFDF8;">Looking for a Hassle-Free Ayodhya Tour Package?</h4>
        <p style="margin:0; font-size:0.95rem; color:rgba(255,255,255,0.9); max-width:620px;">
          Get verified 3★/4★ hotel stays near Ram Mandir, private AC cabs (Sedan/Ertiga/Innova), Sugam Darshan assistance, and pure sattvic food arranged seamlessly.
        </p>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20book%20an%20Ayodhya%20Darshan%20tour%20package." target="_blank" rel="noopener" class="btn" style="background:#25D366; color:#fff; border:none; font-weight:700; padding:12px 22px; border-radius:8px; text-decoration:none;">
          Chat on WhatsApp →
        </a>
        <a href="tel:+919235222399" class="btn" style="background:#fff; color:var(--maroon); border:none; font-weight:700; padding:12px 22px; border-radius:8px; text-decoration:none;">
          Call +91 92352 22399
        </a>
      </div>
    </div>

  </div>
</section>

"""

    target_anchor = "<!-- ===== POPULAR PACKAGES ===== -->"
    if "id=\"ayodhya-darshan-guide\"" not in content and target_anchor in content:
        content = content.replace(target_anchor, darshan_guide_section + target_anchor)
        print("✅ Added Ayodhya Darshan Guide & Timings section before Popular Packages")

    # 7. Update Popular Packages section header
    old_pkg_head = """      <p class="eyebrow center">Popular tour packages</p>
      <h2>Ayodhya, Varanasi &amp; Prayagraj tour packages</h2>"""
    new_pkg_head = """      <p class="eyebrow center">Verified 2026 Pilgrimage Packages</p>
      <h2>Ayodhya Tour Packages &amp; Ram Mandir Darshan Yatras</h2>"""
    if old_pkg_head in content:
        content = content.replace(old_pkg_head, new_pkg_head)
        print("✅ Updated Popular Packages Section Header")

    # 8. Update FAQ Section Heading
    old_faq_h2 = '<h2>Ayodhya tour package — your questions, answered</h2>'
    new_faq_h2 = '<h2>Ayodhya Darshan &amp; Tour Packages — Frequently Asked Questions</h2>'
    if old_faq_h2 in content:
        content = content.replace(old_faq_h2, new_faq_h2)
        print("✅ Updated FAQ Section Heading")

    # 9. Inject 2 High-Intent FAQs into on-page FAQ details
    new_faq_details = """    <details class="faq"><summary>What are the official Ram Mandir Ayodhya Darshan and Aarti timings in 2026?<span class="pm">+</span></summary>
      <div class="ans">Shri Ram Janmabhoomi Mandir general darshan is open daily in two slots: <strong>Morning: 07:00 AM to 11:30 AM</strong> and <strong>Evening: 01:35 PM to 09:30 PM</strong> (gates close at 10:00 PM). Key aarti timings are Mangala Aarti (04:30 AM), Shringar Aarti (06:30 AM), Bhog Aarti (12:00 PM), and Shayan Aarti (09:30 PM). Free passes are issued by the official Temple Trust portal (srjbtkshetra.org).</div></details>
    <details class="faq"><summary>Can I do Ayodhya Darshan in 1 day from Lucknow or Gorakhpur?<span class="pm">+</span></summary>
      <div class="ans">Yes, our <strong>Ayodhya same day tour package</strong> is specially curated for 1-day pilgrims. A private AC cab picks you up from Lucknow or Gorakhpur early morning (6:00 AM), arrives in Ayodhya by 8:30 AM, covers Hanuman Garhi, Shri Ram Janmabhoomi VIP Darshan, Kanak Bhawan, and evening Saryu Aarti, returning the same night. Prices start from <strong>₹2,900 per vehicle</strong>.</div></details>
"""
    if "What are the official Ram Mandir Ayodhya Darshan and Aarti timings in 2026?" not in content:
        faq_anchor = '<details class="faq" open>'
        content = content.replace(faq_anchor, new_faq_details + faq_anchor)
        print("✅ Injected high-intent Ayodhya Darshan FAQs into details list")

    # 10. Update Schema FAQPage with new questions
    schema_faq_addition = """    { "@type": "Question", "name": "What are the official Ram Mandir Ayodhya Darshan and Aarti timings in 2026?", "acceptedAnswer": { "@type": "Answer", "text": "Shri Ram Janmabhoomi Mandir general darshan is open daily: Morning 07:00 AM to 11:30 AM and Evening 01:35 PM to 09:30 PM. Mangala Aarti is at 04:30 AM, Shringar Aarti at 06:30 AM, Bhog Aarti at 12:00 PM, and Shayan Aarti at 09:30 PM. Free passes are available on the official Temple Trust website." } },
    { "@type": "Question", "name": "How to book an all-inclusive Ayodhya tour package?", "acceptedAnswer": { "@type": "Answer", "text": "You can book custom Ayodhya tour packages directly by calling or messaging +91 92352 22399. Packages include 3-star/4-star hotel stays, private AC cab transfers, local pandit guides, and complete Ram Janmabhoomi Sugam Darshan assistance." } },
"""
    if "What are the official Ram Mandir Ayodhya Darshan and Aarti timings in 2026?" not in content:
        content = content.replace('"mainEntity": [\n', '"mainEntity": [\n' + schema_faq_addition)
        print("✅ Injected high-intent FAQs into Schema JSON-LD")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("🎯 Successfully wrote all updates to index.html!")

def update_nextjs_metadata():
    layout_path = "ayodhya-landing-main/app/layout.tsx"
    if os.path.exists(layout_path):
        with open(layout_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update title
        content = re.sub(
            r'title:\s*"[^"]*",',
            'title: "Ayodhya Darshan & Ayodhya Tour Packages 2026 | Ram Mandir VIP Yatra Starting ₹1,499",',
            content,
            count=1
        )
        # Update description
        content = re.sub(
            r'description:\s*"[^"]*",',
            'description: "⭐ 4.9/5 Rated. Book Ayodhya Darshan & Ayodhya tour packages from ₹1,499. Includes Ram Mandir VIP Sugam darshan pass assistance, 3★/4★ hotels, airport transfers, private AC cabs, and 24x7 expert guide. Call +91 92352 22399.",',
            content,
            count=1
        )

        with open(layout_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Updated Next.js app/layout.tsx metadata title & description")

def update_cannibalization_links():
    # Link back to homepage from ayodhya-dharshan-tour-package.html
    p1 = "ayodhya-dharshan-tour-package.html"
    if os.path.exists(p1):
        with open(p1, "r", encoding="utf-8") as f:
            c1 = f.read()
        anchor_text = '<p style="margin-top:20px; font-size:0.95rem; background:#fff8ee; padding:12px 18px; border-radius:8px; border-left:4px solid var(--saffron);">Looking for live temple timings, same-day routes, and family pilgrimage itineraries? Visit our main <a href="https://www.ayodhyadharshan.com/" style="color:var(--maroon); font-weight:700; text-decoration:underline;">Ayodhya Darshan &amp; Tour Packages Portal</a>.</p>'
        if "Visit our main" not in c1 and "</h1>" in c1:
            c1 = c1.replace("</h1>", "</h1>\n" + anchor_text, 1)
            with open(p1, "w", encoding="utf-8") as f:
                f.write(c1)
            print("✅ Added authority backlink to homepage in ayodhya-dharshan-tour-package.html")

    # Link back to homepage from blog-ayodhya-dharshan-tour-package.html
    p2 = "blog-ayodhya-dharshan-tour-package.html"
    if os.path.exists(p2):
        with open(p2, "r", encoding="utf-8") as f:
            c2 = f.read()
        anchor_text_blog = '<p style="margin:24px 0; font-size:1rem; background:#fff8ee; padding:14px 20px; border-radius:8px; border-left:4px solid var(--saffron);"><strong>Planning Your Visit?</strong> Check live temple schedules, aarti slots, and package pricing directly on our official <a href="https://www.ayodhyadharshan.com/" style="color:var(--maroon); font-weight:700; text-decoration:underline;">Ayodhya Darshan &amp; Ayodhya Tour Packages</a> homepage.</p>'
        if "official" not in c2 and "</h1>" in c2:
            c2 = c2.replace("</h1>", "</h1>\n" + anchor_text_blog, 1)
            with open(p2, "w", encoding="utf-8") as f:
                f.write(c2)
            print("✅ Added authority backlink to homepage in blog-ayodhya-dharshan-tour-package.html")

if __name__ == "__main__":
    update_index_html()
    update_nextjs_metadata()
    update_cannibalization_links()
