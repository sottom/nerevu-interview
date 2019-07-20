import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import csv
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint

# page = requests.get(f'https://www.timeanddate.com/holidays/us/{datetime.now().year}')
# soup = BeautifulSoup(page.text, 'lxml')
# try:
#     rows = soup.find('table', id='holidays-table').find_all('tr')
#     for row in rows:
#         cells = row.find_all('td')
#         for cell in cells:
#             print(cell)
# except e:
#     print('Check your scraping')



def getNextTen(holidayType=None):
    today = datetime.today()
    holidays = []
    next_ten_holidays = []

    with open('holidays.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i,row in enumerate(csv_reader):
            if(i > 0 and row[0]):
                date = datetime.strptime(f'{row[0]}-{today.year}', '%d-%b-%Y')
                holidays.append({
                    'date': date,
                    'date_formatted': date.strftime('%A, %B %d, %Y'),
                    'name': row[2],
                    'type': row[3],
                    'details': row[4]
                })

    for holiday in holidays:
        # added 'in' so it's easier for user to use
        if(holiday['date'] > today and len(next_ten_holidays) < 11 and holidayType and holidayType.lower() in holiday['type'].lower()):
            next_ten_holidays.append(holiday)

    return next_ten_holidays

# getNextTen()
pp(getNextTen(holidayType='federal'))