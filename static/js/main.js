// $(document).ready(function () {
//     $(".slide-left").click(function () {
//         $(".add-to-cart-box").animate({
//             right: "0"
//         });
//     });
//     $(".slide-right").click(function () {
//         $(".add-to-cart-box").animate({
//             right: "-350px"
//         });
//     });
// });


const cartBtn = document.getElementsByClassName('cart-btn');
const price = document.getElementsByClassName('price');
const slug = document.getElementsByTagName("button")[0].getAttribute('data-price');

// for (var i = 0; i < cartBtn.length; i++) {
//     var addItem = cartBtn[i];

//     addItem.addEventListener('click', function () {
//         console.log(slug)
//     });
// }

$(document).ready(function () {
    $(".cartBtn").click(function () {
        for (var i = 0; i < cartBtn.length; i++) {
            var addItem = cartBtn[i];

            addItem.addEventListener('click', function () {
                console.log(slug)
            });
        }
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


///////////////////////////////////////////////////
// dropdown
///////////////////////////////////////////////////