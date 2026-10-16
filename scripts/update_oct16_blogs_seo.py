import os, re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-16</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-gorakhpur-to-ayodhya-taxi-fare-cab-booking.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-16</lastmod>
  </url>
'''

if 'blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Refresh all lastmod timestamps to 2026-10-16
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-16</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with Oct 16 blog posts and 2026-10-16 timestamps!")

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Ram Mandir Locker Facility &amp; Mobile Rules (2026)</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html</guid>
      <description>Can you carry mobile phones inside Ayodhya Ram Mandir? Complete guide to free locker facility at Janmabhoomi Path, prohibited items, luggage deposit &amp; security rules.</description>
      <pubDate>Fri, 16 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Gorakhpur to Ayodhya Taxi Fare &amp; Cab Booking 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-gorakhpur-to-ayodhya-taxi-fare-cab-booking.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-gorakhpur-to-ayodhya-taxi-fare-cab-booking.html</guid>
      <description>Book Gorakhpur Airport (GOP) &amp; Railway Station to Ayodhya private AC cabs: Dzire from ₹2,499, Ertiga ₹3,799, Innova Crysta ₹4,899. Highway tolls &amp; GST included.</description>
      <pubDate>Fri, 16 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print("Updated rss.xml feed with today's 2 blog posts!")

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Ram Mandir Locker Facility & Mobile Deposit Rules" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Mandir Advisory · 5 min read</span>
          <h3><a href="blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html">Ayodhya Ram Mandir Locker Facility &amp; Mobile Rules (2026)</a></h3>
          <p>Where to deposit mobiles, smartwatches, bags and shoes at Janmabhoomi Path. Prohibited item list &amp; tips to save 45 minutes in locker lines.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html" style="color:var(--saffron-deep);">Read Locker Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-gorakhpur-to-ayodhya-taxi-fare-cab-booking.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Gorakhpur to Ayodhya Taxi Fare Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Airport & Station Transfer · 5 min read</span>
          <h3><a href="blog-gorakhpur-to-ayodhya-taxi-fare-cab-booking.html">Gorakhpur to Ayodhya Taxi Fare &amp; Cab Booking 2026</a></h3>
          <p>Verified AC cab rates for Dzire (₹2,499), Ertiga (₹3,799), and Innova Crysta from Gorakhpur Airport / Junction to Ram Mandir via NH27.</p>
          <a class="link-arrow bc-foot" href="blog-gorakhpur-to-ayodhya-taxi-fare-cab-booking.html" style="color:var(--saffron-deep);">Read Gorakhpur Cab Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-ram-mandir-locker-facility-mobile-deposit-rules.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print("Added today's 2 blog cards to blog.html!")
