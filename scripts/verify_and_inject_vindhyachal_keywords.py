import os
import json

jsonl_path = '/Users/rishabhjaiswal/.gemini/antigravity/brain/b79eec1d-24f9-4c55-87db-f35573cc67e6/.system_generated/logs/transcript_full.jsonl'

keywords = []
seen = set()
with open(jsonl_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('source') == 'USER_EXPLICIT':
            content = data.get('content', '')
            if 'https://www.ayodhyadharshan.com/vindhyachal-tour-package.html' in content:
                for l in content.split('\n'):
                    l = l.strip()
                    if l and not l.startswith('https://') and not l.startswith('<') and not l.startswith('The current'):
                        l_lower = l.lower()
                        if l_lower not in seen:
                            seen.add(l_lower)
                            keywords.append(l)

print(f"Extracted {len(keywords)} unique Vindhyachal keywords.")

# Construct chip HTML
chips_html = []
for kw in keywords:
    chip = f'<span style="display:inline-flex; align-items:center; gap:6px; padding:5px 12px; background:var(--bg-panel); border:1px solid var(--line); border-radius:20px; font-size:0.82rem; color:var(--ink-2); font-weight:500;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg><span>{kw}</span></span>'
    chips_html.append(chip)

chips_joined = "\n        ".join(chips_html)

section_html = f'''
<!-- Collapsible Master Search Index Section -->
<section class="section" style="padding: 40px 0 60px;">
  <div class="container">
    <details style="background:var(--bg-card); border:1px solid var(--line); border-radius:var(--r-md); padding:22px 26px; cursor:pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
      <summary style="display:flex; align-items:center; justify-content:space-between; list-style:none; outline:none; font-weight:700; color:var(--maroon); font-size:1.15rem; font-family:var(--font-display);">
        <span style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:1.4rem;">🔍</span>
          <span>Vindhyachal Tourism & Maa Vindhyavasini Master Search Index</span>
        </span>
        <span style="background:rgba(122,28,28,0.08); border:1px solid var(--line); color:var(--maroon); padding:4px 14px; border-radius:20px; font-size:0.82rem; font-weight:600; font-family:var(--font-sans);">Explore {len(keywords)}+ Topics (Read More ▾)</span>
      </summary>
      
      <div style="margin-top:24px; padding-top:20px; border-top:1px solid var(--line);">
        <p style="font-size:0.9rem; color:var(--ink-2); margin-bottom:18px; line-height:1.5;">Comprehensive index of search queries, destinations, temples, Trikon Parikrama routes, and booking details for Vindhyachal Dham pilgrimages:</p>
        <div style="display:flex; flex-wrap:wrap; gap:8px;">
        {chips_joined}
        </div>
      </div>
    </details>
  </div>
</section>
'''

file_path = '/Users/rishabhjaiswal/ayodhya-darshan/vindhyachal-tour-package.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace or inject before <footer class="site-foot">
if '<!-- Collapsible Master Search Index Section -->' in html_content:
    parts = html_content.split('<!-- Collapsible Master Search Index Section -->')
    footer_pos = parts[1].find('<footer class="site-foot">')
    html_content = parts[0] + section_html + '\n\n' + parts[1][footer_pos:]
else:
    html_content = html_content.replace('<footer class="site-foot">', section_html + '\n\n<footer class="site-foot">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated {file_path} successfully.")

# Verification
with open(file_path, 'r', encoding='utf-8') as f:
    verify_html = f.read()

missing = []
for kw in keywords:
    if kw.lower() not in verify_html.lower():
        missing.append(kw)

if missing:
    print(f"VERIFICATION FAILURE: {len(missing)} keywords missing!")
    print("Missing sample:", missing[:10])
else:
    print(f"VERIFICATION SUCCESS: 100.0% of all {len(keywords)} keywords verified on page!")
