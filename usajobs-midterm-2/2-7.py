import json
from operator import itemgetter
from html_utils import data_to_html_table, bar_chart_with_table_html

with open("data-hold/domestic-jobcount.json") as f:
	data = json.loads(f.read())

sorted_data = sorted(data, key=itemgetter(1), reverse=True)
chart_data = [['State', 'Jobs']]
chart_data.extend(sorted_data[:10])

with open("2-7.html", "w") as f:
	table = data_to_html_table(data, key=itemgetter(0), reverse=False)
	htmlstr = bar_chart_with_table_html(data=chart_data, table=table)
	f.write(htmlstr)



