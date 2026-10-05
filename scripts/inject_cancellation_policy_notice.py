import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

# Policy Notice HTML snippet
policy_box_html = '''
<!-- ===== CANCELLATION & RESCHEDULING POLICY NOTICE ===== -->
<div class="cancellation-policy-box" style="background:#fffbe0; border:1px solid #f59e0b; border-radius:8px; padding:20px; margin:28px 0; font-size:14px; line-height:1.6; color:#78350f;">
  <h4 style="margin:0 0 10px 0; font-weight:700; color:#b45309; font-size:16px;">📋 Booking, Cancellation &amp; Rescheduling Policy Notice</h4>
  <ul style="margin:0; padding-left:20px;">
    <li><strong>Advance Booking Amount:</strong> Strictly 100% NON-REFUNDABLE under any circumstances.</li>
    <li><strong>Full Cancellation Rule:</strong> Written notice required at least <strong>1 week (7 days) before travel date</strong>. If cancelled less than 7 days prior, <strong>100% cancellation fee applies (FULL PACKAGE AMOUNT PAYABLE)</strong>.</li>
    <li><strong>Package Modification Rule:</strong> Any itinerary/hotel/vehicle changes allowed <strong>ONLY up to 1 month (30 days) before travel</strong>. Modifications within 30 days incur 50% charges.</li>
    <li><strong>Rescheduling Fee:</strong> Travel date change requests incur a <strong>25% rescheduling fee</strong> of total package cost.</li>
  </ul>
  <p style="margin:10px 0 0 0; font-size:13px; color:#92400e;">Read our official legal terms: <a href="terms.html" style="color:#b45309; font-weight:700; text-decoration:underline;">Complete Terms &amp; Cancellation Policy &rarr;</a></p>
</div>
'''

target_files = [
    'services.html',
    'ayodhya-dharshan-tour-package.html',
    'contact.html',
    'thankyou.html',
    'yatra-cost-calculator.html',
    'ayodhya-same-day-tour.html',
    'varanasi-same-day-tour-package.html',
    'ayodhya-prayagraj-varanasi-tour-package.html'
]

for fname in target_files:
    fpath = os.path.join(base_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'CANCELLATION & RESCHEDULING POLICY NOTICE' not in content:
            # Inject before </main> or inside main section or before footer
            if '</main>' in content:
                content = content.replace('</main>', f'{policy_box_html}\n</main>', 1)
            elif '<footer' in content:
                content = content.replace('<footer', f'{policy_box_html}\n<footer', 1)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Injected policy box into {fname}')

# Also ensure terms.html is linked in internal linking footer across all HTML files
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'terms.html' not in content:
        # Add link in footer or navigation
        if 'Yatra Cost Calculator</a></li>' in content:
            content = content.replace(
                'Yatra Cost Calculator</a></li>',
                'Yatra Cost Calculator</a></li>\n        <li><a href="terms.html" style="color:#fef08a; text-decoration:none;">Terms &amp; Cancellation Policy</a></li>'
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Linked terms.html in {fname}')

print('Policy injection completed successfully!')
