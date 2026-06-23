import re

# 1. Update HTML
with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

new_html = """        <div class="services-grid">
          <div class="service-card">
            <div class="service-img">
              <img src="images/col_living_1780394489698.jpg" alt="Custom Furniture">
            </div>
            <div class="service-content">
              <div class="service-title-wrap">
                <span class="service-num">01</span>
                <h3 class="service-title">Custom Furniture Manufacturing</h3>
              </div>
              <p class="service-desc">Furniture designed exclusively for your space and lifestyle.</p>
              <ul class="service-list">
                <li>Sofas & Seating</li>
                <li>Dining Tables</li>
                <li>Coffee Tables</li>
                <li>TV Units</li>
                <li>Study Units</li>
                <li>Storage Solutions</li>
                <li>Wardrobes</li>
                <li>Custom Wooden Furniture</li>
              </ul>
            </div>
          </div>

          <div class="service-card">
            <div class="service-img">
              <img src="images/col_bedroom_1780394502893.jpg" alt="Interior Design">
            </div>
            <div class="service-content">
              <div class="service-title-wrap">
                <span class="service-num">02</span>
                <h3 class="service-title">Interior Design Solutions</h3>
              </div>
              <p class="service-desc">Transforming spaces with thoughtful design and functionality.</p>
              <ul class="service-list">
                <li>Residential Interiors</li>
                <li>Apartment Interiors</li>
                <li>Villa Interiors</li>
                <li>Office Interiors</li>
                <li>Retail Interiors</li>
                <li>Space Planning</li>
                <li>Material Selection</li>
                <li>Interior Styling</li>
              </ul>
            </div>
          </div>

          <div class="service-card">
            <div class="service-img">
              <img src="images/col_accents_1780394536248.jpg" alt="Bespoke Decor">
            </div>
            <div class="service-content">
              <div class="service-title-wrap">
                <span class="service-num">03</span>
                <h3 class="service-title">Bespoke Décor Elements</h3>
                """

html = re.sub(r'        <div class="services-grid">.*?<h3 class="service-title">Bespoke Décor Elements</h3>\n                ', new_html, html, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

# 2. Update CSS
with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

new_css = """/* Break the symmetry trap by offsetting the middle card */
@media (min-width: 900px) {
  .service-card:nth-child(2) {
    margin-top: 80px;
  }
}

.service-card {
  position: relative;
  background: transparent;
  border-radius: 0;
  overflow: hidden;
  transition: transform 0.4s;
}

.service-card:hover { transform: translateY(-4px); }
.service-img { position: relative; z-index: 1; }
.service-img img {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.service-content {
  padding: 24px 0;
}

.service-title-wrap {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 8px;
}

.service-num {
  font-family: var(--serif);
  font-size: 1.3rem;
  color: var(--accent);
  font-style: italic;
  font-weight: 500;
}

.service-title {
  font-family: var(--serif);
  font-size: 1.4rem;
  margin-bottom: 8px;
  color: var(--text);
}

.service-desc {
  font-size: var(--f-body);
  color: var(--text-muted);
  margin-bottom: 20px;
}

.service-list {
  list-style: none;
  padding: 0;
}

.service-list li {
  font-size: 0.85rem;
  color: var(--text);
  margin-bottom: 12px;
  position: relative;
  padding-left: 0;
}

/* Process */"""

# Let's replace the current CSS block for .service-card down to .service-list li:hover
css = re.sub(r'\.service-card\s*\{.*?(?=\/\* Process \*\/)', new_css + '\n\n', css, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("Reverted HTML and CSS perfectly.")
