from midterm_utils import get_state_total_jobs

states = ['California', 'Florida', 'New York', 'Maryland']
jobs = []

for state in states:
	jobs += [[state, get_state_total_jobs(state)]] 
	
print(jobs)
