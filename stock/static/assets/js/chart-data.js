
//배열이 아닌 var로 구성해야 id값 부여해서 html에서 사용 가능

var names1 = 'hanmi';
document.getElementById("names1").innerHTML=names1;
document.getElementById("names1").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names1 +".html";
};
var names2 = 'amore';
document.getElementById("names2").innerHTML=names2;
document.getElementById("names2").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names2 +".html";
};
var names3 = 'hmm';
document.getElementById("names3").innerHTML=names3;
document.getElementById("names3").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names3 +".html";
};
var names4 = 'orion';
document.getElementById("names4").innerHTML=names4;
document.getElementById("names4").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names4 +".html";
};
var names5 = 'lg';
document.getElementById("names5").innerHTML=names5;
document.getElementById("names5").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names5 +".html";
};

var shares1 = 10;
document.getElementById("shares1").innerHTML=shares1;
var shares2 = 20;
document.getElementById("shares2").innerHTML=shares2;
var shares3 = 30;
document.getElementById("shares3").innerHTML=shares3;
var shares4 = 40;
document.getElementById("shares4").innerHTML=shares4;
var shares5 = 50;
document.getElementById("shares5").innerHTML=shares5;



var amount1 = 250;
document.getElementById("amount1").innerHTML=amount1;
var amount2 = 300;
document.getElementById("amount2").innerHTML=amount2;
var amount3 = 450;
document.getElementById("amount3").innerHTML=amount3;
var amount4 = 550;
document.getElementById("amount4").innerHTML=amount4;
var amount5 = 250;
document.getElementById("amount5").innerHTML=amount5;


var ratio1 = 0.1;
document.getElementById("ratio1").innerHTML=ratio1;
var ratio2 = 0.2;
document.getElementById("ratio2").innerHTML=ratio2;
var ratio3 = 0.3;
document.getElementById("ratio3").innerHTML=ratio3;
var ratio4 = 0.4;
document.getElementById("ratio4").innerHTML=ratio4;
var ratio5 = 0.5;
document.getElementById("ratio5").innerHTML=ratio5;
