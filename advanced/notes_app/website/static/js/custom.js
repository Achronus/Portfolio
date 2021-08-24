document.addEventListener("DOMContentLoaded", function() {
  // Create back to top button
  const scrollToTopButton = document.querySelector('.top-link');

  const scrollFunc = () => {
    let y = window.scrollY;
    
    // Add and remove sticky navbar styles
    if (window.scrollY > 20) {
      document.getElementById('site-navigation').classList.add('sticky-nav');
    } else {
      document.getElementById('site-navigation').classList.remove('sticky-nav');
    } 

    // Display button after view-height reached
    if (y > 500) {
      scrollToTopButton.className = "top-link show";
    } else {
      scrollToTopButton.className = "top-link hide";
    }
  };

  window.addEventListener("scroll", scrollFunc);

  const scrollToTop = () => {
    const c = document.documentElement.scrollTop || document.body.scrollTop;
    
    // Scroll back to top
    if (c > 200) {
      window.requestAnimationFrame(scrollToTop);
      window.scrollTo(0, c - c / 1.8);
    }
  };

  scrollToTopButton.onclick = function(e) {
    e.preventDefault();
    scrollToTop();
  };

  // Float labels above input text
  const inputLabels = (() => {
    const handleFocus = (element) => {
      const target = element.target;
      target.parentNode.classList.add('active');
      target.setAttribute('placeholder', target.getAttribute('data-placeholder'));
    };
    const handleBlur = (element) => {
      const target = element.target;
      if (!target.value) {
        target.parentNode.classList.remove('active');
      }
      target.removeAttribute('placeholder');
    };

    const bindEvents = (element) => {
      const floatField = element.querySelector('input');
      floatField.addEventListener('focus', handleFocus);
      floatField.addEventListener('blur', handleBlur);
    };

    const init = () => {
      const floatLabel = document.querySelectorAll('.float-label');

      floatLabel.forEach((element) => {
        if (element.querySelector('input').value) {
          element.classList.add('active');
        }

        bindEvents(element);
      });
    };

    return {
      init: init
    };
  })();
  inputLabels.init();
});

// JQuery functionality
$(document).ready(function() {
  // Add style to navbar toggler
  $(".navbar-toggler").click(function() {
    $("#site-navigation .container").toggleClass("toggler-bg");
  });
});

// Delete Notes on button press
function deleteNote(noteId) {
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId })
  }).then((_res) => {
    window.location.href = "/notes"; // Refresh page
  });
};