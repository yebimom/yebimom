(function(){
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
})();

$(document).ready(function(){
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

  $('.center i.favorite-border').click(function(){
    var center_hash_id = $(this).closest('.center').data('center_hash_id');
    var favorite = $(this).parent(".center").find(".favorite");

    if (favorite.hasClass('favorite-on')) {
      favorite.removeClass('favorite-on');
      favorite.addClass('favorite-off');

      $.ajax({
        method: "DELETE",
        url: "/api/centers/" + center_hash_id + "/favorite/delete/"
      });

    } else {
      favorite.removeClass('favorite-off');
      favorite.addClass('favorite-on');

      $.ajax({
        method: "POST",
        url: "/api/centers/" + center_hash_id + "/favorite/"
      });
    }
  });
});
