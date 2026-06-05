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
      }
    });
  });
});
