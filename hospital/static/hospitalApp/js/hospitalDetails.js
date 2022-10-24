$(document).ready( function () {
    $('#HosdoctorListTable').DataTable({
        pageLength : 2,
        lengthMenu: [[2,5, 10, 20,], [2,5, 10, 20,]],
        responsive: true
    });
  
  } );
  


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
  
  //change active status of hospital
  function changeStatusdoc(id){
  
  if ( document.getElementById(id).checked === true ) {
        //id of table
        var passid=document.getElementById(id).value;
        var senddata= {"id":passid,"status":1};
        var csrftoken = getCookie('csrftoken');
  
        $.ajax({
          url: 'changeStatusHospitalDoctor',
          type: "POST",
          dataType: "json",
          data: JSON.stringify(senddata),
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
          },
          success: (data) => {
            //get data
            data['status']?
            (
                 //set label
                $('label[for='+id+']').text('Active'),
                location.reload(true)

            )
            :
            (  
                alert( "Failed")
            )  
          },
          error: (error) => {
            console.log(error);
          }
        });
    }
    else{
      var passid=document.getElementById(id).value;
      var senddata= {"id":passid,"status":0};
      var csrftoken = getCookie('csrftoken');
  
      $.ajax({
        url: 'changeStatusHospitalDoctor',
        type: "POST",
        dataType: "json",
        data: JSON.stringify(senddata),
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
        },
        success: (data) => {
          //get data
          data['status']?
          (
            //set label
            $('label[for='+id+']').text('InActive'),
            location.reload(true)
          )
          :
          (  
              alert( "Failed")
          )  
        },
        error: (error) => {
          console.log(error);
        }
      });
    }
  }
  