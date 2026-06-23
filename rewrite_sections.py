import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    content = f.read()

# 1. Remove "Why Choose Woodberry?" and .why-list
content = re.sub(r'<span class="eyebrow" style="margin-top: 24px; display: block"\s*>Why Choose Woodberry\?</span\s*>\s*<ul class="why-list" style="margin-top: 12px">.*?</ul>', '', content, flags=re.DOTALL)

# 2. Replace .section-quality with .section-standard
new_standard_html = """
    <!-- ========================================
     THE WOODBERRY STANDARD
     ======================================== -->
    <section class="section-standard" id="standard">
      <div class="container" style="text-align: center; max-width: 800px; margin: 0 auto; padding: 120px 20px;">
        <span class="eyebrow" style="color: var(--accent); margin-bottom: 24px; display: block; letter-spacing: 0.2em;">THE WOODBERRY STANDARD</span>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(32px, 5vw, 56px); font-weight: 300; line-height: 1.1; color: var(--text); margin-bottom: 32px;">
          Uncompromising Quality.<br/>Timeless Design.
        </h2>
        <p class="body-copy" style="font-size: 1.1rem; color: var(--text-muted);">
          We believe furniture should be more than beautiful—it should stand the test of time. Every piece reflects our commitment to superior materials, expert craftsmanship, and bespoke personalization. No shortcuts. Just enduring luxury.
        </p>
      </div>
    </section>
"""
content = re.sub(r'<section class="section-quality">.*?</section>', new_standard_html.strip(), content, flags=re.DOTALL)

# 3. Move .section-masonry-full to after .section-services
# Find the masonry section
masonry_start = content.find('<!-- ========================================\n     EXTENDED GALLERY (FULL WIDTH)')
if masonry_start == -1:
    masonry_start = content.find('<section class="section-masonry-full"')

masonry_end = content.find('</section>', masonry_start) + 10
masonry_html = content[masonry_start:masonry_end]

# Remove it from its current position
content = content[:masonry_start] + content[masonry_end:]

# Find the end of .section-services
services_start = content.find('<section class="section-services"')
services_end = content.find('</section>', services_start) + 10

# Insert masonry after services
content = content[:services_end] + "\n\n" + masonry_html + content[services_end:]

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(content)

print("Rewritten.")
