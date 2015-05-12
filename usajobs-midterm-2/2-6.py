import json
from operator import itemgetter

with open("data-hold/intl-jobcount.json") as f:
	data = json.loads(f.read())

sorted_data = sorted(data, key=itemgetter(1), reverse=True)
others = 0

for d in sorted_data:
	if d[1] > 10:
		print("%s, %s" %(d[0],d[1]))
	else:
		others += d[1]

print("Others,", others)