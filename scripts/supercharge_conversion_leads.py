import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# Primary conversion phone & WhatsApp number
PRIMARY_PHONE = '9235222399'
FORMATTED_PHONE = '+91 74087 63401'

updated_count = 0
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Update old WhatsApp wa.me links from 9235222399 to 9235222399
    if 'wa.me/919235222399' in content:
        content = content.replace('wa.me/919235222399', f'wa.me/91{PRIMARY_PHONE}')
        modified = True
    
    if 'tel:+919235222399' in content:
        content = content.replace('tel:+919235222399', f'tel:+91{PRIMARY_PHONE}')
        modified = True
        
    if '+91 92352 22399' in content:
        content = content.replace('+91 92352 22399', FORMATTED_PHONE)
        modified = True

    # 2. Ensure mobile-sticky-cta uses updated phone & WhatsApp number
    sticky_cta_html = f'''
<!-- High-Converting Mobile Sticky Bottom CTA Bar -->
<div class="mobile-sticky-cta" style="position:fixed; bottom:0; left:0; right:0; z-index:9999; display:grid; grid-template-columns:1fr 1fr; gap:0; background:#2C0B0E; border-t:2px solid #f59e0b; box-shadow:0 -4px 15px rgba(0,0,0,0.3);">
  <a href="tel:+91{PRIMARY_PHONE}" class="cta-call" style="display:flex; align-items:center; justify-content:center; gap:8px; padding:12px 10px; background:#b45309; color:#ffffff; font-weight:700; font-size:14px; text-decoration:none;">
    <svg viewBox="0 0 24 24" style="width:20px; height:20px; fill:currentColor;"><path d="M6.62,10.79C8.06,13.62 10.38,15.94 13.21,17.38L15.41,15.18C15.69,14.9 16.08,14.82 16.43,14.93C17.55,15.3 18.75,15.5 20,15.5A1,1 0 0,1 21,16.5V20A1,1 0 0,1 20,21A17,17 0 0,1 3,4A1,1 0 0,1 4,3H7.5A1,1 0 0,1 8.5,4C8.7,5.25 8.9,6.45 9.27,7.57C9.38,7.92 9.3,8.31 9.03,8.59L6.62,10.79Z"/></svg>
    <span>📞 Call Now</span>
  </a>
  <a href="https://wa.me/91{PRIMARY_PHONE}?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20Ayodhya%20Dharshan%20tour%20packages." class="cta-whatsapp" target="_blank" rel="noopener noreferrer" style="display:flex; align-items:center; justify-content:center; gap:8px; padding:12px 10px; background:#25d366; color:#ffffff; font-weight:700; font-size:14px; text-decoration:none;">
    <svg viewBox="0 0 24 24" style="width:20px; height:20px; fill:currentColor;"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm5.83 14.12c-.24.68-1.22 1.25-1.7 1.29-.48.04-.97.19-3.07-.63-2.67-1.05-4.4-3.76-4.53-3.94-.13-.18-1.07-1.42-1.07-2.72 0-1.29.67-1.93.91-2.19.24-.26.54-.33.72-.33.18 0 .36.01.52.02.17.01.39-.06.61.47.24.58.82 2.01.89 2.16.07.15.12.33.02.52-.1.19-.21.31-.36.48-.15.17-.32.39-.46.52-.16.15-.33.31-.14.63.19.32.85 1.4 1.82 2.26.97.86 1.79 1.13 2.11 1.26.32.13.51.1.7-.12.19-.22.82-.96 1.04-1.29.22-.33.45-.28.76-.16.31.12 1.99.94 2.33 1.11.34.17.57.26.65.41.08.15.08.88-.16 1.56z"/></svg>
    <span>💬 WhatsApp</span>
  </a>
</div>
'''

    # Ensure mobile sticky CTA is present before </body>
    if 'mobile-sticky-cta' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{sticky_cta_html}\n</body>', 1)
            modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

print(f'Successfully updated {updated_count} HTML files for lead conversion and phone synchronization!')
