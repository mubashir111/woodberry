import re

with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

# 2. Hero Content Padding
hero_css = """
@media (min-width: 900px) {
  .hero-content {
    padding-left: 60px;
  }
}
"""
css += "\n" + hero_css

# 3. Testimonials Polish
css = re.sub(
    r'\.testimonial-card\s*\{.*?\}',
    '.testimonial-card {\n  background: var(--bg-card);\n  padding: 40px;\n  border-radius: 12px;\n  box-shadow: 0 4px 20px rgba(0,0,0,0.05);\n  position: relative;\n}',
    css,
    flags=re.DOTALL
)

# Add large quotation mark
testimonial_quotes = """
.testimonial-card::before {
  content: '"';
  position: absolute;
  top: 10px;
  left: 20px;
  font-family: var(--serif);
  font-size: 120px;
  color: var(--accent);
  opacity: 0.15;
  line-height: 1;
}
"""
css += "\n" + testimonial_quotes

# 4. Icons Section (Quality Without Compromise)
css = re.sub(
    r'\.q-icon svg\s*\{\s*width:\s*24px;\s*height:\s*24px;\s*\}',
    '.q-icon svg {\n  width: 32px;\n  height: 32px;\n}',
    css
)
css = re.sub(
    r'\.quality-item\s*\{\s*display:\s*flex;\s*align-items:\s*center;\s*gap:\s*16px;\s*\}',
    '.quality-item {\n  display: flex;\n  align-items: center;\n  gap: 24px;\n}',
    css
)
css = re.sub(
    r'\.q-text\s*\{\s*font-family:\s*var\(--sans\);\s*font-size:\s*0\.85rem;\s*letter-spacing:\s*0\.05em;\s*text-transform:\s*uppercase;\s*color:\s*var\(--text\);\s*\}',
    '.q-text {\n  font-family: var(--sans);\n  font-size: 0.95rem;\n  font-weight: 600;\n  letter-spacing: 0.05em;\n  text-transform: uppercase;\n  color: var(--text);\n}',
    css
)

# 5. Button Hover Animation
css = re.sub(
    r'\.btn-primary\s*\{\s*display:\s*inline-block;.*?\}',
    '.btn-primary {\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n  padding: 18px 40px;\n  background: var(--text);\n  color: var(--bg);\n  font-family: var(--sans);\n  font-size: 0.85rem;\n  font-weight: 500;\n  letter-spacing: 0.1em;\n  text-transform: uppercase;\n  text-decoration: none;\n  border-radius: 4px;\n  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);\n}\n.btn-primary:hover {\n  background: var(--accent);\n  transform: translateY(-4px);\n  box-shadow: 0 12px 24px rgba(155, 108, 66, 0.3);\n}',
    css,
    flags=re.DOTALL
)

# 6. Footer Upgrades
css = re.sub(
    r'\.footer-socials a svg\s*\{\s*width:\s*16px;\s*height:\s*16px;\s*\}',
    '.footer-socials a svg {\n  width: 24px;\n  height: 24px;\n}',
    css
)
css = re.sub(
    r'\.footer-grid\s*\{\s*display:\s*grid;\s*gap:\s*48px;\s*\}',
    '.footer-grid {\n  display: grid;\n  gap: 64px;\n}',
    css
)

# 7. Global Spacing
css = css.replace("--s6: 64px;", "--s6: 48px;")
css = css.replace("--s7: 88px;", "--s7: 64px;")
css = css.replace("--s8: 128px;", "--s8: 96px;")

# Scroll Animation Classes
animation_css = """
/* Scroll Animations */
.fade-up {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1), transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
.fade-up.is-visible {
  opacity: 1;
  transform: translateY(0);
}
"""
css += "\n" + animation_css

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("CSS updates complete.")
