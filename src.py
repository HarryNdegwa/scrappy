from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/"

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html,"html.parser")

# print(soup.get_text())  # prints all text from the html without html tags

# print(soup.find("img")) # returns the first image

# print(soup.find_all("img")) # returns all images in that page
