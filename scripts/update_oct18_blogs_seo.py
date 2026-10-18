import os, re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Update sitemap.xml
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_urls = '''  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-18</lastmod>
  </url>
  <url>
    <loc>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-prasad-online-booking-guide.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <lastmod>2026-10-18</lastmod>
  </url>
'''

if 'blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', f'{new_urls}</urlset>')

# Refresh all lastmod timestamps to 2026-10-18
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-18</lastmod>', sitemap_content)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with Oct 18 blog posts and 2026-10-18 timestamps!")

# 2. Update rss.xml
rss_path = os.path.join(base_dir, 'rss.xml')
with open(rss_path, 'r', encoding='utf-8') as f:
    rss_content = f.read()

new_rss_items = '''    <item>
      <title>Ayodhya Ram Mandir Senior Citizen &amp; Wheelchair Guide 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html</guid>
      <description>Visiting Ayodhya Ram Mandir with elderly parents? Complete 2026 guide to free wheelchairs, battery golf carts, ramp corridors, Sugam Darshan passes &amp; medical aid.</description>
      <pubDate>Sun, 18 Oct 2026 00:00:00 +0530</pubDate>
    </item>
    <item>
      <title>Ayodhya Ram Mandir Prasad Booking &amp; Counter Guide 2026</title>
      <link>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-prasad-online-booking-guide.html</link>
      <guid>https://www.ayodhyadharshan.com/blog-ayodhya-ram-mandir-prasad-online-booking-guide.html</guid>
      <description>Looking for authentic Ayodhya Ram Mandir Prasad? Complete 2026 guide to Trust counter rates, home delivery facts, fraud warnings &amp; pure desi ghee laddoo prasad.</description>
      <pubDate>Sun, 18 Oct 2026 00:00:00 +0530</pubDate>
    </item>
'''

if 'blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html' not in rss_content:
    rss_content = rss_content.replace('<channel>', f'<channel>\n{new_rss_items}', 1)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
print("Updated rss.xml feed with today's 2 blog posts!")

# 3. Add blog cards to blog.html
blog_path = os.path.join(base_dir, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_content = f.read()

new_cards = '''      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Ram Mandir Senior Citizen Wheelchair Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Elderly Care Guide · 5 min read</span>
          <h3><a href="blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html">Ayodhya Ram Mandir Senior Citizen &amp; Wheelchair Guide 2026</a></h3>
          <p>Complete guide to free wheelchairs, electric golf carts on Janmabhoomi Path, elevator lifts, ramp corridors, and escorted yatra packages for elderly parents.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html" style="color:var(--saffron-deep);">Read Senior Care Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <article class="card blog-card" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-ram-mandir-prasad-online-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ram-mandir.webp" alt="Ayodhya Ram Mandir Prasad Booking & Counter Guide" loading="lazy"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Holy Offerings Guide · 5 min read</span>
          <h3><a href="blog-ayodhya-ram-mandir-prasad-online-booking-guide.html">Ayodhya Ram Mandir Prasad Booking &amp; Counter Guide 2026</a></h3>
          <p>Verified Trust counter rates for pure cow ghee besan laddoos, free elaichi dana, caution against online delivery scams, and airport packaging tips.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-ram-mandir-prasad-online-booking-guide.html" style="color:var(--saffron-deep);">Read Prasad Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
'''

if 'blog-ayodhya-ram-mandir-senior-citizen-wheelchair-guide.html' not in blog_content:
    blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{new_cards}', 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(blog_content)
print("Added today's 2 blog cards to blog.html!")
