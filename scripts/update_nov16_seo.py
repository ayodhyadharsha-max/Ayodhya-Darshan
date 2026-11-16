#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html"
        if new_url not in content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-11-16</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            content = content.replace("</urlset>", url_entry + "</urlset>")
            print("✅ Added Parikrama Traffic Advisory blog URL to sitemap.xml")

        # Update all lastmod dates to 2026-11-16
        content = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", "<lastmod>2026-11-16</lastmod>", content)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Updated all lastmod dates in sitemap.xml to 2026-11-16")

    # Also update Next.js public sitemap if present
    next_sitemap = "ayodhya-landing-main/public/sitemap.xml"
    if os.path.exists(next_sitemap):
        with open(next_sitemap, "r", encoding="utf-8") as f:
            n_content = f.read()
        if new_url not in n_content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-11-16</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            n_content = n_content.replace("</urlset>", url_entry + "</urlset>")
        n_content = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", "<lastmod>2026-11-16</lastmod>", n_content)
        with open(next_sitemap, "w", encoding="utf-8") as f:
            f.write(n_content)
        print("✅ Updated Next.js public/sitemap.xml to 2026-11-16")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026 Traffic Advisory: Road Diversions &amp; 16 Parking Zones</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html</guid>
      <description>Official Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026 Traffic Advisory: NH-27 highway diversions, entry ban dates (Nov 17-21), 16 satellite parking lots, EV shuttle routes &amp; cab drop points.</description>
      <pubDate>Mon, 16 Nov 2026 21:45:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Parikrama Traffic Advisory guide to rss.xml")
    else:
        print("ℹ️ Guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Parikrama 2026 Traffic Advisory and Parking Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Parikrama Traffic Advisory · 8 min read</span>
          <h3><a href="blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html">Ayodhya 14 Kosi &amp; 5 Kosi Parikrama 2026 Traffic Advisory: Road Diversions &amp; 16 Parking Zones</a></h3>
          <p>Official road restrictions, NH-27 diversions, entry ban dates (Nov 17-21), 16 satellite parking lots, zero-vehicle zones, EV shuttle buggies, and authorized tour cab drop points.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html" style="color:var(--saffron-deep);">Read Traffic Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)

        # Also add to schema blogPost list
        schema_entry = '    { "@type": "BlogPosting", "headline": "Ayodhya 14 Kosi & 5 Kosi Parikrama 2026 Traffic Advisory: Road Diversions & 16 Parking Zones", "url": "https://www.ayodhyadharshan.com/blog-ayodhya-14-kosi-parikrama-traffic-advisory-parking-routes.html" },\n'
        content = content.replace('"blogPost": [\n', '"blogPost": [\n' + schema_entry)

        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Parikrama Traffic Advisory card and Schema entry to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
