with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

# Remove the symmetry trap offset because it makes it look misaligned to some users
css = css.replace("""/* Break the symmetry trap by offsetting the middle card */
@media (min-width: 900px) {
  .service-card:nth-child(2) {
    margin-top: 80px;
  }
}""", "")

# Add editorial luxury styling
new_service_css = """
/* Break the symmetry trap by offsetting the middle card */
@media (min-width: 900px) {
  .service-card:nth-child(2) {
    margin-top: 40px;
  }
}

.service-card {
  position: relative;
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 0, 0, 0.05);
  padding-bottom: 24px;
  overflow: hidden;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.06);
}

.service-img img {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  display: block;
}

.service-content {
  padding: 32px 24px 0;
  position: relative;
}

.service-title-wrap {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 16px;
  position: relative;
}

.service-num {
  font-family: var(--serif);
  font-size: 5rem;
  color: var(--accent);
  opacity: 0.15;
  font-style: italic;
  font-weight: 300;
  position: absolute;
  top: -40px;
  left: -10px;
  z-index: 0;
  pointer-events: none;
}

.service-title {
  font-family: var(--serif);
  font-size: 1.5rem;
  margin-bottom: 8px;
  color: var(--text);
  z-index: 1;
  position: relative;
}

.service-desc {
  font-size: var(--f-body);
  color: var(--text-muted);
  margin-bottom: 24px;
  line-height: 1.6;
}

.service-list {
  list-style: none;
  padding: 0;
  border-top: 1px solid rgba(0,0,0,0.05);
  padding-top: 16px;
}

.service-list li {
  font-size: 0.85rem;
  color: var(--text);
  margin-bottom: 12px;
  position: relative;
  padding-left: 20px;
  transition: transform 0.2s ease, color 0.2s ease;
}

.service-list li::before {
  content: "—";
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 600;
  opacity: 0.6;
}

.service-list li:hover {
  transform: translateX(4px);
  color: var(--accent);
}
"""

# We need to replace the old .service-card rules with our new ones
# This is tricky with simple string replace, so let's just append to the end of the file.
# CSS overrides work by specificity/order, but appending !important might be needed if specificity matches.
# Wait, actually let's use regex to replace the block from .service-card down to .service-list li:hover

import re
css = re.sub(r'\.service-card\s*\{.*?(?=\/\* Process \*\/)', new_service_css + '\n\n', css, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("CSS upgraded.")
