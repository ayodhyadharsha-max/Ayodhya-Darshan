#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_url = "https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html"
        if new_url not in content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            content = content.replace("</urlset>", url_entry + "</urlset>")
            print("✅ Added Senior Citizen Tour Package blog URL to sitemap.xml")

        # Update all lastmod dates to 2026-11-18
        content = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", "<lastmod>2026-11-18</lastmod>", content)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Updated all lastmod dates in sitemap.xml to 2026-11-18")

    # Also update Next.js public sitemap if present
    next_sitemap = "ayodhya-landing-main/public/sitemap.xml"
    if os.path.exists(next_sitemap):
        with open(next_sitemap, "r", encoding="utf-8") as f:
            n_content = f.read()
        if new_url not in n_content:
            url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
            n_content = n_content.replace("</urlset>", url_entry + "</urlset>")
        n_content = re.sub(r"<lastmod>2026-\d\d-\d\d</lastmod>", "<lastmod>2026-11-18</lastmod>", n_content)
        with open(next_sitemap, "w", encoding="utf-8") as f:
            f.write(n_content)
        print("✅ Updated Next.js public/sitemap.xml to 2026-11-18")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Ayodhya Tour Package for Senior Citizens 2026: Wheelchair, VIP Darshan, Hotels &amp; Price Guide</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html</guid>
      <description>Verified Ayodhya tour package for senior citizens &amp; elderly parents (from ₹4,999/person): Ram Mandir wheelchair &amp; golf cart assistance, VIP darshan passes, lift hotels &amp; private AC cabs.</description>
      <pubDate>Wed, 18 Nov 2026 15:30:00 +0530</pubDate>
    </item>
"""
    if "blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Senior Citizen guide to rss.xml")
    else:
        print("ℹ️ Guide already present in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Tour Package for Senior Citizens 2026 Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Elder Care Pilgrimage · 8 min read</span>
          <h3><a href="blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html">Ayodhya Tour Package for Senior Citizens 2026: Wheelchair &amp; VIP Darshan Guide</a></h3>
          <p>Verified 2026 prices (from ₹4,999), 2-day &amp; 3-day relaxed itineraries, Ram Mandir wheelchair &amp; battery golf cart assistance, accessible lift hotels, and pure sattvic meals.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html" style="color:var(--saffron-deep);">Read Senior Care Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)

        # Also add to schema blogPost list
        schema_entry = '    { "@type": "BlogPosting", "headline": "Ayodhya Tour Package for Senior Citizens 2026: Wheelchair, VIP Darshan, Hotels & Price Guide", "url": "https://www.ayodhyadharshan.com/blog-ayodhya-tour-package-for-senior-citizens-parents-guide.html" },\n'
        content = content.replace('"blogPost": [\n', '"blogPost": [\n' + schema_entry)

        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Senior Citizen card and Schema entry to blog.html")
    else:
        print("ℹ️ Card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
