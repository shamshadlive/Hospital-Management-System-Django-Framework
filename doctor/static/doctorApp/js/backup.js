
window.addEventListener('load', function () {

    //getting view data and parsing 
    var getbookinglist = bookinglist;

            // create table upcoming booking table
            var $table1= $('<table>').addClass('table');
            $table1
            // thead
            .append('<thead>').children('thead')
            .append('<tr />').children('tr').append('<th>#</th><th>Patient Name</th><th>Time of Apoinment</th><th>Department</th><th>Hospital</th><th>Apoinment Date</th><th>Apoinment Status</th><th>Action</th>');
            //tbody
            var $tbody1 = $table1.append('<tbody />').children('tbody');
            // add table to dom
            $table1.appendTo('#upcomingBookingTable');

            // create table completed booking table
            var $table2 = $('<table>').addClass('table');
            $table2
            // thead
            .append('<thead>').children('thead')
            .append('<tr />').children('tr').append('<th>#</th><th>Patient Name</th><th>Time of Apoinment</th><th>Department</th><th>Hospital</th><th>Apoinment Date</th><th>Apoinment Status</th><th>Action</th>');
            //tbody
            var $tbody2 = $table2.append('<tbody />').children('tbody');
            // add table to dom
            $table2.appendTo('#completedBookingTable');

            // create table deleted booking table
            var $table3 = $('<table>').addClass('table');
            $table3
            // thead
            .append('<thead>').children('thead')
            .append('<tr />').children('tr').append('<th>#</th><th>Patient Name</th><th>Time of Apoinment</th><th>Department</th><th>Hospital</th><th>Apoinment Date</th><th>Apoinment Status</th>');
            //tbody
            var $tbody3 = $table3.append('<tbody />').children('tbody');
            // add table to dom
            $table3.appendTo('#deletedBookingTable');

            i=1;
            j=1;
            k=1;
            getbookinglist.map(m=>
            {
                if (m.patientstate=='PENDING')
                {
                    // add  row on upcoming
                    $tbody1.append('<tr />').children('tr:last')
                    .append("<th>"+i+"</th>")
                    .append("<td>"+m.patientName+"</td>")
                    .append("<td>"+m.timeslot+"</td>")
                    .append("<td>"+m.depName+"</td>")
                    .append("<td>"+m.hospitalName+"</td>")
                    .append("<td>"+m.appointmentDate+"</td>")
                    .append("<td>"+m.patientstate+"</td>")
                    .append("<td>"+
                            "<a href="+docCreateUrlMarkCompeleted+m.bkTableToken+"><button type='button' class='btn btn-success'>Mark as Completed</button></a>"+"</td>");
                    i++
                }
                else if(m.patientstate=='COMPLETED')
                {
                     // add  row on completed
                     $tbody2.append('<tr />').children('tr:last')
                     .append("<th>"+j+"</th>")
                     .append("<td>"+m.patientName+"</td>")
                     .append("<td>"+m.timeslot+"</td>")
                     .append("<td>"+m.depName+"</td>")
                     .append("<td>"+m.hospitalName+"</td>")
                     .append("<td>"+m.appointmentDate+"</td>")
                     .append("<td>"+m.patientstate+"</td>")
                     .append("<td>"+
                            "<a href="+docCreateUrlMarkPending+m.bkTableToken+"><button type='button' class='btn btn-warning'>Change To Pending</button></a>"+
                            "<a href="+docCreateUrlMarkDeleted+m.bkTableToken+"><button type='button' class='ms-1 btn btn-danger'> Delete Appoinment</button></a>"
                            +"</td>");
                     j++   
                } 
                else if(m.patientstate=='DELETED')
                {
                     // add  row on deleted
                     $tbody3.append('<tr />').children('tr:last')
                     .append("<th>"+k+"</th>")
                     .append("<td>"+m.patientName+"</td>")
                     .append("<td>"+m.timeslot+"</td>")
                     .append("<td>"+m.depName+"</td>")
                     .append("<td>"+m.hospitalName+"</td>")
                     .append("<td>"+m.appointmentDate+"</td>")
                     .append("<td>"+m.patientstate+"</td>")
                     k++   

                } 
                else{
                    this.print("error on booking patinet")
                }   
            })      

});


//   +"<a href="+doctorChangeState+">Shoes</a>"