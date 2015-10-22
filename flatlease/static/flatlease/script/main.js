/**
 * Created by pinballwizard on 02.10.15.
 */

$( document ).ready(function(){

//  open and close client card
    $(".more").click(function(){
        $(this).parent().parent().animate({
            width:'100%'
        }).removeClass("mdl-cell--3-col").addClass("mdl-cell--12-col");
        $(this).removeClass("more").addClass("less");
    });
    $(".less").click(function(){
        $(this)
            .parent()
            .parent()
            .removeClass("mdl-cell--12-col")
            .addClass("mdl-cell--3-col")
            .animate({width:'25%'});
        $(this).removeClass("less").addClass("more");
    });

//  clean form
    $(":reset").click(function(){
        $("form").reset();
    });

//  calculator function
    $("#calculate").click(function(){
        var price = $("#price").val();
        var firstpay = $("#first-pay").val();
        var payment = $("#payment").val();
        var period = Math.ceil((price - firstpay)/payment);
        $(".total").text(period + " месяцев");
    });
});