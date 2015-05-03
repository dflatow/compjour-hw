import requests

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

def get_state_total_jobs(state_name):
	atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	return int(resp.json()['TotalJobs'])

def get_country_total_jobs(country_name):
	atts = {"Country": country_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	return int(resp.json()['TotalJobs'])