# CLI Based Nike Scraper Using GET Requests
import requests
from bs4 import BeautifulSoup

def NikeScraper():
    r = requests.get("https://www.nike.com/sg/en_gb/launch")
    soup = BeautifulSoup(r.content, 'html.parser')
    sgList = soup.find_all(class_="exp-calendar-card-title edf-title-font-size--xlarge nsg-font-family--platform nsg-text--dark-grey")
    sgDate = soup.find_all(class_="exp-calendar-card-badge")

    r = requests.get("https://www.nike.com/au/en_gb/launch")
    soup = BeautifulSoup(r.content, 'html.parser')
    auList = soup.find_all(class_="exp-calendar-card-title edf-title-font-size--xlarge nsg-font-family--platform nsg-text--dark-grey")
    auDate = soup.find_all(class_="exp-calendar-card-badge")

    print('Nike SG:')
    for x, y in zip(sgList, sgDate):
        date = y.text.splitlines()
        print(date[1], date[2], '-', x.text.splitlines()[0])

    print()
    print('Nike AU:')
    for x, y in zip(auList, auDate):
        date = y.text.splitlines()
        print(date[1], date[2], '-', x.text.splitlines()[0])

if __name__ == '__main__':
    NikeScraper()