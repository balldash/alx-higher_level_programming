$(document).ready(function () {
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
	const $element = $('div#hello');

	function getWord () {
		return $.get({
			url: url,
			dataType: 'json'
		});
	}

	getWord().then((data) => {
		$element.text(data.hello);
	});
});
