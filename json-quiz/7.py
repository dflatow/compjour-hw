import doctest
import requests
import json
import numpy as np
from time import gmtime, strftime
from math import radians, cos, sin, asin, sqrt

def get_data():
	data_url = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
	return json.loads(requests.get(data_url).text)

def run():
	""" get answers!
	>>> run()
	A. USGS Significant Earthquakes, Past Month
	B. 6
	C. 7.5
	D. 3
	E. M 3.6 - 1km NNW of San Ramon, California
	F. M 3.6 - 1km NNW of San Ramon, California
	G. 2015-04-02 07:06
	H. Wednesday, March 18
	I. 5
	J. 3
	K. M 7.5 - 56km SE of Kokopo, Papua New Guinea
	L. M 6.5 - 99km ENE of Hihifo, Tonga
 	M. https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400&markers=color:orange%7C37.792,-121.9868333%7C-15.5149,-172.9402%7C-15.388,-172.9038%7C-4.7632,152.5606%7C-18.3534,-69.1663%7C-36.0967,-73.6259
	N. https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400&markers=color:orange%7C37.792,-121.9868333&markers=color:red%7C-15.5149,-172.9402%7C-15.388,-172.9038%7C-4.7632,152.5606%7C-18.3534,-69.1663%7C-36.0967,-73.6259
	"""
	data = get_data()
	quakes = data['features']

	# A. Print the title of this particular feed.
	print("A.", data['metadata']['title'])

	# B. Print the number of earthquakes contained in the sample feed.
	print("B.", len(quakes))

	# C. Print the largest magnitude value of the earthquakes.
	print("C.", max([q['properties']['mag'] for q in quakes]))

	# D. Print the number of earthquakes that occurred in "oceanic regions" (Hint: read the documentation here).
	print("D.", len([1 for q in quakes if q['properties']['tsunami'] == 1]))

	# E. Print the title of the earthquake with the smallest magnitude
	small_index = np.argmin([x['properties']['mag'] for x in quakes])
	print("E.",quakes[small_index]['properties']['title'])

	# F. Print the title of the earthquake with the most number of "felt" reports.
	most_felt_index = np.argmax([x['properties']['felt'] for x in quakes])
	print("F.",quakes[most_felt_index]['properties']['title'])

	# G. Print the date of the most recent earthquake in YYYY-MM-DD HH:MM format, e.g. "2015-02-22 17:10" 
	# (note: for this, and subsequent tasks, the answers should be in reference to Greenwich Mean Time, i.e. UTC)
	most_recent_index = np.argmax([x['properties']['time'] for x in quakes])
	event_time = gmtime(quakes[most_recent_index]['properties']['time'] / 1e3)
	print("G.", strftime("%Y-%m-%d %H:%M", event_time))

	# H. Print the date of the oldest earthquake in WEEKDAYNAME, MONTHNAME DD format, e.g. "Tuesday, February 22"
	oldest_index = np.argmin([x['properties']['time'] for x in quakes])
	event_time = gmtime(quakes[oldest_index]['properties']['time'] / 1e3)
	print("H.", strftime("%A, %B %d", event_time))

	# I. Print the number of earthquakes that occurred on a weekday.
	print("I.", len([1 for x in quakes if epoch_to_is_weekday(x['properties']['time'])]))

	# J. Print the number of earthquakes that happened between 5AM and 9AM.
	print("J.", len([1 for x in quakes if epoch_to_is_AM(x['properties']['time'])]))

	# K. Print the title of the earthquake farthest away from Stanford, California
	far_from_school_index = np.argmax([distance_from_stanford(x) for x in quakes])
	print("K.", quakes[far_from_school_index]['properties']['title'])

	# L. Print the title of the earthquake farthest away from Paris, France
	far_from_paris_index = np.argmax([distance_from_paris(x) for x in quakes])
	print("L.", quakes[far_from_paris_index]['properties']['title'])

	# M. Print the URL for a Google Static Map that marks the locations of the earthquakes in orange markers on a world map (i.e. having a zoom factor of 1) that is 500 pixels wide by 400 pixels high.
	print("M.", gen_quake_map_url(quakes, large_threshold=None))

	# N. Same as above, but use red markers to denote earthquakes with magnitudes 6.0 or stronger.
	print("N.", gen_quake_map_url(quakes))

def gen_quake_map_url(quakes, small_color='orange', large_color='red', large_threshold=6.0,
					 zoom=1, dim=(500, 400)):
	map_url = 'https://maps.googleapis.com/maps/api/staticmap' 
	map_url += '?zoom=' + str(zoom)
	map_url += '&size=' + str(dim[0]) + 'x' + str(dim[1])

	map_url += '&markers=color:' + small_color
	for q in quakes:
		if (large_threshold is None) or (q['properties']['mag'] < large_threshold):
			lng, lat = get_lng_lat(q)
			map_url += '%7C' + lat + ',' + lng

	if (large_threshold is None):
		return map_url

	map_url += '&markers=color:' + large_color
	for q in quakes:
		if q['properties']['mag'] >= large_threshold:
			lng, lat = get_lng_lat(q)
			map_url += '%7C' + lat + ',' + lng

	return map_url

def get_lng_lat(quake):
	coords = quake['geometry']['coordinates']
	return str(coords[0]), str(coords[1])

def epoch_to_is_AM(milliseconds_since_epoch):
	hr = gmtime(milliseconds_since_epoch / 1e3).tm_hour
	return (hr >= 5) and (hr <= 8)
	
def epoch_to_is_weekday(milliseconds_since_epoch):
	weekday_num = strftime("%w", gmtime(milliseconds_since_epoch / 1e3)) 
	return not ((weekday_num == '0') or (weekday_num == '6'))

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.
    return c * r

def distance_from_stanford(quake):
    lng = -122.166
    lat = 37.424
    return distance_from_location(quake, lng, lat)

def distance_from_paris(quake):
	lng = 2.3508
	lat = 48.8567
	return distance_from_location(quake, lng, lat)

def distance_from_location(quake, loc_lng, loc_lat):
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, loc_lng, loc_lat)


if __name__ == "__main__":
	run()
	doctest.testmod()



