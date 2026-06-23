with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

new_testim_css = """
/* Asymmetrical staggering for social proof */
@media (min-width: 900px) {
  .testim-card:nth-child(2) {
    margin-top: 40px;
  }

  .testim-card:nth-child(3) {
    margin-top: 80px;
  }
}

.testim-card {
  position: relative;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  padding: 40px;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 0;
  display: flex;
  flex-direction: column;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  overflow: hidden;
}

.testim-card::before {
  content: "”";
  position: absolute;
  top: -20px;
  right: 20px;
  font-family: var(--serif);
  font-size: 8rem;
  color: var(--accent);
  opacity: 0.1;
  line-height: 1;
  pointer-events: none;
}

.testim-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.06);
}

.testim-stars {
  display: flex;
  gap: 4px;
  margin-bottom: 24px;
  position: relative;
  z-index: 1;
}

.testim-text {
  font-size: 1.1rem;
  font-family: var(--serif);
  color: var(--text);
  font-style: italic;
  flex-grow: 1;
  line-height: 1.6;
  position: relative;
  z-index: 1;
}

.testim-client {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
  position: relative;
  z-index: 1;
}

.testim-name {
  font-family: var(--serif);
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--text);
  line-height: 1.4;
}
"""

import re
css = re.sub(r'\/\* Asymmetrical staggering for social proof \*\/.*?\.testim-name\s*\{.*?(?=\.testim-avatar)', new_testim_css + '\n\n', css, flags=re.DOTALL)

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("Testimonial CSS upgraded.")
