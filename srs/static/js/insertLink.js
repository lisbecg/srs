$('#open-btn2').click(function(){
  // Open modal​
	$(".backdrop").show();
	$("#linkmodal").fadeIn();
});

$('#close-btn2').click(function(){
  // Open modal​
	$(".backdrop").hide();
	$("#linkmodal").fadeOut();
  $("#display").val('');
  $("#url").val('');
  $('#err').hide();
});

$('#insert-btn2').click(function(){
  if(!$("#url").val() || !$("#display").val()){
    $('#err').show();
  }
  else{
    $('#id_body').val($('#id_body').val() + '<a href="' + $("#url").val() + '">' + $("#display").val() + '</a>');
    $(".backdrop").hide();
  	$("#linkmodal").fadeOut();
    $("#display").val('');
    $("#url").val('');
    $('#err').hide();
  }
});
