import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Add overlay text to all masonry items
# Find <div class="masonry-item mix CATEGORY" data-category="CATEGORY">
#   <img src="..." alt="ALT_TEXT" loading="lazy">
# </div>

def replacer(match):
    full_match = match.group(0)
    category = match.group(1).capitalize()
    
    # We will insert the overlay right before the closing div
    # Wait, the closing div is matched in group 0? No, let's just match the start of the item and the img tag
    return full_match

# A safer approach is to replace <img> with <img>\n<div class="masonry-overlay"><span>Category</span></div>
def img_replacer(match):
    img_tag = match.group(0)
    # The category can be derived from the wrapper, but let's just use the alt text if possible.
    # To do this safely, let's find the whole masonry-item block
    pass

masonry_blocks = re.findall(r'(<div class="masonry-item mix (.*?)" data-category=".*?">\s*<img src=".*?" alt="(.*?)" loading="lazy">\s*)</div>', html)

for block in masonry_blocks:
    full_string = block[0] + "</div>"
    category = block[1].capitalize()
    alt_text = block[2]
    
    # Capitalize the category name for display
    display_text = alt_text if alt_text else category
    
    new_string = block[0] + f'  <div class="masonry-overlay"><span>{display_text}</span></div>\n        </div>'
    html = html.replace(full_string, new_string)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Updated HTML.")

# Update CSS
with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

overlay_css = """
/* Masonry Overlay */
.masonry-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 24px;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: #fff;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.4s ease, transform 0.4s ease;
  pointer-events: none;
  display: flex;
  align-items: flex-end;
}

.masonry-overlay span {
  font-family: var(--sans);
  font-size: 0.9rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 500;
}

.masonry-item:hover .masonry-overlay {
  opacity: 1;
  transform: translateY(0);
}

@media (max-width: 900px) {
  .masonry-overlay {
    opacity: 1;
    transform: translateY(0);
    padding: 16px;
    background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
  }
}
"""

# Replace the @media (max-width: 600px) block for masonry-grid
mobile_css_replacement = """@media (max-width: 600px) {
  .masonry-grid {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 16px;
    padding-bottom: 24px;
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  .masonry-grid::-webkit-scrollbar {
    display: none;
  }
  .masonry-item {
    min-width: 80vw;
    scroll-snap-align: center;
    margin-bottom: 0; /* Override masonry vertical margin */
  }
  .masonry-item img {
    height: 400px; /* Fixed height so the horizontal row looks neat */
    object-fit: cover;
  }
}"""

css = css.replace("""@media (max-width: 600px) {
  .masonry-grid {
    column-count: 1;
  }
}""", mobile_css_replacement)

# Append overlay css
css += "\n" + overlay_css

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("Updated CSS.")
