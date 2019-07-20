import csv
import os.path as path
from flask import Flask, request, jsonify
from datetime import datetime
from helpers import scrapeHolidays

app = Flask(__name__)

@app.route('/holidays/', defaults={'holidayType': None})
@app.route("/holidays/<holidayType>")
def holidays(holidayType):
    '''
    Return the next 10 holidays in the current year. Adding a 
    holiday type to the url (e.g. site.com/holidays/federal)
    as well as specifying a "holidayType" query parameter 
    (e.g. site.com/holidays?holidayType=federal) will filter 
    the results by the holidayType (path takes precendence over
    query parameter if both are specified)
    '''
    # variables
    if(not holidayType):
        holidayType = request.args.get('holidayType')
    today = datetime.today()
    filename = f'csvs/holidays_{today.year}.csv'
    holidays = []
    next_ten_holidays = []

    # get holidays if they don't already exist
    if(not path.exists(filename)):
        try: scrapeHolidays(filename)
        except Exception as e:
            return jsonify(str(e))

    # parse holidays csv into readable object
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i,row in enumerate(csv_reader):
            if(i > 0 and row[0]):
                date = datetime.strptime(f'{row[0]}-{today.year}', '%b %d-%Y')
                holidays.append({
                    'date': date,
                    'name': row[2],
                    'type': row[3],
                    'details': row[4]
                })

    # get the next ten holidays
    for holiday in holidays:
        if(holiday['date'] > today and len(next_ten_holidays) < 10):
            if(holidayType):
                if(holidayType.lower() in holiday['type'].lower()):
                    next_ten_holidays.append(holiday)
            else: next_ten_holidays.append(holiday)

    return jsonify(next_ten_holidays)