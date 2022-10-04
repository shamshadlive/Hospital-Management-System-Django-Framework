 //toggle password button register
  
function togglebutton(id) {
        var x = document.getElementById(id);
        if (x.type === "password") {
          x.type = "text";
          document.getElementById(id+"_passButton").className = "btn bi bi-eye-fill";
        } else {
          x.type = "password";
          document.getElementById("passtogglebutton2").className = "btn bi bi-eye-slash-fill";
        }
      }
  
  