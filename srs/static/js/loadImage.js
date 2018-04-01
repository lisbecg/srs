$('.image-trigger').click(function(e){
  // Assign image source after clicking image
  $("#modal-image").attr("src", $(this).attr('data-path'));
  $("#image-source").text('Source: ' + $(this).attr('data-source'));
  $("#image-caption").text($(this).attr('title'));

  // Open modal​
  $(".backdrop").show();
  $("#imagemodal").show();
});

$('.image-close').click(function(e){
	// Close modal
	$(".backdrop").hide();
	$("#imagemodal").hide();
});
