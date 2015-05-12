from midterm_utils import get_all_CA_jobs, cleanmoney, cleansalarymax

jobs = get_all_CA_jobs()

# sort the jobs list based on the result of cleansalarymax
sortedjobs = sorted(jobs, key = cleansalarymax, reverse = True)

for job in sortedjobs[0:5]:
    print('%s,%d,%d' % (job['JobTitle'], cleanmoney(job['SalaryMin']), cleanmoney(job['SalaryMax'])))