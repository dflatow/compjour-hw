from midterm_utils import get_all_CA_data
from datetime import datetime
import pandas as pd

def parse_start_date(dt):
	return datetime.strptime(dt, '%m/%d/%Y')

def parse_date_collected(dt):
	return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')

# Using the data dump of all California jobs, calculate the number of days since each job posting has been on the list (i.e. its StartDate) 
# relative to the time it was collected, i.e. how many days the job has been on the list since the data file was collected.
jobs_data = get_all_CA_data()
jobs = jobs_data['jobs']

DATE_COLLECTED = parse_date_collected(jobs_data['date_collected'])

def days_on_list(job, date_collected=DATE_COLLECTED):
    post_date = parse_start_date(job['StartDate'])
    return (date_collected - post_date).days

#Sort the job listings by the number of days they've been on the list, then filter it to show just jobs that have been on the list 2 days or fewer.
#Then print the listings as comma-separated values: job title, days since the job was first posted, and the URL to apply for the job
for job in sorted(jobs, key=days_on_list):
    days = days_on_list(job)
    if days <= 2:
        print('%s,%s,%s' % (job['JobTitle'], days, job['ApplyOnlineURL']))
