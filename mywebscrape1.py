from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.imdb.com/chart/top/")  # get page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser')  # parse content using beautifulsoup

links = soup.select("table tbody tr td.titleColumn a")  # select all the anchors with titles
first10 = links[:10]  # keep the first 10 anchors
for anchor in first10:
    print(anchor.text)  # display the innerText of each anchor
