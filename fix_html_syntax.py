import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    content = f.read()

content = content.replace('<!-- EXTENDED GALLERY (MASONRY) -->', '</div>\n\n      <!-- EXTENDED GALLERY (MASONRY) -->')

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(content)

print("HTML syntax fixed.")
