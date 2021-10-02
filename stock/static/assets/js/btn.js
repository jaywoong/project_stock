$(document).ready(function () {
    $('#radioButton').click(function () {
        var R1 = $('input[name="Q1"]:checked').val();
        var R2 = $('input[name="Q2"]:checked').val();
        //var R3 = $('input[name="Q3"]:checked').val();
        var R4 = $('input[name="Q4"]:checked').val();
        var R5 = $('input[name="Q5"]:checked').val();
        var R6 = $('input[name="Q6"]:checked').val();

        var Q1 = parseInt(R1);
        var Q2 = parseInt(R2);
        //var Q3 = parseInt(R3);
        var Q4 = parseInt(R4);
        var Q5 = parseInt(R5);
        var Q6 = parseInt(R6);

        //var result = Q1 + Q2 + Q3 + Q4 + Q5 + Q6;
        alert(Q1 + Q2 + Q4 + Q5 + Q6);
    });
});

