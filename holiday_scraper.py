import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from holiday_classes import CurrentYearHolidays

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


holidays = CurrentYearHolidays()
print(holidays.getNextTen())


