var names10 = 'hanmi';var names20 = 'lg';var names30 = 'orion';var names40 = 'hmm';var names50 = 'amore';
var amount10 = 111;var amount20 = 242;var amount30 = 333;var amount40 = 121;var amount50 = 242;

new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: [names10, names20, names30, names40, names50],
      datasets: [{
        label: "기업",
        backgroundColor: ["#3e95cd", "#8e5ea2","#FF00DD","#FFD400", "00FF00"],
        data: [amount10, amount20, amount30, amount40, amount50]
      }]
    },
    options: {
      title: {
        display: true,
//        text: '기업'
      }
    }
});


