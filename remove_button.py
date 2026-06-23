import re

# Update HTML
with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# 1. Remove hidden-project class
html = html.replace("hidden-project", "")

# 2. Remove View More button
# <div style="text-align: center; margin-top: 60px;">
#   <a href="#" class="btn-primary fade-up">VIEW MORE PROJECTS &rarr;</a>
# </div>
btn_pattern = r'<div style="text-align: center; margin-top: 60px;">\s*<a href="#" class="btn-primary fade-up">VIEW MORE PROJECTS &rarr;</a>\s*</div>'
html = re.sub(btn_pattern, "", html)

# 3. Remove JS logic
js_pattern = r'<script>\s*document\.addEventListener\("DOMContentLoaded", \(\) => \{\s*const viewMoreBtn = document\.querySelector\(\'\.btn-primary\[href="#"\]\'\);.*?</script>'
html = re.sub(js_pattern, "", html, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

# Update CSS
with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

# 4. Remove .hidden-project class from CSS
css = css.replace(".hidden-project { display: none; }", "")

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("Removed view more button and unhid all images.")
