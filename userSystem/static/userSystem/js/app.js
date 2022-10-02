
//disabling button until the all field filled
$(document).ready(function(){

  //disabling button until the all field filled
    $('#UserRegForm input').keyup(function() {

        var empty = false;
        $('#UserRegForm input').each(function() {
            if ($(this).val() == '') {
                empty = true;
            }
        });

        if (empty) {
            $('#id_registerButton').attr('disabled', 'disabled');
        } else {
            $('#id_registerButton').removeAttr('disabled');
        }
    });

    // $("#id_user_Type").addClass("form-select") 

//disabling button until the all field filled
    $('#UserLogForm input').keyup(function() {

      var empty = false;
      $('#UserLogForm input').each(function() {
          if ($(this).val() == '') {
              empty = true;
          }
      });

      if (empty) {
          $('#id_LOGButton').attr('disabled', 'disabled');
      } else {
          $('#id_LOGButton').removeAttr('disabled');
      }
  });

//setting processing showing on button
  $('#UserRegForm').on('submit', function(){

    $("#id_registerButton").prop('value', 'Processing…');
    $('#id_registerButton').attr('disabled', 'disabled');

   
});

$('#UserLogForm').on('submit', function(){

  $("#id_LOGButton").prop('value', 'Processing…');
  $('#id_LOGButton').attr('disabled', 'disabled');

 
});


$('#resendemailForm').on('submit', function(){

  $("#Id_resendemailForm").prop('value', 'Processing…');
  $('#Id_resendemailForm').attr('disabled', 'disabled');

 
});

$('#fromResetPassword').on('submit', function(){

  $("#Id_fromResetPassword").prop('value', 'Processing…');
  $('#Id_fromResetPassword').attr('disabled', 'disabled');
 

 
});







});  







//get Csrf Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
    

  
  
  //check availablity of username inputed field
 checkUsername=(id)=>
  {
      var usernameCheck=document.getElementById(id).value;
      //checking if null value then removing the bottom area 
      if (!usernameCheck)
        {
          
          $("#id_username_Error").addClass("d-none");
        }
      else
      {
  
        var senddata= {"id":id,"usernameCheck":usernameCheck};
        var csrftoken = getCookie('csrftoken');
  
        $.ajax({
          url: 'checkUsername',
          type: "POST",
          dataType: "json",
          data: JSON.stringify(senddata),
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
          },
          success: (data) => {
            //get data



            data['is_taken']?
            (
                $("#id_username_Error").removeClass("d-none") ,
                $("#id_username_Error").addClass("text-danger d-block bi bi-exclamation-circle") 
            )
            :
            (  
                $("#id_username_Error").removeClass("d-none text-danger bi bi-exclamation-circle "),
                $("#id_username_Error").addClass("text-success bi bi-check-circle")    
            )

            
          },
          error: (error) => {
            console.log(error);
          }
        });
    }}
  

  //check availablity of phone number inputed field
  function checkPhone(id)
  {
      var phoneCheck=document.getElementById(id).value;
      //checking if null value then removing the bottom area 
      if (!phoneCheck)
        {
          
          $("#id_phone_number_Error").addClass("d-none");
        }
      else
      {
  
        var senddata= {"id":id,"phoneCheck":phoneCheck};
        var csrftoken = getCookie('csrftoken');
  
        $.ajax({
          url: 'checkPhone',
          type: "POST",
          dataType: "json",
          data: JSON.stringify(senddata),
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
          },
          success: (data) => {
            //get data
            if ( data['is_taken']) 
                {
                    $("#id_phone_number_Error").removeClass("d-none");  
                    $("#id_phone_number_Error").addClass("text-danger d-block bi bi-exclamation-circle");
                   
                    
                }
  
                else {

                    $("#id_phone_number_Error").removeClass("d-none text-danger bi bi-exclamation-circle ");  
                    $("#id_phone_number_Error").addClass("text-success bi bi-check-circle");     

                }
            },

          error: (error) => {
            console.log(error);
          }
        });
    }}
  
//check availablity of email inputed field
  function checkEmail(id)
  {
        var emailCheck=document.getElementById(id).value;
        var senddata= {"id":id,"emailCheck":emailCheck};
        var csrftoken = getCookie('csrftoken');
  
        $.ajax({
          url: 'checkEmail',
          type: "POST",
          dataType: "json",
          data: JSON.stringify(senddata),
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
          },
          success: (data) => {
            //get data
            if ( data['is_taken']) 
                {
                    $("#id_email_Error").removeClass("d-none text-success bi bi-check-circle");  
                    $("#id_email_Error").addClass("text-danger d-block bi bi-exclamation-circle");
                  
                    
                }
  
                else {

                    $("#id_email_Error").removeClass("d-none text-danger bi bi-exclamation-circle ");  
                    $("#id_email_Error").addClass(" d-block text-success bi bi-check-circle");     

                }
            },

          error: (error) => {
            console.log(error);
          }
        });
    }
  
  
  //to check email id  format is valid or not
  function checkemailFormat(id){
        var email=document.getElementById(id).value;
        //checking wheather nullvalue
        if (!email)
        {
            $("#id_email_Error").addClass("d-none");
        }
        //checking email formaT
        else{
            var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,3})$/;
     
            if (reg.test(email) == false) {
            //setting error
            $("#id_email_Error").removeClass("d-none text-success bi bi-check-circle");  
            $("#id_email_Error").addClass("text-danger d-block bi bi-exclamation-circle");
           
             
            }
            else{
            //checking availibitly of email
            checkEmail(id)
            }
        }
    }
    
   
  //to check firstname tik mark
  function checkFirstName(id){
    var firstName=document.getElementById(id).value;
    //checking wheather null value
    if (!firstName)
    {
        $("#id_first_name_Error").addClass("d-none");
       
    }
    else{
       
        //setting error
        $("#id_first_name_Error").removeClass("d-none");
        $("#id_first_name_Error").addClass("text-success d-block  bi bi-check-circle");  
        }
      
    }


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


  //check both password
    function checkpassword(){


      if (document.getElementById('id_input_Password1').value ==
      document.getElementById('id_input_Password2').value) {
      document.getElementById('Input_Password_Error').style.color = 'green';
      document.getElementById('Input_Password_Error').innerHTML = 'Perfect Match';
      document.getElementById("Id_resetpsButton").disabled = false;
  
    } else {
      document.getElementById('Input_Password_Error').style.color = 'red';
      document.getElementById('Input_Password_Error').innerHTML = 'Password Not Matching';
      document.getElementById("Id_resetpsButton").disabled = true;
    }
  }