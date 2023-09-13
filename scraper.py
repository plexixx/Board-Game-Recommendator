import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://boardgamegeek.com/browse/boardgame/page/"

for i in range(1, 251):
    # Send an HTTP GET request to the URL
    response = requests.get(url + str(i))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        filename = "mini_project/html/" + str(i) + ".html"
        with open(filename, "w", encoding="utf-8") as f:
            # Write the HTML content to the file
            f.write(soup.prettify())
        print(f"HTML content saved to {filename}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
