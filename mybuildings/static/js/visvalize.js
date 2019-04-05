alert("ok");
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawVisualization);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data1 = google.visualization.arrayToDataTable([
          ['Month', 'Bolivia', 'Ecuador', 'Madagascar', 'Papua New Guinea', 'Rwanda'],
          ['2004/05',  165,      938,         522,             998,           450],
          ['2005/06',  135,      1120,        599,             1268,          288,
          ['2006/07',  157,      1167,        587,             807,           397],
          ['2007/08',  139,      1110,        615,             968,           215],
          ['2008/09',  136,      691,         629,             1026,          366]
        ]);

  var options1 = {
    title : 'Average Power consumption',
    vAxis: {title: 'Power'},
    hAxis: {title: 'Time'},
    seriesType: 'bars'
  };

  var chart1 = new google.visualization.ComboChart(document.getElementById('chart_power'));
  chart1.draw(data, options1);
}


google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data2 = google.visualization.arrayToDataTable({{ total_energy_chart|safe }});

  var options2 = {
    title: 'Energy consumption',
    hAxis: {title: 'Time',  titleTextStyle: {color: '#333'}},
    vAxis: {title: 'Energy', minValue: 0}
  };

  var chart2 = new google.visualization.AreaChart(document.getElementById('chart_energy'));
  chart2.draw(data2, options2);
}