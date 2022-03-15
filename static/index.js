// TOGGLE MENU
const menuToggle = document.querySelector('.toggle');
const showcase = document.querySelector('.showcase');

function toggle() {
    menuToggle.classList.toggle('active');
    showcase.classList.toggle('active');
}

const menuToggleDomList = [
    menuToggle,
    document.querySelector('.about-menu'),
    document.querySelector('.blog-menu'),
    document.querySelector('.contact-menu'),
]

for (var menuToggleItem of menuToggleDomList) {
    menuToggleItem.addEventListener('click', toggle);
}

// SCROLL FUNCTION
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function aboutFunction() {
    document.getElementById('about').scrollIntoView();
}

function blogFunction() {
    document.getElementById('blog').scrollIntoView();
}

function contactFunction() {
    document.getElementById('contact').scrollIntoView();
}

// TOGGLE THEME
function themeFunction() {
    const elements = [
        document.body,
        document.querySelector('.menu'),
        document.querySelector('.theme'),
        document.querySelector('.about-container'),
        document.querySelector('.text'),
        document.querySelector('.social-icons'),
        document.querySelector('footer'),
        document.querySelector('.overlay'),
    ];

    for (var element of elements) {
        element.classList.toggle('light');
    }
}