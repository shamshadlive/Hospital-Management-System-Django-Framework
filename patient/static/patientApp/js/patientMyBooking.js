
$(document).ready( function () {
        $('#patientupcomingBookingTable').DataTable({
            order: [[5, 'desc']],
            responsive: true
        });
    
        $('#patientcompletedBookingTable').DataTable({
            order: [[5, 'desc']],
            responsive: true
        });
    
        $('#patientdeletedBookingTable').DataTable({
            order: [[5, 'desc']],
        });
    
    
    } );

