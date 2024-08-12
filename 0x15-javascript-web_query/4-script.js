const $header = $('header');
const $divHeader = $('DIV#toggle_header');

$divHeader.on('click', () => {
	const currClass = $header.attr('class');

	if (currClass === 'green') {
		$header.toggleClass(`${currClass} red`);
	}

	if (currClass === 'red') {
		$header.toggleClass(`${currClass} green`);
	}
});
