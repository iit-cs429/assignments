""" Fetch data for this assignment.
You don't need to run this; just here for your reference.

This parses https://en.wikipedia.org/wiki/List_of_computer_scientists for links to computer scientists and downloads each linked page.
"""

from  bs4 import BeautifulSoup
import os
import re
import requests
import time
from urllib.request import urlretrieve

def myfilter(tag):
    """ Find <a> tags like [ <li><a href='/wiki/' ]that are inside of A-Z headings.
    """
    def tryparent(tag):
        try:
            return re.match('[A-Z]', tag.parent.parent.previous_sibling.previous_sibling.span.text)
        except:
            False
    return tag and tag.name == 'a' and tag.parent.name == 'li' and tag.get('href').startswith('/wiki/') and not tag.previous_sibling and tryparent(tag)

def get_links(soup):
    return [l.get('href') for l in soup.find_all(myfilter)]

soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/List_of_computer_scientists').text, "html.parser")

links = get_links(soup)
print('found %d links' % len(links))


os.makedirs('data', exist_ok=True)
for link in links:
    url = 'https://en.wikipedia.org' + link
    print('fetching %s' % url)
    urlretrieve(url, 'data/' + link[6:])
    time.sleep(.6)
