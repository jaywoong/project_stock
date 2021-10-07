$(document).ready(function () {
    $('#Q333').click(function () {
//    var A1 = $('input[name="Q1"]:checked').val();


        var totals = $('input[name="Q36"]').val();
        window.location.href = "getdata.html?totals=" + totals

    });
});


//var totals = document.getElementById('Q3').value;
//    window.location.href = "getdata.html?total=" + total