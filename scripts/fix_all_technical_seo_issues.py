import os
import xml.etree.ElementTree as ET

repo_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# 1. Fix sitemap.xml
sitemap_path = os.path.join(repo_dir, 'sitemap.xml')

missing_pages_info = [
    ('prayagraj-tour-package.html', 'weekly', '0.9'),
    ('chitrakoot-tour-package.html', 'weekly', '0.9'),
    ('naimisharanya-tour-package.html', 'weekly', '0.9'),
    ('vindhyachal-tour-package.html', 'weekly', '0.9'),
    ('mathura-tour-package.html', 'weekly', '0.9'),
    ('vrindavan-tour-package.html', 'weekly', '0.9'),
    ('feedback.html', 'monthly', '0.5'),
    ('thankyou.html', 'monthly', '0.5'),
]

with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Update lastmod dates in sitemap to today
import re
sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-09-24</lastmod>', sitemap_content)

for page_file, freq, prio in missing_pages_info:
    url = f'https://www.ayodhyadharshan.com/{page_file}'
    if url not in sitemap_content:
        url_entry = f'''  <url>
    <loc>{url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
    <lastmod>2026-09-24</lastmod>
  </url>
'''
        sitemap_content = sitemap_content.replace('</urlset>', f'{url_entry}</urlset>')

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print("Updated sitemap.xml with missing URLs and latest lastmod dates.")

# 2. Fix Title in blog-ayodhya-tour-cost-budget-planner.html
blog_cost_path = os.path.join(repo_dir, 'blog-ayodhya-tour-cost-budget-planner.html')
if os.path.exists(blog_cost_path):
    with open(blog_cost_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<title>Ayodhya Jane Ka Kharcha: Complete Ayodhya Trip Cost & Budget Planner | Ayodhya Dharshan</title>',
                  '<title>Ayodhya Trip Cost Planner 2026: Ayodhya Jane Ka Kharcha | Ayodhya Dharshan</title>')
    with open(blog_cost_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed title length in blog-ayodhya-tour-cost-budget-planner.html")

# 3. Fix Meta Description in destinations.html
dest_path = os.path.join(repo_dir, 'destinations.html')
if os.path.exists(dest_path):
    with open(dest_path, 'r', encoding='utf-8') as f:
        c = f.read()
    old_desc = 'Explore sacred spiritual destinations in Uttar Pradesh — Ayodhya, Varanasi, Prayagraj, Chitrakoot, Naimisharanya, Vindhyachal, Mathura, and Vrindavan. Custom tour packages, VIP darshan passes, and AC transfers available.'
    new_desc = 'Explore top spiritual tour destinations in Uttar Pradesh including Ayodhya, Varanasi, Prayagraj, Chitrakoot, Mathura, Vrindavan, Vindhyachal & Naimisharanya.'
    c = c.replace(old_desc, new_desc)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed meta description length in destinations.html")

# 4. Fix OpenGraph & Schema in utility pages: feedback.html, privacy-policy.html, terms.html, thankyou.html
utility_pages = [
    {
        'file': 'feedback.html',
        'title': 'Pilgrim Feedback & Reviews | Ayodhya Dharshan',
        'desc': 'Share your feedback, reviews, and teerth yatra experiences with Ayodhya Dharshan. Help us serve pilgrims better.',
        'type': 'WebPage'
    },
    {
        'file': 'privacy-policy.html',
        'title': 'Privacy Policy | Ayodhya Dharshan Teerth Yatra',
        'desc': 'Privacy policy and data protection commitment for Ayodhya Dharshan pilgrims and website visitors.',
        'type': 'WebPage'
    },
    {
        'file': 'terms.html',
        'title': 'Terms & Conditions | Ayodhya Dharshan Teerth Yatra',
        'desc': 'Terms of service, package booking conditions, and cancellation policies for Ayodhya Dharshan yatra services.',
        'type': 'WebPage'
    },
    {
        'file': 'thankyou.html',
        'title': 'Thank You | Ayodhya Dharshan Teerth Yatra',
        'desc': 'Thank you for contacting Ayodhya Dharshan. Our Yatra Seva desk will get in touch with you shortly.',
        'type': 'WebPage'
    },
]

for util in utility_pages:
    f_path = os.path.join(repo_dir, util['file'])
    if not os.path.exists(f_path):
        continue

    with open(f_path, 'r', encoding='utf-8') as f:
        c = f.read()

    og_tags = f'''<meta property="og:type" content="website">
<meta property="og:site_name" content="Ayodhya Dharshan">
<meta property="og:title" content="{util['title']}">
<meta property="og:description" content="{util['desc']}">
<meta property="og:url" content="https://www.ayodhyadharshan.com/{util['file']}">
<meta property="og:image" content="https://www.ayodhyadharshan.com/assets/logo.webp">'''

    schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "{util['type']}",
  "name": "{util['title']}",
  "description": "{util['desc']}",
  "url": "https://www.ayodhyadharshan.com/{util['file']}"
}}
</script>'''

    # Inject OG tags before </head> if missing
    if 'og:title' not in c:
        c = c.replace('</head>', f'{og_tags}\n{schema}\n</head>')
    elif 'application/ld+json' not in c:
        c = c.replace('</head>', f'{schema}\n</head>')

    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Updated OpenGraph and Schema for {util['file']}")

