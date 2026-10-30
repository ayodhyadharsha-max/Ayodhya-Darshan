#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html"
    if new_url not in content:
        url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-29</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
        content = content.replace("</urlset>", url_entry + "</urlset>")
        print("✅ Added new Deepotsav Traffic blog URL to sitemap.xml")

    # Update all lastmod dates to 2026-10-29
    content = re.sub(r"<lastmod>2026-10-\d\d</lastmod>", "<lastmod>2026-10-29</lastmod>", content)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Updated all lastmod dates in sitemap.xml to 2026-10-29")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya Deepotsav 2026 Traffic Advisory: Parking &amp; Cab Routes</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html</guid>
      <description>Official Ayodhya Deepotsav 2026 Traffic Advisory: NH-27 highway diversions, Saket &amp; Tedhi Bazar zero-vehicle zones, satellite parking spots &amp; cab drop points.</description>
      <pubDate>Thu, 29 Oct 2026 14:15:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Deepotsav Traffic guide to rss.xml")
    else:
        print("ℹ️ Guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Deepotsav 2026 Traffic Advisory and Parking Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Deepotsav Travel Advisory · 5 min read</span>
          <h3><a href="blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html">Ayodhya Deepotsav 2026 Traffic Advisory: Road Diversions &amp; Parking Guide</a></h3>
          <p>Official road restrictions, Saket &amp; Tedhi Bazar zero-vehicle zones, 12 satellite parking lots, NH-27 bypass diversions, and authorized cab drop-off points.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html" style="color:var(--saffron-deep);">Read Traffic Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-deepotsav-traffic-advisory-parking-routes.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Traffic Guide card to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
