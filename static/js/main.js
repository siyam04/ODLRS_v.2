$(document).ready(function () {
    $(".slide-left").click(function () {
        $(".add-to-cart-box").animate({
            // width: "350px"

            right: "0"
        });
    });
    $(".slide-right").click(function () {
        $(".add-to-cart-box").animate({
            // width: "0"
            right: "-350px"
        });
    });
});