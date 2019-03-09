import sys
import requests
import bs4
import urlparse

urls = ('https://www.datascience.com/resources', 
	'http://blog.udacity.com/2014/12/24-data-science-resources-keep-finger-pulse.html',
	'http://www.datasciencecentral.com/group/resources/forum/topics/comprehensive-list-of-data-science-resources',
	'http://www.dataschool.io/resources/',
	'https://www.datacamp.com/community/tutorials/learn-data-science-resources-for-python-r',
	'https://www.ngdata.com/top-data-science-resources/',
	'https://www.iq.harvard.edu/data-science-resources',
	'https://www.datascienceweekly.org/data-science-resources',
	'https://www.datascienceweekly.org/data-science-resources',
	'http://datasciencetoronto.com/resources/',
	'https://conductrics.com/data-science-resources/',
	'http://www.kdnuggets.com/2015/03/free-data-mining-data-science-books-resources.html'
	)

links = {}
for url in urls:
    r  = requests.get(url)
    soup  = bs4.BeautifulSoup(r.text, 'html5lib')
    for l in soup.find_all('a'):
	urlloc  = urlparse.urlparse(url).netloc
	# if this is a http link and not self promotion
        if l.has_attr('href') and l['href'].startswith('http') and urlparse.urlparse(l['href']).netloc <> urlloc:
	    link = l['href'].strip('/') 
            links.setdefault(link, set()).add(url)
        
for k, v in sorted(links.items(), key=lambda x: len(links[x[0]]), reverse=True):
    if len(v) > 1: 
        print(k, len(v))
