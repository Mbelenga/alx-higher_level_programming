$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        // extract character from the fetched data
        const translation = data.hello;

        // Displays the translation
        $('DIV#hello').text(translation);
    }
});