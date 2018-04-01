var editor;

window.onload = function () {
  editor = com.wiris.jsEditor.JsEditor.newInstance ({'language': 'en'});
  editor.insertInto (document.getElementById ('editorContainer'));
}

$('#eqn-btn').click(function(){
  $('#id_equation').val(editor.getMathML());
  $('.post-form').submit();
});

// set #id_equation to latex values
// trigger click on #submit-btn
