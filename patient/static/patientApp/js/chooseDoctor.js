//reset page if user clicks backbutton
    window.addEventListener("pageshow", () => {
      
        $("form").get(0).reset()
       });
 




    window.addEventListener('load', function () {

        $('form').get(0).reset();
    
        //getting view data and parsing to hospital data
        var doctorData = doctor;

         // intializing a set  for loading all hospital name  in unique
         const doctorName = new Set();
         const doctorId = new Set();

        doctorData.map(doctorData=>
        {
           
            if(doctorData.doctorDep==selectedHosDepartment)
            {

                doctorName.add(doctorData.doctorName)
                doctorId.add(doctorData.doctorID)
            }
            
        })
       

        //accessing set and with foreach adding each option
        doctorName.forEach(eachDocName => {

            doctorId.forEach(eachDocId => {

                $('#id_DoctorName').append(`<option value="${eachDocId}"> ${eachDocName} </option>`)
                });

           
            });


  });

 


    function updateDoctorTiming(){

        $('#id_DoctorTimeSlot').find('option').remove().end().append('<option value="" disabled selected>---Choose Time Slot---</option>')
        var selectedDoctor = $('#id_DoctorName').val();
       //getting view data and parsing to hospital data
        var doctorData = doctor;
        doctorData.map(doctorData=>
        {
          (doctorData.doctorID==selectedDoctor)?
            (doctorData.doctorSlot=='NULL')?
                $('#id_DoctorTimeSlot').append(`<option value="" disabled > Not Available </option>`):
                    $('#id_DoctorTimeSlot').append(`<option value="${doctorData.doctorSlot}"> ${doctorData.doctorSlot} </option>`):""   
        }) 
    }