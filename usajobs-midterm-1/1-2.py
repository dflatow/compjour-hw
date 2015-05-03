from midterm_utils import get_state_total_jobs

state_name = "New York"
ny_tot_jobs = get_state_total_jobs(state_name)
print("%s has %s job listings." % (state_name, ny_tot_jobs))

state_name = "Hawaii"
hi_tot_jobs = get_state_total_jobs(state_name)
print("%s has %s job listings." % (state_name, hi_tot_jobs))

print("Together, they have %s total job listings." % (ny_tot_jobs + hi_tot_jobs))