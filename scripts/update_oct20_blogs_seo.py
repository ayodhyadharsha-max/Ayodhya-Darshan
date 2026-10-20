import os, re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-photography-camera-drone-rules.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-20</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-prayagraj-to-ayodhya-taxi-fare-cab-booking.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-20</lastmod>
  </url>
'''

if 'blog-ayodhya-ram-mandir-photography-camera-drone-rules.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Refresh all lastmod timestamps to 2026-10-20
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-20</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with Oct 20 blog posts and 2026-10-20 timestamps!")

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Ram Mandir Photography, Camera &amp; Drone Rules (2026)</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-photography-camera-drone-rules.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-photography-camera-drone-rules.html</guid>
      <description>Can you take cameras or mobile phones inside Ayodhya Ram Mandir? Official 2026 rules on DSLR, GoPro, drone flying permissions, red zones &amp; top photo spots in Ayodhya.</description>
      <pubDate>Tue, 20 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Prayagraj to Ayodhya Taxi Fare &amp; Cab Booking 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-prayagraj-to-ayodhya-taxi-fare-cab-booking.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-prayagraj-to-ayodhya-taxi-fare-cab-booking.html</guid>
      <description>What is the taxi fare from Prayagraj to Ayodhya Ram Mandir? Check verified 2026 rates for Dzire (₹2,899), Ertiga (₹4,199), Innova Crysta, travel time &amp; direct cabs.</description>
      <pubDate>Tue, 20 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-ram-mandir-photography-camera-drone-rules.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print("Updated rss.xml feed with today's 2 blog posts!")

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-ram-mandir-photography-camera-drone-rules.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Ram Mandir Photography and Drone Rules 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Photography Advisory · 5 min read</span>
          <h3><a href="blog-ayodhya-ram-mandir-photography-camera-drone-rules.html">Ayodhya Ram Mandir Photography, Camera &amp; Drone Rules (2026)</a></h3>
          <p>Official rules on DSLR, GoPro, red-zone drone restrictions, security locker deposit, and top 6 legal photography spots across Ayodhya Dham.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-ram-mandir-photography-camera-drone-rules.html" style="color:var(--saffron-deep);">Read Camera Rules Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-prayagraj-to-ayodhya-taxi-fare-cab-booking.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Prayagraj to Ayodhya Taxi Fare Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Intercity Cab Guide · 5 min read</span>
          <h3><a href="blog-prayagraj-to-ayodhya-taxi-fare-cab-booking.html">Prayagraj to Ayodhya Taxi Fare &amp; Cab Booking 2026</a></h3>
          <p>Verified AC cab rates for Dzire (₹2,899), Ertiga (₹4,199), and Innova Crysta from Triveni Sangam / Junction to Ram Mandir via NH330.</p>
          <a class="link-arrow bc-foot" href="blog-prayagraj-to-ayodhya-taxi-fare-cab-booking.html" style="color:var(--saffron-deep);">Read Prayagraj Cab Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-ram-mandir-photography-camera-drone-rules.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print("Added today's 2 blog cards to blog.html!")
