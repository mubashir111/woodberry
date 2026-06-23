import re

with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

new_coll_foot = """
.coll-card-foot {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
  padding: 16px 0 0 0;
  background: transparent;
  margin-top: 0;
  gap: 4px;
}
"""

css = re.sub(r'\.coll-card-foot\s*\{[^}]*\}', new_coll_foot.strip(), css, count=1)

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    f.write(css)

print("CSS updated.")
