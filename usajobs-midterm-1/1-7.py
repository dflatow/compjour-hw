from midterm_utils import get_state_total_jobs, pie_chart_html

chart_title = "Job Count by State"
html_filename = "1-7"

states = ['California', 'Florida', 'New York', 'Maryland']

# init list with header
jobs = [['State', 'Jobs']]

for state in states:
  jobs += [[state, get_state_total_jobs(state)]] 
  
with open(html_filename + ".html", "w") as f:
  f.write(pie_chart_html(data=jobs, title=chart_title))