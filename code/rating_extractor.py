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

df_dict = {}

for id in id_list:
    init_url = "https://boardgamegeek.com/boardgame/" + str(id)
    time.sleep(2)
    driver.get(init_url)
    cur_url = driver.current_url
    rate_dict = {}
    for i in range(1, 11):
        url = cur_url + '/ratings?rating=' + str(i)
        time.sleep(2)
        driver.get(url)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        rate_scope = soup.find("span", class_="panel-body-toolbar-count")
        if rate_scope != None:
            rate_num = rate_scope.find("strong", class_="ng-binding").get_text(strip=True)
        else:
            rate_num = -1
        rate_dict[i] = rate_num
    df_dict[id] = rate_dict

df = pd.DataFrame(df_dict).T
df.to_csv('data/rating.csv', index=True)