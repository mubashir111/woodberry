with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

# I need to completely replace the service card section.
# I will use regex to find the block.
import re

new_services_css = """
.service-card {
  position: relative;
  background: transparent;
  padding: 0;
  border: none;
  border-radius: 0;
  display: flex;
  flex-direction: column;
  transition: transform 0.4s ease;
  overflow: visible;
}

.service-card:hover {
  transform: translateY(-4px);
}

.service-img img {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  display: block;
}

.service-content {
  padding: 24px 0 0;
  position: relative;
}

.service-title-wrap {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 12px;
}

.service-num {
  font-family: var(--serif);
  font-size: 1.1rem;
  color: var(--accent);
  font-style: italic;
  font-weight: 400;
}

.service-title {
  font-family: var(--serif);
  font-size: 1.5rem;
  margin-bottom: 0;
  color: var(--text);
  line-height: 1.2;
}

.service-desc {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-top: 12px;
  margin-bottom: 24px;
  line-height: 1.6;
}

.service-list {
  list-style: none;
  padding: 0;
  border-top: 1px solid rgba(0,0,0,0.06);
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

# Replace everything from @media (min-width: 900px) { \n  .service-card:nth-child(2) ... down to .service-list li:hover
css = re.sub(r'\/\* Break the symmetry trap by offsetting the middle card \*\/.*?\.service-list li:hover\s*\{.*?\}', new_services_css, css, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("Reverted to clean minimalist layout.")
