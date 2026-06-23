import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# We need to completely rebuild the masonry grid to have 16 images and no view more button.
# First, let's locate the masonry grid wrapper.
# From: <div class="masonry-gallery-wrap">
# To:   </section>
# Wait, the masonry grid is inside a section or just the wrap?
# Let's extract exactly what's there and replace it.
masonry_start = html.find('<div class="masonry-gallery-wrap">')
# Find the next section: <section class="section-testimonials">
masonry_end = html.find('<section class="section-testimonials">')

if masonry_start != -1 and masonry_end != -1:
    categories = ["bespoke", "living", "commercial"]
    # Let's just generate 16 items. The original order might have been specific, but we'll distribute categories.
    new_grid = '      <div class="masonry-gallery-wrap">\n        <div class="masonry-grid">\n'
    for i in range(1, 17):
        cat = categories[i % 3]
        new_grid += f"""          <div class="masonry-item mix {cat}" data-category="{cat}">
            <img src="images/portfolio_optimized/woodberry-interior-gallery-{i}.jpg" alt="Woodberry Gallery Image {i}" loading="lazy" />
          </div>\n"""
    new_grid += '        </div>\n      </div>\n\n    <!-- ========================================\n'
    
    html = html[:masonry_start] + new_grid + html[masonry_end - 47:] # 47 is for the comment block "TESTIMONIALS & CTA"

# Clean up any leftover VIEW MORE button if the above replace didn't catch it
html = re.sub(r'<div[^>]*?>\s*<a href="#" class="btn-primary fade-up">VIEW MORE PROJECTS &rarr;</a>\s*</div>', '', html)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Rebuilt masonry grid with 16 images and removed button.")
