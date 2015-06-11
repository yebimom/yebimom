(function(){
  "use strict";
  $(document).ready(function(){
    // CSRF CORS
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });
    
    // Smooth Scrolling
    $('body').scrollspy({target: '#scrollspy'});

    $(function() {
      $('a[href*=#]:not([href=#]):not([data-toggle])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top
            }, 500);
            return false;
          }
        }
      });
    });
  });
})();
