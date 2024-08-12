const $header = $('header');
const $divHeader = $('div#red_header');

$divHeader.on('click', function() {
	$header.css('color', '#FF0000');
});
