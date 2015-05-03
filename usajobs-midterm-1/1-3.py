from midterm_utils import get_country_total_jobs

countries = ['China', 'South Africa', 'Tajikistan']
total = 0
for country in countries:
	count = get_country_total_jobs(country)
	print("%s has %s job listings." % (country, count))
	total += count

print("Together, they have %s total job listings." % total)
