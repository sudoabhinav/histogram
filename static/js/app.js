google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawStacked);

function drawStacked() {

  var data = google.visualization.arrayToDataTable([
   ['Element', 'Density', { role: 'style' }],
   ['Copper', 8.94, '#b87333'],
]);

  var options = {
    title: 'Motivation and Energy Level Throughout the Day',
    isStacked: true,
    hAxis: {
      title: 'Time of Day',
      format: 'h:mm a',
      viewWindow: {
        min: [7, 30, 0],
        max: [17, 30, 0]
      }
    },
    vAxis: {
      title: 'Rating (scale of 1-10)'
    }
  };

  var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}