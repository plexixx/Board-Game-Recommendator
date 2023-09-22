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
            dict['Name'] = item.find(".//name[@type='primary']").attrib["value"]
            dict['Year'] = item.find(".//yearpublished").attrib["value"]
            dict['min_players'] = item.find(".//minplayers").attrib["value"]
            dict['max_players'] = item.find(".//maxplayers").attrib["value"]
            dict['min_playtime'] = item.find(".//minplaytime").attrib["value"]
            dict['max_playtime'] = item.find(".//maxplaytime").attrib["value"]
            dict['min_age'] = item.find(".//minage").attrib["value"]
            dict['category'] = []
            dict['mechanic'] = []
            for c in item.findall(".//link[@type='boardgamecategory']"):
                dict['category'].append(c.attrib["value"])
            for m in item.findall(".//link[@type='boardgamemechanic']"):
                dict['mechanic'].append(m.attrib["value"])
            for rate in item.findall(".//ratings"):
                dict['userrated'] = rate.find(".//usersrated").attrib["value"]
                dict['avg_rate'] = rate.find(".//average").attrib["value"]
                dict['rank'] = rate.findall(".//rank[@type='subtype']")[0].attrib["value"]
                dict['owned'] = rate.find(".//owned").attrib["value"]
                dict['trading'] = rate.find(".//trading").attrib["value"]
                dict['wanting'] = rate.find(".//wanting").attrib["value"]
                dict['wishing'] = rate.find(".//wishing").attrib["value"]
                dict['num_comments'] = rate.find(".//numcomments").attrib["value"]
                dict['num_weights'] = rate.find(".//numweights").attrib["value"]
                dict['avg_weight'] = rate.find(".//averageweight").attrib["value"]
        dict_list.append(dict)
        time.sleep(2)
        print(count)
        count += 1
    


df = pd.DataFrame(dict_list)
df.to_csv('data/board-game.csv', index=False)
