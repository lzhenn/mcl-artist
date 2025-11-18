import os
import json

def scan(dir_path="", base=""):
    result = {"name": os.path.basename(dir_path) or "MCL_ARTIST", "path": dir_path}
    entries = []
    images = []
    for entry in os.listdir(dir_path or "."):
        full = os.path.join(dir_path or ".", entry)
        if os.path.isdir(full):
            entries.append(scan(full, base))
        elif entry.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            images.append(entry)
    if images:
        result["images"] = images
    if entries:
        result["children"] = entries
    return result

structure = scan()
with open("structure.js", "w", encoding="utf-8") as f:
    f.write(f"const directoryStructure = {json.dumps(structure, ensure_ascii=False, indent=2)};")
