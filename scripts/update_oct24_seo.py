#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html"
    if new_url not in content:
        url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-24</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
        content = content.replace("</urlset>", url_entry + "</urlset>")
        print("✅ Added new Parikrama blog URL to sitemap.xml")

    # Update all lastmod dates to 2026-10-24
    content = re.sub(r"<lastmod>2026-10-\d\d</lastmod>", "<lastmod>2026-10-24</lastmod>", content)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Updated all lastmod dates in sitemap.xml to 2026-10-24")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026: Dates, Route &amp; Guide</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html</guid>
      <description>Official Ayodhya 14 Kosi (Nov 18-19) &amp; 5 Kosi (Nov 20-21) Parikrama 2026 dates, 45 km &amp; 15 km route maps, Saryu snan muhurat &amp; yatra tour packages.</description>
      <pubDate>Sat, 24 Oct 2026 14:20:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Parikrama guide to rss.xml")
    else:
        print("ℹ️ Parikrama guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya 14 Kosi and 5 Kosi Parikrama 2026 Dates and Route Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Kartik Mela Special · 6 min read</span>
          <h3><a href="blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html">Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026: Dates, Route &amp; Guide</a></h3>
          <p>Official 14 Kosi (45 km, Nov 18-19) and 5 Kosi (15 km, Nov 20-21) Parikrama dates, Panchang muhurat, route maps from Naya Ghat to Guptar Ghat, and hotel yatra packages.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html" style="color:var(--saffron-deep);">Read Parikrama Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-14-kosi-5-kosi-parikrama-2026-dates-route-guide.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Parikrama card to blog.html")
    else:
        print("ℹ️ Parikrama card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
