document.getElementById('add_item').addEventListener('click', function() {
    const ul = document.querySelector('.my_list');
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    ul.appendChild(newLi);
});
