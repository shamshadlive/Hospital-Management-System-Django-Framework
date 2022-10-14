
window.addEventListener('load', function () {

    //getting view data and parsing 
    var getbookinglist = bookinglist;

            // create table upcoming booking table
            var $table1= $('<table>').addClass('table');
            $table1
            // thead
            .append('<thead>').children('thead')
            .append('<tr />').children('tr').append('<th>#</th><th>Doctor Name</th><th>Time of Apoinment</th><th>Department</th><th>Hospital</th><th>Apoinment Date</th><th>Apoinment Status</th>');
            //tbody
            var $tbody1 = $table1.append('<tbody />').children('tbody');
            // add table to dom
            $table1.appendTo('#upcomingBookingTable');

            // create table completed booking table
            var $table2 = $('<table>').addClass('table');
            $table2
            // thead
            .append('<thead>').children('thead')
            .append('<tr />').children('tr').append('<th>#</th><th>Doctor Name</th><th>Time of Apoinment</th><th>Department</th><th>Hospital</th><th>Apoinment Date</th><th>Apoinment Status</th>');
            //tbody
            var $tbody2 = $table2.append('<tbody />').children('tbody');
            // add table to dom
            $table2.appendTo('#completedBookingTable');

            // create table rejected booking table
            var $table3 = $('<table>').addClass('table');
            $table3
            // thead
            .append('<thead>').children('thead')
            .append('<tr />').children('tr').append('<th>#</th><th>Doctor Name</th><th>Time of Apoinment</th><th>Department</th><th>Hospital</th><th>Apoinment Date</th><th>Apoinment Status</th>');
            //tbody
            var $tbody3 = $table3.append('<tbody />').children('tbody');
            // add table to dom
            $table3.appendTo('#rejectedBookingTable');

            i=1;
            j=1;
            k=1;
            getbookinglist.map(m=>
            {
                if (m.state=='PENDING')
                {
                    // add  row on upcoming
                    $tbody1.append('<tr />').children('tr:last')
                    .append("<th>"+i+"</th>")
                    .append("<td>"+m.doctorName+"</td>")
                    .append("<td>"+m.doctorSlot+"</td>")
                    .append("<td>"+m.doctorDep+"</td>")
                    .append("<td>"+m.hospital+"</td>")
                    .append("<td>"+m.appointmentDate+"</td>")
                    .append("<td>"+m.state+"</td>");
                    i++
                }
                else if(m.state=='COMPLETED')
                {
                     // add  row on completed
                     $tbody2.append('<tr />').children('tr:last')
                     .append("<th>"+j+"</th>")
                     .append("<td>"+m.doctorName+"</td>")
                     .append("<td>"+m.doctorSlot+"</td>")
                     .append("<td>"+m.doctorDep+"</td>")
                     .append("<td>"+m.hospital+"</td>")
                     .append("<td>"+m.appointmentDate+"</td>")
                     .append("<td>"+m.state+"</td>");
                     j++   
                }    
                else if(m.state=='DELETED')
                {
                     // add  row on completed
                     $tbody3.append('<tr />').children('tr:last')
                     .append("<th>"+k+"</th>")
                     .append("<td>"+m.doctorName+"</td>")
                     .append("<td>"+m.doctorSlot+"</td>")
                     .append("<td>"+m.doctorDep+"</td>")
                     .append("<td>"+m.hospital+"</td>")
                     .append("<td>"+m.appointmentDate+"</td>")
                     .append("<td>"+m.state+"</td>");
                     k++   
                }   
            })      

});
