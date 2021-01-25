import requests
from bs4 import BeautifulSoup

url = "https://www.netflix.com/signup/planform"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
price = soup.find_all("span")
print(price)