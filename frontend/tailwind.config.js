/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      // Define pattern
      backgroundImage: () => ({
        "hero-pattern":
          "url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80')",
      }),
      // Define animation class
      animation: {
        "ltr-linear-infinite": "move-bg 100s linear infinite",
      },
      // Define keyframes
      keyframes: {
        "move-bg": {
          "0%": { "background-position": "0 0" },
          "100%": {
            "background-position": "400% 0%",
          },
        },
      },
    },
  },
  plugins: [],
};
