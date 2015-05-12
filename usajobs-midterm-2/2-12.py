from midterm_utils import get_all_CA_jobs, cleanmoney
import pandas as pd

jobs = get_all_CA_jobs()

data = [[job['JobTitle'], cleanmoney(job['SalaryMin']), cleanmoney(job['SalaryMax'])] for job in jobs]
df = pd.DataFrame(data, columns=['JobTitle', 'SalaryMin', 'SalaryMax'])
df = df.query('SalaryMax < 100000.0')
df['SalaryRange'] = df['SalaryMax'] - df['SalaryMin']

job = df.sort('SalaryRange', ascending=False).iloc[0]
print("%s, %d, %d" % (job['JobTitle'], job['SalaryMin'], job['SalaryMax']))