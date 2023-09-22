from bs4 import BeautifulSoup
import re
import os

# Read HTML file
html_content = ''
for i in range(1, 251):
    with open("./html/" + str(i) + ".html", 'r', encoding='utf-8') as file:
        html_content += file.read()
soup = BeautifulSoup(html_content, 'html.parser')

# Use CSS selector to extract all elements satisfying the requirement
links = soup.select('a[href^="/boardgame/"]')
id_set = set()

for link in links:
    href = link.get('href')
    id_match = re.search(r'/boardgame/(\d+)/', href)
    if id_match:
        id_set.add(id_match.group(1))

# Write ids into file id.txt'
with open(os.path.join(os.getcwd(), 'data/id.txt'), 'w') as f:
    for id in id_set:
        f.write(id + '\n')