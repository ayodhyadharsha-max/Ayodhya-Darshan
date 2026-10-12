import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-12</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-to-prayagraj-taxi-fare-cab-booking.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-12</lastmod>
  </url>
'''

if 'blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Update all lastmod dates to 2026-10-12
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-12</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print('Updated sitemap.xml with Oct 12 blog posts and fresh lastmod dates!')

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Deepotsav 2026 Dates, Schedule &amp; VIP Passes</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html</guid>
      <description>Official Ayodhya Deepotsav 2026 dates, full event schedule, Ram Ki Paidi diya lighting, laser show timings, VIP entry passes, and guided yatra packages.</description>
      <pubDate>Mon, 12 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Ayodhya to Prayagraj Taxi Fare: AC Cab Booking 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-to-prayagraj-taxi-fare-cab-booking.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-to-prayagraj-taxi-fare-cab-booking.html</guid>
      <description>What is the taxi fare from Ayodhya to Prayagraj Triveni Sangam? Check verified 2026 cab rates for Dzire, Ertiga, Innova, route map via NH330, and book on WhatsApp.</description>
      <pubDate>Mon, 12 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print('Updated rss.xml feed!')

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Deepotsav 2026 Dates & Passes Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Festival Yatra Guide · 6 min read</span>
          <h3><a href="blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html">Ayodhya Deepotsav 2026 Dates, Schedule &amp; VIP Passes</a></h3>
          <p>Official schedule for 25+ lakh Diya lighting at Ram Ki Paidi, laser show, Pushpak Viman coronation, and festival tour packages.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html" style="color:var(--saffron-deep);">Read Deepotsav Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-to-prayagraj-taxi-fare-cab-booking.html" class="bc-img"><img width="600" height="400" src="assets/destinations/triveni-sangam.webp" alt="Ayodhya to Prayagraj Taxi Fare Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Cab Fare Guide · 5 min read</span>
          <h3><a href="blog-ayodhya-to-prayagraj-taxi-fare-cab-booking.html">Ayodhya to Prayagraj Taxi Fare: AC Cab Booking 2026</a></h3>
          <p>Verified cab rates for Dzire (₹2,800), Ertiga (₹4,200), and Innova Crysta for Triveni Sangam Snan and temple drop.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-to-prayagraj-taxi-fare-cab-booking.html" style="color:var(--saffron-deep);">Read Cab Fare Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-deepotsav-2026-dates-schedule-passes-guide.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print('Added Oct 12 blog cards to blog.html!')
