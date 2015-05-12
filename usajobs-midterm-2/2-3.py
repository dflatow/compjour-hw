import json

def count_jobs(data):
	return sum([x[1] for x in data])

with open("data-hold/domestic-jobcount.json") as f:
	domestic_data = json.loads(f.read())

with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

print("There are %s domestic jobs." % count_jobs(domestic_data))
print("There are %s international jobs." % count_jobs(intl_data))



