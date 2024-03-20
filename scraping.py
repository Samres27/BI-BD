import requests
from bs4 import BeautifulSoup
page="https://clasificados.lostiempos.com/inmuebles"

text=requests.get(page)
print(text.text)