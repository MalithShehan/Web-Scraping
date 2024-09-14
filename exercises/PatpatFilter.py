import requests
from bs4 import BeautifulSoup
import csv
import time

def slicetext(text, start, end):
    try:
        return text.split(start)[1].split(end)[0]
    except IndexError:
        return ""

csv_file_path = 'patpat.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Land Size', 'Location', 'Total Price', 'Monthly Payment', 'num', 'image'])


for i in range(500):
    url = f'https://www.patpat.lk/property?page={i}&city=&sub_category=&sub_category_name=&category=property&search_txt=&sort_by='

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        cards = soup.find_all(class_='result-item')

        for card in cards:
            try:
                title = card.find(class_='result-title').text.strip()
                size = card.select_one('p.clearfix')
                image = card.find(class_='result-img').img['src']
                print(image)
                data = card.find(class_='result-data')
                link = data.find(class_='col-12 d-none d-lg-block').a['href']
                print(link)
                response = requests.get(link)
                try:
                    su = BeautifulSoup(response.content, 'html.parser')
                    num = su.find(id='mobile-number-toggle-lable-hide').text
                    print(num)
                except:
                    num = ""
                titlw = data.find(class_='result-title').text
                print(title)

                size = data.find(class_='clearfix mb-2')
                size = size.find(class_='d-block w-50 float-left').text
                size = size.replace(" ", "").replace("\n", " ").replace("<spanclass=\"hidden-on-mobile\">, ", " ")
                print(size)
                location = data.find(class_='clearfix result-agent mb-2')
                location = location.find(class_='d-block w-50 float-left').text
                location = location.replace(" ", "").replace("\n", " ").replace("<spanclass=\"hidden-on-mobile\">, ", " ").replace(".", "").replace(" | ","|")
                print(location)
                payment = data.find(class_='pl-lg-0 mt-lg-2 col-lg-6 col-xl-5')

                total = payment.find(class_='clearfix my-1 d-block d-md-none')
                price = payment.find_all(class_='money-wr col-6 m-0 p-0')
                price = price[0].find(class_='money').text
                print(price)
                price1 = card.find_all(class_='money-wr col-6 m-0 p-0')
                price1 = price1[1].find(class_='money').text
                print(price1)
                print("*" * 10)

                arr = [title, size, location, price, price1, num, image]
                with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(arr)
            except:
                pass
    else:
        print("Error to Get File")

    #time.sleep(1)