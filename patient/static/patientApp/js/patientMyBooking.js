
$(document).ready( function () {
    $('#upcomingBookingTable').DataTable({
        order: [[5, 'desc']],
        responsive: true
    });

    $('#completedBookingTable').DataTable({
        order: [[5, 'desc']],
        responsive: true
    });

    $('#deletedBookingTable').DataTable({
        order: [[5, 'desc']],
    });


} );