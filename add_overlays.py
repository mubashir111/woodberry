import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Add overlay back to the masonry items
def add_overlay(match):
    full_tag = match.group(0)
    category = match.group(1).capitalize()
    return f'{full_tag}\n            <div class="masonry-overlay fade-up"><span>{category} Collection</span></div>'

html = re.sub(r'<div class="masonry-item mix (.*?)" data-category=".*?">\s*<img src=".*?" alt=".*?" loading="lazy" />', add_overlay, html)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Added text overlays to masonry items.")
