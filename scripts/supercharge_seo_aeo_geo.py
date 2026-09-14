import os
import re

root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

# 1. Organization & Breadcrumb Schema snippet for AI / AEO / GEO recognition
aeo_geo_schema = """
<!-- Organization & Breadcrumb Schema for AI & Generative Engine Optimization (AEO / GEO) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.ayodhyadharshan.com/#organization",
  "name": "Ayodhya Dharshan",
  "legalName": "Ayodhya Dharshan Teerth Yatra",
  "url": "https://www.ayodhyadharshan.com/",
  "logo": "https://www.ayodhyadharshan.com/assets/logo.webp",
  "foundingDate": "2024",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+91-92352-22399",
    "contactType": "customer service",
    "areaServed": "IN",
    "availableLanguage": ["en", "hi"]
  },
  "sameAs": [
    "https://www.facebook.com/ayodhyadharshan",
    "https://www.instagram.com/ayodhyadharshan",
    "https://twitter.com/ayodhyadharshan",
    "https://en.wikipedia.org/wiki/Ayodhya"
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.ayodhyadharshan.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Ayodhya Tour Packages",
      "item": "https://www.ayodhyadharshan.com/services.html"
    }
  ]
}
</script>
"""

# Security & Hreflang headers block
security_meta_block = """<meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval';">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="permissions-policy" content="geolocation=(), microphone=(), camera=()">
<link rel="alternate" hreflang="en-IN" href="https://www.ayodhyadharshan.com/">
<link rel="alternate" hreflang="hi-IN" href="https://www.ayodhyadharshan.com/">
<link rel="alternate" hreflang="x-default" href="https://www.ayodhyadharshan.com/">
"""

def update_page(filename):
    filepath = os.path.join(root_dir, filename)
    if not os.path.exists(filepath):
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add security & hreflang meta if missing
    if "X-Content-Type-Options" not in content:
        content = content.replace("<head>", f"<head>\n{security_meta_block}")

    # Add AEO & GEO schemas if missing
    if "BreadcrumbList" not in content:
        content = content.replace("</head>", f"{aeo_geo_schema}\n</head>")

    # Fix Google Fonts font-display: swap
    content = content.replace("display=optional", "display=swap")

    # Wrap images with missing width/height or loading lazy
    content = content.replace('<img src="assets/logo.webp"', '<img src="assets/logo.webp" width="500" height="500"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Enhanced AEO/GEO & Security headers in {filename}")

def main():
    pages = ["index.html", "services.html", "blog.html", "destinations.html", "about.html", "contact.html"]
    for p in pages:
        update_page(p)

    print("\n🚀 Supercharged SEO, AEO & GEO audit optimizations completed!")

if __name__ == "__main__":
    main()
