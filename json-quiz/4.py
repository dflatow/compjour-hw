import requests
import json
from numpy import argmax

data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print('A.', len(data['artists']))
print('B.', data['artists'][4]['name'])
print('C.', data['artists'][11]['followers']['total'])

sep = ', '
print('D.', sep.join(data['artists'][0]['genres']))


def calc_size(img):
	return img['width'] * img['height']

def find_largest_img_ind(artist):
	return argmax([calc_size(x) for x in artist['images']])

artist = data['artists'][-1]
print('E.', artist['images'][find_largest_img_ind(artist)]['url'])

