import os
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

repo_dir = '/Users/rishabhjaiswal/ayodhya-darshan'

html_files = [f for f in os.listdir(repo_dir) if f.endswith('.html')]

issues = []

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = []
        self.in_title = False
        self.meta_desc = None
        self.canonical = None
        self.h1_count = 0
        self.images_without_alt = []
        self.og_title = None
        self.og_desc = None
        self.og_url = None
        self.og_image = None
        self.robots = None
        self.json_ld = []
        self.in_script = False
        self.script_type = None
        self.current_script = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag = tag.lower()

        if tag == 'title':
            self.in_title = True

        elif tag == 'meta':
            name = attrs_dict.get('name', '').lower()
            prop = attrs_dict.get('property', '').lower()
            content = attrs_dict.get('content', '')

            if name == 'description':
                self.meta_desc = content
            elif name == 'robots':
                self.robots = content

            if prop == 'og:title':
                self.og_title = content
            elif prop == 'og:description':
                self.og_desc = content
            elif prop == 'og:url':
                self.og_url = content
            elif prop == 'og:image':
                self.og_image = content

        elif tag == 'link':
            rel = attrs_dict.get('rel', '').lower()
            if rel == 'canonical':
                self.canonical = attrs_dict.get('href', '')

        elif tag == 'h1':
            self.h1_count += 1

        elif tag == 'img':
            alt = attrs_dict.get('alt')
            src = attrs_dict.get('src', 'unknown')
            if alt is None or alt.strip() == '':
                self.images_without_alt.append(src)

        elif tag == 'script':
            stype = attrs_dict.get('type', '').lower()
            if stype == 'application/ld+json':
                self.in_script = True
                self.current_script = []

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'title':
            self.in_title = False
        elif tag == 'script' and self.in_script:
            self.in_script = False
            self.json_ld.append("".join(self.current_script))
            self.current_script = []

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        elif self.in_script:
            self.current_script.append(data)


for file_name in sorted(html_files):
    file_path = os.path.join(repo_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parser = SEOParser()
    try:
        parser.feed(content)
    except Exception as e:
        issues.append((file_name, 'Parser', 'HTML_PARSE_ERROR', str(e)))
        continue

    # Skip verification files like google0dc20d35f8fb3bcd.html
    if file_name.startswith('google'):
        continue

    # 1. Title Tag
    title_text = "".join(parser.title).strip()
    if not title_text:
        issues.append((file_name, 'Title', 'MISSING_TITLE', 'Title tag is missing or empty'))
    elif len(title_text) < 20:
        issues.append((file_name, 'Title', 'SHORT_TITLE', f'Title is too short ({len(title_text)} chars): "{title_text}"'))
    elif len(title_text) > 85:
        issues.append((file_name, 'Title', 'LONG_TITLE', f'Title is too long ({len(title_text)} chars): "{title_text}"'))

    # 2. Meta Description
    if not parser.meta_desc:
        issues.append((file_name, 'MetaDescription', 'MISSING_DESC', 'Meta description is missing or empty'))
    else:
        desc_text = parser.meta_desc.strip()
        if len(desc_text) < 50:
            issues.append((file_name, 'MetaDescription', 'SHORT_DESC', f'Meta description is too short ({len(desc_text)} chars)'))
        elif len(desc_text) > 200:
            issues.append((file_name, 'MetaDescription', 'LONG_DESC', f'Meta description is too long ({len(desc_text)} chars)'))

    # 3. Canonical Tag
    if not parser.canonical:
        issues.append((file_name, 'Canonical', 'MISSING_CANONICAL', 'Canonical tag is missing'))
    else:
        canonical_href = parser.canonical.strip()
        expected = f'https://www.ayodhyadharshan.com/{file_name}'
        if file_name == 'index.html':
            expected_alt = 'https://www.ayodhyadharshan.com/'
            if canonical_href != expected and canonical_href != expected_alt:
                issues.append((file_name, 'Canonical', 'MISMATCH_CANONICAL', f'Canonical href "{canonical_href}" does not match "{expected}"'))
        elif canonical_href != expected:
            issues.append((file_name, 'Canonical', 'MISMATCH_CANONICAL', f'Canonical href "{canonical_href}" does not match "{expected}"'))

    # 4. H1 Tag
    if parser.h1_count == 0:
        issues.append((file_name, 'H1', 'MISSING_H1', 'No <h1> tag found on page'))
    elif parser.h1_count > 1:
        issues.append((file_name, 'H1', 'MULTIPLE_H1', f'Multiple ({parser.h1_count}) <h1> tags found'))

    # 5. Image Alt Attributes
    for img_src in parser.images_without_alt:
        issues.append((file_name, 'ImageAlt', 'MISSING_ALT', f'Image "{img_src}" has missing or empty alt attribute'))

    # 6. OpenGraph Tags
    if not parser.og_title:
        issues.append((file_name, 'OpenGraph', 'MISSING_OG_TITLE', 'og:title meta tag missing'))
    if not parser.og_desc:
        issues.append((file_name, 'OpenGraph', 'MISSING_OG_DESC', 'og:description meta tag missing'))
    if not parser.og_url:
        issues.append((file_name, 'OpenGraph', 'MISSING_OG_URL', 'og:url meta tag missing'))
    if not parser.og_image:
        issues.append((file_name, 'OpenGraph', 'MISSING_OG_IMAGE', 'og:image meta tag missing'))

    # 7. JSON-LD Structured Data
    if not parser.json_ld:
        issues.append((file_name, 'Schema', 'MISSING_SCHEMA', 'No JSON-LD schema script found'))
    else:
        for idx, script_str in enumerate(parser.json_ld):
            try:
                data = json.loads(script_str)
                if isinstance(data, dict):
                    if '@context' not in data:
                        issues.append((file_name, 'Schema', 'INVALID_SCHEMA_CONTEXT', f'JSON-LD #{idx+1} missing @context'))
                    if '@type' not in data and '@graph' not in data:
                        issues.append((file_name, 'Schema', 'INVALID_SCHEMA_TYPE', f'JSON-LD #{idx+1} missing @type or @graph'))
                    elif '@graph' in data:
                        for g_idx, item in enumerate(data['@graph']):
                            if isinstance(item, dict) and '@type' not in item:
                                issues.append((file_name, 'Schema', 'INVALID_GRAPH_ITEM_TYPE', f'JSON-LD #{idx+1} @graph[{g_idx}] missing @type'))
            except Exception as e:
                issues.append((file_name, 'Schema', 'INVALID_JSON_LD', f'JSON-LD #{idx+1} invalid JSON syntax: {str(e)}'))

    # 8. Meta Robots
    if not parser.robots:
        issues.append((file_name, 'Robots', 'MISSING_ROBOTS', 'meta robots tag missing'))

print("\n--- REFINED TECHNICAL SEO AUDIT RESULTS ---")
print(f"Total Audit Findings/Issues: {len(issues)}")

category_counts = {}
for issue in issues:
    cat = issue[1]
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("\nSummary by Category:")
for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {cat}: {count} issues")

print("\nDetailed Issues:")
for issue in issues:
    print(f"[{issue[0]}] [{issue[1]}] {issue[2]}: {issue[3]}")

# Check sitemap.xml
sitemap_path = os.path.join(repo_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls_in_sitemap = [loc.text for loc in root.findall('ns:url/ns:loc', namespace)]
    print(f"\nSitemap.xml contains {len(urls_in_sitemap)} URLs.")
    
    missing_from_sitemap = []
    for f_name in html_files:
        if f_name.startswith('google'):
            continue
        expected_url = f'https://www.ayodhyadharshan.com/{f_name}'
        if expected_url not in urls_in_sitemap and (f_name != 'index.html' or 'https://www.ayodhyadharshan.com/' not in urls_in_sitemap):
            missing_from_sitemap.append(f_name)
    
    if missing_from_sitemap:
        print(f"\nSITEMAP WARNING: {len(missing_from_sitemap)} HTML files missing from sitemap.xml:")
        for m in missing_from_sitemap:
            print(f"  - {m}")
    else:
        print("\nSITEMAP SUCCESS: All HTML files are included in sitemap.xml!")

