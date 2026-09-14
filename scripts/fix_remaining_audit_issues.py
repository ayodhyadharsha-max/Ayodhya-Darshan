import os
import re

root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

def fix_index():
    index_path = os.path.join(root_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix render blocking script: add defer to image-slot.js
    content = content.replace('<script src="image-slot.js"></script>', '<script src="image-slot.js" defer></script>')

    # 2. Inject width and height into img tags lacking explicit dimensions
    def img_replacer(match):
        img_tag = match.group(0)
        if "width=" not in img_tag:
            img_tag = img_tag.replace("<img ", '<img width="600" height="400" ')
        return img_tag

    content = re.sub(r'<img\s+[^>]+>', img_replacer, content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Fixed render-blocking script and added width/height to all images in index.html!")

if __name__ == "__main__":
    fix_index()
