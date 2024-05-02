$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        // extract the character
        const characterName = data.name;
        $('DIV#character').text(characterName);
    }
});