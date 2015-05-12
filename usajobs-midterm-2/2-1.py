from midterm_utils import get_country_total_jobs
import os
import json
import requests

CODES_URL = "http://stash.compjour.org/data/usajobs/CountryCode.json"
data = requests.get(CODES_URL).json()
out = []

for d in data['CountryCodes']:

	# filter on non-US countries
	if d['Code'] == 'US' or d['Value'] == 'Undefined':
		continue

	country_name = d['Value']
	print("getting: ", country_name)
	out.append([country_name, get_country_total_jobs(country_name)])

# save the file on to your hard drive
os.makedirs("data-hold", exist_ok = True)
with open("data-hold/intl-jobcount.json", 'w') as f:
	f.write(json.dumps(out, indent = 2))
