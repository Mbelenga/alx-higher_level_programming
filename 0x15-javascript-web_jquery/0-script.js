const element = document.querySelector('header');

// Checks if the element was found
if (element) {
    // sets the color
    element.style.color = '#FF0000';
} else {
    console.error('Header element not found');
}