import re

with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

# Add media query for tailored-container
mobile_css = """
@media (max-width: 900px) {
  .tailored-container {
    grid-template-columns: 1fr;
    gap: 40px;
    text-align: center;
  }
  .tailored-icons {
    flex-wrap: wrap;
    justify-content: center;
    gap: 32px;
  }
}
"""

css += "\n" + mobile_css

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("Fixed mobile tailored section.")
