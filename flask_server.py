from flask import Flask, request, jsonify
from datetime import datetime
import csv

app = Flask(__name__)

@app.route("/holidays/")
def holidays():
    # variables
    holidayType = request.args.get('holidayType')
    today = datetime.today()
    holidays = []
    next_ten_holidays = []

    # parse csv into readable object
    with open('../holidays.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i,row in enumerate(csv_reader):
            if(i > 0 and row[0]):
                date = datetime.strptime(f'{row[0]}-{today.year}', '%d-%b-%Y')
                holidays.append({
                    'date': date,
                    'name': row[2],
                    'type': row[3],
                    'details': row[4]
                })

    # get the next ten holidays
    for holiday in holidays:
        if(holiday['date'] > today and len(next_ten_holidays) < 11):
            if(holidayType):
                if(holidayType.lower() in holiday['type'].lower()):
                    next_ten_holidays.append(holiday)
            else: next_ten_holidays.append(holiday)

    return jsonify(next_ten_holidays)
