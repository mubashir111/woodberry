import re
import random

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    content = f.read()

# 1. We need to extract the gallery filters block so we can move it
filters_match = re.search(r'<div class="gallery-filters">.*?</div>', content, re.DOTALL)
if filters_match:
    filters_html = filters_match.group(0)
    # Remove the old filters from wherever they are
    content = content.replace(filters_html, "")

# 2. We need to remove the entire <div class="portfolio-grid"> ... </div> block
portfolio_grid_pattern = re.compile(r'<div class="portfolio-grid">.*?</div>\s*</div>\s*</div>', re.DOTALL)
# Wait, parsing HTML with regex for nested divs is tricky.
# Let's just remove from '<span class="eyebrow">Featured Projects</span>' down to '<div class="masonry-gallery-wrap">'
remove_pattern = re.compile(r'<span class="eyebrow">Featured Projects</span>.*?<!-- EXTENDED GALLERY \(MASONRY\) -->', re.DOTALL)

# Let's replace that whole section with just the eyebrow and h2, plus the filters
new_header = """<span class="eyebrow">Featured Portfolio</span>
        <h2 class="section-h2">Crafted Spaces. Lasting Impressions.</h2>
        <p class="body-copy" style="max-width: 700px; margin: 0 0 var(--s5)">
          Explore our portfolio featuring custom furniture, elegant interiors,
          premium woodwork, bespoke décor solutions, and thoughtfully designed
          spaces.
        </p>

"""
if filters_match:
    new_header += filters_html + "\n\n"

new_header += '      <!-- EXTENDED GALLERY (MASONRY) -->'

content = remove_pattern.sub(new_header, content)

# 3. Add data-category to all .masonry-item elements
random.seed(42)
categories = ['living', 'commercial', 'bespoke']

def replace_masonry_item(match):
    cat = random.choice(categories)
    return f'<div class="masonry-item mix {cat}" data-category="{cat}">'

content = re.sub(r'<div class="masonry-item">', replace_masonry_item, content)

# 4. Change "Extended Gallery" title to something empty or just remove it since we have the H2 now
content = content.replace('<h3 class="masonry-title">Extended Gallery</h3>', '')

# 5. Update JS to target .masonry-item instead of .coll-card
content = content.replace("const cards = document.querySelectorAll('.coll-card');", "const cards = document.querySelectorAll('.masonry-item');")

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(content)

print("HTML fixed.")
