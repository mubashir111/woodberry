import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Remove any "VIEW MORE PROJECTS" link and its wrapper completely
# Just find the a tag and its surrounding div
html = re.sub(r'<div[^>]*?>\s*<a[^>]*?>VIEW MORE PROJECTS &rarr;</a>\s*</div>', '', html)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Double checked button removal.")
