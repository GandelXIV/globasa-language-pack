#!/usr/bin/env python3
import json
from pathlib import Path

EN_FILE = Path("en_us.json")
GLB_FILE = Path("assets/minecraft/lang/glb_glb.json")
PREFIX = "§n"
SUFFIX = "§r"

def main():
    with EN_FILE.open("r", encoding="utf-8") as f:
        en_data = json.load(f)

    with GLB_FILE.open("r", encoding="utf-8") as f:
        glb_data = json.load(f)

    styled_count = 0

    for key, val in glb_data.items():
        clean_val = val.removeprefix(PREFIX).removesuffix(SUFFIX)
        en_val = en_data.get(key)

        if en_val is not None and clean_val != en_val and clean_val.strip() != "":
            glb_data[key] = f"{PREFIX}{clean_val}{SUFFIX}"
            styled_count += 1
            print(en_val, "=>", clean_val)

        else:
            glb_data[key] = clean_val

    with GLB_FILE.open("w", encoding="utf-8") as f:
        json.dump(glb_data, f, ensure_ascii=False, indent=2)

    print(f"Done! Styled {styled_count} translated strings in {GLB_FILE}.")


if __name__ == "__main__":
    main()
