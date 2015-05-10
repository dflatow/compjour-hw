import requests
import json

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
POSTAL_CODES_URL = 'https://gist.githubusercontent.com/mshafrir/2646763/raw/f2a89b57193e71010386a73976df92d32221d7ba/states_hash.json'

def get_state_total_jobs(state_name):
	atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	return int(resp.json()['TotalJobs'])

def get_country_total_jobs(country_name):
	atts = {"Country": country_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	return int(resp.json()['TotalJobs'])


def state_iso_code_dict():

	state_codes = json.loads(requests.get(POSTAL_CODES_URL).text)

	# swap keys and values and add 'US-' to make iso-code
	# http://stackoverflow.com/questions/1087694/how-to-swap-keys-for-values-in-a-dictionary
	iso_codes = ['US-'  + x for x in state_codes.keys()]

	return dict (zip(state_codes.values(), iso_codes)) 

def iso_code_state_dict():

	state_codes = state_iso_code_dict()
	return dict(zip(state_codes.values(), state_codes.keys()))

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

