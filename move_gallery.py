import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    content = f.read()

# Find the philosophy section end
phil_end = content.find("</section>", content.find("class=\"section-philosophy\"")) + 10

# Find the gallery start
gallery_start_comment = "<!-- EXTENDED GALLERY (MASONRY) -->"
gallery_start = content.find(gallery_start_comment)

# Find the end of the masonry-gallery-wrap div
# It ends right before the closing </section> of section-portfolio
portfolio_end = content.find("</section>", gallery_start)

gallery_html = content[gallery_start:portfolio_end]

# Remove the gallery from the original location
new_content = content[:gallery_start] + content[portfolio_end:]

# Insert the gallery after the philosophy section
new_gallery_block = f"""
    <!-- ========================================
     EXTENDED GALLERY (FULL WIDTH)
     ======================================== -->
    <section class="section-masonry-full" id="gallery">
{gallery_html}
    </section>
"""

new_content = new_content[:phil_end] + new_gallery_block + new_content[phil_end:]

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(new_content)

print("Moved gallery.")
