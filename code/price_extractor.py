import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

id_list = []
with open('data/id.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        id_list.append(line.strip())

options = webdriver.ChromeOptions()
options.add_argument('-headless')
driver = webdriver.Chrome(options=options)

dict_list = []

for id in id_list:
    url = "https://boardgamegeek.com/boardgame/" + str(id)
    time.sleep(2)
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    ads = [ad for ad in soup.find_all("li", class_="summary-item summary-sale-item ng-scope")\
        if ad.get("ng-if") is not None or "ad" in ad.get("ng-repeat")]
    store_names = [ad.find('div', class_='summary-item-title bottom ng-binding').get_text(strip=True) for ad in ads]
    prices = [ad.find("strong", class_="ng-binding").get_text(strip=True) for ad in ads]
    dict_list.append(dict(zip(store_names, prices)))
    print(f"Current id: {id}")

df = pd.DataFrame(dict_list)
df.to_csv('data/prices.csv', index=False)