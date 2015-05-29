import twit_utils as tw
from random import random

CREDSFILE = "~/Dropbox/keys/foxBot.json"

def make_sherman_text(user, lng, lat):
	"""
	Create a custom #sherman message that he found you!
	Arguments:
	None
	Returns:
	A text string with the #hereyouare hashtag and something extra special
	"""
	if random() > 0.7:
		return "I am the finder. #hereyouare: " + lng + "," + lat
	elif random() > 0.5:
		return "Great job, human internet. I will be back soon. #hereyouare: " + lng + "," + lat
	else:
		return "don't fret #hereyouare: " + lng + "," + lat

def get_latest_geo(count=100, hashtag="#whereami"):
	""" 
	Get the latest geotagged tweets with the hashtag (e.g. #whereami)
	Arguments:
		count: limit number of tweets to pull
		hashtag: hashtag to search for
	Returns:
		list of tweet objects
	"""
	hashtag = "#whereami"
	api = tw.get_api(CREDSFILE)
	tweets = tw.get_latest_tweets(CREDSFILE, q=hashtag, opts = {'count':count})
	for tweet in tweets:
		if (tweet['coordinates'] is not None) and (tweet['coordinates']['coordinates'][0] != 0.0):
			return tweet
	return None

def sherman_reply(tweet):
	lng, lat = get_coordinates(tweet)
	user = get_user(tweet)
	txt = make_sherman_text(user, lng, lat)
	#print(txt)
	tw.reply(CREDSFILE, txt, tweet)

def get_coordinates(tweet):
	return str(tweet['coordinates']['coordinates'][0]), str(tweet['coordinates']['coordinates'][1])

def get_user(tweet):
	return tweet['user']['screen_name']


# txt = "#oiasnfoiafasf"

# #tw.reply(credsfile, "nice!", recent_tweets[0])
# print(recent_tweets[0].keys())


# print_coordinate(recent_tweets)