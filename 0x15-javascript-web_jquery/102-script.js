$(document).ready(function() {
	$('#btn_translate').click(function() {
    		const languageCode = $('#language_code').val();
		const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
	
		$.get(apiUrl, function(response) {
			$('#hello').text(response.hello);
		});
	});
});	             
