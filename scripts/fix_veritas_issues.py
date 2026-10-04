import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# Internal linking block HTML to be inserted before <footer>
internal_links_html = '''
<!-- ===== SACRED YATRA CIRCUITS & GUIDES FOOTER NAV ===== -->
<section class="bg-amber-950 text-amber-100 py-10 border-t border-amber-800/60" style="background:#2C0B0E; color:#fde68a; padding:40px 20px; font-family:sans-serif; font-size:14px; line-height:1.6;">
  <div style="max-width:1200px; margin:0 auto; display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:24px;">
    <div>
      <h4 style="color:#fbbf24; font-weight:700; font-size:16px; margin-bottom:12px; border-bottom:1px solid #78350f; padding-bottom:6px;">Sacred Yatra Packages</h4>
      <ul style="list-style:none; padding:0; margin:0;">
        <li><a href="ayodhya-dharshan-tour-package.html" style="color:#fef08a; text-decoration:none;">Ayodhya Tour Package</a></li>
        <li><a href="ayodhya-same-day-tour.html" style="color:#fef08a; text-decoration:none;">Ayodhya Same Day Tour</a></li>
        <li><a href="ayodhya-varanasi-tour-package.html" style="color:#fef08a; text-decoration:none;">Ayodhya Varanasi Tour Package</a></li>
        <li><a href="ayodhya-prayagraj-tour-package.html" style="color:#fef08a; text-decoration:none;">Ayodhya Prayagraj Package</a></li>
        <li><a href="ayodhya-prayagraj-varanasi-tour-package.html" style="color:#fef08a; text-decoration:none;">Ayodhya Kashi Prayagraj Yatra</a></li>
        <li><a href="full-ramayana-circuit-tour-package.html" style="color:#fef08a; text-decoration:none;">Full Ramayana Circuit Package</a></li>
      </ul>
    </div>
    <div>
      <h4 style="color:#fbbf24; font-weight:700; font-size:16px; margin-bottom:12px; border-bottom:1px solid #78350f; padding-bottom:6px;">Regional Tour Packages</h4>
      <ul style="list-style:none; padding:0; margin:0;">
        <li><a href="delhi-to-ayodhya-tour-package.html" style="color:#fef08a; text-decoration:none;">Delhi to Ayodhya Package</a></li>
        <li><a href="mumbai-to-ayodhya-tour-package.html" style="color:#fef08a; text-decoration:none;">Mumbai to Ayodhya Package</a></li>
        <li><a href="bengaluru-to-ayodhya-tour-package.html" style="color:#fef08a; text-decoration:none;">Bangalore to Ayodhya Package</a></li>
        <li><a href="kolkata-to-ayodhya-tour-package.html" style="color:#fef08a; text-decoration:none;">Kolkata to Ayodhya Package</a></li>
        <li><a href="chennai-to-ayodhya-tour-package.html" style="color:#fef08a; text-decoration:none;">Chennai to Ayodhya Package</a></li>
        <li><a href="hyderabad-to-ayodhya-tour-package.html" style="color:#fef08a; text-decoration:none;">Hyderabad to Ayodhya Package</a></li>
      </ul>
    </div>
    <div>
      <h4 style="color:#fbbf24; font-weight:700; font-size:16px; margin-bottom:12px; border-bottom:1px solid #78350f; padding-bottom:6px;">Other Sacred Destinations</h4>
      <ul style="list-style:none; padding:0; margin:0;">
        <li><a href="varanasi-same-day-tour-package.html" style="color:#fef08a; text-decoration:none;">Varanasi Same Day Tour</a></li>
        <li><a href="prayagraj-tour-package.html" style="color:#fef08a; text-decoration:none;">Prayagraj Sangam Tour</a></li>
        <li><a href="chitrakoot-tour-package.html" style="color:#fef08a; text-decoration:none;">Chitrakoot Dham Package</a></li>
        <li><a href="naimisharanya-tour-package.html" style="color:#fef08a; text-decoration:none;">Naimisharanya Package</a></li>
        <li><a href="vindhyachal-tour-package.html" style="color:#fef08a; text-decoration:none;">Vindhyachal Devi Package</a></li>
        <li><a href="vrindavan-tour-package.html" style="color:#fef08a; text-decoration:none;">Mathura Vrindavan Package</a></li>
      </ul>
    </div>
    <div>
      <h4 style="color:#fbbf24; font-weight:700; font-size:16px; margin-bottom:12px; border-bottom:1px solid #78350f; padding-bottom:6px;">Yatra Travel Guides</h4>
      <ul style="list-style:none; padding:0; margin:0;">
        <li><a href="blog-ram-mandir-vip-pass-booking-guide.html" style="color:#fef08a; text-decoration:none;">Ram Mandir VIP Pass Guide</a></li>
        <li><a href="blog-saryu-ghat-aarti-timings-ayodhya-guide.html" style="color:#fef08a; text-decoration:none;">Saryu Aarti Timings Guide</a></li>
        <li><a href="blog-kashi-vishwanath-sugam-darshan-guide.html" style="color:#fef08a; text-decoration:none;">Kashi Sugam Darshan Guide</a></li>
        <li><a href="blog-mathura-vrindavan-vip-darshan-guide.html" style="color:#fef08a; text-decoration:none;">Banke Bihari VIP Pass Guide</a></li>
        <li><a href="blog-faizabad-to-varanasi-distance-travel-guide.html" style="color:#fef08a; text-decoration:none;">Faizabad to Varanasi Distance</a></li>
        <li><a href="yatra-cost-calculator.html" style="color:#fef08a; text-decoration:none;">Yatra Cost Calculator</a></li>
      </ul>
    </div>
  </div>
</section>
'''

updated_count = 0
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Trim og:title if over 58 chars
    def trim_og_title(m):
        val = m.group(1)
        if len(val) > 58:
            new_val = val[:55].rstrip() + '...'
            return f'<meta property="og:title" content="{new_val}">'
        return m.group(0)

    new_content = re.sub(r'<meta\s+property=[\"\']og:title[\"\']\s+content=[\"\'](.*?)[\"\']\s*\/?>', trim_og_title, content)
    if new_content != content:
        content = new_content
        modified = True

    # 2. Add Twitter card tags if missing
    if 'name="twitter:card"' not in content and "name='twitter:card'" not in content:
        title_match = re.search(r'<title>(.*?)</title>', content)
        desc_match = re.search(r'<meta\s+name=[\"\']description[\"\']\s+content=[\"\'](.*?)[\"\']', content)
        
        t_title = title_match.group(1) if title_match else 'Ayodhya Dharshan Tour Packages'
        t_desc = desc_match.group(1) if desc_match else 'Book Ayodhya Ram Mandir VIP Darshan & Tour Packages.'
        if len(t_title) > 58:
            t_title = t_title[:55].rstrip() + '...'
            
        twitter_block = f'''<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@ayodhyadharshan">
<meta name="twitter:title" content="{t_title}">
<meta name="twitter:description" content="{t_desc}">
<meta name="twitter:image" content="https://www.ayodhyadharshan.com/assets/reviews/ayodhya-night.jpg">'''
        
        if '</head>' in content:
            content = content.replace('</head>', f'{twitter_block}\n</head>')
            modified = True

    # 3. Inject internal links section before <footer if not already present
    if 'SACRED YATRA CIRCUITS & GUIDES FOOTER NAV' not in content:
        if '<footer' in content:
            content = content.replace('<footer', f'{internal_links_html}\n<footer', 1)
            modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

print(f'Successfully updated {updated_count} HTML files with Twitter cards, trimmed og:title, and internal links grid.')
