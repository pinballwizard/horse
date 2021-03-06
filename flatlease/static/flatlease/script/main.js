/**
 * Created by pinballwizard on 02.10.15.
 */

$(document).ready(function(){
//  calculator function
    $('#calculate').click(function(){
        var price = $("#price").val();
        var firstpay = $("#first-pay").val();
        var payment = $("#payment").val();
        var residue = price - firstpay;
        var period = Math.ceil(residue/payment);
        //  filling table
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth()+1;
        var yyyy = today.getFullYear();
        $(".total").text(period + " месяцев");
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
    });
    $('.search-dropdown-button').dropdown({
            inDuration: 300,
            outDuration: 225,
            constrain_width: false, // Does not change width of dropdown to that of the activator
            hover: false, // Activate on hover
            gutter: 0, // Spacing from edge
            belowOrigin: true, // Displays dropdown below the button
            alignment: 'left' // Displays dropdown with edge aligned to the left of button
        }
    );
});