"""
Zips all files listed in manifest["include"]
"""
import json
import os
import zipfile

with open("manifest.json", "r") as f:
    manifest = json.load(f)

to_be_zipped = []
for include in manifest["include"]:
    if os.path.isdir(include):
        for path, dirs, files in os.walk(include):
            for file in files:
                to_be_zipped.append(f"{path}/{file}")
    else:
        to_be_zipped.append(include)

with zipfile.ZipFile("include.zip", "w") as _zip:
    for file in to_be_zipped:
        _zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
