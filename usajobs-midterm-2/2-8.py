from html_utils import map_with_table_html, data_to_html_table
from operator import itemgetter
import json

with open("data-hold/intl-jobcount.json") as f:
	data = json.loads(f.read())

data = [x for x in data if x[1] > 0]

chart_data = [['Country', 'Jobs']]
for d in data:
	if d[1] > 0:
		chart_data.append([d[0], d[1]])

with open("2-8.html", "w") as f:
	table = data_to_html_table(data, key=itemgetter(0), reverse=False)
	htmlstr = map_with_table_html(data=chart_data, table=table)
	f.write(htmlstr)