import os

repo_dir = '/Users/rishabhjaiswal/ayodhya-darshan'
html_files = [f for f in os.listdir(repo_dir) if f.endswith('.html')]

script_tag = '<script src="js/pandit-ji-ai-agent.js" defer></script>'
count = 0

for file_name in sorted(html_files):
    if file_name.startswith('google'):
        continue

    file_path = os.path.join(repo_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if script_tag not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{script_tag}\n</body>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1

print(f"Successfully injected Pandit Ji AI Agent widget script into {count} HTML pages.")
