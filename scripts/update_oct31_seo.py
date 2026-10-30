#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_url = "https://www.ayodhyadharshan.com/blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html"
        if new_url not in content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-31</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            content = content.replace("</urlset>", url_entry + "</urlset>")
            print("✅ Added Dev Deepawali 2026 blog URL to sitemap.xml")

        # Update all lastmod dates to 2026-10-31
        content = re.sub(r"<lastmod>2026-10-\d\d</lastmod>", "<lastmod>2026-10-31</lastmod>", content)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Updated all lastmod dates in sitemap.xml to 2026-10-31")

    # Also update Next.js public sitemap if present
    next_sitemap = "ayodhya-landing-main/public/sitemap.xml"
    if os.path.exists(next_sitemap):
        with open(next_sitemap, "r", encoding="utf-8") as f:
            n_content = f.read()
        if new_url not in n_content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-31</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            n_content = n_content.replace("</urlset>", url_entry + "</urlset>")
        n_content = re.sub(r"<lastmod>2026-10-\d\d</lastmod>", "<lastmod>2026-10-31</lastmod>", n_content)
        with open(next_sitemap, "w", encoding="utf-8") as f:
            f.write(n_content)
        print("✅ Updated Next.js public/sitemap.xml to 2026-10-31")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Varanasi Dev Deepawali 2026: Official Dates, Boat Booking &amp; Laser Show Schedule</title>
      <link>https://www.ayodhyadharshan.com/blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html</guid>
      <description>Varanasi Dev Deepawali 2026 confirmed Kartik Purnima date (Nov 24), 84-ghat lighting schedule, Chet Singh Ghat 3D laser show timings, Ganga boat booking price rates, traffic advisory, and combined Ayodhya Varanasi tour packages.</description>
      <pubDate>Sat, 31 Oct 2026 10:00:00 +0530</pubDate>
    </item>
"""
    if "blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Dev Deepawali guide to rss.xml")
    else:
        print("ℹ️ Guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html" class="bc-img"><img width="600" height="400" src="assets/reviews/ayodhya-night.jpg" alt="Varanasi Dev Deepawali 2026 Boat Booking and Ghat Lighting" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Festival Special · 7 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html">Varanasi Dev Deepawali 2026: Dates, Boat Booking &amp; Laser Show Schedule</a></h3>
          <p>Confirmed Kartik Purnima schedule (Nov 24, 2026), 84-ghat lighting with 12+ lakh diyas, Chet Singh Ghat 3D laser show, boat booking rate matrix, traffic advisory, and combined Ayodhya-Varanasi tour packages.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html" style="color:var(--saffron-deep);">Read Dev Deepawali Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)

        # Also add to schema blogPost list
        schema_entry = '    { "@type": "BlogPosting", "headline": "Varanasi Dev Deepawali 2026: Official Dates, Boat Booking & Laser Show Schedule", "url": "https://www.ayodhyadharshan.com/blog-varanasi-dev-deepawali-2026-dates-boat-booking-laser-show-schedule.html" },\n'
        content = content.replace('"blogPost": [\n', '"blogPost": [\n' + schema_entry)

        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Dev Deepawali card and Schema entry to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
