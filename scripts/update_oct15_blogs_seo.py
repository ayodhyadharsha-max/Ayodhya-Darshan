import os, re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-winter-travel-guide-darshan-timings.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-15</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-to-chitrakoot-distance-taxi-fare.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-15</lastmod>
  </url>
'''

if 'blog-ayodhya-winter-travel-guide-darshan-timings.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Update all lastmod timestamps to 2026-10-15
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-15</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with today's 2 blog posts and 2026-10-15 timestamps!")

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Ram Mandir Winter Travel Guide (2026–2027): Timings &amp; Tips</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-winter-travel-guide-darshan-timings.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-winter-travel-guide-darshan-timings.html</guid>
      <description>Planning a winter trip to Ayodhya Ram Mandir? Check revised winter darshan timings, morning Mangala Aarti passes, warm hotel bookings, fog travel advisory &amp; cab fares.</description>
      <pubDate>Thu, 15 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Ayodhya to Chitrakoot Distance, Route &amp; Taxi Fare (2026)</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-to-chitrakoot-distance-taxi-fare.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-to-chitrakoot-distance-taxi-fare.html</guid>
      <description>What is the distance from Ayodhya to Chitrakoot? Check 2026 highway driving routes, travel time, AC cab fares for Dzire, Ertiga, Innova Crysta &amp; yatra itinerary.</description>
      <pubDate>Thu, 15 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-winter-travel-guide-darshan-timings.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print("Updated rss.xml feed with today's 2 blog posts!")

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-winter-travel-guide-darshan-timings.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Ram Mandir Winter Travel Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Winter Pilgrimage Guide · 5 min read</span>
          <h3><a href="blog-ayodhya-winter-travel-guide-darshan-timings.html">Ayodhya Ram Mandir Winter Travel Guide (2026–2027): Timings &amp; Tips</a></h3>
          <p>Revised winter Mangala &amp; Shringar Aarti hours, fog advisory for morning trains, heated 3-star stays, and senior citizen darshan essentials.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-winter-travel-guide-darshan-timings.html" style="color:var(--saffron-deep);">Read Winter Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-to-chitrakoot-distance-taxi-fare.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya to Chitrakoot Distance & Taxi Fare 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Ramayana Circuit Guide · 6 min read</span>
          <h3><a href="blog-ayodhya-to-chitrakoot-distance-taxi-fare.html">Ayodhya to Chitrakoot Distance, Route &amp; Taxi Fare (2026)</a></h3>
          <p>Complete 260 km highway guide via Sultanpur/Prayagraj: verified AC cab fares for Dzire (₹4,499), Ertiga (₹5,999), Innova Crysta, and Kamadgiri Parikrama.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-to-chitrakoot-distance-taxi-fare.html" style="color:var(--saffron-deep);">Read Chitrakoot Cab Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-winter-travel-guide-darshan-timings.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print("Added today's 2 blog cards to blog.html!")
