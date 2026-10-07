import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-07</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-electric-bus-routes-fare-timings.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-07</lastmod>
  </url>
'''

if 'blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Update all lastmod dates to 2026-10-07 in sitemap
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-07</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print('Updated sitemap.xml with today\'s 2 viral blog posts!')

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Airport to Ram Mandir Distance &amp; Cab Fare (2026)</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html</guid>
      <description>Complete travel guide for Maharishi Valmiki Ayodhya Airport (AYJ) to Ram Mandir: distance, travel time, AC taxi fares, e-bus routes, and hotel pickup tips.</description>
      <pubDate>Wed, 07 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Ayodhya Electric Bus Routes, Fare &amp; Timings (2026)</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-electric-bus-routes-fare-timings.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-electric-bus-routes-fare-timings.html</guid>
      <description>Official guide to Ayodhya City Electric Bus services: routes connecting Ayodhya Airport, Ram Mandir, Ayodhya Dham station, Saryu Aarti, fare list, and timings.</description>
      <pubDate>Wed, 07 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print('Updated rss.xml feed!')

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Airport to Ram Mandir Distance & Cab Fare Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Airport &amp; Cab Guide · 5 min read</span>
          <h3><a href="blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html">Ayodhya Airport to Ram Mandir Distance &amp; Cab Fare (2026)</a></h3>
          <p>Distance breakdown, AC taxi fares, e-bus routes, and terminal pickup tips from Maharishi Valmiki Airport (AYJ) to Shri Ram Janmabhoomi.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html" style="color:var(--saffron-deep);">Read Airport Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-electric-bus-routes-fare-timings.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Electric Bus Routes, Fare & Timings 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Local Transport Guide · 4 min read</span>
          <h3><a href="blog-ayodhya-electric-bus-routes-fare-timings.html">Ayodhya Electric Bus Routes, Fare &amp; Timings (2026)</a></h3>
          <p>UPSRTC AC electric bus ticket prices, routes connecting Ayodhya Station, Airport, Ram Mandir, and Saryu Aarti ghats.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-electric-bus-routes-fare-timings.html" style="color:var(--saffron-deep);">Read E-Bus Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-airport-to-ram-mandir-distance-taxi-fare.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print('Added viral blog cards to blog.html!')
