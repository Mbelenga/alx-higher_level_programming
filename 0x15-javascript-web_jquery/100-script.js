document.addEventListener('DOMContentLoaded', function () {
    const headerElement = document.querySelector('header');
    // If the element was found
    if (headerElement) {
        headerElement.style.color = '#FF0000';
    } else {
        console.error('Header element not found');
    }
});