//from portfolio_model import OptimizePortfolio
//opti = OptimizePortfolio()
//
//var custom_df = pd.DataFrame({'stock_name' : ['samsung', 'lg', 'sk', 'naver', 'kakao'] ,
//'num_of_shares' : [10, 2, 23, 7, 8],
//'amount' : [3000, 22222, 444444, 789000, 232323],
//'ratio' : [0.3, 0.1, 0.2, 0.1, 0.3]});
//
//var stock_n = custom_df['stock_name'];
//
//
//
//
//function printName() {
//    const total_asset = document.getElementById('Q3').value;
//}

//배열이 아닌 var로 구성해야 id값 부여해서 html에서 사용 가능
var stock_name = ['고려아연', '삼성전기', 'SK이노베이션', 'S-Oil', '한화솔루션'];
var num_of_shares = [31, 70, 39, 69, 118];
var amount = [15872000, 11550000, 9828000, 7452000, 4985500];
var ratio = [0.32, 0.23, 0.2, 0.15, 0.1];

var names1 = stock_name[0];
document.getElementById("names1").innerHTML=names1;
document.getElementById("names1").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names1 +".html";
};
var names2 = stock_name[1];
document.getElementById("names2").innerHTML=names2;
document.getElementById("names2").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names2 +".html";
};
var names3 = stock_name[2];
document.getElementById("names3").innerHTML=names3;
document.getElementById("names3").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names3 +".html";
};
var names4 = stock_name[3];
document.getElementById("names4").innerHTML=names4;
document.getElementById("names4").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names4 +".html";
};
var names5 = stock_name[4];
document.getElementById("names5").innerHTML=names5;
document.getElementById("names5").onclick = function() {
    var openNewWindow = window.open("about:blank");
    openNewWindow.location.href = names5 +".html";
};

var shares1 = num_of_shares[0];
document.getElementById("shares1").innerHTML=shares1;
var shares2 = num_of_shares[1];
document.getElementById("shares2").innerHTML=shares2;
var shares3 = num_of_shares[2];
document.getElementById("shares3").innerHTML=shares3;
var shares4 = num_of_shares[3];
document.getElementById("shares4").innerHTML=shares4;
var shares5 = num_of_shares[4];
document.getElementById("shares5").innerHTML=shares5;



var amount1 = amount[0];
document.getElementById("amount1").innerHTML=amount1;
var amount2 = amount[1];
document.getElementById("amount2").innerHTML=amount2;
var amount3 = amount[2];
document.getElementById("amount3").innerHTML=amount3;
var amount4 = amount[3];
document.getElementById("amount4").innerHTML=amount4;
var amount5 = amount[4];
document.getElementById("amount5").innerHTML=amount5;


var ratio1 = ratio[0];
document.getElementById("ratio1").innerHTML=ratio1;
var ratio2 = ratio[1];
document.getElementById("ratio2").innerHTML=ratio2;
var ratio3 = ratio[2];
document.getElementById("ratio3").innerHTML=ratio3;
var ratio4 = ratio[3];
document.getElementById("ratio4").innerHTML=ratio4;
var ratio5 = ratio[4];
document.getElementById("ratio5").innerHTML=ratio5;

new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: [names1, names2, names3, names4, names5],
      datasets: [{
        label: "기업",
        backgroundColor: ["#3e95cd", "#8e5ea2","#FF00DD","#FFD400", "00FF00"],
        data: [amount1, amount2, amount3, amount4, amount5]
      }]
    },
    options: {
      title: {
        display: true,
//        text: '기업'
      }
    }
});

