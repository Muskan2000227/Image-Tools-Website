function showFileName(input) {
    var fileNameContainer = document.getElementById('file-name');
    fileNameContainer.textContent = input.files[0].name;
    
    if (input.value !== '') {
      alert('File selected!');
    }
  }
  