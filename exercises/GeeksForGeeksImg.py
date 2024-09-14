import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

response = requests.get(url)

if not os.path.exists('images'):
    os.makedirs('images')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    img = soup.find('img', {'src': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191016135223/What-is-Algorithm_-1024x631.jpg'})

    if img:
        img_url = urljoin(url, img['src'])

        img_response = requests.get(img_url)

        img_name = os.path.basename(img_url)

        with open(f'images/{img_name}', 'wb') as f:
            f.write(img_response.content)

        print(f"Downloaded {img_name}")
    else:
        print("No image found with the specified src")
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")