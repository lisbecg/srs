/**
 * Opens and shows the popup in first view.
 */
$('#open-btn-delete').click(function(){
    // Open modal​
    $(".backdrop").show();
    $("#deleteModal").fadeIn();
});

/**
 * Closes the popup.
 */
$("#close-btn-delete").click(function(){
    // Close modal​
    $(".backdrop").hide();
    $("#deleteModal").fadeOut();
    $('#err').hide();
});