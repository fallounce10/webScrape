import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.imdb.com/chart/top/")

if page.status_code == 200:
    print("Response 200: OK")

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select("table tbody tr td.titleColumn a")
first5 = links[:10]

movies_list = []

for movie_title in first5:
    movies_list.append(movie_title.text)

for i, k in enumerate(movies_list):
    print(f"{i+1}º lugar: {k}")
