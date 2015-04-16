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

  $('.center i.favorite').click(function(){
    var center_hash_id = $(this).closest('.center').data('center_hash_id');

    if ($(this).hasClass('favorite-on')) {
      $(this).removeClass('favorite-on');
      $(this).addClass('favorite-off');

      $.ajax({
        method: "DELETE",
        url: "/api/centers/" + center_hash_id + "/favorite/delete/"
      });

    } else {
      $(this).removeClass('favorite-off');
      $(this).addClass('favorite-on');

      $.ajax({
        method: "POST",
        url: "/api/centers/" + center_hash_id + "/favorite/"
      });
    }
  });
});
