import datetime

def blueMoonsCalc(start_date, end_date):
    bluemoon_calendar = []
    prev_fullmoon = start_date

    while prev_fullmoon.year <= end_date:
        current_fullmoon = prev_fullmoon + datetime.timedelta(days=29, hours=12, minutes=44)
        # print current_fullmoon
        if current_fullmoon.month == prev_fullmoon.month:
            bluemoon_calendar.append(current_fullmoon)
        prev_fullmoon = current_fullmoon
    print bluemoon_calendar 
    return len(bluemoon_calendar)

startDate = datetime.datetime(2001, 11, 1, 5, 40, 0, 0)
endDate = 2999

print blueMoonsCalc(startDate, endDate)

assert blueMoonsCalc(startDate, 2005) == 2, "Test failed for 5 years"
assert blueMoonsCalc(startDate, 2200) == 83, "Test failed for 200 years" 

