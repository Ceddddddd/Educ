let loginForm = document.querySelector('.login-form');

document.querySelector('#login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    loginForm.classList.remove('active');
}

window.onscroll = () =>{
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

// Get the SVG element by its ID
const customShape = document.getElementById('custom-shape');

// Function to handle scroll event
function handleScroll() {
    // Check if the user has scrolled down
    if (window.scrollY > 0) {
        // If scrolled down, hide the SVG element with a smooth transition
        customShape.style.transition = 'opacity 0.3s ease-in-out';
        customShape.style.opacity = '0';
    } else {
        // If not scrolled down, show the SVG element with a smooth transition
        customShape.style.transition = 'opacity 0.3s ease-in-out';
        customShape.style.opacity = '1';
    }
}

// Add event listener for scroll event
window.addEventListener('scroll', handleScroll);

