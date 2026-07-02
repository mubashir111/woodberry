document.addEventListener('DOMContentLoaded', () => {
  const header = document.getElementById('site-header');

  /* ── Sticky header on scroll ─────────────────────────── */
  const onScroll = () => {
    if ((window.scrollY || window.pageYOffset) > 60) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // run once on load

  /* ── Product heart / wishlist toggle ─────────────────── */
  document.querySelectorAll('.prod-heart').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      btn.classList.toggle('liked');
      const svg = btn.querySelector('svg');
      if (svg) svg.setAttribute('fill', btn.classList.contains('liked') ? 'currentColor' : 'none');
    });
  });

  /* ── Collection card hover — subtle lift is CSS-only ─── */

  /* ── Watch Our Story modal ───────────────────────────── */
  const watchBtn = document.querySelector('.watch-btn');
  if (watchBtn) {
    watchBtn.addEventListener('click', () => {
      const modal = document.createElement('div');
      modal.style.cssText = [
        'position:fixed;inset:0;display:flex;align-items:center',
        'justify-content:center;background:rgba(0,0,0,0.78);z-index:9999'
      ].join(';');
      modal.innerHTML = `
        <div style="position:relative;width:min(860px,92vw);border-radius:8px;overflow:hidden;background:#000;box-shadow:0 40px 100px rgba(0,0,0,0.7);">
          <button id="wbCloseModal" style="position:absolute;right:10px;top:10px;z-index:10;background:rgba(255,255,255,0.1);border:none;color:#fff;width:34px;height:34px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">&times;</button>
          <div style="position:relative;padding-top:56.25%;">
            <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"
              style="position:absolute;inset:0;width:100%;height:100%;border:none;"
              allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen>
            </iframe>
          </div>
        </div>`;
      document.body.appendChild(modal);
      document.body.style.overflow = 'hidden';

      const close = () => { modal.remove(); document.body.style.overflow = ''; };
      modal.addEventListener('click', e => { if (e.target === modal) close(); });
      modal.querySelector('#wbCloseModal').addEventListener('click', close);
    });
  }

  /* ── Smooth scroll for anchor links ──────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length > 1) {
        e.preventDefault();
        const el = document.querySelector(id);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        
        // If it's a mobile nav link, close the drawer
        if (a.classList.contains('mobile-nav-link') || a.classList.contains('mobile-sub-link') || a.classList.contains('mobile-cta')) {
          closeMobileMenu();
        }
      }
    });
  });

  /* ── Mobile Menu Logic ───────────────────────────────── */
  const mobileMenuBtn = document.querySelector('.hdr-menu-btn');
  const mobileMenuDrawer = document.getElementById('mobileMenu');
  
  if (mobileMenuBtn && mobileMenuDrawer) {
    const closeBtn = mobileMenuDrawer.querySelector('.mobile-close-btn');

    const openMobileMenu = () => {
      mobileMenuDrawer.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    };

    const closeMobileMenu = () => {
      mobileMenuDrawer.classList.remove('is-open');
      document.body.style.overflow = '';
    };

    mobileMenuBtn.addEventListener('click', openMobileMenu);
    if (closeBtn) closeBtn.addEventListener('click', closeMobileMenu);

    // Accordion Toggle Logic
    const accordionToggles = mobileMenuDrawer.querySelectorAll('.accordion-toggle');
    accordionToggles.forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        const content = toggle.nextElementSibling;
        const arrow = toggle.querySelector('.arr');
        
        if (content.style.maxHeight) {
          content.style.maxHeight = null;
          toggle.classList.remove('active');
          if(arrow) arrow.textContent = '▼';
        } else {
          content.style.maxHeight = content.scrollHeight + "px";
          toggle.classList.add('active');
          if(arrow) arrow.textContent = '▲';
        }
      });
    });
  }

  /* ── Hero Slider Logic ───────────────────────────────── */
  const slides = document.querySelectorAll('.hero-slide');
  const indicators = document.querySelectorAll('.indicator');
  let currentSlide = 0;
  let slideInterval;

  if (slides.length > 0 && indicators.length > 0) {
    const goToSlide = (index) => {
      // Remove active from all
      slides.forEach(s => s.classList.remove('active'));
      indicators.forEach(i => i.classList.remove('active'));
      
      // Add active to current
      currentSlide = index;
      slides[currentSlide].classList.add('active');
      indicators[currentSlide].classList.add('active');
    };

    const nextSlide = () => {
      goToSlide((currentSlide + 1) % slides.length);
    };

    // Auto slide every 6 seconds
    const startSlider = () => {
      slideInterval = setInterval(nextSlide, 6000);
    };

    const resetSlider = () => {
      clearInterval(slideInterval);
      startSlider();
    };

    // Manual click
    indicators.forEach((ind, index) => {
      ind.addEventListener('click', () => {
        goToSlide(index);
        resetSlider();
      });
    });

    startSlider();
  }

  /* ── Contact Form AJAX ───────────────────────────────── */
  function checkmail(input) {
    var pattern1 = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (pattern1.test(input)) { return true; } else { return false; }
  }

  window.proceed = function() {
    var name = document.getElementById("name");
    var email = document.getElementById("email");
    var phone = document.getElementById("phone");
    var msg = document.getElementById("message");
    
    if (name.value == "") {
      name.focus();
      return false;
    }
    else if (email.value == "") {
      email.focus();
      return false;
    }
    else if (checkmail(email.value.trim()) == false) {
      alert('Please provide a valid email address.');
      return false;
    }
    else if (msg.value == "") {
      msg.focus();
      return false;
    }
    else {
      var contactForm = document.getElementById("contactForm");
      var formData = new FormData(contactForm);
      
      fetch("php/submit.php", {
        method: "POST",
        body: formData
      })
      .then(response => response.text())
      .then(msgResponse => {
        if (msgResponse) {
          // Fade out form
          contactForm.style.transition = "opacity 1s";
          contactForm.style.opacity = "0";
          setTimeout(() => {
            contactForm.style.display = "none";
            // Fade in message
            var contactMsg = document.getElementById("contact_message");
            if(contactMsg) {
              contactMsg.style.display = "block";
              contactMsg.style.opacity = "0";
              contactMsg.style.transition = "opacity 1s";
              setTimeout(() => { contactMsg.style.opacity = "1"; }, 10);
            }
          }, 1000);
          
          // Execute scripts returned by PHP
          var tempDiv = document.createElement('div');
          tempDiv.innerHTML = msgResponse;
          var scripts = tempDiv.getElementsByTagName('script');
          for(var i = 0; i < scripts.length; i++) {
            eval(scripts[i].innerText);
          }
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  };
});
