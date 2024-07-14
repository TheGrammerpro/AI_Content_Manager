import datetime as dt
from hijridate import Gregorian


class Themes:
    def __init__(self):
        self.current_month = (dt.datetime.now().month, dt.datetime.now().strftime('%B'))
        self.current_weekday = (dt.datetime.now().weekday(), dt.datetime.now().strftime('%A'))
        self.current_day = dt.datetime.now().day
        self.current_year = dt.datetime.now().year
        self.full_date = dt.datetime.now().strftime('%Y/%m/%d')

        self.hijri_date = Gregorian(self.current_year, self.current_month[0], self.current_day).to_hijri()
        self.current_day_hijri = self.hijri_date.day
        self.current_month_hijri = self.hijri_date.month

        self.day = "Day not decided yet"
        self.season = "Season not decided yet"
        self.holiday_today = (False, "No holiday")
        self.themes = {}

        self.holiday_list = [{'holiday': 'New Year', 'day': 1, 'month': 1, 'date': 'Gregorian'},
                             {'holiday': 'Christmas', 'day': 25, 'month': 12, 'date': 'Gregorian'},
                             {'holiday': "Valentine's Day", 'day': 14, 'month': 2, 'date': 'Gregorian'},
                             {'holiday': 'Halloween', 'day': 31, 'month': 10, 'date': 'Gregorian'},
                             {'holiday': 'Ramadan', 'day': 1, 'month': 9, 'date': 'Hijri'},
                             {'holiday': 'Eid Al Fitr', 'day': 1, 'month': 10, 'date': 'Hijri'},
                             {'holiday': 'Thanksgiving Day', 'day': 4, 'month': 11, 'date': 'Gregorian'},
                             {'holiday': "St. Patrick's Day", 'day': 17, 'month': 3, 'date': 'Gregorian'},
                             {'holiday': 'Diwali', 'day': 14, 'month': 11, 'date': 'Gregorian'},
                             {'holiday': 'Independence Day US', 'day': 4, 'month': 7, 'date': 'Gregorian'},
                             {'holiday': 'Bodhi Japan', 'day': 8, 'month': 12, 'date': 'Gregorian'},
                             {'holiday': 'Festa Junina Brazil', 'day': 24, 'month': 6, 'date': 'Gregorian'},
                             {'holiday': 'Earth Day', 'day': 22, 'month': 4, 'date': 'Gregorian'},
                             {'holiday': "Mother's day", 'day': 2, 'month': 5, 'date': 'Gregorian'},
                             {'holiday': "Father's day", 'day': 3, 'month': 6, 'date': 'Gregorian'},
                             {'holiday': 'Islamic New Year', 'day': 1, 'month': 1, 'date': 'Hijri'}]
        self.holiday_check()
        self.season_check()
        self.check_weekday()

    def holiday_check(self):
        for holiday in self.holiday_list:
            if (holiday['day'] == self.current_day and holiday['month'] == self.current_month[0]
                    and holiday['date'] == "Gregorian"):
                print(f"We should celebrate {holiday['holiday']}")
                self.holiday_today = (True, holiday['holiday'])
            elif (holiday['day'] == self.current_day_hijri and holiday['month'] == self.current_month_hijri
                  and holiday['date'] == "Hijri"):
                print(f"We should celebrate {holiday['holiday']}")
                self.holiday_today = (True, holiday['holiday'])

    def season_check(self):
        # Checks what the current season is:
        if 1 <= self.current_month[0] <= 3:
            self.season = "Winter"
        elif 4 <= self.current_month[0] <= 6:
            self.season = "Sprint"
        elif 7 <= self.current_month[0] <= 9:
            self.season = "Summer"
        elif 10 <= self.current_month[0] <= 12:
            self.season = "Autumn"

        print(f"The season is: {self.season}")

    def check_weekday(self):
        # Checks if it's weekend or Monday or mid-week:
        if self.current_weekday[0] >= 4:
            if self.current_weekday[0] == 4:
                print("It's Friday, get ready for the weekend!")
                self.day = "It's Friday, get ready for the weekend!"
            else:
                print("It's the weekend! Time to have fun!")
                self.day = "It's the weekend! Time to have fun!"
        elif self.current_weekday[1] == "Monday":
            print("Bruh, it's Monday again")
            self.day = "It's Monday"
        else:
            print(f"It's the middle of the week, specifically {self.current_weekday[1]}")
            self.day = f"It's the middle of the week, specifically {self.current_weekday[1]}"

    def get_theme(self):
        # If there's a holiday, themes prioritizes the holiday:
        if self.holiday_today[0]:
            self.themes = (f"it's {self.holiday_today[1]} today, wish the audience that celebrates "
                           f"a happy {self.holiday_today[1]}")
        else:
            self.themes = {"day": self.day, "season": self.season}

        return self.themes
