with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    css = f.read()

masonry_styles = """
/* Force varying heights for a true masonry effect */
.masonry-item:nth-child(5n + 1) img {
  aspect-ratio: 3 / 4;
  object-fit: cover;
}
.masonry-item:nth-child(5n + 2) img {
  aspect-ratio: 4 / 3;
  object-fit: cover;
}
.masonry-item:nth-child(5n + 3) img {
  aspect-ratio: 1 / 1.2;
  object-fit: cover;
}
.masonry-item:nth-child(5n + 4) img {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
.masonry-item:nth-child(5n + 5) img {
  aspect-ratio: 1 / 1;
  object-fit: cover;
}
"""

with open("/Users/mubashirt/websites/woodwill/css/index.css", "a") as f:
    f.write("\n" + masonry_styles)

print("Masonry styles added.")
