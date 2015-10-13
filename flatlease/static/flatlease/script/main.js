/**
 * Created by pinballwizard on 02.10.15.
 */

$( document ).ready(function(){

//  open and close client card
    $(".more").click(function(){
        $(this).parent().parent().animate({
            width:'100%'
        }).toggleClass("mdl-cell--12-col");
        //$(this).
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