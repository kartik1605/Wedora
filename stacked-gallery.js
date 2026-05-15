/* ══════════════════════════════════════
   STACKED GALLERY — JavaScript
   Infinite loop carousel for Wedora
══════════════════════════════════════ */

function initStackedGallery(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const cards = Array.from(container.querySelectorAll('.sg-card'));
  const dotsWrap = container.querySelector('.sg-dots');
  const prevBtn = container.querySelector('.sg-nav-prev');
  const nextBtn = container.querySelector('.sg-nav-next');
  const total = cards.length;
  if (total === 0) return;

  let current = 0;
  let autoTimer = null;
  let isAnimating = false;

  // Build dots
  if (dotsWrap) {
    dotsWrap.innerHTML = '';
    cards.forEach((_, i) => {
      const dot = document.createElement('div');
      dot.className = 'sg-dot' + (i === 0 ? ' active' : '');
      dot.addEventListener('click', () => { if (!isAnimating) goTo(i); });
      dotsWrap.appendChild(dot);
    });
  }

  // Infinite loop: wrap index around
  function wrapIndex(i) {
    return ((i % total) + total) % total;
  }

  function positionCards() {
    cards.forEach((card, i) => {
      // Calculate shortest circular distance from current
      let diff = i - current;
      // Wrap for infinite loop
      if (diff > total / 2) diff -= total;
      if (diff < -total / 2) diff += total;

      if (diff >= -2 && diff <= 2) {
        card.dataset.pos = String(diff);
        card.style.pointerEvents = diff === 0 ? 'auto' : 'auto';
      } else {
        // Stage hidden cards on the correct side for smooth entry
        if (diff > 0) {
          card.dataset.pos = 'hidden-right';
        } else {
          card.dataset.pos = 'hidden-left';
        }
      }
    });

    // Update dots
    if (dotsWrap) {
      const dots = dotsWrap.querySelectorAll('.sg-dot');
      dots.forEach((d, i) => d.classList.toggle('active', i === current));
    }
  }

  function goTo(n) {
    isAnimating = true;
    current = wrapIndex(n);
    positionCards();
    resetAuto();
    setTimeout(() => { isAnimating = false; }, 600);
  }

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  function resetAuto() {
    if (autoTimer) clearInterval(autoTimer);
    autoTimer = setInterval(next, 3500);
  }

  // Nav buttons
  if (prevBtn) prevBtn.addEventListener('click', () => { if (!isAnimating) prev(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { if (!isAnimating) next(); });

  // Click on side cards to navigate
  cards.forEach((card, i) => {
    card.addEventListener('click', () => {
      if (isAnimating) return;
      const pos = parseInt(card.dataset.pos);
      if (pos !== 0 && !isNaN(pos)) goTo(i);
    });
  });

  // Touch/swipe support
  let touchStartX = 0;
  const wrap = container.querySelector('.sg-carousel-wrap');
  if (wrap) {
    wrap.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    wrap.addEventListener('touchend', (e) => {
      const diff = touchStartX - e.changedTouches[0].screenX;
      if (Math.abs(diff) > 50 && !isAnimating) {
        diff > 0 ? next() : prev();
      }
    }, { passive: true });
  }

  // Initialize
  positionCards();
  resetAuto();

  // Pause auto on hover
  container.addEventListener('mouseenter', () => { if (autoTimer) clearInterval(autoTimer); });
  container.addEventListener('mouseleave', resetAuto);
}

// Auto-init all stacked galleries on page load
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.stacked-gallery').forEach(g => {
    if (g.id) initStackedGallery(g.id);
  });
});
