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
        }
    );

//  calculator function
    $("#calculate").click(function(){
        var price = $("#price").val();
        var firstpay = $("#first-pay").val();
        var payment = $("#payment").val();
        var residue = price - firstpay;
        var period = Math.ceil(residue/payment);
        $(".total").text(period + " месяцев");
//  filling table
        var today = new Date();
        $(".today").text(today.getDate()+"."+(today.getMonth()+1)+"."+today.getFullYear());
        $(".firstpay").text(firstpay);
        $(".residue").text(residue);
        $("tbody").append(row);
        if (payment<residue){
            for(var i=1; i<period; i++){
                var row = document.createElement("tr");
                $("tbody").append(row);
                $("<td></td>").appendTo(row).text(today);
                $("<td></td>").appendTo(row).text(payment);
                $("<td></td>").appendTo(row).text(residue)
            }
        } else {
            $("tbody").append(row);
            $(cell).text(today);
            $(cell).text(residue);
            $(cell).text("0")
        }
    });

});