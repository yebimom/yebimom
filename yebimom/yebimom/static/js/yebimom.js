$(document).ready(function(){
  $('.center i.favorite').click(function(){
    var center_hash_id = $(this).closest('.center').data('center_hash_id');

    if ($(this).hasClass('favorite-on')) {
      $(this).removeClass('favorite-on');
      $(this).addClass('favorite-off');
    } else {
      $(this).removeClass('favorite-off');
      $(this).addClass('favorite-on');
    }
  });
});
