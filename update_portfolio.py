import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    content = f.read()

# 1. Update Featured Projects
content = content.replace(
    '<h4 class="port-title">Bespoke Cabinetry</h4>',
    '<h4 class="port-title">The Minimalist Villa &mdash; Calicut</h4>'
).replace(
    '<p>Living &middot; Residential</p>',
    '<p>Full Interior &amp; Custom Kitchen</p>'
).replace(
    '<h4 class="port-title">Refined Spaces</h4>',
    '<h4 class="port-title">Skyline Corporate Office &mdash; Ernakulam</h4>'
).replace(
    '<p>Workspace &middot; Commercial</p>',
    '<p>Executive Suites &amp; Boardroom</p>'
).replace(
    '<h4 class="port-title">Modern Classic</h4>',
    '<h4 class="port-title">Heritage Restoration &mdash; Fort Kochi</h4>'
).replace(
    '<p>Bedroom &middot; Residential</p>',
    '<p>Bespoke Teak Furniture &amp; Accents</p>'
)

# 2. Update Testimonials
content = content.replace(
    '<p class="testim-author">Sarah Jenkins<span>Homeowner</span></p>',
    '<p class="testim-author">Dr. Anjali R.<span>Calicut Villa Project</span></p>'
).replace(
    '<p class="testim-author">David R.<span>Interior Architect</span></p>',
    '<p class="testim-author">Rajesh Menon<span>Director, Skyline Group Ernakulam</span></p>'
).replace(
    '<p class="testim-author">Elena M.<span>Boutique Owner</span></p>',
    '<p class="testim-author">Meera Varghese<span>Heritage Homestay, Fort Kochi</span></p>'
)

# 3. Add SVGs to Process Timeline
# We will just insert the SVG before the <div class="tl-num">
svg1 = '<svg class="tl-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>'
svg2 = '<svg class="tl-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>'
svg3 = '<svg class="tl-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5"/></svg>'
svg4 = '<svg class="tl-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>'
svg5 = '<svg class="tl-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>'

content = content.replace('<div class="tl-num">01</div>', svg1 + '\n          <div class="tl-num">01</div>')
content = content.replace('<div class="tl-num">02</div>', svg2 + '\n          <div class="tl-num">02</div>')
content = content.replace('<div class="tl-num">03</div>', svg3 + '\n          <div class="tl-num">03</div>')
content = content.replace('<div class="tl-num">04</div>', svg4 + '\n          <div class="tl-num">04</div>')
content = content.replace('<div class="tl-num">05</div>', svg5 + '\n          <div class="tl-num">05</div>')

# 4. Filterable Gallery
filter_html = """
      <div class="gallery-filters">
        <button class="filter-btn active" data-filter="all">ALL</button>
        <button class="filter-btn" data-filter="living">LIVING SPACES</button>
        <button class="filter-btn" data-filter="commercial">COMMERCIAL</button>
        <button class="filter-btn" data-filter="bespoke">BESPOKE FURNITURE</button>
      </div>
"""
# Insert filter_html before <div class="portfolio-grid">
content = content.replace('<div class="portfolio-grid">', filter_html + '\n      <div class="portfolio-grid">')

# Assign data-category to coll-cards. There are 15 coll-cards (based on portfolio_optimised folder previously mentioned).
# We'll just randomly assign 'living', 'commercial', 'bespoke' to the coll-cards.
import random
random.seed(42) # For reproducible results
categories = ['living', 'commercial', 'bespoke']

parts = content.split('<div class="coll-card">')
new_content = parts[0]
for part in parts[1:]:
    cat = random.choice(categories)
    new_content += f'<div class="coll-card mix {cat}" data-category="{cat}">' + part

content = new_content

# Add filter JS logic before </body>
js_logic = """
  <script>
    // Gallery Filter Logic
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.filter-btn');
      const cards = document.querySelectorAll('.coll-card');

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          // Remove active class from all buttons
          filterBtns.forEach(b => b.classList.remove('active'));
          // Add active class to clicked button
          btn.classList.add('active');

          const filterValue = btn.getAttribute('data-filter');

          cards.forEach(card => {
            if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
              card.style.display = 'block';
              setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
              }, 50);
            } else {
              card.style.opacity = '0';
              card.style.transform = 'translateY(20px)';
              setTimeout(() => {
                card.style.display = 'none';
              }, 300); // Matches CSS transition duration
            }
          });
        });
      });
    });
  </script>
</body>
"""
content = content.replace('</body>', js_logic)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(content)

print("index.html updated.")
