from midterm_utils import get_state_jobs
import pandas as pd
import re

jobs = get_state_jobs("California", number_of_jobs=250)['JobData']

data = [[x['OrganizationName'], 1] for x in jobs]
df = pd.DataFrame(data, columns=['name', 'count'])
print(df.groupby('name').sum())
