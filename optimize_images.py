import os
import hashlib
import subprocess
import shutil

src_dir = "/Users/mubashirt/websites/woodwill/images/portfolio2"
dest_dir = "/Users/mubashirt/websites/woodwill/images/portfolio_optimized"

if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
os.makedirs(dest_dir)

hashes = {}
files_to_process = []

for filename in sorted(os.listdir(src_dir)):
    if filename.startswith('.'):
        continue
    filepath = os.path.join(src_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        
        if filehash not in hashes:
            hashes[filehash] = filename
            files_to_process.append(filepath)
        else:
            print(f"Skipping duplicate: {filename} (same as {hashes[filehash]})")

print(f"Found {len(files_to_process)} unique files to process.")

counter = 1
for filepath in files_to_process:
    new_name = f"woodberry-interior-gallery-{counter}.jpg"
    dest_path = os.path.join(dest_dir, new_name)
    print(f"Processing {filepath} -> {new_name}...")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "80", "-Z", "1200", filepath, "--out", dest_path], stdout=subprocess.DEVNULL)
    counter += 1

print("Done!")
