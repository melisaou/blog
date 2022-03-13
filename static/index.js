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
    document.querySelector('.projects-menu'),
    document.querySelector('.contact-menu'),
]

for (var menuToggleItem of menuToggleDomList) {
    menuToggleItem.addEventListener('click', toggle);
}

// TOP BUTTON
mybutton = document.getElementById('topBtn');
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 60 || document.documentElement.scrollTop > 60) {
        mybutton.style.display = 'block';
    } else {
        mybutton.style.display = 'none';
    }
}

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// LOADER
const loader = document.querySelector('.loader');
const main = document.querySelector('.main');

function init() {
    setTimeout(() => {
        loader.style.opacity = 0;
        loader.style.display = 'none';

        main.style.display = 'block';
        setTimeout(() => (main.style.opacity = 1), 50);
    }, 1500);
}

init();

// TOGGLE THEME
function themeFunction() {
    const elements = [
        document.body,
        document.querySelector('.showcase'),
        document.querySelector('.menu'),
        document.querySelector('.theme'),
        document.querySelector('.about-container'),
        document.querySelector('.spinner'),
        document.querySelector('footer'),
        document.querySelector('.social-icons'),
        document.querySelector('.overlay'),
        document.querySelector('.text'),
        document.querySelector('.toggle')
    ];

    for (var element of elements) {
        element.classList.toggle('light');
    }
}

// // DOMINO
// var textWrapper = document.querySelector('.domino .letters');
// textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

// anime.timeline({ loop: true })
//     .add({
//         targets: '.domino .letter',
//         rotateY: [-90, 0],
//         duration: 1500,
//         delay: (el, i) => 60 * i
//     }).add({
//         targets: '.domino',
//         opacity: 0,
//         duration: 500,
//         easing: "easeOutExpo",
//         delay: 500
//     });