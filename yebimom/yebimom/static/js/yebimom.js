$(document).ready(function(){
  $('.center i.favorite').click(function(){
    var center_hash_id = $(this).closest('.center').data('center_hash_id');
    alert(center_hash_id);
  });
});
