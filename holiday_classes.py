from datetime import datetime
import csv

class Holiday(object):
    ''' '''

    def __init__(self, date, day_of_week, name, details):
        ''' '''
        self.date = date
        self.day_of_week = day_of_week
        self.name = name
        self.details = details


class CurrentYearHolidays(object):
    ''' '''
    def __init__(self):
        ''' '''
        self.date = datetime.now()
        self.holidays = self.scrapeHolidays()

    def get_holidays(self):
        return sorted(self.holidays, key=lambda x:x.date)

    def add(self, holiday):
        self.holidays.append(holiday)
        return self.holidays

    def getNextTen(self):
        next_ten_holidays = []
        for holiday in self.get_holidays():
            # should I make a getter (getDate())
            # TODO: think about list comprehension
            if(holiday.date > today and len(next_ten_holidays) < 11):
                next_ten_holidays.append(holiday)
        return next_ten_holidays

    def scrapeHolidays(self):
        with open('holidays.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i,row in enumerate(csv_reader):
                if(i > 0 and row[0]):
                    self.add(
                        Holiday(
                            date=datetime.strptime(f'{row[0]}-{today.year}', '%d-%b-%Y'),
                            day_of_week=row[1],
                            name=row[2],
                            details=row[3]
                        )
                    )