#!/usr/bin/env python3
"""
Comprehensive Nov 28, 2026 SEO Master Optimization Script:
1. Resolves Keyword Cannibalization between ayodhya-dharshan-tour-package.html & ayodhya-tour-package.html
   - Sets canonical on ayodhya-dharshan-tour-package.html to ayodhya-tour-package.html
   - Adds 301 redirects in .htaccess and _redirects
   - Updates homepage links to point directly to ayodhya-tour-package.html
2. Fixes all Technical SEO Audit issues (Title & Description length cutoffs)
3. Injects 'Ayodhya Darshan Portal' anchor across all remaining pages
4. Refreshes Schema dateModified to 2026-11-28 and sharpens FAQ pricing text
5. Updates all sitemap lastmod tags to 2026-11-28
"""

import os
import re
import glob

def step1_resolve_cannibalization():
    print("--- [Step 1] Resolving Tour Package Keyword Cannibalization ---")
    
    # 1. Update ayodhya-dharshan-tour-package.html canonical
    dharshan_file = "ayodhya-dharshan-tour-package.html"
    if os.path.exists(dharshan_file):
        with open(dharshan_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace canonical with clean ayodhya-tour-package.html
        content = re.sub(
            r'<link\s+rel="canonical"\s+href="https://www\.ayodhyadharshan\.com/ayodhya-dharshan-tour-package\.html">',
            '<link rel="canonical" href="https://www.ayodhyadharshan.com/ayodhya-tour-package.html">',
            content
        )
        content = re.sub(
            r'<meta\s+property="og:url"\s+content="https://www\.ayodhyadharshan\.com/ayodhya-dharshan-tour-package\.html">',
            '<meta property="og:url" content="https://www.ayodhyadharshan.com/ayodhya-tour-package.html">',
            content
        )
        with open(dharshan_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Canonical in ayodhya-dharshan-tour-package.html pointed to ayodhya-tour-package.html")

    # 2. Add 301 Redirect to .htaccess
    htaccess_file = ".htaccess"
    if os.path.exists(htaccess_file):
        with open(htaccess_file, "r", encoding="utf-8") as f:
            h_content = f.read()
        rule = "RewriteRule ^ayodhya-dharshan-tour-package\\.html$ https://www.ayodhyadharshan.com/ayodhya-tour-package.html [R=301,L]\n"
        if "ayodhya-dharshan-tour-package" not in h_content:
            target = "RewriteEngine On\n"
            h_content = h_content.replace(target, target + rule)
            with open(htaccess_file, "w", encoding="utf-8") as f:
                f.write(h_content)
            print("✅ Added 301 redirect in .htaccess")
        else:
            print("ℹ️ Redirect already in .htaccess")

    # 3. Add 301 Redirect to _redirects
    redirects_file = "_redirects"
    if os.path.exists(redirects_file):
        with open(redirects_file, "r", encoding="utf-8") as f:
            r_content = f.read()
        r_rule = "/ayodhya-dharshan-tour-package.html https://www.ayodhyadharshan.com/ayodhya-tour-package.html 301!\n"
        if "/ayodhya-dharshan-tour-package.html" not in r_content:
            r_content = r_rule + r_content
            with open(redirects_file, "w", encoding="utf-8") as f:
                f.write(r_content)
            print("✅ Added 301 redirect in _redirects")
        else:
            print("ℹ️ Redirect already in _redirects")

    # 4. Update index.html package card and footer links
    index_file = "index.html"
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            idx = f.read()
        idx = idx.replace('href="ayodhya-dharshan-tour-package.html"', 'href="ayodhya-tour-package.html"')
        idx = idx.replace('<h3>Ayodhya Dharshan Tour Package</h3>', '<h3>Ayodhya Tour Package (2N/3D)</h3>')
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(idx)
        print("✅ Updated index.html links to point directly to ayodhya-tour-package.html")


def step2_fix_technical_audit_issues():
    print("\n--- [Step 2] Fixing Technical SEO Audit Issues (Titles & Descriptions) ---")
    
    replacements = [
        (
            "blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html",
            "<title>Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026 Traffic Advisory: Road Diversions &amp; 16 Parking Zones</title>",
            "<title>Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026: Traffic &amp; Parking Guide</title>"
        ),
        (
            "blog-ayodhya-new-year-2027-tour-package-ram-mandir-darshan-guide.html",
            "<title>Ayodhya New Year Tour Package 2027: 31st Dec &amp; 1st Jan Ram Mandir Darshan &amp; Price List</title>",
            "<title>Ayodhya New Year Tour Package 2027: Ram Mandir Darshan Guide</title>"
        ),
        (
            "blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html",
            "<title>Ayodhya to Varanasi Tour Package 2026: Price List, 3-Day &amp; 4-Day Itinerary, Cabs &amp; VIP Darshan Guide</title>",
            "<title>Ayodhya to Varanasi Tour Package 2026: Price &amp; Itinerary Guide</title>"
        ),
        (
            "blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html",
            "<title>Ayodhya Tour Package for Senior Citizens 2026: Wheelchair, VIP Darshan, Hotels &amp; Price Guide</title>",
            "<title>Ayodhya Tour Package for Senior Citizens 2026: Wheelchair &amp; VIP</title>"
        ),
        (
            "blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html",
            '<meta name="description" content="Planning an Ayodhya pilgrimage for elderly parents? Verified 2026 senior citizen packages (from ₹4,999/person): Ram Mandir wheelchair &amp; golf cart assistance, VIP darshan, lift hotels &amp; private AC cabs.">',
            '<meta name="description" content="Verified Ayodhya tour package for senior citizens from ₹4,999: Ram Mandir wheelchair assistance, VIP darshan passes, lift hotels &amp; AC cabs. Call +91 92352 22399.">'
        ),
        (
            "blog-ayodhya-varanasi-prayagraj-tour-package-price-itinerary-guide.html",
            "<title>Ayodhya Varanasi Prayagraj Tour Package 2026: Price, 4-Day &amp; 5-Day Itinerary, Sangam &amp; VIP Darshan Guide</title>",
            "<title>Ayodhya Varanasi Prayagraj Tour Package 2026: Itinerary &amp; Price</title>"
        ),
        (
            "blog-ayodhya-varanasi-prayagraj-tour-package-price-itinerary-guide.html",
            '<meta name="description" content="Complete Ayodhya Varanasi Prayagraj tour package guide for 2026: verified price list (from ₹8,999/person), 4-day &amp; 5-day itineraries, Ram Mandir &amp; Kashi VIP darshan, Triveni Sangam boat ride, AC hotels &amp; private cabs.">',
            '<meta name="description" content="Ayodhya Varanasi Prayagraj tour package 2026 from ₹8,999: 4D/5D itinerary, Triveni Sangam boat snan, Ram Mandir &amp; Kashi VIP darshan &amp; AC cabs. Call +91 92352 22399.">'
        ),
        (
            "blog-varanasi-tour-package-price-itinerary-booking-guide.html",
            "<title>Varanasi Tour Package 2026: Price List, 2-Day &amp; 3-Day Itinerary, Kashi VIP Darshan &amp; Ganga Aarti Guide</title>",
            "<title>Varanasi Tour Package 2026: Price List &amp; 3-Day Itinerary</title>"
        )
    ]

    for filepath, old_s, new_s in replacements:
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            txt = f.read()
        if old_s in txt:
            txt = txt.replace(old_s, new_s)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"✅ Replaced in {filepath}: {new_s[:60]}...")
        else:
            print(f"⚠️ Target string not found in {filepath}")


def step3_inject_missing_portal_links():
    print("\n--- [Step 3] Ingesting 'Ayodhya Darshan Portal' Sitewide Backlinks ---")
    all_html = glob.glob("*.html")
    link_html = '<li><a href="https://www.ayodhyadharshan.com/" style="color:#fef08a; text-decoration:none; font-weight:700;">Ayodhya Darshan Portal</a></li>'
    
    updated_count = 0
    for f in all_html:
        if f == "index.html" or f.startswith("google"):
            continue
        with open(f, "r", encoding="utf-8") as fp:
            txt = fp.read()
        
        if "Ayodhya Darshan Portal" in txt:
            continue
        
        # Pattern 1: standard Sacred Yatra Packages list
        if '<h4 style="color:#fbbf24; font-weight:700; font-size:16px; margin-bottom:12px; border-bottom:1px solid #78350f; padding-bottom:6px;">Sacred Yatra Packages</h4>\n      <ul style="list-style:none; padding:0; margin:0;">' in txt:
            target = '<h4 style="color:#fbbf24; font-weight:700; font-size:16px; margin-bottom:12px; border-bottom:1px solid #78350f; padding-bottom:6px;">Sacred Yatra Packages</h4>\n      <ul style="list-style:none; padding:0; margin:0;">'
            txt = txt.replace(target, target + f"\n        {link_html}")
            updated_count += 1
        elif 'Ayodhya Darshan Homepage' in txt:
            txt = txt.replace('<li><a href="https://www.ayodhyadharshan.com/" style="color:#fef08a; text-decoration:none;">Ayodhya Darshan Homepage</a></li>', link_html)
            updated_count += 1
        elif '<footer' in txt and '<ul' in txt:
            # Inject into the first <ul> found in footer
            parts = txt.split('<footer', 1)
            if len(parts) == 2:
                footer_part = parts[1]
                footer_part = re.sub(r'(<ul[^>]*>)', r'\1\n        ' + link_html, footer_part, count=1)
                txt = parts[0] + '<footer' + footer_part
                updated_count += 1

        with open(f, "w", encoding="utf-8") as fp:
            fp.write(txt)

    print(f"✅ Injected 'Ayodhya Darshan Portal' backlink into {updated_count} files")


def step4_schema_and_faq_updates():
    print("\n--- [Step 4] Updating Freshness Dates & FAQ Accuracy in index.html ---")
    index_file = "index.html"
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Update dateModified to 2026-11-28
    content = re.sub(r'"dateModified":\s*"2026-\d\d-\d\d"', '"dateModified": "2026-11-28"', content)
    
    # Update FAQ question and text to be accurate and exact match
    content = content.replace(
        '"name": "How much does an Ayodhya Dharshan tour package cost?"',
        '"name": "How much does an Ayodhya tour package cost?"'
    )
    content = content.replace(
        '"text": "An Ayodhya Dharshan tour package starts from ₹7,900 per person for a 3-day / 2-night trip, including stays, private travel, a guide and darshan assistance. The final price depends on hotel category, group size and season."',
        '"text": "An Ayodhya tour package starts from ₹1,499 per person for a same-day sightseeing tour, and ₹4,499 to ₹7,900 per person for an all-inclusive 3-day / 2-night trip, including 3★ hotel stays near Ram Mandir, private AC cab, local pandit guide, and Ram Janmabhoomi VIP Sugam Darshan assistance."'
    )

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Updated dateModified to 2026-11-28 and FAQ pricing in index.html")


def step5_sitemap_lastmod():
    print("\n--- [Step 5] Refreshing Sitemap Dates to 2026-11-28 ---")
    for sm in ["sitemap.xml", "ayodhya-landing-main/public/sitemap.xml"]:
        if os.path.exists(sm):
            with open(sm, "r", encoding="utf-8") as f:
                content = f.read()
            content = re.sub(r'<lastmod>2026-\d\d-\d\d</lastmod>', '<lastmod>2026-11-28</lastmod>', content)
            with open(sm, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Updated all lastmod dates in {sm} to 2026-11-28")


if __name__ == "__main__":
    step1_resolve_cannibalization()
    step2_fix_technical_audit_issues()
    step3_inject_missing_portal_links()
    step4_schema_and_faq_updates()
    step5_sitemap_lastmod()
    print("\n🎉 Master Nov 28 SEO Optimization Complete!")
