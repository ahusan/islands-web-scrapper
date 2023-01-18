import requests
from bs4 import BeautifulSoup
import csv
import time

#Decalaring URL
url = 'https://isles.gov.mv/Island/DetailsEn/'

filename = 'islands.csv'

with open(filename, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Atoll', 'Island', 'Status', 'IslandCode']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for page in range(0, 1500):
        req = requests.get(url + str(page))
        soup = BeautifulSoup(req.content, 'html.parser')

        # title = soup.find('div', class_='island-heading')
        title = soup.find('div', class_='shadow-box grey-box')
        code = soup.find('div', class_='english-text')
        if(title):
            # d = {}
            titletext= title.text
            codetext = code.text
            e = titletext.strip().splitlines()
            
            if len(e)==9:
                atoll_name = e[4].split('|')
                island_status = e[7].split('|')
            else:
                atoll_name = e[6].split('|')
                island_status = e[9].split('|')

            island_code = codetext.split('|')
            atoll_island = atoll_name[0].split('.')
                

            if(len(island_status)>1 and len(atoll_island)>1 and len(atoll_name)>1):
                print(page)
                print(atoll_island[0].strip())
                print(island_code[1].strip())
                print(atoll_island[1].strip())
                print(island_status[0].strip())
                w.writerow({'Atoll':atoll_island[0].strip(), 'Island':atoll_island[1].strip(), 'Status':island_status[0].strip(), 'IslandCode':island_code[1].strip()})
            else:
                print(page)
                print(atoll_island[0].strip())
                print(atoll_name[0].strip())
                print(atoll_name)
                print(island_status[0].strip())
                w.writerow({'Atoll':atoll_island[0].strip(), 'Island':atoll_name[0].strip(), 'Status':island_status[0].strip(), 'IslandCode':island_code[1].strip()})
        else:
            print('No page found')
        time.sleep(0.10)