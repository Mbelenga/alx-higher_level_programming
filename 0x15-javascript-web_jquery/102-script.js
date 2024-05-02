$(document).ready(function () {
    // add a click event to the translate button
    $('#btn_translate').click(function () {
        //language code
        const languagecode = $('#language_code').val();
        // Ajax to fetch data
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languagecode}`,
            method: 'GET',
            datatype: 'json',
            success: function (data) {
                $('#hello').text(translation);
            },
            error: function () {
                // Handle Errors
                $('#hello').text('Translation not found.');
            }
        });
    });
});