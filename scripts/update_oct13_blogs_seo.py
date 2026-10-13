import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-dharamshala-booking-online-price-list.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-13</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-lucknow-airport-to-ayodhya-taxi-fare-cab-booking.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-13</lastmod>
  </url>
'''

if 'blog-ayodhya-dharamshala-booking-online-price-list.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Refresh all lastmod timestamps to 2026-10-13
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-13</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print('Updated sitemap.xml with Oct 13 blog posts and fresh lastmod dates!')

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Dharamshala Online Booking: List &amp; Rates 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-dharamshala-booking-online-price-list.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-dharamshala-booking-online-price-list.html</guid>
      <description>Verified 2026 price list and booking guide for top dharamshalas in Ayodhya near Shri Ram Janmabhoomi Mandir. AC rooms, family suites &amp; dormitories.</description>
      <pubDate>Tue, 13 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Lucknow Airport to Ayodhya Taxi Fare &amp; Cab Booking 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-lucknow-airport-to-ayodhya-taxi-fare-cab-booking.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-lucknow-airport-to-ayodhya-taxi-fare-cab-booking.html</guid>
      <description>Book Lucknow Airport (LKO) to Ayodhya private AC cabs: Dzire from ₹2,499, Ertiga ₹3,800, Innova Crysta ₹4,900. Flight pickup, highway tolls included.</description>
      <pubDate>Tue, 13 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-dharamshala-booking-online-price-list.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print('Updated rss.xml feed with today\'s blog posts!')

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-dharamshala-booking-online-price-list.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Dharamshala Online Booking Rates 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Accommodation Guide · 6 min read</span>
          <h3><a href="blog-ayodhya-dharamshala-booking-online-price-list.html">Ayodhya Dharamshala Online Booking: List &amp; Rates 2026</a></h3>
          <p>Verified list of top dharamshalas near Ram Mandir: Gujarati, Birla, Kanak Bhawan, room tariffs, and booking assistance.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-dharamshala-booking-online-price-list.html" style="color:var(--saffron-deep);">Read Dharamshala Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-lucknow-airport-to-ayodhya-taxi-fare-cab-booking.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Lucknow Airport to Ayodhya Taxi Fare Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Airport Transfer Guide · 5 min read</span>
          <h3><a href="blog-lucknow-airport-to-ayodhya-taxi-fare-cab-booking.html">Lucknow Airport to Ayodhya Taxi Fare &amp; Cab Booking 2026</a></h3>
          <p>Verified cab rates for Dzire (₹2,499), Ertiga (₹3,799), and Innova Crysta from Lucknow CCS Airport to Ram Mandir.</p>
          <a class="link-arrow bc-foot" href="blog-lucknow-airport-to-ayodhya-taxi-fare-cab-booking.html" style="color:var(--saffron-deep);">Read Airport Cab Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-dharamshala-booking-online-price-list.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print('Added Oct 13 blog cards to blog.html!')
