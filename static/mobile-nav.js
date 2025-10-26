// Mobile navigation toggle
const nav = document.querySelector('#site-nav nav');
const homeButton = document.querySelector('#home a');

// Start with menu closed on mobile
if (window.innerWidth <= 480) {
	nav.classList.add('mobile-menu-closed');
}

// Toggle menu on mobile when clicking home button
homeButton.addEventListener('click', (e) => {
	if (window.innerWidth <= 480) {
		e.preventDefault();
		nav.classList.toggle('mobile-menu-closed');
	}
	// On desktop, let the link work normally (navigate to /about)
});

// Reset on window resize
window.addEventListener('resize', () => {
	if (window.innerWidth > 480) {
		nav.classList.remove('mobile-menu-closed');
	} else if (!nav.classList.contains('mobile-menu-closed')) {
		nav.classList.add('mobile-menu-closed');
	}
});
