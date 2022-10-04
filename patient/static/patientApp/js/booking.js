
function hideElement(idBtn,idDiv)
{

 $(idBtn).addClass("d-none");
 $(idDiv).addClass("d-block");
 $(idDiv).removeClass("d-none");

}

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
    

function updateHospitalDepartment(){
    //removing all other options using id and setting new option
    $('#id_HospitalDepartment').find('option').remove().end().append('<option value="" disabled selected>---Hospital Department---</option>')  
   // intializing for loading hospital id
   var hospital_id
    //getting name of hospital selected
    var selectedHosName = $('#id_HospitalName').val();
    //getting view data and parsing to hospital data and deparment data
    var hospitalData = JSON.parse(gethospital);
    // intializing a set  for loading all hospital DEPARTMENT  in unique
    const hospitalDepartment = new Set();
   
    //get all hospital  and geting id of hospital name is uniique so no array
    hospitalData.map(hospitalData=>
    {
        //geting id according to the name of hospital
        (hospitalData.name==selectedHosName)? hospital_id= hospitalData.id:""
        
    })
    var senddata= {"hospital_id":hospital_id,};
    var csrftoken = getCookie('csrftoken');
    var obj=""
    $.ajax({
      url: 'getHospitalDepartment',
      type: "POST",
      dataType: "json",
      data: JSON.stringify(senddata),
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
      },
      success: (data) => 
      {
        //saving to option
        value=data.getdepartmentValue
        value.map(n=>n.map(m=>
            hospitalDepartment.add(m.name)
            ))
    //accessing set and with foreach adding each option
     hospitalDepartment.forEach(eachHosDepName => {
    //adding optin
     $('#id_HospitalDepartment').append(`<option value="${eachHosDepName}"> ${eachHosDepName} </option>`)
     });


      },
      error: (error) => {
        alert(error);
      }
    });
  
 
   
    

}




function  updateHospitalName(){

        //removing all other options using id and setting new option
        $('#id_HospitalName').find('option').remove().end().append('<option value="" disabled selected>---Hospital Name---</option>')
        $('#id_HospitalDepartment').find('option').remove().end().append('<option value="" disabled selected>---Hospital Department---</option>') 
       
        // intializing a set  for loading all hospital name  in unique
        const hospitalName = new Set();
        
       
        // geting selected disticit value 
        var selectedDistrict = $('#id_hospital_district').val();
  
        var selectedHosType = $('#id_HospitalType').val();
     

        //getting view data and parsing to hospital data
        var hospitalData = JSON.parse(gethospital);

        
        //get all hospital  and name
        hospitalData.map(hospitalData=>
        {
             //selecting district and save according to each type only saving to set
             (hospitalData.district == selectedDistrict && hospitalData.hos_type == selectedHosType )? hospitalName.add(hospitalData.name) :""
             
        })
    
 
         //accessing set and with foreach adding each option
         hospitalName.forEach(eachHosName => {

            $('#id_HospitalName').append(`<option value="${eachHosName}"> ${eachHosName} </option>`)
            });

}


//for to update hospital type
function updateHospitalType()
    {
        //removing all other options using id and setting new option
        $('#id_HospitalType').find('option').remove().end().append('<option value="" disabled selected>---Hospital Type---</option>')
        $('#id_HospitalName').find('option').remove().end().append('<option value="" disabled selected>---Hospital Name---</option>')
        $('#id_HospitalDepartment').find('option').remove().end().append('<option value="" disabled selected>---Hospital Department---</option>')
    
        // intializing a set  for loading all hospital type  in unique
        const hospitalType = new Set();
        
        // geting selected disticit value 
        var selectedDistrict = $('#id_hospital_district').val();

        //getting view data and parsing to hospital data
        var hospitalData = JSON.parse(gethospital);

        //get all hospital type
        hospitalData.map(hospitalData=>
        {
            //selecting district and save according to each type only saving to set
            (hospitalData.district == selectedDistrict)? hospitalType.add(hospitalData.hos_type) :""
           
        })
       
        //accessing set and with foreach adding each option
        hospitalType.forEach(hostype => {

            $('#id_HospitalType').append(`<option value="${hostype}"> ${hostype} </option>`)
            });

        
    }

//reset page if user clicks backbutton
    window.addEventListener("pageshow", () => {

       $("form").get(0).reset()
      });

    window.addEventListener('load', function () {
    

        //getting view data and parsing to hospital data
        var hospitalData = JSON.parse(gethospital);

        // intializing a set  for loading all hospital district  in unique
        const district = new Set();

        hospitalData.map(hospitalData=>
        {
            //saving each district to set
           district.add(hospitalData.district)
          
        })

        //accessing set and with foreach adding each option
        district.forEach(eachDistrict => {

            $('#id_hospital_district').append(`<option value="${eachDistrict}"> ${eachDistrict} </option>`)
            });
  
  });