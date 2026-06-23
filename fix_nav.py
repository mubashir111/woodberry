import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    content = f.read()

# 1. Remove hdr-bottom-nav completely
start_bottom = content.find('<!-- Secondary Category Nav Bar -->')
end_bottom = content.find('<!-- Mobile Menu Drawer -->')
content = content[:start_bottom] + content[end_bottom:]

# 2. Build the new COLLECTIONS mega menu
mega_menu_html = """
          <div class="nav-dropdown-wrapper">
            <a href="#portfolio" class="hdr-nav-link">COLLECTIONS</a>
            <div class="mega-menu">
              <div class="mega-menu-inner">
                <div class="mega-col">
                  <h4 class="mega-title"><span class="mega-num">01 /</span> Bespoke Furniture</h4>
                  <ul class="mega-list">
                    <li><a href="#">Sofas & Sectionals</a></li>
                    <li><a href="#">Dining Chairs</a></li>
                    <li><a href="#">Dining Tables</a></li>
                    <li><a href="#">Storage Units</a></li>
                  </ul>
                </div>
                <div class="mega-col">
                  <h4 class="mega-title"><span class="mega-num">02 /</span> Architectural Spaces</h4>
                  <ul class="mega-list">
                    <li><a href="#">Living Room Design</a></li>
                    <li><a href="#">Bedroom Design</a></li>
                    <li><a href="#">Kitchen Design</a></li>
                    <li><a href="#">Workspace Design</a></li>
                  </ul>
                </div>
                <div class="mega-col">
                  <h4 class="mega-title"><span class="mega-num">03 /</span> Curated Accents</h4>
                  <ul class="mega-list">
                    <li><a href="#">Wall Art & Decor</a></li>
                    <li><a href="#">Rugs & Carpets</a></li>
                    <li><a href="#">Vases & Sculptures</a></li>
                    <li><a href="#">Lighting Setup</a></li>
                  </ul>
                </div>
                <div class="mega-col-img">
                  <img src="images/portfolio_optimized/woodberry-interior-gallery-1.jpg" alt="Living Room Collection" />
                  <p class="mega-img-subtitle">The Oak Series<br /><span>Handcrafted minimalist forms for contemporary living.</span></p>
                  <a href="#" class="mega-img-link">View Featured Collection &rarr;</a>
                </div>
              </div>
            </div>
          </div>
"""

# Replace the existing COLLECTIONS link
content = content.replace('<a href="#portfolio" class="hdr-nav-link">COLLECTIONS</a>', mega_menu_html.strip())

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(content)

print("Nav updated.")
