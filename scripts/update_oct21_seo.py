#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-price-itinerary-booking-guide.html"
    if new_url not in content:
        url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
        content = content.replace("</urlset>", url_entry + "</urlset>")
        print("✅ Added new blog URL to sitemap.xml")

    # Update all lastmod dates to 2026-10-21
    content = re.sub(r"<lastmod>2026-10-\d\d</lastmod>", "<lastmod>2026-10-21</lastmod>", content)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Updated all lastmod dates in sitemap.xml to 2026-10-21")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya Tour Package 2026: Price, Itinerary, Hotels &amp; Cab Guide</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-price-itinerary-booking-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-price-itinerary-booking-guide.html</guid>
      <description>Looking for the best Ayodhya tour package? Verified 2026 price list (from ₹1,499), 1-day, 2-day &amp; 3-day itineraries, Ram Mandir VIP darshan, 3-star AC hotels &amp; private cabs.</description>
      <pubDate>Wed, 21 Oct 2026 14:15:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-tour-package-price-itinerary-booking-guide.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Ayodhya Tour Package guide to rss.xml")
    else:
        print("ℹ️ Guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-tour-package-price-itinerary-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Tour Package 2026 Price, Itinerary and Cab Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Pillar Yatra Guide · 6 min read</span>
          <h3><a href="blog-ayodhya-tour-package-price-itinerary-booking-guide.html">Ayodhya Tour Package 2026: Price, Itinerary, Hotels &amp; Cab Guide</a></h3>
          <p>Verified 2026 price breakdown from ₹1,499, detailed 1, 2, and 3-day itineraries, 3-star AC hotels near Ram Mandir, private AC cabs, and VIP darshan pass assistance.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-tour-package-price-itinerary-booking-guide.html" style="color:var(--saffron-deep);">Read Tour Package Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-tour-package-price-itinerary-booking-guide.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Ayodhya Tour Package card to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
