#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html"
    if new_url not in content:
        url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
        content = content.replace("</urlset>", url_entry + "</urlset>")
        print("✅ Added new Deepotsav Drone Show blog URL to sitemap.xml")

    # Update all lastmod dates to 2026-10-28
    content = re.sub(r"<lastmod>2026-10-\d\d</lastmod>", "<lastmod>2026-10-28</lastmod>", content)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Updated all lastmod dates in sitemap.xml to 2026-10-28")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya Deepotsav 2026 Drone &amp; Laser Show: Timings, Free Spots &amp; Passes</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html</guid>
      <description>Ayodhya Deepotsav 2026 Mega Drone &amp; Laser Show: Ram Ki Paidi timings (7:15 PM, Nov 7), 2,000+ aerial drones, free viewing spots along Saryu Ghats &amp; VIP passes guide.</description>
      <pubDate>Wed, 28 Oct 2026 18:15:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Deepotsav Drone Show guide to rss.xml")
    else:
        print("ℹ️ Drone show guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html" class="bc-img"><img width="600" height="400" src="assets/reviews/ayodhya-night.jpg" alt="Ayodhya Deepotsav 2026 Drone Show and Laser Show at Ram Ki Paidi" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Deepotsav Special · 5 min read</span>
          <h3><a href="blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html">Ayodhya Deepotsav 2026 Drone &amp; Laser Show: Timings, Free Spots &amp; Passes</a></h3>
          <p>Ram Ki Paidi timings (Nov 7, 7:15 PM), 2,000+ synchronized aerial drones over River Saryu, 3D holographic laser show, free public viewing ghats, and cab packages.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html" style="color:var(--saffron-deep);">Read Drone Show Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-deepotsav-drone-laser-show-timings-viewing-spots.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Drone Show card to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
