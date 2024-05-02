// This is a jquery script
$(document).ready(function () {
    // jquery selector
    const element = $('header');

    // checks if the header element was found
    if (element) {
        element.css('color', '#FF0000');
    } else {
        console.error('Header element not found');
    }
});