// Select element with ID “red_header”
const button = document.querySelector('#red_header');

// Add a click event listener to the button
button.addEventListener('click', function () {
    // Change the text color of the header to red
    document.querySelector('header').style.color = '#FF0000';
});