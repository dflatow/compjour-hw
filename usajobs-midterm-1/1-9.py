from midterm_utils import get_state_total_jobs, iso_code_state_dict, geo_map_html

chart_title = "Job Count by State"
html_filename = "1-9"

iso_codes = iso_code_state_dict()

# init list with header
jobs = [['State', 'Jobs']]

for code in iso_codes:
  jobs += [[code, get_state_total_jobs(iso_codes[code])]] 

with open(html_filename + ".html", "w") as f:
  f.write(geo_map_html(data=jobs,  title=chart_title))
