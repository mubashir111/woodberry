import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Duplicate some masonry items to have hidden ones
masonry_blocks = re.findall(r'<div class="masonry-item .*?</div>', html, flags=re.DOTALL)
if len(masonry_blocks) > 0:
    # Let's create 6 hidden blocks by duplicating the first 6
    hidden_blocks = []
    for block in masonry_blocks[:6]:
        # Add a class "hidden-project"
        modified_block = block.replace('class="masonry-item', 'class="masonry-item hidden-project"')
        hidden_blocks.append(modified_block)
    
    all_blocks_html = "\n          ".join(hidden_blocks)
    
    # Insert them before the closing of masonry-grid
    html = html.replace('</div>\n      </div>\n      <div style="text-align: center; margin-top: 60px;">', 
                        f'\n          {all_blocks_html}\n        </div>\n      </div>\n      <div style="text-align: center; margin-top: 60px;">')

# Add JS for the button
js_logic = """
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const viewMoreBtn = document.querySelector('.btn-primary[href="#"]');
    if (viewMoreBtn && viewMoreBtn.textContent.includes("VIEW MORE PROJECTS")) {
      viewMoreBtn.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent jump to top
        
        const hiddenProjects = document.querySelectorAll('.hidden-project');
        hiddenProjects.forEach(proj => {
          proj.style.display = 'block';
          // Small delay for fade-in effect if desired
          setTimeout(() => {
            proj.classList.add('is-visible');
          }, 50);
        });
        
        // Hide button after clicking
        viewMoreBtn.parentElement.style.display = 'none';
      });
    }
  });
</script>
"""

if "VIEW MORE PROJECTS" in js_logic: # Just a check
    html = html.replace("</body>", js_logic + "\n</body>")

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

with open("/Users/mubashirt/websites/woodwill/css/index.css", "a") as f:
    f.write("\n.hidden-project { display: none; }\n")

print("Fixed View More Projects button.")
