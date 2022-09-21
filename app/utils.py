from datetime import datetime

class Utils:
    def current_time(self):
        return datetime.now()

    def time_breakup(self, timespan):
        days = timespan.days
        hours = timespan.total_seconds() // 3600
        minutes = (timespan.total_seconds() % 3600) // 60
        return days, hours, minutes