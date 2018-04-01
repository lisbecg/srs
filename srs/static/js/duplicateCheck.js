$('#fakeSubmit').click(function(e){
	// Initiate json object to hold selections
	var jsonRes = new Object();
	jsonRes.videos = [];
	jsonRes.audios = [];
	jsonRes.images = [];
	jsonRes.equations = [];
	jsonRes.documents = [];

	$('#videos input:checked').each(function() {
	    jsonRes.videos.push($(this).attr('name'));
	});

	$('#audios input:checked').each(function() {
	    jsonRes.audios.push($(this).attr('name'));
	});

	$('#images input:checked').each(function() {
	    jsonRes.images.push($(this).attr('name'));
	});

	$('#documents input:checked').each(function() {
	    jsonRes.documents.push($(this).attr('name'));
	});

	$('#equations input:checked').each(function() {
	    jsonRes.equations.push($(this).attr('name'));
	});


	var jsonString = JSON.stringify(jsonRes);
	$('#id_hiddenField').val(jsonString);

	// Finally submit
	$('#submit').click();
});
