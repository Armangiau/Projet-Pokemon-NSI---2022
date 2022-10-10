/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html'],
  theme: {
    extend: {
      colors: {
        gold : 'rgb(247, 201, 142)'
      },
      height: {
        '120' : '30rem',
      },
      maxHeight: {
        '120' : '30rem',
      },
      gridTemplateColumns: {
        'auto-fill-96': 'repeat(auto-fill, minmax(24rem, 1fr))',
        'auto-fit-96': 'repeat(auto-fit, minmax(24rem, 1fr))',
      },
      gridTemplateRows: {
        '2-(0-150)' : 'repeat(2, minmax(0, 600px))'
      },
    },
  },
  plugins: [require("daisyui")],
}
