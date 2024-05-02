$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        // Extract character
        const movieTitles = data.results.map(function (movie) {
            return movie.title;
        })
        const listElement = $('UL#list_movies');
        $.each(movieTitles, function (index, title) {
            const listitem = $('<li>' + title + '</li>');
            listElement.append(listItem);
        })
    }
});