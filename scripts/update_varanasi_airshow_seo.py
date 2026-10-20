#!/usr/bin/env python3
import os
import re

def update_sitemap():
    sitemap_path = "sitemap.xml"
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_url = "https://www.ayodhyadharshan.com/blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html"
    if new_url not in content:
        url_entry = f"""  <url>
    <loc>{new_url}</loc>
    <lastmod>2026-10-20</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
        content = content.replace("</urlset>", url_entry + "</urlset>")
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Varanasi Air Show guide to sitemap.xml")
    else:
        print("ℹ️ Varanasi Air Show URL already in sitemap.xml")

def update_rss():
    rss_path = "rss.xml"
    with open(rss_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_item = """    <item>
      <title>Varanasi Air Show 2026: Wings Over Ganges Dates, Namo Ghat Timings &amp; Free Entry Guide</title>
      <link>https://www.ayodhyadharshan.com/blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html</guid>
      <description>Complete spectator and travel guide to Indian Air Force mega air show 'Wings Over Ganges' at Namo Ghat, Varanasi: Oct 22-25 schedule, Rafale, Surya Kiran flypasts, best viewing ghats &amp; Ayodhya cab transfers.</description>
      <pubDate>Tue, 20 Oct 2026 15:15:00 +0530</pubDate>
    </item>
"""
    if "blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html" not in content:
        content = content.replace("<channel>\n", "<channel>\n" + new_item)
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Varanasi Air Show guide to rss.xml")
    else:
        print("ℹ️ Varanasi Air Show guide already in rss.xml")

def update_blog_html():
    blog_path = "blog.html"
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_card = """      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Air Show Wings Over Ganges at Namo Ghat 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Breaking Event Guide · 5 min read</span>
          <h3><a href="blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html">Varanasi Air Show 2026: Wings Over Ganges Dates, Timings &amp; Free Entry</a></h3>
          <p>Indian Air Force mega aerial display at Namo Ghat &amp; Ganga Riverfront: Oct 22-25 schedule, Rafale &amp; Surya Kiran aerobatics, top 6 viewing ghats, and Ayodhya to Varanasi cab transfers.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html" style="color:var(--saffron-deep);">Read Air Show Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""
    if "blog-varanasi-air-show-wings-over-ganges-namo-ghat-guide.html" not in content:
        target = '<div class="blog-grid">\n'
        content = content.replace(target, target + new_card)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Added Varanasi Air Show card to blog.html")
    else:
        print("ℹ️ Varanasi Air Show card already in blog.html")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
