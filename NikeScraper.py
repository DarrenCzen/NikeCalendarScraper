#      __ _ _            ___      _                _            
#   /\ \ (_) | _____    / __\__ _| | ___ _ __   __| | __ _ _ __ 
#  /  \/ / | |/ / _ \  / /  / _` | |/ _ \ '_ \ / _` |/ _` | '__|
# / /\  /| |   <  __/ / /__| (_| | |  __/ | | | (_| | (_| | |   
# \_\ \/ |_|_|\_\___| \____/\__,_|_|\___|_| |_|\__,_|\__,_|_|   

# CLI Based Nike Scraper Using GET Requests coded in Python
# Credits to danielbrzn for URL

import requests
import json
from pyfiglet import figlet_format

def NikeScraper():
    locales = ['SG', 'AU']
    for locale in locales:
        url = 'https://www.nike.com/nikestore/html/services/launchCalendar?country={}&lang_locale=en_GB&sortOrder=asc'.format(locale)
        r = requests.get(url)
        itemList = json.loads(r.text)
        print('Nike {}'.format(locale))
        for item in itemList['launchCalendarItems']:
            print(item['month'], item['days'], '-', item['title'])

        print()

if __name__ == '__main__':
    print(figlet_format('Nike Calendar', font='doom'))
    NikeScraper()