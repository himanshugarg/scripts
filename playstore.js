var r = {};
jQuery('.details').each(function() {
    var link = $.trim($(this).find('.title').attr('href'));
    r[link] = [];
    r[link].push('"' + $.trim($(this).find('.title').text()) + '"');       // name
    r[link].push('"' + link + '"'); // details page link
    r[link].push('"' + $.trim($(this).find('.subtitle').text()) + '"');    // company
    r[link].push(/Free|\d+(\.\d+)?/.exec($.trim($(this).find('.display-price').text()))[0]);
    var rating = $(this).parent().find('.tiny-star');                // star rating
    r[link].push((rating.length && /\d+(\.\d+)+/.exec(rating.attr('aria-label'))[0]) || '');
    console.log(r[link].join(','));
});
