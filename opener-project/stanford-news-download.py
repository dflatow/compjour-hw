import requests

# directory to hold data
dirname = "data-hold/stuff"
print("Downloading the news.stanford.edu homepage")

# fetch the page from the URL
response = requests.get("http://news.stanford.edu/")

# get the "text" attribute of the response
rawhtml = response.text
print("news.stanford.edu has", len(rawhtml), "characters")

# fancy string interpolation
print("Saving the current news.stanford.edu to my %s folder" % dirname)

# open a file and prepare it for writing
with open(dirname + "/news.stanford.edu.html", "w") as f:
	f.write(rawhtml)