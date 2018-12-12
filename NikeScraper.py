# CLI Based Nike Scraper Using GET Requests coded in Python
# Credits to danielbrzn for URL 

import requests
import json

def NikeScraper():
    locales = ['SG', 'AU']
    for locale in locales:
        url = 'https://www.nike.com/nikestore/html/services/launchCalendar?country={}&lang_locale=en_GB&sortOrder=asc'.format(locale)
        r = requests.get(url)
        itemList = json.loads(r.text)
        print('\nNike {}'.format(locale))
        for item in itemList['launchCalendarItems']:
            print(item['month'], item['days'], '-', item['title'])

if __name__ == '__main__':
    print('Nike Launch Calendar')
    NikeScraper()