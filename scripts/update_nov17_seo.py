#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html"
        if new_url not in content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            content = content.replace("</urlset>", url_entry + "</urlset>")
            print("✅ Added Ayodhya to Varanasi Tour Package blog URL to sitemap.xml")

        # Update all lastmod dates to 2026-11-17
        content = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", "<lastmod>2026-11-17</lastmod>", content)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Updated all lastmod dates in sitemap.xml to 2026-11-17")

    # Also update Next.js public sitemap if present
    next_sitemap = "ayodhya-landing-main/public/sitemap.xml"
    if os.path.exists(next_sitemap):
        with open(next_sitemap, "r", encoding="utf-8") as f:
            n_content = f.read()
        if new_url not in n_content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            n_content = n_content.replace("</urlset>", url_entry + "</urlset>")
        n_content = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", "<lastmod>2026-11-17</lastmod>", n_content)
        with open(next_sitemap, "w", encoding="utf-8") as f:
            f.write(n_content)
        print("✅ Updated Next.js public/sitemap.xml to 2026-11-17")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya to Varanasi Tour Package 2026: Price List, 3-Day &amp; 4-Day Itinerary, Cabs &amp; VIP Darshan Guide</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html</guid>
      <description>Verified Ayodhya to Varanasi tour package 2026 price list (from ₹6,499/person), 3-day &amp; 4-day itineraries, Ram Mandir &amp; Kashi Vishwanath VIP darshan passes, private AC highway cabs &amp; 3-star hotels.</description>
      <pubDate>Tue, 17 Nov 2026 17:45:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Ayodhya to Varanasi guide to rss.xml")
    else:
        print("ℹ️ Guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya to Varanasi Tour Package 2026 Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Pilgrimage Circuit · 8 min read</span>
          <h3><a href="blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html">Ayodhya to Varanasi Tour Package 2026: Price List &amp; 4-Day Itinerary</a></h3>
          <p>Verified 2026 prices (from ₹6,499), 3-day &amp; 4-day itineraries, highway cab travel (NH-330 / Purvanchal), Ram Mandir &amp; Kashi Vishwanath VIP Darshan assistance, and private Ganga boat rides.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html" style="color:var(--saffron-deep);">Read Circuit Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)

        # Also add to schema blogPost list
        schema_entry = '    { "@type": "BlogPosting", "headline": "Ayodhya to Varanasi Tour Package 2026: Price List, 3-Day & 4-Day Itinerary, Cabs & VIP Darshan Guide", "url": "https://www.ayodhyadharshan.com/blog-ayodhya-to-varanasi-tour-package-price-itinerary-booking-guide.html" },\n'
        content = content.replace('"blogPost": [\n', '"blogPost": [\n' + schema_entry)

        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Ayodhya to Varanasi card and Schema entry to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
