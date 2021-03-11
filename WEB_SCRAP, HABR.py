url = "https://habr.com/ru/all/"
import requests
import lxml
from bs4 import BeautifulSoup
KEYWORDS = ['дизайн', 'value', 'web', 'python', 'YouTube']
list_of_posts = [ ]
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
ground = soup.find_all("article", class_="post post_preview")
result_of_cycle = [ ]
for element in ground:
    date = element.find("span", class_="post__time").text
    title = element.find("h2", class_="post__title").text.strip()
    post = element.find("div", class_="post__body post__body_crop").text
    links = element.find_all("a")
    for position in links:
        link = position.get("href")
    for key in KEYWORDS:
        if key in post:
            result_of_cycle.append("n")
            print(date, title, link)
if len(result_of_cycle) == 0:
    print("Sorry, no keywords in post")




