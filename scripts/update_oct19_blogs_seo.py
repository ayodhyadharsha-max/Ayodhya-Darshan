import os, re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-19</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-varanasi-to-ayodhya-taxi-fare-travel-comparison.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-19</lastmod>
  </url>
'''

if 'blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Refresh all lastmod timestamps to 2026-10-19
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-19</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with Oct 19 blog posts and 2026-10-19 timestamps!")

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Ram Mandir Offline Aarti Pass &amp; Counter Guide 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html</guid>
      <description>Online slots full? Complete 2026 guide on how to get Ayodhya Ram Mandir Offline Aarti Passes: counter locations at Ram Katha Camp, opening timings &amp; Aadhaar rules.</description>
      <pubDate>Mon, 19 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Varanasi to Ayodhya Taxi Fare, Cab &amp; Travel Guide (2026)</title>
      <link>https://www.ayodhyadharshan.com/blog-varanasi-to-ayodhya-taxi-fare-travel-comparison.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-varanasi-to-ayodhya-taxi-fare-travel-comparison.html</guid>
      <description>What is the taxi fare from Varanasi (Kashi) to Ayodhya Ram Mandir? Compare 2026 AC cab rates (Dzire ₹3,499, Ertiga ₹4,899, Innova Crysta), Vande Bharat &amp; travel times.</description>
      <pubDate>Mon, 19 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print("Updated rss.xml feed with today's 2 blog posts!")

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Ram Mandir Offline Aarti Pass Guide 2026" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Pass Advisory · 5 min read</span>
          <h3><a href="blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html">Ayodhya Ram Mandir Offline Aarti Pass &amp; Counter Guide 2026</a></h3>
          <p>Online quota full? Verified guide on Ram Katha Camp offline pass counters, opening queue timings, Aadhaar verification rules, and Sugam Darshan tips.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html" style="color:var(--saffron-deep);">Read Offline Pass Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-to-ayodhya-taxi-fare-travel-comparison.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Varanasi to Ayodhya Taxi Fare & Travel Comparison Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Intercity Cab Guide · 5 min read</span>
          <h3><a href="blog-varanasi-to-ayodhya-taxi-fare-travel-comparison.html">Varanasi to Ayodhya Taxi Fare, Cab &amp; Travel Guide (2026)</a></h3>
          <p>Verified AC cab rates for Dzire (₹3,499), Ertiga (₹4,899), and Innova Crysta from Varanasi hotels/Ghats to Ram Mandir vs Vande Bharat train comparison.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-to-ayodhya-taxi-fare-travel-comparison.html" style="color:var(--saffron-deep);">Read Varanasi Cab Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-ram-mandir-offline-aarti-pass-counter-guide.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print("Added today's 2 blog cards to blog.html!")
