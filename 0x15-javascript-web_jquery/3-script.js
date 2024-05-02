// jQuery script
$(document).ready(function() {

    const redHeaderDiv = $('DIV#red_header');

    // add an event handler
    redHeaderDiv.click(function() {
        // find the header
        const headerElement = $('header');

        // check if header was found
        if (headerElement) {
            // use addClass method
            headerElement.addClass('red');
        } else {
            console.error('Header elemnet not found');
        }
    });
});