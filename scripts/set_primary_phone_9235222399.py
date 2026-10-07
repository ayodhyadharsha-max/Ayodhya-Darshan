import os
import re

base_dir = '/Users/rishabhjaiswal/ayodhya-darshan'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
js_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith('.js')]

PRIMARY_PHONE = '9235222399'
FORMATTED_PHONE = '+91 92352 22399'

OLD_PHONE = '9235222399'
OLD_FORMATTED = '+91 74087 63401'

updated_count = 0

# 1. Process HTML files
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    if OLD_PHONE in content:
        content = content.replace(OLD_PHONE, PRIMARY_PHONE)
        modified = True

    if '74087 63401' in content:
        content = content.replace('74087 63401', '92352 22399')
        modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

# 2. Process JS files (including conversion-tracker.js)
for fpath in js_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        if OLD_PHONE in content:
            content = content.replace(OLD_PHONE, PRIMARY_PHONE)
            modified = True

        if '74087 63401' in content:
            content = content.replace('74087 63401', '92352 22399')
            modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated JS file: {os.path.basename(fpath)}')

# 3. Process scripts folder python files if necessary
scripts_dir = os.path.join(base_dir, 'scripts')
for fname in os.listdir(scripts_dir):
    if fname.endswith('.py'):
        fpath = os.path.join(scripts_dir, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if OLD_PHONE in content:
            content = content.replace(OLD_PHONE, PRIMARY_PHONE)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated python script: {fname}')

print(f'Successfully updated {updated_count} HTML files to use primary phone/WhatsApp number: {FORMATTED_PHONE}!')
