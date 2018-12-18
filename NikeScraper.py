#      __ _ _            ___      _                _            
#   /\ \ (_) | _____    / __\__ _| | ___ _ __   __| | __ _ _ __ 
#  /  \/ / | |/ / _ \  / /  / _` | |/ _ \ '_ \ / _` |/ _` | '__|
# / /\  /| |   <  __/ / /__| (_| | |  __/ | | | (_| | (_| | |   
# \_\ \/ |_|_|\_\___| \____/\__,_|_|\___|_| |_|\__,_|\__,_|_|   

# CLI Based Nike Scraper Using GET Requests & Python
# Credits to danielbrzn for URL

import requests
import json

def NikeScraper():
    locales = ['SG', 'AU']
    for locale in locales:
        print('Nike {}'.format(locale))
        try:
            url = 'https://www.nike.com/nikestore/html/services/launchCalendar?country={}&lang_locale=en_GB&sortOrder=asc'.format(locale)
            r = requests.get(url)
            itemList = json.loads(r.text)
            for item in itemList['launchCalendarItems']:
                print(item['month'], item['days'], '-', item['title'])
        except:
            print("Nothing listed on Calendar.")
            
        print()

if __name__ == '__main__':
    print('Nike Launch Calendar Loading...\n')
    NikeScraper()