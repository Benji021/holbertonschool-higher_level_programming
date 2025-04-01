window.onload = function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => response.json())
      .then(data => {
        const helloMessage = data.hello;
        document.getElementById('hello').textContent = helloMessage;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  };
  