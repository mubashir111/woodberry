import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# 1. Truncate Masonry Items
# Find all masonry items
masonry_blocks = re.findall(r'<div class="masonry-item .*?</div>', html, flags=re.DOTALL)
if len(masonry_blocks) > 9:
    # Get the HTML to replace
    # Keep the first 9
    kept_items = "\n          ".join(masonry_blocks[:9])
    
    # We will replace the content between <div class="masonry-grid"> and the closing </div>
    # Let's extract the whole wrapper
    old_grid = re.search(r'<div class="masonry-grid">.*?</div>\n      </div>', html, flags=re.DOTALL)
    if old_grid:
        new_grid = f'<div class="masonry-grid">\n          {kept_items}\n        </div>\n      </div>\n      <div style="text-align: center; margin-top: 60px;">\n        <a href="#" class="btn-primary fade-up">VIEW MORE PROJECTS &rarr;</a>\n      </div>'
        html = html.replace(old_grid.group(0), new_grid)

# 2. Add IntersectionObserver JS at the end of body
js_script = """
    <script>
      // Intersection Observer for Scroll Animations
      document.addEventListener("DOMContentLoaded", () => {
        const observerOptions = {
          root: null,
          rootMargin: "0px",
          threshold: 0.15
        };

        const observer = new IntersectionObserver((entries, observer) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              observer.unobserve(entry.target);
            }
          });
        }, observerOptions);

        document.querySelectorAll('.fade-up').forEach(el => {
          observer.observe(el);
        });
      });
    </script>
  </body>
"""
html = html.replace("  </body>", js_script)

# 3. Add fade-up classes
html = html.replace('<div class="hero-content">', '<div class="hero-content fade-up">')
html = html.replace('<h2 class="section-h2">', '<h2 class="section-h2 fade-up">')
html = html.replace('<div class="testimonial-card">', '<div class="testimonial-card fade-up">')
html = html.replace('<div class="quality-item">', '<div class="quality-item fade-up">')
html = html.replace('<div class="footer-col">', '<div class="footer-col fade-up">')

# 4. Footer Logo
html = html.replace(
    '<img src="images/logo1.png" alt="Woodberry Logo" class="footer-logo-img" />',
    '<img src="images/logo1.png" alt="Woodberry Logo" class="footer-logo-img" style="width: 140px;" />'
)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("HTML updates complete.")
