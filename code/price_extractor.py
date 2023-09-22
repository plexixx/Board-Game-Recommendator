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
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    amazon_scope = soup.find("li", class_="summary-item summary-sale-item ng-scope",\
                      attrs={"ng-if": "::storesitemsctrl.amazon_ads.url"})
    if amazon_scope != None:
        price = amazon_scope.find("strong", class_="ng-binding").get_text(strip=True)
    else:
        price = -1
    dict_list.append({'id':id, 'price':price})
    filename = "html/item_pages/" + str(id) + ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    print(f"HTML content saved to {filename}")

df = pd.DataFrame(dict_list)
df.to_csv('data/price.csv', index=False)