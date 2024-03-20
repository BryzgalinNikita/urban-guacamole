from datetime import datetime

class SuperDate(datetime):
    def get_season(self):
        month = self.month
        if 3 <= month <= 5:
            return 'Spring'
        elif 6 <= month <= 8:
            return 'Summer'
        elif 9 <= month <= 11:
            return 'Autumn'
        else:
            return 'Winter'

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 18:
            return 'Day'
        elif 18 <= hour < 24:
            return 'Evening'
        else:
            return 'Night'

today = SuperDate.now()
print("Date:", today)
print("Season:", today.get_season())
print("Time of day:", today.get_time_of_day())
