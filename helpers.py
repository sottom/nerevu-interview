# coding: utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

def scrapeHolidays(filename, year=datetime.today().year):
    '''
    Scrape Holidays from https://www.timeanddate.com/holidays/us/
    by year and save them in a csv file
    '''
    # load html page into beautiful soup
    # page = requests.get(f'https://www.timeanddate.com/holidays/us/{year}')
    browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
    url = f'https://www.timeanddate.com/holidays/us/'
    browser.get(url) #navigate to the page
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    browser.close()
    soup = BeautifulSoup(innerHTML, 'lxml')

    # make sure table exists
    try: 
        rows = soup.find('table', id='holidays-table').find_all('tr', class_='showrow')
    except Exception as e:
        # TODO: maybe better to catch the error, log it, then end the program
        raise Exception("Holiday scraper failed.")

    # create csv string
    csv_string = ''
    for i, row in enumerate(rows):
        cells = row.find_all(recursive=False)
        for j, cell in enumerate(cells):
            cell_text = cell.get_text().strip()
            # get headers
            if(i == 0):
                csv_string += (cell_text or "Day of Week") + ','
            # ignore last line of unuseful text
            elif(i == len(rows) - 1): 
                pass 
            # get cells
            else:
                if(j == len(cells)-1): 
                    csv_string += f'"{cell_text}",'
                else: csv_string += cell_text + ','
        csv_string = (csv_string[:-1] + "\n")

    # save csv file
    csv_string = csv_string[:-1]
    f = open(filename, 'w')
    f.write(csv_string)
