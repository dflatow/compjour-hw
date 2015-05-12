from midterm_utils import get_all_CA_jobs, dict_to_list_of_lists
from html_utils import geo_marker_map_with_table_html, data_to_html_table
from operator import itemgetter

jobs = get_all_CA_jobs()

def get_city_state(location):

	city_state = location.split(',')
	if len(city_state) == 2:
		return city_state[0].strip(), city_state[1].strip()
	else:
		return None, None

def add_city_to_count(city, count):

	if city in count:
		count[city] += 1
	else:
		count[city] = 1

def add_job_ca_cities_to_count(job, count):

	locations = job['Locations'].split(';')

	for location in locations:
		city, state = get_city_state(location)
		if state == "California":
			add_city_to_count(city, count)

			
count = {}
for job in jobs: 
	add_job_ca_cities_to_count(job, count)

data = dict_to_list_of_lists(count)

with open("2-15.html", "w") as f:
	table = data_to_html_table(data, key=itemgetter(1), reverse=True)
	chart_data =  [['City', 'Jobs']]
	chart_data.extend(data)
	htmlstr = geo_marker_map_with_table_html(data=chart_data, table=table)
	f.write(htmlstr)
