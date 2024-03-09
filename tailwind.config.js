/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    'apps/*/templates/*/*.html',
    'apps/*/templates/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
      },
      colors: {
        'text-color': '#6D6D6D',
      },
    },
  },
  plugins: [],
}

