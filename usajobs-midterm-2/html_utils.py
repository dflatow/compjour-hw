
def geo_marker_map_with_table_html(data=None, table=None):
  template="""<html>
    <head>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

      <script type='text/javascript' src='https://www.google.com/jsapi'></script>

    </head>
    <body>

      <script type='text/javascript'>
       google.load('visualization', '1', {{'packages': ['geochart']}});
       google.setOnLoadCallback(drawMarkersMap);

        function drawMarkersMap() {{
        var data = {data};
        var datatable = google.visualization.arrayToDataTable(data)

        var options = {{
          region: 'US-CA',
          resolution: 'provinces',
          displayMode: 'markers',
          backgroundColor: {{fill: '#A5C5FF', strokeWidth: 2, stroke: '#333'}},
          datalessRegionColor: '#ddeedd',
          colorAxis: {{colors: ['yellow', 'red']}}
        }};

        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));
        chart.draw(datatable, options);
      }};
      </script>


      <div class="container">
        <div id="mychart" style="width: 900px; height: 500px;"></div>
        <table class="table table-striped table-condensed">
          <thead>
            <tr>
              <th>City</th>
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

def data_to_html_table(data, key=None, reverse=None):

  sorted_data = sorted(data, key=key, reverse=reverse)

  table_rows = []
  for d in sorted_data:
    table_rows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

  return "\n".join(table_rows)


def map_with_table_html(data=None, table=None):

  template="""
  <html>
    <head>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
      <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    </head>

    <body>
      <script type="text/javascript">
        google.load("visualization", "1", {{packages:["geochart"]}});
        google.setOnLoadCallback(drawRegionsMap);
        function drawRegionsMap() {{
          var data = {data};
          var datatable = google.visualization.arrayToDataTable(data);
          var options = {{'width': 800, 'height': 500, 'resolution': 'countries'}};
          var chart = new google.visualization.GeoChart(document.getElementById('mychart'));
          chart.draw(datatable, options);
        }}
      </script>

      <div class="container">
        <h1 style="text-align:center">Foreign Country Jobs</h1>
        <div id="mychart"></div>

        <h2 style="text-align:center">Data</h2>
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
      </div> <!--end container -->

    <body>
      <div id="mychart"></div>
    </body>
  </html>""".format(data=data, table=table)
  return template

def bar_chart_with_table_html(data=None, table=None):

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

        <h1 style="text-align:center">Job Totals, Top 10 states</h1>
        <div id="mychart"></div>

        <h2 style="text-align:center">Data</h2>
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

