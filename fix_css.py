import re

with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    content = f.read()

# Remove .hdr-bottom-nav blocks
content = re.sub(r'\.hdr-bottom-nav\s*\{[^}]*\}', '', content)
content = re.sub(r'#site-header\.scrolled \.hdr-bottom-nav\s*\{[^}]*\}', '', content)
content = re.sub(r'\.hdr-bottom-inner\s*\{[^}]*\}', '', content)
content = re.sub(r'\.cat-link\s*\{[^}]*\}', '', content)
content = re.sub(r'\.cat-link:hover\s*\{[^}]*\}', '', content)
content = re.sub(r'#site-header\.scrolled \.cat-link\s*\{[^}]*\}', '', content)
content = re.sub(r'#site-header\.scrolled \.cat-link:hover\s*\{[^}]*\}', '', content)

# Remove from media query
content = content.replace("  .hdr-bottom-nav,\n", "")

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(content)

print("CSS updated.")
