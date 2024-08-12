const $header = $('header');
const $updateElem = $('div#update_header');

$updateElem.on('click', () => {
	$header.text('New Header!!!');
});
