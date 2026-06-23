with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

new_styles = """
/* Gallery Filters */
.gallery-filters {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-bottom: 64px;
  flex-wrap: wrap;
}

.filter-btn {
  background: transparent;
  border: none;
  font-family: var(--sans);
  font-size: var(--f-label);
  font-weight: 500;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  cursor: pointer;
  padding: 8px 0;
  position: relative;
  transition: color 0.3s ease;
}

.filter-btn::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 1px;
  background-color: var(--accent);
  transition: width 0.3s ease;
}

.filter-btn:hover {
  color: var(--text);
}

.filter-btn.active {
  color: var(--text);
}

.filter-btn.active::after {
  width: 100%;
}

/* Timeline Icons */
.tl-icon {
  width: 32px;
  height: 32px;
  color: var(--accent);
  margin-bottom: 16px;
  opacity: 0.8;
  transition: transform 0.4s ease;
}

.timeline-card:hover .tl-icon {
  transform: scale(1.1) translateY(-4px);
  color: var(--text);
}

/* Base state for coll-card transitions (filtering) */
.coll-card {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
"""

with open("/Users/mubashirt/websites/woodwill/css/index.css", "a") as f:
    f.write("\n" + new_styles)

print("CSS updated.")
