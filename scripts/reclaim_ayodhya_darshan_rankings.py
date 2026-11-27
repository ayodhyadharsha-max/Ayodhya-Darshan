#!/usr/bin/env python3
import os
import re

def optimize_index_html():
    file_path = "index.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Title Tag
    new_title = "<title>Ayodhya Darshan 2026: Ram Mandir Timings, Yatra Guide &amp; Tour Packages</title>"
    content = re.sub(r"<title>.*?</title>", new_title, content, count=1)
    print("✅ Updated Title tag to exact match 'Ayodhya Darshan 2026'")

    # 2. Meta Description
    new_desc = '<meta name="description" content="⭐ 4.9/5 Rated. Complete Ayodhya Darshan 2026 Guide &amp; Tour Packages from ₹1,499. Ram Mandir darshan timings, daily aarti schedule, VIP Sugam pass assistance, AC cabs &amp; 3★ hotels. Call +91 92352 22399.">'
    content = re.sub(r'<meta name="description" content="[^"]*">', new_desc, content, count=1)
    print("✅ Updated Meta Description")

    # 3. Meta Keywords
    new_kw = '<meta name="keywords" content="Ayodhya Darshan, Ayodhya darshan timings, Ayodhya darshan booking, Ram Mandir Ayodhya darshan, Ayodhya tour package, Ayodhya tour packages, Ayodhya darshan online, Ayodhya same day tour, Ayodhya cab booking, Ram Mandir VIP darshan">'
    content = re.sub(r'<meta name="keywords" content="[^"]*">', new_kw, content, count=1)
    print("✅ Updated Meta Keywords")

    # 4. OpenGraph & Twitter
    og_title = '<meta property="og:title" content="Ayodhya Darshan 2026: Ram Mandir Timings, Yatra Guide &amp; Tour Packages">'
    og_desc = '<meta property="og:description" content="Complete guide to Ayodhya Darshan 2026: Ram Mandir darshan timings, aarti passes, places to visit, and custom pilgrimage tour packages with AC cabs and hotels.">'
    tw_title = '<meta name="twitter:title" content="Ayodhya Darshan 2026: Ram Mandir Timings, Yatra Guide &amp; Tour Packages">'
    tw_desc = '<meta name="twitter:description" content="Complete guide to Ayodhya Darshan 2026: Ram Mandir darshan timings, aarti passes, places to visit, and custom pilgrimage tour packages with AC cabs and hotels.">'

    content = re.sub(r'<meta property="og:title" content="[^"]*">', og_title, content, count=1)
    content = re.sub(r'<meta property="og:description" content="[^"]*">', og_desc, content, count=1)
    content = re.sub(r'<meta name="twitter:title" content="[^"]*">', tw_title, content, count=1)
    content = re.sub(r'<meta name="twitter:description" content="[^"]*">', tw_desc, content, count=1)
    print("✅ Updated OpenGraph & Twitter metadata")

    # 5. Schema alternateName
    schema_old = '"alternateName": "Ayodhya Dharshan Teerth Yatra",'
    schema_new = """"alternateName": [
        "Ayodhya Darshan",
        "Ayodhya Darshan Travels",
        "Ayodhya Darshan Yatra",
        "Ayodhya Darshan Tour Packages",
        "Ayodhya Dharshan Teerth Yatra"
      ],"""
    if schema_old in content:
        content = content.replace(schema_old, schema_new, 1)
        print("✅ Added 'Ayodhya Darshan' brand aliases to Schema.org Knowledge Graph")

    # 6. Hero Section H1 and Lead
    old_h1_pattern = r'<h1 class="display">.*?</h1>'
    new_h1 = """<h1 class="display">
        <span style="display:block;">Ayodhya Darshan 2026</span>
        <span style="display:block; font-size:clamp(1.4rem,2.6vw,2.35rem); color:var(--saffron-deep); font-weight:600; margin-top:4px;">Ram Mandir Timings, Yatra Guide &amp; Tour Packages</span>
      </h1>"""
    content = re.sub(old_h1_pattern, new_h1, content, count=1, flags=re.DOTALL)

    old_lead_pattern = r'<p class="lead">Plan your holy <strong>Ayodhya Darshan</strong>.*?</p>'
    new_lead = '<p class="lead">Plan your holy <strong>Ayodhya Darshan</strong> with verified Ram Mandir timings, Aarti passes, and guided <strong>Ayodhya tour packages</strong>. Private AC cabs, 3★/4★ hotels, Sugam darshan assistance, and 24/7 yatra care across Ayodhya, Varanasi, and Prayagraj.</p>'
    content = re.sub(old_lead_pattern, new_lead, content, count=1, flags=re.DOTALL)
    print("✅ Updated Hero H1 and Lead")

    # 7. Move #ayodhya-darshan-guide Section from below Services to directly below Header (Above the fold!)
    guide_section_match = re.search(r'(<!-- ===== COMPLETE AYODHYA DARSHAN & TOUR PACKAGES GUIDE ===== -->\s*<section class="section" id="ayodhya-darshan-guide".*?</section>\s*)', content, re.DOTALL)
    if guide_section_match:
        guide_section_html = guide_section_match.group(1)
        # Remove it from its current position
        content = content.replace(guide_section_html, "")
        # Insert it directly after </header>
        content = content.replace("</header>\n", "</header>\n\n" + guide_section_html)
        print("🚀 MOVED 'Ayodhya Darshan Guide' to directly below Hero header (Above Destinations & Bell!)")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("🎯 Successfully wrote optimized index.html!")

def update_nextjs_metadata():
    layout_path = "ayodhya-landing-main/app/layout.tsx"
    if os.path.exists(layout_path):
        with open(layout_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = re.sub(
            r'title:\s*"[^"]*",',
            'title: "Ayodhya Darshan 2026: Ram Mandir Timings, Yatra Guide & Tour Packages",',
            content,
            count=1
        )
        content = re.sub(
            r'description:\s*"[^"]*",',
            'description: "⭐ 4.9/5 Rated. Complete Ayodhya Darshan 2026 Guide & Tour Packages from ₹1,499. Ram Mandir darshan timings, daily aarti schedule, VIP Sugam pass assistance, AC cabs & 3★ hotels. Call +91 92352 22399.",',
            content,
            count=1
        )

        with open(layout_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Updated Next.js metadata title & description")

def update_sitewide_internal_links():
    html_files = [f for f in os.listdir(".") if f.endswith(".html") and os.path.isfile(f)]
    count = 0

    target_anchor = '<ul style="list-style:none; padding:0; margin:0;">\n        <li><a href="ayodhya-dharshan-tour-package.html"'
    replacement = '<ul style="list-style:none; padding:0; margin:0;">\n        <li><a href="https://www.ayodhyadharshan.com/" style="color:#fef08a; text-decoration:none; font-weight:700;">Ayodhya Darshan Portal</a></li>\n        <li><a href="ayodhya-dharshan-tour-package.html"'

    for fn in html_files:
        if fn == "index.html":
            continue
        with open(fn, "r", encoding="utf-8") as f:
            c = f.read()

        if "Ayodhya Darshan Portal" not in c and target_anchor in c:
            c = c.replace(target_anchor, replacement, 1)
            with open(fn, "w", encoding="utf-8") as f:
                f.write(c)
            count += 1

    print(f"✅ Injected 'Ayodhya Darshan Portal' homepage anchor link in footer of {count} HTML files!")

def update_sitemaps_date():
    today = "2026-11-27"
    for s_path in ["sitemap.xml", "ayodhya-landing-main/public/sitemap.xml"]:
        if os.path.exists(s_path):
            with open(s_path, "r", encoding="utf-8") as f:
                s = f.read()
            s = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", f"<lastmod>{today}</lastmod>", s)
            with open(s_path, "w", encoding="utf-8") as f:
                f.write(s)
            print(f"✅ Updated all lastmod dates in {s_path} to {today}")

if __name__ == "__main__":
    optimize_index_html()
    update_nextjs_metadata()
    update_sitewide_internal_links()
    update_sitemaps_date()
