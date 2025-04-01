document.getElementById('toggle_header').addEventListener('click', function() {
    const header = document.querySelector('header');
    
    // If the header has the 'red' class, remove it and add 'green', otherwise add 'red'
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});