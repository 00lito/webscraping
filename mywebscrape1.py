import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/chart/top/')  # get page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')  # parse content using beautifulsoup

links = soup.select("table tbody tr td.titleColumn a")  # select all the anchors with titles
first10 = links[:10]  # keep the first 10 anchors
for anchor in first10:
    print(anchor.text)  # display the innerText of each anchor
