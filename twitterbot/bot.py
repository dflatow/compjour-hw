import foo

def make_it_so():
	tweet = foo.get_latest_geo(hashtag="#whereami")
	if tweet is not None:
		foo.sherman_reply(tweet)

if __name__ == "__main__":
	make_it_so()