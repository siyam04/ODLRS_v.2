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

    ///////////////////////////
});

const itemPrice = $("#itemPrice");

const cartBtn = document.getElementsByClassName('cart-btn');
const slug = document.getElementsByTagName('span').getAttribute('data-price');


cartBtn.addEventListener('click', function () {

    for (let i = 0; i < cartBtn.length; i++) {
        const element = cartBtn[i];

        console.log('clicked')
    }

});