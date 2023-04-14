"""
Zips all files listed in manifest["include"]
"""
from __future__ import annotations

import json
import os
import zipfile

with open("manifest.json", "r") as f:
    manifest = json.load(f)

to_be_zipped: dict[str, list[str]] = {}
for include in manifest["include"]:
    location = include["location"]
    id = include.get("id", "default")
    if not to_be_zipped.get(id):
        to_be_zipped[id] = []
    if os.path.isdir(location):
        for path, dirs, files in os.walk(location):
            for file in files:
                to_be_zipped[id].append(f"{path}/{file}")
    else:
        to_be_zipped[id].append(location)

zips = []

for k, v in to_be_zipped.items():
    os.makedirs("out", exist_ok=True)
    with zipfile.ZipFile(f"out/{k}.zip", "w") as _zip:
        for file in v:
            _zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
    zips.append(f"out/{k}.zip")

print('\n'.join(zips))
