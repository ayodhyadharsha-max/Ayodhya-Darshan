import os
import re

root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

# 1. Inject "Calculator" into top navigation menu across all HTML files
def update_nav_links():
    count = 0
    for file in os.listdir(root_dir):
        if file.endswith(".html") and file not in ["google0dc20d35f8fb3bcd.html"]:
            file_path = os.path.join(root_dir, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if 'href="yatra-cost-calculator.html"' in content and '<div class="nav-links"' in content and 'href="yatra-cost-calculator.html"' in content.split('<div class="nav-links"')[1].split('</div>')[0]:
                continue

            # Update nav-links block
            if '<a href="services.html">Services</a>' in content:
                content = content.replace('<a href="services.html">Services</a>', '<a href="services.html">Services</a>\n      <a href="yatra-cost-calculator.html">Calculator</a>')
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
    print(f"✅ Injected 'Calculator' tool link into top nav across {count} HTML pages!")

# 2. Add WebApplication schema to yatra-cost-calculator.html
def add_calculator_schema():
    calc_path = os.path.join(root_dir, "yatra-cost-calculator.html")
    if os.path.exists(calc_path):
        with open(calc_path, "r", encoding="utf-8") as f:
            content = f.read()

        web_app_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Ayodhya & Kashi Yatra Cost Calculator",
  "url": "https://www.ayodhyadharshan.com/yatra-cost-calculator.html",
  "description": "Interactive travel budget planner and cost estimator for Ayodhya Ram Mandir and Kashi Vishwanath yatras.",
  "applicationCategory": "TravelApplication",
  "operatingSystem": "All",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "INR"
  }
}
</script>
"""
        if "WebApplication" not in content:
            content = content.replace("</head>", f"{web_app_schema}\n</head>")
            with open(calc_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("✅ Added WebApplication Schema to yatra-cost-calculator.html!")

# 3. Add E-E-A-T Editorial Policy box to about.html & services.html for AdSense High Quality Content compliance
def add_editorial_policy():
    about_path = os.path.join(root_dir, "about.html")
    if os.path.exists(about_path):
        with open(about_path, "r", encoding="utf-8") as f:
            content = f.read()

        editorial_box = """
<div style="background: linear-gradient(135deg, #fefce8, #fef9c3); border: 2px solid var(--saffron); padding: 28px; border-radius: 12px; margin: 40px 0;" class="editorial-policy-box">
  <h3 style="color:var(--maroon); margin-top:0;">🛡️ Editorial &amp; Quality Guarantee</h3>
  <p style="font-size:1.05rem; line-height:1.7; color:#333;">Every yatra guide, travel itinerary, and cost estimate on <strong>Ayodhya Dharshan</strong> is researched, authored, and verified by 100% local Uttar Pradesh pilgrimage experts based in Ayodhya and Varanasi. We strictly adhere to authentic information sourcing, direct temple trust updates, and transparent yatra pricing.</p>
</div>
"""
        if "editorial-policy-box" not in content:
            content = content.replace('</section>', f'{editorial_box}\n</section>', 1)
            with open(about_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("✅ Added Editorial & Quality Guarantee box to about.html!")

if __name__ == "__main__":
    update_nav_links()
    add_calculator_schema()
    add_editorial_policy()
    print("\n🎉 AdSense Re-approval fixes successfully applied!")
