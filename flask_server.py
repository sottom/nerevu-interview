import csv
import os.path as path
from flask import Flask, request, jsonify
from datetime import datetime
from helpers import getHolidays

app = Flask(__name__)

@app.route("/holidays/")
def holidays():
    '''
    Return the next 10 holidays in the current year.
    Passing in a "holidayType" query parameter will
    filter the results (e.g. ?holidayType=federal)
    '''
    # variables
    holidayType = request.args.get('holidayType')
    today = datetime.today()
    holidays = []
    next_ten_holidays = []
    filename = f'csvs/holidays_{today.year}.csv'

    # get holidays if they don't already exist
    if(not path.exists(filename)):
        getHolidays(filename)

    # parse holidays csv into readable object
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            for i,row in enumerate(csv_reader):
                if(i > 0 and row[0]):
                    date = datetime.strptime(f'{row[0]}-{today.year}', '%b %d-%Y')
                    holidays.append({
                        'date': date,
                        'name': row[2],
                        'type': row[3],
                        'details': row[4]
                    })
        except Exception as e:
            print(e)

    # get the next ten holidays
    for holiday in holidays:
        if(holiday['date'] > today and len(next_ten_holidays) < 10):
            if(holidayType):
                if(holidayType.lower() in holiday['type'].lower()):
                    next_ten_holidays.append(holiday)
            else: next_ten_holidays.append(holiday)

    return jsonify(next_ten_holidays)


# https://services.timeanddate.com/api/packages/free-trial.html
# Try our API service for FREE for 3 months.
# The following locations are available in our trial package: Amsterdam (Netherlands), Philipsburg (Netherlands), Maputo (Mozambique), Oslo (Norway), Lord Howe Island (Australia), and Romania for our holiday service.