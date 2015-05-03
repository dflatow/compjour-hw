from midterm_utils import get_state_total_jobs, state_iso_code_dict, geo_map_html

chart_title = "Job Count by State"
html_filename = "1-8"

iso_codes = state_iso_code_dict()

states = ['California', 'Florida', 'New York', 'Maryland']

# init list with header
jobs = [['State', 'Jobs']]

for state in states:
  jobs += [[iso_codes[state], get_state_total_jobs(state)]] 

with open(html_filename + ".html", "w") as f:
  f.write(geo_map_html(data=jobs,  title=chart_title))
