/**
 * main.js — Additional site-wide JavaScript (non-Alpine).
 * Alpine handles reactive components; this file is for vanilla utilities.
 */

// ─── Page Loader (branded boot-up, once per session) ────────────────────────
(function () {
  var loader = document.getElementById('page-loader');
  if (!loader) return;

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var alreadyLoaded = false;

  try {
    alreadyLoaded = sessionStorage.getItem('lc_loaded') === '1';
  } catch (e) {
    // sessionStorage blocked (private browsing etc.) — treat as first visit
  }

  // Skip entirely if already shown this session
  if (alreadyLoaded) {
    loader.style.display = 'none';
    return;
  }

  // Reduced-motion: show briefly then remove
  if (prefersReduced) {
    setTimeout(function () {
      loader.style.display = 'none';
      try { sessionStorage.setItem('lc_loaded', '1'); } catch (e) {}
    }, 300);
    return;
  }

  // ── Full animation sequence ──
  var wordmark = document.getElementById('loader-wordmark');
  var scales   = document.getElementById('loader-scales');
  var paths    = loader.querySelectorAll('.loader-scales-path');
  var rule     = document.getElementById('loader-rule');

  // Phase 1: Wordmark fades/rises in (0–500ms)
  wordmark.style.animation = 'loaderWordmarkIn 500ms cubic-bezier(0.22,1,0.36,1) forwards';

  // Phase 2: Scales icon stroke-draw (400–1100ms)
  setTimeout(function () {
    scales.style.opacity = '1';
    paths.forEach(function (path) {
      path.style.animation = 'loaderScalesDraw 700ms cubic-bezier(0.22,1,0.36,1) forwards';
    });
  }, 400);

  // Phase 3: Rule expands (1100–1400ms)
  setTimeout(function () {
    rule.style.animation = 'loaderRuleExpand 300ms cubic-bezier(0.22,1,0.36,1) forwards';
  }, 1100);

  // Phase 4: Brief hold, then entire loader fades out (1700–2100ms)
  setTimeout(function () {
    loader.style.animation = 'loaderFadeOut 400ms ease forwards';
    loader.addEventListener('animationend', function () {
      loader.style.display = 'none';
    }, { once: true });
    try { sessionStorage.setItem('lc_loaded', '1'); } catch (e) {}
  }, 1700);

  // Safety net: if animation somehow fails, remove loader after 3s
  setTimeout(function () {
    if (loader.style.display !== 'none') {
      loader.style.display = 'none';
      try { sessionStorage.setItem('lc_loaded', '1'); } catch (e) {}
    }
  }, 3000);
})();
// ─── Navbar scroll behavior ─────────────────────────────────────────────────────
(function () {
  const navbar = document.getElementById('main-navbar');
  if (!navbar) return;

  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;

    if (currentScroll > 80) {
      navbar.classList.add('shadow-md');
    } else {
      navbar.classList.remove('shadow-md');
    }

    lastScroll = currentScroll;
  }, { passive: true });
})();

// ─── Smooth anchor links ────────────────────────────────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ─── PHASE 2: Scroll-Reveal System ──────────────────────────────────────────────
(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const revealElements = document.querySelectorAll('[data-reveal]');
  if (!revealElements.length) return;

  // Reduced motion: reveal all immediately with no delay/animation
  if (prefersReduced) {
    revealElements.forEach(el => el.classList.add('is-visible'));
    return;
  }

  // Set up staggered delay CSS custom property
  revealElements.forEach(el => {
    const delay = el.getAttribute('data-reveal-delay');
    if (delay) {
      el.style.setProperty('--reveal-delay', `${delay}ms`);
    }
  });

  // Native continuous scroll reveal via IntersectionObserver
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.15,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback if IntersectionObserver is unsupported
    revealElements.forEach(el => el.classList.add('is-visible'));
  }

  // Defensive fallback: force all elements visible after 3 seconds
  setTimeout(() => {
    revealElements.forEach(el => {
      if (!el.classList.contains('is-visible')) {
        el.classList.add('is-visible');
      }
    });
  }, 3000);
})();

// ─── PHASE 2: Animated Number Counters ──────────────────────────────────────────
(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const counters = document.querySelectorAll('[data-counter]');
  if (!counters.length) return;

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function animateCounter(el) {
    const targetStr = el.getAttribute('data-counter-to') || el.textContent;
    const target = parseFloat(targetStr.replace(/[^0-9.]/g, '')) || 0;
    const suffix = el.getAttribute('data-counter-suffix') || '';
    const duration = 1400; // ~1.4s

    if (prefersReduced || target === 0) {
      el.textContent = `${target}${suffix}`;
      return;
    }

    let startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      const progress = Math.min((timestamp - startTime) / duration, 1);
      const eased = easeOutCubic(progress);
      const current = Math.floor(eased * target);

      el.textContent = `${current}${suffix}`;

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = `${target}${suffix}`;
      }
    }

    requestAnimationFrame(step);
  }

  if ('IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.4
    });

    counters.forEach(counter => counterObserver.observe(counter));
  } else {
    counters.forEach(counter => animateCounter(counter));
  }
})();

// ─── PHASE 3: Hero Parallax ─────────────────────────────────────────────────────
(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  const heroSection = document.querySelector('.hero-section');
  const parallaxLayers = document.querySelectorAll('.hero-parallax-bg');
  if (!heroSection || !parallaxLayers.length) return;

  let ticking = false;

  function updateParallax() {
    const scrollY = window.scrollY;
    const heroHeight = heroSection.offsetHeight;

    if (scrollY <= heroHeight) {
      const translateY = scrollY * 0.18; // 18% parallax shift
      parallaxLayers.forEach(layer => {
        layer.style.transform = `translate3d(0, ${translateY.toFixed(1)}px, 0)`;
      });
    }
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(updateParallax);
      ticking = true;
    }
  }, { passive: true });
})();

// ─── PHASE 4: Subtle 3D Card Tilt (Desktop Only) ────────────────────────────────
(function () {
  const isHoverable = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!isHoverable || prefersReduced) return;

  const tiltCards = document.querySelectorAll('.pa-card, .team-card');
  if (!tiltCards.length) return;

  tiltCards.forEach(card => {
    let bounds;

    function mouseMoveHandler(e) {
      if (!bounds) bounds = card.getBoundingClientRect();
      const mouseX = e.clientX - bounds.left;
      const mouseY = e.clientY - bounds.top;

      const xPct = (mouseX / bounds.width) - 0.5;
      const yPct = (mouseY / bounds.height) - 0.5;

      // Subtle tilt max ~4-5 degrees
      const rotateX = (-yPct * 8).toFixed(2);
      const rotateY = (xPct * 8).toFixed(2);

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    }

    card.addEventListener('mouseenter', () => {
      bounds = card.getBoundingClientRect();
      card.style.transition = 'transform 0.1s ease-out, box-shadow 0.3s ease';
    });

    card.addEventListener('mousemove', mouseMoveHandler);

    card.addEventListener('mouseleave', () => {
      bounds = null;
      card.style.transition = 'transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease';
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
    });
  });
})();

