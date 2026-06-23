import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# I need to add </section> right after the closing </div> of <div class="masonry-gallery-wrap">
# Since it's followed by <!-- ======================================== TESTIMONIALS & CTA
pattern = r'(      </div>\s*)(    <!-- ========================================\s*TESTIMONIALS)'
html = re.sub(pattern, r'\1    </section>\n\n\2', html)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Fixed closing section tag.")
