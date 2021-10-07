$(document).ready(function () {
    $('#radioButton').click(function () {
        var R1 = $('input[name="Q1"]:checked').val();
        var R2 = $('input[name="Q2"]:checked').val();
        var R3 = $('input[name="Q3"]')val();
        var R4 = $('input[name="Q4"]:checked').val();
        var R5 = $('input[name="Q5"]:checked').val();
        var R6 = $('input[name="Q6"]:checked').val();

        var T1 = parseInt(R1);
        var T2 = parseInt(R2);
        var T3 = parseInt(R3*10000);
        var T4 = parseInt(R4);
        var T5 = parseInt(R5);
        var T6 = parseInt(R6);

        var result = T1 + T2 + T4 + T5 + T6;
//        var moneyInput = prompt("ddd"+"");
        alert(result00 + '점 입니다');

    });
});

