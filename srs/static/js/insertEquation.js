var editor;

window.onload = function () {
  editor = com.wiris.jsEditor.JsEditor.newInstance ({'language': 'en'});
  editor.insertInto (document.getElementById ('editorContainer'));
};

$('#open-btn').click(function(){
  // Open modal​
	$(".backdrop").show();
	$("#eqnmodal").fadeIn();
});

$('#close-btn').click(function(){
  // Open modal​
	$(".backdrop").hide();
	$("#eqnmodal").fadeOut();
  editor.setMathML('<math xmlns="http://www.w3.org/1998/Math/MathML"/>');
});

$('#insert-btn').click(function(){
  $('#id_body').val($('#id_body').val() + editor.getMathML());
  $(".backdrop").hide();
	$("#eqnmodal").fadeOut();
  editor.setMathML('<math xmlns="http://www.w3.org/1998/Math/MathML"/>');
});
