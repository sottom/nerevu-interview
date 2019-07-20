# coding: utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def getHolidays(filename, year=datetime.today().year):
    '''
    Scrape Holidays from https://www.timeanddate.com/holidays/us/
    by year and save them in a csv file
    '''
    # variables
    f = open(filename, 'w')
    csv_string = ''

    # load html page into beautiful soup
    page = requests.get(f'https://www.timeanddate.com/holidays/us/{year}')
    soup = BeautifulSoup(page.text, 'lxml')

    # make sure table exists
    try:
        rows = soup.find('table', id='holidays-table').find_all('tr')
    except Exception as e:
        raise Exception("Table Holidays not found. Check your scraping selectors to make sure they haven't changed")

    # create csv string
    for i, row in enumerate(rows):
        cells = row.find_all(recursive=False)
        for j, cell in enumerate(cells):
            cell_text = cell.get_text().strip()
            # get headers
            if(i == 0):
                csv_string += (cell_text if cell_text else "Day of Week") + ','
            # ignore last line of unuseful text
            elif(i =J len(rows) - 1): pass 
            # get cells
            else:
                if(j == len(cells)-1): 
                    csv_string += f'"{cell_text}",'
                else: csv_string += cell_text + ','
        csv_string = (csv_string[:-1] + "\n")

    # save csv file
    csv_string = csv_string[:-1]
    f.write(csv_string)
