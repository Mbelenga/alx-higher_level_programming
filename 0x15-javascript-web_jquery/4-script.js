// This is a jquery script
$(document).ready(function() {
    const toggleDiv = $('DIV#toggle_header');
    const headerElement = $('header');
    // click event handler
    toggleDiv.click(function () {
        headerElement.toggleClass('red green');
    });
});