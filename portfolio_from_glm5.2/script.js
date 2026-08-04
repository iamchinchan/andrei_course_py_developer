/* =====================================================
   PORTFOLIO JAVASCRIPT
   Handles navigation, form submission, and
   redirects to the thank you page
   ===================================================== */

document.addEventListener('DOMContentLoaded', function () {
    /* ----------  Active nav link on scroll  ---------- */
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    function updateActiveLink() {
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + sectionId) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', updateActiveLink);

    /* ----------  Smooth scroll for nav links  ---------- */
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                e.preventDefault();
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    window.scrollTo({
                        top: targetSection.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    /* ----------  Auto-fill year  ---------- */
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    /* ----------  Contact form handling  ---------- */
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // Collect form data
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Basic validation (HTML5 covers required + email type, but double-check)
            if (!name || !email || !message) {
                showToast('Please fill in all fields before sending.', 'warning');
                return;
            }

            // Show inline toast while we redirect
            showToast('Thank you, ' + name + '! Redirecting...', 'success');

            // Store the visitor's name so the thank you page can personalize itself
            try {
                localStorage.setItem('visitor_name', name);
                localStorage.setItem('visitor_email', email);
            } catch (err) {
                // localStorage may be unavailable (private mode); continue silently
            }

            // Redirect to the thank you page after a short delay
            setTimeout(() => {
                window.location.href = 'thank_you.html';
            }, 1200);
        });
    }

    /* ----------  Toast helper  ---------- */
    function showToast(message, type) {
        // Remove any existing toast first
        const existing = document.querySelector('.toast');
        if (existing) existing.remove();

        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.innerHTML =
            '<span class="iconify" data-icon="mdi:check-circle"></span>' +
            '<span>' + message + '</span>';
        document.body.appendChild(toast);

        // Re-render iconify icons inside the toast
        if (window.Iconify) window.Iconify.render();

        // Trigger show animation
        requestAnimationFrame(() => toast.classList.add('show'));

        // Auto-hide after 2.5s (unless we're redirecting)
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 400);
        }, 2500);
    }
});
