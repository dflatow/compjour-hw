import doctest
import requests
import json
import numpy as np
from time import gmtime, strftime
import re

def get_data():
	data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
	data = json.loads(requests.get(data_url).text)
	return data

def run():
	""" get answers!
	>>> run()
	A. 3
	B. 3
	C. THE GOLDFINCH|56
	D. SOMEWHERE SAFE WITH SOMEBODY GOOD|16|14
	E. 6
	F. REDEPLOYMENT|9
	G. THE GOLDFINCH|11|2
	H. THE BOSTON GIRL|15|-3
	I. 4
	J. 6|-12
	K. 33
	L. 16
	"""
	data = get_data()
	books = data['results']['books']


	# A. Count the number of books published by Scribner
	print("A.", len([1 for x in books if x['publisher'] ==  'Scribner']))

	# B. Find the number of books with the word "detective" (case-insensitive) in their descriptions.
	print("B.", len([1 for x in books if re.search("detective", x['description'], re.IGNORECASE) is not None]))

	# C. Find the book with the most weeks on the list and print its title and the number of weeks it's been listed (as pipe-separated values, i.e. PSV).
	book = books[np.argmax([x['weeks_on_list'] for x in books])]
	out_str = "|".join([book['title'], str(book['weeks_on_list'])])
	print("C.", out_str)

	# D. Find the book that had the lowest rank (i.e. highest rank numerically) last week. Print its title, current rank, and last week's rank, as PSV.
	book = books[np.argmax([x['rank_last_week'] for x in books])]
	out_str = "|".join([book['title'], str(book['rank']), str(book['rank_last_week'])])
	print("D.", out_str)

	# E. Count the books that are new this week (i.e. had a rank of 0 last week)
	new_books = [x for x in books if x['rank_last_week'] == 0]
	print("E.", len(new_books))

	# F. Print the title and rank (as PSV) of the highest-ranked book that is new this week.
	book = new_books[np.argmin([x['rank'] for x in new_books])]
	out_str = "|".join([book['title'], str(book['rank'])])
	print("F.", out_str)

	# G. Find the book that was ranked last week and had the biggest increase in rank this week.
	incumbent_books = [x for x in books if x['rank_last_week'] != 0]
	book = incumbent_books[np.argmax([calc_rank_change(x) for x in incumbent_books])]
	out_str = "|".join([book['title'], str(book['rank']), str(calc_rank_change(book))])
	print("G.", out_str)

	# H. Find the book that was ranked last week and had the biggest drop in rank this week. Print its title, current rank, and change in rank (as PSV).
	book = incumbent_books[np.argmin([calc_rank_change(x) for x in incumbent_books])]
	out_str = "|".join([book['title'], str(book['rank']), str(calc_rank_change(book))])
	print("H.", out_str)

	# I. Among books ranked last week, find and print the sum of the positive changes in rank.
	result = sum([calc_rank_change(x) for x in incumbent_books if calc_rank_change(x) > 0])
	print("I.", result)

	# J. Among books ranked last week, find the sum of the negative changes in rank. Print the number of books that dropped rank and the sum of their rank changes (as PSV).
	dropped_rank_books = [x for x in incumbent_books if calc_rank_change(x) < 0]
	result = sum([calc_rank_change(x) for x in dropped_rank_books])
	out_str = "|".join([str(len(dropped_rank_books)), str(result)])
	print("J.", out_str)

	# K. Print the number of characters in the longest title.
	result = max([len(x['title']) for x in books])
	print("K.", result)

	# L. Print the average number of characters for titles (rounded to the nearest integer).
	result = np.round(np.mean([len(x['title']) for x in books]))
	print("L. {0:0.0f}".format(result))

def calc_rank_change(book):
    return book["rank_last_week"] - book["rank"]

if __name__ == "__main__":
	run()
	doctest.testmod()

