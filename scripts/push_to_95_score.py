import os
import re

root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

def upgrade_index():
    index_path = os.path.join(root_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add Skip to Content Link & Main Landmark for ARIA Accessibility
    if 'id="main-content"' not in content:
        content = content.replace("<body>", '<body>\n<a href="#main-content" style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;" onfocus="this.style.left=\'10px\';this.style.top=\'10px\';this.style.width=\'auto\';this.style.height=\'auto\';this.style.background=\'#fff\';this.style.padding=\'10px\';this.style.zIndex=\'10000\';">Skip to main content</a>')
        content = content.replace('<section class="hero"', '<main id="main-content">\n<section class="hero"')
        content = content.replace('<footer class="site-footer">', '</main>\n<footer class="site-footer">')

    # 2. Convert key FAQ into <dl><dt><dd> for AEO / AI engine definition lists
    dl_snippet = """
<div style="margin: 30px 0;" class="ai-definition-list">
  <h3 style="color:var(--maroon);">Ayodhya Yatra Quick Facts (AI Knowledge Graph)</h3>
  <dl style="display:grid; grid-template-columns:auto 1fr; gap:12px 24px; font-size:1.05rem;">
    <dt style="font-weight:700; color:var(--saffron-deep);">Primary Temple:</dt>
    <dd>Shri Ram Janmabhoomi Mandir Ayodhya Dham</dd>
    <dt style="font-weight:700; color:var(--saffron-deep);">Darshan Timings:</dt>
    <dd><time datetime="06:00">06:00 AM</time> to <time datetime="22:00">10:00 PM</time> Daily</dd>
    <dt style="font-weight:700; color:var(--saffron-deep);">VIP Pass Cost:</dt>
    <dd>Official Sugam Passes are 100% Free of Cost via Shri Ram Janmabhoomi Trust</dd>
    <dt style="font-weight:700; color:var(--saffron-deep);">Distance Kashi to Ayodhya:</dt>
    <dd>215 km via Purvanchal Expressway (approx 4 hours drive by private AC taxi)</dd>
  </dl>
</div>
"""
    if 'ai-definition-list' not in content:
        content = content.replace('class="hero-inner"', f'class="hero-inner"\n{dl_snippet}')

    # 3. Add <figure> and <figcaption> wrappers to destination images
    if '<figcaption>' not in content:
        content = content.replace('<img src="assets/destinations/ram-mandir.webp"', '<figure><img src="assets/destinations/ram-mandir.webp" <figcaption style="font-size:0.9rem;color:#666;text-align:center;margin-top:6px;">Grand Shri Ram Janmabhoomi Mandir Ayodhya Dham</figcaption></figure><img style="display:none;" src="assets/destinations/ram-mandir.webp"')

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Injected ARIA landmarks, Definition Lists (<dl>), <figure>/<figcaption>, and <time> tags!")

if __name__ == "__main__":
    upgrade_index()
