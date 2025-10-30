// Mobile navigation toggle
const nav = document.querySelector('#site-nav nav');
const menuToggle = document.querySelector('#menu-toggle button');

// Start with menu closed on mobile
if (window.innerWidth <= 480) {
	nav.classList.add('mobile-menu-closed');
}

// Toggle menu on mobile when clicking menu toggle button
if (menuToggle) {
	menuToggle.addEventListener('click', (e) => {
		if (window.innerWidth <= 480) {
			e.preventDefault();
			nav.classList.toggle('mobile-menu-closed');
		}
	});
}

// Reset on window resize
window.addEventListener('resize', () => {
	if (window.innerWidth > 480) {
		nav.classList.remove('mobile-menu-closed');
	} else if (!nav.classList.contains('mobile-menu-closed')) {
		nav.classList.add('mobile-menu-closed');
	}
});
