jQuery('.minirating').each(function() { 
    if (!jQuery(this).text().match(/\d\d\d,\d\d\d/))
        jQuery(this).closest('tr').hide();
});