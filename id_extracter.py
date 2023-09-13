from bs4 import BeautifulSoup
import re

# Read HTML file
with open("./mini_project/html/1.html", 'r', encoding='utf-8') as file:
    html_content = file.read()
# 创建BeautifulSoup对象
soup = BeautifulSoup(html_content, 'html.parser')

# 使用CSS选择器提取所有符合条件的<a>元素
# 这里使用[href^="/boardgame/"]表示选择所有href属性以/boardgame/开头的<a>元素
# 这样你可以获取所有这种格式的链接
target_links = soup.select('a[href^="/boardgame/"]')

# 遍历提取到的链接并打印它们的href属性

with open("./mini_project/id_list/1.txt", 'w', encoding='utf-8') as out:
    for link in target_links:
        href = link.get('href')
        id_match = re.search(r'/boardgame/(\d+)/', href)
        if id_match:
            game_id = id_match.group(1)
            # 写入ID部分到文件，每个ID占一行
            out.write(game_id + '\n')
