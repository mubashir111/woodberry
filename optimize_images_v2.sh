#!/bin/bash
set -e

DIR="/Users/mubashirt/websites/woodwill/images/portfolio2"
DEST="/Users/mubashirt/websites/woodwill/images/portfolio_optimized"
# clean up destination folder first
rm -rf "$DEST"
mkdir -p "$DEST"

cd "$DIR"

TMP_DIR=$(mktemp -d)
cp * "$TMP_DIR/"
cd "$TMP_DIR"

# Deduplicate by hash
declare -A hashes
for file in *; do
    hash=$(md5 -q "$file")
    if [[ -z "${hashes[$hash]}" ]]; then
        hashes[$hash]="$file"
    else
        echo "Removing duplicate: $file (same as ${hashes[$hash]})"
        rm "$file"
    fi
done

# Convert and Resize
COUNTER=1
for img in *; do
  if [ -f "$img" ]; then
    echo "Processing $img..."
    # Convert to jpeg with max width/height of 1200
    NEW_NAME="woodberry-interior-gallery-${COUNTER}.jpg"
    
    # sips allows resizing with --resampleHeightWidthMax
    sips -s format jpeg -s formatOptions 80 -Z 1200 "$img" --out "$DEST/$NEW_NAME" > /dev/null
    
    COUNTER=$((COUNTER + 1))
  fi
done

echo "Done! Processed $((COUNTER - 1)) images."
rm -rf "$TMP_DIR"
