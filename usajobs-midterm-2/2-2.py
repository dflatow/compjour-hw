from midterm_utils import get_state_total_jobs
import os
import json
import requests

CODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
state_names = requests.get(CODES_URL).json().keys()

out = []
for state_name in state_names:

	print("getting ", state_name)
	out.append([state_name, get_state_total_jobs(state_name)])

# save the file on to your hard drive
os.makedirs("data-hold", exist_ok = True)
with open("data-hold/domestic-jobcount.json", 'w') as f:
	f.write(json.dumps(out, indent = 2))
