# coding: utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

def scrapeHolidays(filename, year=datetime.today().year):
    '''
    Scrape Holidays from https://www.timeanddate.com/holidays/us/
    by year and save them in a csv file
    '''
    # create a headless browser
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    browser = webdriver.Chrome(chrome_options=chrome_options)

    # navigate to page
    url = f'https://www.timeanddate.com/holidays/us/'
    browser.get(url)

    # Grab the innerHTML and load into Beautiful Soup 
    # Alternatively do the scraping from selenium instead of beautiful soup
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
