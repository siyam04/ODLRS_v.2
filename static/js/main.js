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


const cartBtn = document.getElementsByClassName('cart-btn');
const price = document.getElementsByClassName('price');

for (var i = 0; i < cartBtn.length; i++) {
    var addItem = cartBtn[i];

    addItem.addEventListener('click', function () {
        console.log(cartBtn)
    });
}