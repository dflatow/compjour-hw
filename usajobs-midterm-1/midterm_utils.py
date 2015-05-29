import requests
import json

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
POSTAL_CODES_URL = 'https://gist.githubusercontent.com/mshafrir/2646763/raw/f2a89b57193e71010386a73976df92d32221d7ba/states_hash.json'

def get_state_jobs(state_name, number_of_jobs=1):
	atts = {"CountrySubdivision": state_name, 'NumberOfJobs': number_of_jobs}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	return resp.json()

def get_state_total_jobs(state_name, number_of_jobs=1):
	jobs = get_state_jobs(state_name=state_name, number_of_jobs=number_of_jobs)
	return int(jobs['TotalJobs'])

def get_country_total_jobs(country_name, number_of_jobs=1):
	atts = {"Country": country_name, 'NumberOfJobs': number_of_jobs}
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