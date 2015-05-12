from midterm_utils import get_state_jobs
import pandas as pd
import re

jobs = get_state_jobs("California", number_of_jobs=250)['JobData']

data = [[x['OrganizationName'], 1] for x in jobs]
df = pd.DataFrame(data, columns=['name', 'count'])
s = df.name.value_counts()
print("Counts as a pandas series:\n",s)
print("\nCounts as a dict:\n", dict(s))