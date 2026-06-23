import re

with open("/Users/mubashirt/websites/woodwill/css/index.css", "r") as f:
    lines = f.readlines()

with open("/Users/mubashirt/websites/woodwill/css/index.css", "w") as f:
    for i, line in enumerate(lines):
        # We know lines 162-171 were wrongly added. Let's just write everything except those.
        if 161 <= i <= 169:
            continue
        
        # We also need to add max-width to the actual .hero-sub
        if ".hero-sub {" in line:
            f.write(line)
            f.write("  max-width: 600px;\n")
        else:
            f.write(line)

print("CSS cleaned.")
