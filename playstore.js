jQuery('.details').each(function() {console.log(
  '"' + $.trim($(this).find('.title').text()) 
  + '","' + $.trim($(this).find('.subtitle').text()) 
  + '",' + /Free|\d+(\.\d+)?/.exec($.trim($(this).find('.display-price').text()))[0] 
  + ',' + ($(this).parent().find('.tiny-star').length && /\d+(\.\d+)+/.exec($.trim($(this).parent().find('.tiny-star').attr('aria-label')))[0]) || '')});
