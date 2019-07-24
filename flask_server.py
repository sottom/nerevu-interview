import csv
import os.path as path
from flask import Flask, request, jsonify
from datetime import datetime
from helpers import scrapeHolidays

app = Flask(__name__)

@app.route('/holidays/', defaults={'holiday_type': None, 'start_date': None})
@app.route("/holidays/<holiday_type>/<start_date>")
def holidays(holiday_type, start_date):
    '''
    Return the next 10 holidays in the current year. Adding a 
    holiday type to the url (e.g. site.com/holidays/federal)
    as well as specifying a "holiday_type" query parameter 
    (e.g. site.com/holidays?holiday_type=federal) will filter 
    the results by the holiday_type (path takes precendence over
    query parameter if both are specified).

    View live demo at https://nexttenholidays.herokuapp.com/holidays/
    '''
    # variables
    if(not holiday_type):
        holiday_type = request.args.get('holiday_type')
    today = datetime.today()
    filename = f'./holidays_{today.year}.csv'
    holidays = []
    next_ten_holidays = []
    # TODO: check if start_date not none
    # Jan-1-2019
    start_date = datetime.strptime(start_date, '%b-%d-%Y')

    # get holidays if they don't already exist
    if(not path.exists(filename)):
        try: 
            scrapeHolidays(filename)
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
        if(len(next_ten_holidays) > 9): break
        if(holiday['date'] >= start_date):
            if(not holiday_type): 
                next_ten_holidays.append(holiday)
            elif(holiday_type.lower() in holiday['type'].lower()):
                next_ten_holidays.append(holiday)

    return jsonify(next_ten_holidays)
