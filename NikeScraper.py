# CLI Based Nike Scraper Using GET Requests
import requests
import json

def NikeScraper():
    r = requests.get('https://www.nike.com/nikestore/html/services/launchCalendar?country=SG&lang_locale=en_GB&sortOrder=asc')
    sgList = json.loads(r.text)

    r = requests.get('https://www.nike.com/nikestore/html/services/launchCalendar?country=AU&lang_locale=en_GB&sortOrder=asc')
    auList = json.loads(r.text)

    print('Upcoming Releases for Nike')

    print()
    print('Nike SG:')
    for x in sgList['launchCalendarItems']:
        print(x['month'], x['days'], '-', x['title'])

    print()
    print('Nike AU:')
    for x in auList['launchCalendarItems']:
        print(x['month'], x['days'], '-', x['title'])

if __name__ == '__main__':
    NikeScraper()