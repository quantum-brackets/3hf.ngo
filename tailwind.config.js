/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*.html",
    "apps/*/templates/*/*.html",
    "apps/*/templates/*.html",

    // Flowbite
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ["Inter", "sans-serif"],
        delaGothic: ["Dela Gothic One", "sans-serif"],
      },
      colors: {
        "text-color": "#6D6D6D",
      },
      screens: {
        mdLg: "954px",
        lgXl: "1200px",
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
