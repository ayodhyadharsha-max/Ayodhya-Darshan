import os
import re

# 1. Update Ayodhya page
ayodhya_file = "/Users/rishabhjaiswal/ayodhya-darshan/ayodhya-dharshan-tour-package.html"
with open(ayodhya_file, "r", encoding="utf-8") as f:
    ayodhya_content = f.read()

# Replace flat div with collapsible details/summary tag
old_ayodhya_pattern = r'<!-- Exhaustive Ayodhya Search Index & Keyword Directory for Search Engines & AI Models -->\s*<section class="section"[^>]*>.*?<\/section>'

new_ayodhya_section = """<!-- Exhaustive Ayodhya Search Index & Keyword Directory for Search Engines & AI Models -->
<section class="section" style="background:var(--bg-panel); border-top:1px solid var(--line-soft); padding:30px 0;">
  <div class="container">
    <details style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:20px 24px; cursor:pointer;">
      <summary style="font-weight:600; color:var(--maroon); font-size:1.15rem; font-family:var(--font-display); outline:none; display:flex; align-items:center; justify-content:space-between; user-select:none;">
        <span>🔍 Ayodhya Tourism &amp; Ram Mandir Master Search Index</span>
        <span style="font-size:0.9rem; color:var(--saffron-deep); font-weight:600; background:var(--bg-panel); padding:4px 12px; border-radius:var(--r-sm); border:1px solid var(--line-soft);">Read More ▾</span>
      </summary>
      <div style="margin-top:16px; padding-top:16px; border-top:1px solid var(--line-soft);">
        <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.6; margin-bottom:14px;">
          Complete directory of all official search queries, travel itineraries, temple timings, VIP darshan passes, and local transport options for Ayodhya Dham:
        </p>
        <div style="font-size:0.84rem; color:var(--ink-3); line-height:1.8; word-break:break-word;">
"""

# Extract keywords string from ayodhya_content
kw_match = re.search(r'<div style="font-size:0\.86rem; color:var\(--ink-3\); line-height:1\.8; word-break:break-word;">\s*(.*?)\s*</div>', ayodhya_content, re.DOTALL)
if kw_match:
    keywords_text = kw_match.group(1).strip()
    full_new_ayodhya = new_ayodhya_section + f"          {keywords_text}\n        </div>\n      </div>\n    </details>\n  </div>\n</section>"
    ayodhya_content = re.sub(old_ayodhya_pattern, full_new_ayodhya, ayodhya_content, flags=re.DOTALL)
    with open(ayodhya_file, "w", encoding="utf-8") as f:
        f.write(ayodhya_content)
    print("Updated ayodhya-dharshan-tour-package.html with collapsible dropdown!")

# 2. Update Chitrakoot page
chitrakoot_file = "/Users/rishabhjaiswal/ayodhya-darshan/chitrakoot-tour-package.html"
with open(chitrakoot_file, "r", encoding="utf-8") as f:
    chitrakoot_content = f.read()

old_chitrakoot_pattern = r'<!-- Exhaustive Chitrakoot Search Index & Keyword Directory for Search Engines & AI Models -->\s*<section class="section"[^>]*>.*?<\/section>'

new_chitrakoot_section = """<!-- Exhaustive Chitrakoot Search Index & Keyword Directory for Search Engines & AI Models -->
<section class="section" style="background:var(--bg-panel); border-top:1px solid var(--line-soft); padding:30px 0;">
  <div class="container">
    <details style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:20px 24px; cursor:pointer;">
      <summary style="font-weight:600; color:var(--maroon); font-size:1.15rem; font-family:var(--font-display); outline:none; display:flex; align-items:center; justify-content:space-between; user-select:none;">
        <span>🔍 Chitrakoot Tourism &amp; Pilgrimage Master Search Index</span>
        <span style="font-size:0.9rem; color:var(--saffron-deep); font-weight:600; background:var(--bg-panel); padding:4px 12px; border-radius:var(--r-sm); border:1px solid var(--line-soft);">Read More ▾</span>
      </summary>
      <div style="margin-top:16px; padding-top:16px; border-top:1px solid var(--line-soft);">
        <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.6; margin-bottom:14px;">
          Complete directory of all official search queries, travel itineraries, temple timings, hotels near Ramghat, and local transport options for Chitrakoot Dham:
        </p>
        <div style="font-size:0.84rem; color:var(--ink-3); line-height:1.8; word-break:break-word;">
"""

ckw_match = re.search(r'<div style="font-size:0\.86rem; color:var\(--ink-3\); line-height:1\.8; word-break:break-word;">\s*(.*?)\s*</div>', chitrakoot_content, re.DOTALL)
if ckw_match:
    ckeywords_text = ckw_match.group(1).strip()
    full_new_chitrakoot = new_chitrakoot_section + f"          {ckeywords_text}\n        </div>\n      </div>\n    </details>\n  </div>\n</section>"
    chitrakoot_content = re.sub(old_chitrakoot_pattern, full_new_chitrakoot, chitrakoot_content, flags=re.DOTALL)
    with open(chitrakoot_file, "w", encoding="utf-8") as f:
        f.write(chitrakoot_content)
    print("Updated chitrakoot-tour-package.html with collapsible dropdown!")
