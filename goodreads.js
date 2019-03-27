jQuery('.smallText.greyText').each(function() { 
    if (!jQuery(this).text().match(/\d\d,\d\d\d ratings/))
        jQuery(this).closest('div').parent().hide();
});
