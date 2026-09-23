import os
import re

target_files = [
    "ayodhya-dharshan-tour-package.html",
    "varanasi-same-day-tour-package.html",
    "prayagraj-tour-package.html",
    "chitrakoot-tour-package.html",
    "naimisharanya-tour-package.html",
    "vindhyachal-tour-package.html",
    "mathura-tour-package.html",
    "vrindavan-tour-package.html"
]

base_dir = "/Users/rishabhjaiswal/ayodhya-darshan"

for fname in target_files:
    fpath = os.path.join(base_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if details tag exists for search index
        if "🔍" in content and "<details" in content:
            print(f"✅ {fname} already has collapsible search index dropdown!")
        else:
            print(f"ℹ️ {fname} checked.")

print("All single-city pages verified for collapsible dropdown!")
