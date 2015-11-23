/**
 * Created by pinballwizard on 02.10.15.
 */

$( document ).ready(function(){

    $(".button-collapse").sideNav();
    $('.modal-trigger').leanModal();
    $('select').material_select();
    $(".dropdown-button").dropdown();

//  clean form
//    $(":reset").click(function(){
//        $("form").reset();
//        }
//    );

//  calculator function
    $("#calculate").click(function(){
        var price = $("#price").val();
        var firstpay = $("#first-pay").val();
        var payment = $("#payment").val();
        var residue = price - firstpay;
        var period = Math.ceil(residue/payment);
        $(".total").text(period + " месяцев");
//  filling table
        function fullTable(){
            var today = new Date();
            var dd = today.getDate();
            var mm = today.getMonth()+1;
            var yyyy = today.getFullYear();
            $(".today").text(dd+"."+mm+"."+yyyy);
            $(".firstpay").text(firstpay);
            $(".residue").text(residue);
            var residue2 = residue;
            for(var i=1; i<=period; i++){
                if (residue2<=payment){
                    payment=residue2;
                }
                residue2 -= payment;
                var nextmonth = new Date(yyyy, mm+i, dd);
                var row = document.createElement("tr");
                $("tbody").append(row);
                $("<td></td>").appendTo(row).text(nextmonth.getDate()+"."+(nextmonth.getMonth()+1)+"."+nextmonth.getFullYear());
                $("<td></td>").appendTo(row).text(payment);
                $("<td></td>").appendTo(row).text(residue2);
            }
        }
        function animateTable(){
            $("table").animate({
                height:'100%'
            }, "slow")
        }
        fullTable().animateTable()
    });
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 1000 // Creates a dropdown of number years to control year
    });
});