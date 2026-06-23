import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Define the exact mathematically balanced order
# Tall: 2, 14, 5, 16, 17, 18
# Normal: 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15
order = [
    2, 1, 3, 14, 4, 6,    # Col 1
    5, 7, 8, 16, 9, 10,   # Col 2
    17, 11, 12, 18, 13, 15 # Col 3
]

categories = ["living", "commercial", "bespoke"]

new_grid = '      <div class="masonry-gallery-wrap">\n        <div class="masonry-grid">\n'
for i, img_num in enumerate(order):
    cat = categories[i % 3]
    # some custom categories to make it mixed
    cat_names = {"living": "Living Collection", "commercial": "Commercial Collection", "bespoke": "Bespoke Collection"}
    new_grid += f"""          <div class="masonry-item mix {cat}" data-category="{cat}">
            <img src="images/portfolio_optimized/woodberry-interior-gallery-{img_num}.jpg" alt="Woodberry Gallery Image {img_num}" loading="lazy" />
            <div class="masonry-overlay fade-up"><span>{cat_names[cat]}</span></div>
          </div>\n"""
new_grid += '        </div>\n      </div>'

# Replace the existing masonry gallery wrap
pattern = r'      <div class="masonry-gallery-wrap">.*?</div>\s*</div>\s*</div>'
html = re.sub(r'      <div class="masonry-gallery-wrap">.*?(?=    </section>)', new_grid + '\n', html, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Balanced the gallery heights.")
