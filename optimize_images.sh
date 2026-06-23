#!/bin/bash
set -e

DIR="/Users/mubashirt/websites/woodwill/images/portfolio2"
DEST="/Users/mubashirt/websites/woodwill/images/portfolio_optimized"
mkdir -p "$DEST"

cd "$DIR"

# Step 1: Remove obvious duplicates from our processing list
TMP_DIR=$(mktemp -d)
cp * "$TMP_DIR/"
cd "$TMP_DIR"
rm -f *" (1)".* *" (2)".* 

# Step 2: Convert and Resize
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

echo "Done! Images optimized in $DEST"
rm -rf "$TMP_DIR"
