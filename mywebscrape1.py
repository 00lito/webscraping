from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
# driver = webdriver.Chrome('C:\PythonProjs\chromedriver.exe', options=option)

driver.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(driver.page_source, 'html.parser')  # parse content using beautifulsoup

totalScrapedInfo = []  # list will save all the scraped information
links = soup.select("table tbody tr td.titleColumn a")  # select all the anchors with titles
first10 = links[:10]  # keep the first 10 anchors
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href'])  # Access the movie’s page
    # Find the first element with class ‘ipc-inline-list’
    # old way: infolist = driver.find_element_by_css_selector('.ipc-inline-list')[0]
    # new way
    infolists = driver.find_elements(By.CSS_SELECTOR, ".ipc-inline-list.ipc-inline-list")[0]
    # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
    informations = infolists.find_elements(By.CSS_SELECTOR, "[role='presentation']")
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "rating": informations[1].text,
        "duration": informations[2].text,
    }  # save scraped information in a dictionary
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='firstListCardGroup-editorial']")))
    listElements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='firstListCardGroup-editorial'] .listName") # Extracting the editorial lists elements)
    listNames = [] # creating empty list and then appending only the elements texts
    for el in listElements:
        listNames.append(el.text)
    scrapedInfo['editorial-list'] = listNames # adding the editoral list names to our scapedInfo dictionary
    totalScrapedInfo.append(scrapedInfo)  # append dictionary to the totalScrapedInformation

    print(totalScrapedInfo)  # display the innerText of each anchor
