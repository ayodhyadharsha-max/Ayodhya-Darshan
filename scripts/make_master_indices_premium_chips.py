import os
import re

def convert_to_premium_chips(page_path, title_text, desc_text):
    if not os.path.exists(page_path):
        print(f"File not found: {page_path}")
        return
    
    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract the keywords string between <div style="font-size:0.84rem...
    match = re.search(r'<div style="font-size:0\.84rem; color:var\(--ink-3\); line-height:1\.8; word-break:break-word;">\s*(.*?)\s*</div>', content, re.DOTALL)
    if not match:
        print(f"Could not find keywords block in {page_path}")
        return
    
    raw_text = match.group(1).strip()
    keywords = [k.strip() for k in raw_text.split(",") if k.strip()]
    
    chips_html_list = []
    svg_icon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="width:11px;height:11px;color:var(--saffron-deep);flex-shrink:0;"><path d="M20 6L9 17l-5-5"/></svg>'
    
    for kw in keywords:
        chip = f'<span style="display:inline-flex; align-items:center; gap:6px; padding:5px 12px; background:var(--bg-panel); border:1px solid var(--line); border-radius:20px; font-size:0.82rem; color:var(--ink-2); font-weight:500; transition:all 0.2s ease;">{svg_icon}<span>{kw}</span></span>'
        chips_html_list.append(chip)
    
    chips_container = f"""<div style="display:flex; flex-wrap:wrap; gap:8px 10px; margin-top:14px; max-height:400px; overflow-y:auto; padding-right:6px;">
          {" ".join(chips_html_list)}
        </div>"""
    
    old_section_pattern = r'<!-- Exhaustive (?:Ayodhya|Chitrakoot) Search Index & Keyword Directory for Search Engines & AI Models -->\s*<section class="section"[^>]*>.*?<\/section>'
    
    new_section = f"""<!-- Exhaustive Search Index & Keyword Directory (Ultra-Premium Chip Tags) -->
<section class="section" style="background:var(--bg-panel); border-top:1px solid var(--line-soft); padding:32px 0;">
  <div class="container">
    <details style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:22px 26px; cursor:pointer; box-shadow:var(--shadow-sm);">
      <summary style="font-weight:600; color:var(--maroon); font-size:1.15rem; font-family:var(--font-display); outline:none; display:flex; align-items:center; justify-content:space-between; user-select:none;">
        <span style="display:flex; align-items:center; gap:10px;">
          <span style="display:inline-flex; align-items:center; justify-content:center; width:32px; height:32px; background:#FFF3E0; border-radius:50%; color:var(--saffron-deep); font-size:1rem;">🔍</span>
          <span>{title_text}</span>
        </span>
        <span style="font-size:0.88rem; color:var(--saffron-deep); font-weight:600; background:#FFF8EE; padding:6px 14px; border-radius:20px; border:1px solid var(--saffron-soft); display:flex; align-items:center; gap:6px;">
          <span>Explore 700+ Topics</span>
          <span style="font-size:1.1rem; line-height:1;">▾</span>
        </span>
      </summary>
      <div style="margin-top:18px; padding-top:18px; border-top:1px solid var(--line-soft);">
        <p style="font-size:0.92rem; color:var(--ink-2); line-height:1.6; margin-bottom:12px;">
          {desc_text}
        </p>
        {chips_container}
      </div>
    </details>
  </div>
</section>"""
    
    content = re.sub(old_section_pattern, new_section, content, flags=re.DOTALL)
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully upgraded {os.path.basename(page_path)} to Ultra-Premium Chip Tags!")

# Upgrade Ayodhya Page
convert_to_premium_chips(
    "/Users/rishabhjaiswal/ayodhya-darshan/ayodhya-dharshan-tour-package.html",
    "Ayodhya Tourism & Ram Mandir Master Search Index",
    "Explore complete official directory of travel packages, temple timings, VIP darshan passes, local transport, and sightseeing places for Ayodhya Dham:"
)

# Upgrade Chitrakoot Page
convert_to_premium_chips(
    "/Users/rishabhjaiswal/ayodhya-darshan/chitrakoot-tour-package.html",
    "Chitrakoot Tourism & Pilgrimage Master Search Index",
    "Explore complete official directory of travel packages, Kamadgiri Parikrama, Ramghat Aarti timings, hotels, and transport options for Chitrakoot Dham:"
)
