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
    const itemPrice = $("#itemPrice");
    const cartBtn = $("#cart-btn");

    $('#cart-btn').click(function () {

        const slug = $(this).attr('data-slug');
        let price = $('#price').text();

        for (let i = 0; i < cartBtn.length; i++) {
            const cbtn = cartBtn[i];
            console.log('clicked')
        }

        // console.log(price);
    });
});