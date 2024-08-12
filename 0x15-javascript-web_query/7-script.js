const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const $charDiv = $('div#character');

$.ajax({
	url: url,
	dataType: 'json'
}).done((data) => {
	$charDiv.text(data.name);
});

