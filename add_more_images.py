import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Add items 17 and 18 before the closing of the masonry-grid
item_17 = """        <div class="masonry-item mix bespoke" data-category="bespoke">
          <img src="images/portfolio_optimized/woodberry-interior-gallery-17.jpg" alt="Woodberry Gallery Image 17" loading="lazy" />
          <div class="masonry-overlay fade-up"><span>Bespoke Collection</span></div>
        </div>
"""
item_18 = """        <div class="masonry-item mix living" data-category="living">
          <img src="images/portfolio_optimized/woodberry-interior-gallery-18.jpg" alt="Woodberry Gallery Image 18" loading="lazy" />
          <div class="masonry-overlay fade-up"><span>Living Collection</span></div>
        </div>
"""

# Find the end of the masonry grid
html = html.replace('      </div>\n    </section>\n\n    <!-- ========================================', f'{item_17}{item_18}      </div>\n    </section>\n\n    <!-- ========================================')

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Added images 17 and 18.")
