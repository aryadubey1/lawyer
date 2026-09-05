/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Django templates
    '../../templates/**/*.html',
    '../../apps/**/templates/**/*.html',
    '../../theme/templates/**/*.html',
    // Alpine.js components
    '../../static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        // ─── Firm Design System ───────────────────────────────────
        charcoal: {
          DEFAULT: '#1A1714',
          50: '#F7F5F2',
          100: '#EDE9E3',
          200: '#C9C2B8',
          300: '#A89D8F',
          400: '#8A7D6E',
          500: '#6D6052',
          600: '#5C5650',
          700: '#3D3830',
          800: '#2B2520',
          900: '#1A1714',
          950: '#0D0B09',
        },
        gold: {
          DEFAULT: '#B08D57',
          50: '#F9F3E8',
          100: '#F0E4CA',
          200: '#DFC99A',
          300: '#CEAE6A',
          400: '#C49A48',
          500: '#B08D57',
          600: '#9A7942',
          700: '#7D6234',
          800: '#614C27',
          900: '#45351B',
        },
        'off-white': '#F7F5F2',
        'warm-gray': '#C9C2B8',
        'text-muted': '#5C5650',
      },

      fontFamily: {
        display: ['"Playfair Display"', 'Georgia', 'serif'],
        body: ['Manrope', 'Inter', 'system-ui', 'sans-serif'],
        ui: ['Inter', 'system-ui', 'sans-serif'],
      },

      fontSize: {
        'hero': ['clamp(2.5rem, 6vw, 5rem)', { lineHeight: '1.05', letterSpacing: '-0.02em' }],
        'display': ['clamp(2rem, 4vw, 3.5rem)', { lineHeight: '1.1' }],
        'heading': ['clamp(1.5rem, 3vw, 2.25rem)', { lineHeight: '1.2' }],
      },

      letterSpacing: {
        widest: '0.25em',
        wide: '0.15em',
        kicker: '0.2em',
      },

      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
        '26': '6.5rem',
        '30': '7.5rem',
      },

      boxShadow: {
        'card': '0 4px 24px rgba(26, 23, 20, 0.08)',
        'card-hover': '0 12px 40px rgba(26, 23, 20, 0.16)',
        'gold': '0 4px 20px rgba(176, 141, 87, 0.25)',
      },

      backgroundImage: {
        'grain': "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E\")",
      },

      transitionDuration: {
        '250': '250ms',
        '300': '300ms',
        '400': '400ms',
      },

      animation: {
        'fade-in': 'fadeIn 0.4s ease forwards',
        'slide-up': 'slideUp 0.5s ease forwards',
      },

      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },

      typography: (theme) => ({
        DEFAULT: {
          css: {
            color: theme('colors.charcoal.900'),
            a: {
              color: theme('colors.gold.DEFAULT'),
              '&:hover': { color: theme('colors.gold.700') },
            },
            h2: { fontFamily: theme('fontFamily.display').join(', ') },
            h3: { fontFamily: theme('fontFamily.display').join(', ') },
          },
        },
      }),
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
