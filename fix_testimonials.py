import re

with open("/Users/mubashirt/websites/woodwill/index.html", "r") as f:
    html = f.read()

# Testimonial 1
html = html.replace(
    '''            <p class="testim-text">
              "Woodberry Designs transformed our living space with beautifully
              crafted furniture and exceptional attention to detail."
            </p>
          </div>''',
    '''            <p class="testim-text">
              "Woodberry Designs transformed our living space with beautifully
              crafted furniture and exceptional attention to detail."
            </p>
            <div class="testim-client">
              <span class="testim-name">Dr. Anjali R.<br><span style="font-size: 0.85em; font-family: var(--sans); color: var(--text-muted); font-weight: 400;">Calicut Villa Project</span></span>
            </div>
          </div>'''
)

# Testimonial 2
html = html.replace(
    '''            <p class="testim-text">
              "The quality, finish, and professionalism exceeded our
              expectations."
            </p>
          </div>''',
    '''            <p class="testim-text">
              "The quality, finish, and professionalism exceeded our
              expectations. Truly a premium experience."
            </p>
            <div class="testim-client">
              <span class="testim-name">Rajesh Menon<br><span style="font-size: 0.85em; font-family: var(--sans); color: var(--text-muted); font-weight: 400;">Director, Skyline Group Ernakulam</span></span>
            </div>
          </div>'''
)

# Testimonial 3
html = html.replace(
    '''            <p class="testim-text">
              "From design to installation, the entire process was smooth and
              stress-free."
            </p>
          </div>''',
    '''            <p class="testim-text">
              "From design to installation, the entire process was smooth and
              stress-free. The bespoke teak pieces are stunning."
            </p>
            <div class="testim-client">
              <span class="testim-name">Meera Varghese<br><span style="font-size: 0.85em; font-family: var(--sans); color: var(--text-muted); font-weight: 400;">Heritage Homestay, Fort Kochi</span></span>
            </div>
          </div>'''
)

with open("/Users/mubashirt/websites/woodwill/index.html", "w") as f:
    f.write(html)

print("Testimonials updated in HTML")
