import requests
from bs4 import BeautifulSoup

url = "https://example.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Title : " + soup.title.string)
    print("Text : " + soup.p.string)
    print("Link : " + soup.a['href'])
else:
    print("Failed : " + response.text)