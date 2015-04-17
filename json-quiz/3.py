import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print('A.', data['results'][0]['formatted_address'])
print('B.', data['status'])
print('C.', data['results'][0]['geometry']['location_type'])
print('D.', data['results'][0]['geometry']['location']['lat'])
print('E.', data['results'][0]['geometry']['viewport']['southwest']['lng'])

num_to_print = 2
sep = ', '
print('F.', sep.join([x['long_name'] for x in data['results'][0]['address_components'][:num_to_print]]))