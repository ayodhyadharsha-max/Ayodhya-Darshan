/**
 * Ayodhya Dharshan - Form Inquiry & WhatsApp Direct Submission Tracker
 */
(function() {
  function initFormHandlers() {
    document.querySelectorAll('form').forEach(form => {
      // Set action attribute if empty so HTML validation passes cleanly
      if (!form.getAttribute('action')) {
        form.setAttribute('action', 'thankyou.html');
      }

      form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const nameInput = this.querySelector('[name="name"], [name="fullname"], input[name*="name"], input[type="text"]');
        const phoneInput = this.querySelector('[name="phone"], [name="tel"], input[name*="phone"], input[type="tel"]');
        const dateInput = this.querySelector('[name="date"], [name="dates"], input[name*="date"], input[type="date"]');
        
        const name = nameInput ? nameInput.value : 'Guest';
        const phone = phoneInput ? phoneInput.value : '';
        const date = dateInput ? dateInput.value : 'Upcoming';
        
        let pkg = document.title.split('|')[0].split(':')[0] || 'Ayodhya Tour Package';
        pkg = pkg.replace(/[\n\r]/g, ' ').trim();

        // Direct WhatsApp inquiry URL targeting +919235222399
        const waText = `Hi Ayodhya Dharshan! New Inquiry:\nPackage: ${pkg}\nName: ${name}\nPhone: ${phone}\nTravel Date: ${date}`;
        const waUrl = `https://wa.me/919235222399?text=${encodeURIComponent(waText)}`;

        // Dispatch tracking event for analytics
        if (typeof window.gtag === 'function') {
          window.gtag('event', 'generate_lead', {
            'event_category': 'Form',
            'event_label': pkg,
            'value': 1
          });
        }

        // Direct redirect to WhatsApp
        window.location.href = waUrl;
      });
    });
  }

  // 1. WhatsApp Float Click Event Tracking
  document.addEventListener('click', function(e) {
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.href || '';
    if (href.includes('wa.me') || anchor.classList.contains('whatsapp-float')) {
      const pagePath = window.location.pathname.split('/').pop() || 'index.html';
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'whatsapp_click', { 'page': pagePath });
      }
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFormHandlers);
  } else {
    initFormHandlers();
  }
})();
