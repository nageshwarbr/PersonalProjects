from datetime import datetime


def isNowInTimePeriod(start_time, end_time, now_time):
    return start_time <= now_time <= end_time


timeStart = '6:00PM'
timeEnd = '6:00AM'
timeEnd = datetime.strptime(timeEnd, "%I:%M%p")
timeStart = datetime.strptime(timeStart, "%I:%M%p")
timeNow = datetime.now()

print(isNowInTimePeriod(timeStart, timeEnd, timeNow))
