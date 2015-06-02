(function(){
  "use strict";
  $(document).ready(function(){
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
})();
