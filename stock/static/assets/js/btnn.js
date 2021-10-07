

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

        var res = parseInt(Q1) + parseInt(Q2) + parseInt(Q4) + parseInt(Q5) + parseInt(Q6);


        window.location.href = "portpolio.html?res=" + res;
        alert(res + '점 입니다!!');




    });
});
