$(document).ready(function() {
    // div by ID
    const redHeaderDiv = $('DIV#red_header');

    redHeaderDiv.click(function() {
        const headerElement = $('header');
        // checks if the header element was found
        if (HeaderElement) {
            // css sets the color
            HeaderElement.css('color', '#FF0000');
        } else {
            console.error('Header element not found');
        }
    });
});