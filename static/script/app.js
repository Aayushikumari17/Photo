function showPreviewImage(e) {
    var previewImage = document.getElementById('preview-image');
    previewImage.src = e.target.src;
    document.getElementById('img_url_name').value = e.target.src;
    document.getElementById('image-previewer').style.display = 'block';
   
    document.getElementById('image-previewer').onclick = function() {
        this.style.display = 'none';
    }
  }

  document.querySelectorAll('.my-image').forEach(function(image) {
    image.addEventListener('click', showPreviewImage);
  });




  /* validate */ 

  function validateUsername(username) {
    if (username.length < 8) {
      return false;
    }
    const specialCharacters = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?~]/;
    if (specialCharacters.test(username)) {
      return false;
    }
    // If the username passes all of the validation checks, return true.
    return true;
  }
  

const username = document.getElementById('username');
const alert_box = document.getElementById('alert-box-validation')

// Validate the username when the user types in the input field.
username.addEventListener('input', () => {
  const isValid = validateUsername(username.value);
  if(isValid){
    alert_box.innerHTML = ""
  }
  if(!isValid){
    alert_box.innerHTML = "Avoid using special character"
  }
});

