import requests
import time
import xml.etree.ElementTree as ET
import pandas as pd

id_list = []

with open('data/id.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        id_list.append(line.strip())

dict_list = []
count = 1
for id in id_list:
    url = "https://boardgamegeek.com/xmlapi2/thing?id=" + str(id) + "&stats=1"
    response = requests.get(url)

    while response.status_code != 200:
        print("Failed to retrieve the XML. Status code:", response.status_code)
        time.sleep(5)
        response = requests.get(url)

    if response.status_code == 200:
        dict = {}
        root = ET.fromstring(response.text)
        for item in root.findall(".//item[@type='boardgame']"):
            dict['Description'] = item.find(".//description").text
        dict_list.append(dict)
        time.sleep(2)
        print(count)
        count += 1
    


df = pd.DataFrame(dict_list)
df.to_csv('data/description.csv', index=False)
