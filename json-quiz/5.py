import requests
import json

data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
# fetch the data file and parse the data
data = json.loads(requests.get(data_url).text)


#print(data.keys())
#print(data['user'])
print('A.', data['created_at'])
print('B.', data['user']['created_at'])
print('C.', data['text'])
print('D.', data['user']['screen_name'])
print('E.', data['id'])
print('F.', len(data['entities']['user_mentions']))

# For G.
hashtag_objs = data['entities']['hashtags']
hashtag_texts = [h['text'] for h in hashtag_objs]

print('G.', ','.join(hashtag_texts))

## For H.
url_ojbs = data['entities']['urls']
url_texts = [h['display_url'] for h in url_ojbs]

print('H.', ','.join(url_texts))