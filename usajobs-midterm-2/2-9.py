from midterm_utils import get_state_jobs
import re

jobs = get_state_jobs("California", number_of_jobs=250)['JobData']
mydict = {'Full-time': 0, 'Other': 0}

for job in jobs:
	schedule = job['WorkSchedule']
	if re.search("full", schedule, re.IGNORECASE):
		mydict['Full-time'] += 1
	else:
		mydict['Other'] += 1

print(mydict)