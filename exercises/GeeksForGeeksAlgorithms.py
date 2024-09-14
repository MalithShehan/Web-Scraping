import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    topics = soup.find_all('h2')

    data = []

    for topic in topics:
        content = topic.find_next('p')
        topic_text = topic.text.strip()

        # Set empty text for specific titles
        if topic_text in ["Characteristics of an Algorithm:", "Learn Basics of Algorithms", "Analysis of Algorithms"]:
            content_text = ""
        else:
            content_text = content.text.strip() if content else ""

        data.append({
            'Topic': topic_text,
            'Content': content_text
        })

    # Remove the last line
    if data:
        data.pop()

    filename = 'geeksForGeeks.csv'

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Topic', 'Content'])
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Data has been written to {filename}")
    except IOError as e:
        print(f"Failed to write to file: {e}")
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")
