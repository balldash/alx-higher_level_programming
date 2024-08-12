const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
const movieList = $('ul#list_movies');

$.ajax({
	url: url,
	dataType: 'json'
}).done((data) => {
	const movies = data.results;

	for (let i = 0; i < movies.length; ++i) {
		const title = movies[i].title;
		const element = `<li>${title}</li>`;
		$movieList.append(element);
	}
});
