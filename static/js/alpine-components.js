/**
 * Subhash Mishra & Associates — Alpine.js Components
 * Hero Carousel | Mobile Menu | Gallery Lightbox | Back-to-Top
 * Minimal, professional motion only — no bouncy animations.
 */

// ─── Hero Carousel ─────────────────────────────────────────────────────────────
function heroCarousel(slideCount) {
  return {
    current: 0,
    total: slideCount,
    autoplayInterval: null,
    paused: false,
    AUTOPLAY_MS: 3000,

    init() {
      this.startAutoplay();
      // Pause on hover (set via @mouseenter/@mouseleave on the element)
    },

    startAutoplay() {
      this.stopAutoplay();
      this.autoplayInterval = setInterval(() => {
        if (!this.paused) this.next();
      }, this.AUTOPLAY_MS);
    },

    stopAutoplay() {
      if (this.autoplayInterval) {
        clearInterval(this.autoplayInterval);
        this.autoplayInterval = null;
      }
    },

    next() {
      this.current = (this.current + 1) % this.total;
    },

    prev() {
      this.current = (this.current - 1 + this.total) % this.total;
    },

    goTo(index) {
      this.current = index;
      // Restart autoplay timer on manual navigation
      this.startAutoplay();
    },

    isActive(index) {
      return this.current === index;
    },
  };
}

// ─── Mobile Menu ───────────────────────────────────────────────────────────────
function mobileMenu() {
  return {
    open: false,
    practiceAreasOpen: false,

    toggle() {
      this.open = !this.open;
      // Prevent body scroll when menu is open
      document.body.style.overflow = this.open ? 'hidden' : '';
    },

    close() {
      this.open = false;
      document.body.style.overflow = '';
    },
  };
}

// ─── Navbar Practice Areas Dropdown ────────────────────────────────────────────
function navDropdown() {
  return {
    open: false,
    hoverTimeout: null,

    openMenu() {
      clearTimeout(this.hoverTimeout);
      this.open = true;
    },

    closeMenu() {
      this.hoverTimeout = setTimeout(() => {
        this.open = false;
      }, 150);
    },

    cancelClose() {
      clearTimeout(this.hoverTimeout);
    },
  };
}

// ─── Gallery Lightbox ──────────────────────────────────────────────────────────
function galleryLightbox() {
  return {
    isOpen: false,
    currentSrc: '',
    currentAlt: '',
    currentCaption: '',
    activeFilter: 'all',
    images: [],        // populated by initImages()
    filteredImages: [],
    currentIndex: 0,

    initImages(imagesData) {
      this.images = imagesData;
      this.filteredImages = imagesData;
    },

    setFilter(category) {
      this.activeFilter = category;
      if (category === 'all') {
        this.filteredImages = this.images;
      } else {
        this.filteredImages = this.images.filter(img => img.category === category);
      }
    },

    open(index, src, alt, caption) {
      this.currentIndex = index;
      this.currentSrc = src;
      this.currentAlt = alt;
      this.currentCaption = caption || '';
      this.isOpen = true;
      document.body.style.overflow = 'hidden';

      // Close on Escape key
      this._keyHandler = (e) => {
        if (e.key === 'Escape') this.close();
        if (e.key === 'ArrowRight') this.nextImage();
        if (e.key === 'ArrowLeft') this.prevImage();
      };
      document.addEventListener('keydown', this._keyHandler);
    },

    close() {
      this.isOpen = false;
      document.body.style.overflow = '';
      if (this._keyHandler) {
        document.removeEventListener('keydown', this._keyHandler);
      }
    },

    nextImage() {
      const nextIndex = (this.currentIndex + 1) % this.filteredImages.length;
      const img = this.filteredImages[nextIndex];
      if (img) {
        this.currentIndex = nextIndex;
        this.currentSrc = img.fullSrc || img.src;
        this.currentAlt = img.alt;
        this.currentCaption = img.caption || '';
      }
    },

    prevImage() {
      const prevIndex = (this.currentIndex - 1 + this.filteredImages.length) % this.filteredImages.length;
      const img = this.filteredImages[prevIndex];
      if (img) {
        this.currentIndex = prevIndex;
        this.currentSrc = img.fullSrc || img.src;
        this.currentAlt = img.alt;
        this.currentCaption = img.caption || '';
      }
    },
  };
}

// ─── Back to Top ───────────────────────────────────────────────────────────────
function backToTop() {
  return {
    visible: false,

    init() {
      window.addEventListener('scroll', () => {
        this.visible = window.scrollY > 400;
      }, { passive: true });
    },

    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
  };
}

// ─── Register Alpine Data Components ────────────────────────────────────────────
document.addEventListener('alpine:init', () => {
  Alpine.data('heroCarousel', heroCarousel);
  Alpine.data('mobileMenu', mobileMenu);
  Alpine.data('navDropdown', navDropdown);
  Alpine.data('galleryLightbox', galleryLightbox);
  Alpine.data('backToTop', backToTop);
});
