const $listElem = $('ul.my_list');
const $addItem = $('div#add_item');

$addItem.on('click', () => {
	$listElem.append('<li>Item</li>);
});
