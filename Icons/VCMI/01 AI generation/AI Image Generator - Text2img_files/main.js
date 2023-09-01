$(function () {
    $('body').on('click', '.js-cookie-banner-close', function(){
        $('.cookie-banner').hide();
        setCookie('hide_cookie_banner', 1, 60);
    });
});

function getCookie(e) {
    var s = "(?:; )?" + e + "=([^;]*);?";
    return !!new RegExp(s).test(document.cookie) && decodeURIComponent(RegExp.$1)
}

function setCookie(name, value, days) {
    var expires = "";
    if(days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}