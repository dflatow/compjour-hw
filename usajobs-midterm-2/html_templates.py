


def data_to_html_table(data, key_index=1):

  sorted_data = sorted(data, key = itemgetter(key_index), reverse = True)

  table_rows = []
  for d in sorted_data:
    table_rows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

  return "\n".join(table_rows)

def bar_chart_with_table_html(data=None):

  table = data_to_html_table(data)

  template = """<!DOCTYPE html>
<html>
  <head>
    <title>Sample Google Chart</title>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

  </head>
  <body>
  <script type="text/javascript">
    google.load("visualization", '1.1', {{packages:['corechart']}});
    google.setOnLoadCallback(drawChart);
    function drawChart() {{
      var data = {data};
      var datatable = google.visualization.arrayToDataTable(data);
      var options = {{
        width: 800,
        height: 500,
        legend: {{ position: 'none' }},
      }};
      var chart = new google.visualization.BarChart(document.getElementById('mychart'));
      chart.draw(datatable, options);
  }}
  </script>

    <div class="container">

      <h1 style="text-align:center">Hello chart</h1>
      <div id="mychart"></div>

      <h2 style="text-align:center">Hello table</h2>
      <table class="table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Jobs</th>
          </tr>
        </thead>
        <tbody>
          {table}
        </tbody>
      </table>
    </div>
  </body>
</html>""".format(data=data, table=table)

return template

def bar_chart_html(data=None, title=None):
  template = '''
  <!DOCTYPE html>
  <html>
    <head>
      <title>Sample Chart</title>
      <script type="text/javascript" src="https://www.google.com/jsapi"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

    </head>
    <body>
      <script type="text/javascript">
        google.load("visualization", '1.1', {{packages:['corechart']}});
        google.setOnLoadCallback(drawChart);
        function drawChart() {{
          var data = {data}
          var datatable = google.visualization.arrayToDataTable(data);
          var options = {{
            width: 600,
            height: 400,
            legend: {{position: 'none'}},
          }};
          var chart = new google.visualization.BarChart(document.getElementById('mychart'));
          chart.draw(datatable, options);
      }}
      </script>

        <div class="container">
          <h1 style="text-align:center">{title}</h1>
          <div id="mychart"></div>
        </div>
    </body>
  </html>'''.format(data=data, title=title)
  return template

def pie_chart_html(data=None, title=None):
  template = '''
  <!DOCTYPE html>
  <html>
    <head>
      <title>Sample Chart</title>
      <script type="text/javascript" src="https://www.google.com/jsapi"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

    </head>
    <body>
      <script type="text/javascript">
        google.load("visualization", '1.1', {{packages:['corechart']}});
        google.setOnLoadCallback(drawChart);
        function drawChart() {{
          var data = {data}
          var datatable = google.visualization.arrayToDataTable(data);
          var options = {{
            width: 600,
            height: 400,
            legend: {{ position: 'none' }},
          }};
          var chart = new google.visualization.PieChart(document.getElementById('mychart'));
          chart.draw(datatable, options);
      }}
      </script>

        <div class="container">
          <h1 style="text-align:center">{title}</h1>
          <div id="mychart"></div>
        </div>
    </body>
  </html>'''.format(data=data, title=title)
  return template

def geo_map_html(data=None, title=None):

  template = '''<html>
    <head>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
      <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    </head>
    <body>
      <script type="text/javascript">
        google.load("visualization", "1", {{packages:["geochart"]}});
        google.setOnLoadCallback(drawRegionsMap);

        function drawRegionsMap() {{

          var data = {data}
          var datatable = google.visualization.arrayToDataTable(data);
          var options = {{'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'}};

          var chart = new google.visualization.GeoChart(document.getElementById('mychart'));

          chart.draw(datatable, options);
        }}
      </script>


        <div class="container">
          <h1 style="text-align:center">{title}</h1>
          <div id="mychart"></div>
        </div>
    </body>
  </html>'''.format(data=data, title=title)
  return template

