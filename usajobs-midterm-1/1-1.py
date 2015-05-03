from midterm_utils import get_state_total_jobs

state_name = "New York"
tot_jobs = get_state_total_jobs(state_name)

print("%s has %s job listings." % (state_name, tot_jobs))