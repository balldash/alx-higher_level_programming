const $header = $('header');
const $divHeader = $('div#red_header');

$divHeader.on('click', function () {
	$header.addClass('red');
});
