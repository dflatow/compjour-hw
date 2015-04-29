import tweepy
import json
import requests
import json
import os
import numpy as np
import doctest

""" read directly from twitter
with open("/Users/daflatow/Dropbox/keys/foxBot.json") as f:
	creds = json.load(f)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)


members = api.list_members(owner_screen_name = 'cspan',
						   slug = 'members-of-congress', 
						   count = 1000)
accounts = [m._json for m in members]
"""


def get_accounts(data_url, tempfilename):
	# Because this file is relatively large, let's save it to a tempfile, so that
	# subsequent runs read from that file
	if os.path.exists(tempfilename):
	    tfile = open(tempfilename, "r")
	    j = tfile.read()
	else:    
	    j = requests.get(data_url).text
	    tfile = open(tempfilename, "w")
	    tfile.write(j)

	tfile.close()
	return json.loads(j)

def run():
	""" get answers!
	>>> run()
	A. 571
	B. 231
	C. 543
	D. 1955200
	E. 47169
	F. SenJohnMcCain has 1955200 followers
	G. reppittenger has 3668 tweets
	H. 28909
	I. 8385
	"""
	data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
	tempfilename = "data/congresslist.json"
	accounts = get_accounts(data_url, tempfilename)
	# A. What are the total number of accounts in the list?
	print("A.", len(accounts))

	# B. Find the number of accounts that have more than 10000 followers.
	print("B.", len([x for x in accounts if x['followers_count'] > 10000]))

	# C. Find the number of accounts that are "verified".
	print("C.", len([x for x in accounts if x['verified'] == True]))

	# D. Find the highest number of followers among all the accounts.
	followers = [x['followers_count'] for x in accounts]
	max_followers = max(followers)
	print("D.", max_followers)

	# E. Find the highest number of tweets among all the accounts.
	max_tweets = max([x['statuses_count'] for x in accounts])
	print("E.", max_tweets)

	# F. Find the account with the highest number of followers, then print: "{account's screen_name} has {account's followers_count} followers"
	max_followers_user = accounts[np.argmax(followers)]['screen_name']
	print("F. {screen_name} has {followers_count} followers".format(screen_name=max_followers_user, followers_count=max_followers))

	# G. Find the account that has the highest number of tweets and is also not "verified", then print: "{account's screen_name} has {account's statuses_count} tweets"
	verified_tweet_counts = [x['statuses_count'] if not x['verified'] else 0 for x in accounts] # note the ELSE clause so that argmax works!
	max_verified_tweets = max(verified_tweet_counts)
	max_verified_user = accounts[np.argmax(verified_tweet_counts)]['screen_name']
	print("G. {screen_name} has {statuses_count} tweets".format(screen_name=max_verified_user, statuses_count=max_verified_tweets))

	# H. Print the average number (rounded to nearest integer) of followers among all the accounts.
	print("H. {0:0.0f}".format(round(np.mean(followers))))

	# I. Print the median number of followers among all the accounts.
	print("I. {0:0.0f}".format(round(np.median(followers))))


if __name__ == "__main__":
	run()
	doctest.testmod()



