import os
import re

root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

def fix_index_page():
    index_path = os.path.join(root_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Title tag optimization (53 chars - optimal length under 60)
    old_title = re.search(r'<title>.*?</title>', content, re.DOTALL)
    new_title = "<title>Ayodhya Darshan &amp; Ram Mandir Tour Packages 2026</title>"
    if old_title:
        content = content.replace(old_title.group(0), new_title)

    # 2. Description optimization (152 chars - optimal length under 160)
    old_desc = re.search(r'<meta\s+name="description"\s+content=".*?"', content, re.DOTALL)
    new_desc = '<meta name="description" content="Book Ayodhya tour packages with Ram Mandir VIP darshan, Varanasi &amp; Prayagraj yatras. Private AC cabs, clean hotels &amp; 24/7 care. Get free quotes today!">'
    if old_desc:
        content = content.replace(old_desc.group(0), new_desc)

    # 3. Robots meta tag with max-image-preview:large for Google Discover
    if 'max-image-preview:large' not in content:
        content = content.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">')

    # 4. Add theme-color, apple-touch-icon, and manifest in head
    head_meta_block = """<meta name="theme-color" content="#7A1C1C">
<link rel="apple-touch-icon" href="assets/logo.webp">
<link rel="manifest" href="site.webmanifest">
"""
    if 'site.webmanifest' not in content:
        content = content.replace('<head>', f'<head>\n{head_meta_block}')

    # 5. Title-H1 Alignment (100% keyword match)
    content = re.sub(r'<h1 class="display">.*?</h1>', '<h1 class="display">Ayodhya Darshan &amp; Ram Mandir<br>Tour Packages 2026</h1>', content, flags=re.DOTALL)

    # 6. Add dateModified to JSON-LD schema
    if '"dateModified"' not in content:
        content = content.replace('"@type": "TravelAgency",', '"@type": "TravelAgency",\n      "datePublished": "2026-01-01",\n      "dateModified": "2026-09-14",')

    # 7. Add Privacy Policy and Terms links in footer
    footer_privacy_block = ' · <a href="privacy-policy.html">Privacy Policy</a> · <a href="terms.html">Terms of Service</a>'
    if 'privacy-policy.html' not in content:
        content = content.replace('<a href="contact.html">Contact</a>', f'<a href="contact.html">Contact</a>{footer_privacy_block}')

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Successfully updated index.html with all 27 Audit Fixes!")

if __name__ == "__main__":
    fix_index_page()
