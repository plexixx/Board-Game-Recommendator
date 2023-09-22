import requests
from bs4 import BeautifulSoup

id_list = []

with open('data/id.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        id_list.append(line.strip())

id = id_list[0]

url = "https://boardgamegeek.com/boardgame/" + str(id)
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    filename = "html/item_pages/" + str(id) + ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    print(f"HTML content saved to {filename}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")