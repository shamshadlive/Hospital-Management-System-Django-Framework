
$(document).ready( function () {
  $('#hospitalListTable').DataTable({
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
function changeStatus(id){

if ( document.getElementById(id).checked === true ) {
      //id of table
      var passid=document.getElementById(id).value;
      var senddata= {"id":passid,"status":1};
      var csrftoken = getCookie('csrftoken');
   


      $.ajax({
        url: 'changeStatusHospital',
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
              $('label[for='+id+']').text('Active')
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
      url: 'changeStatusHospital',
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
          $('label[for='+id+']').text('InActive')
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
