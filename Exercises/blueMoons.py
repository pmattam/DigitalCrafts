# Lunar Cycles - The moon goes through phases because it orbits the earth and the sun hits it differently at 
# different places in its orbit. This means that, depending on where it is in its orbit, 
# you might see a full moon, right quarter moon, or even "no" moon (new moon) at all. It takes 
# 27.3 days for the moon to orbit the Earth, but the actual phase difference from one full moon 
# to the next is 29.5 days because the earth cruises a cool 45 million miles around the sun in 
# that 27.3 days. It takes 2.2 days for the the moon to make up for that distance and get all 
# the way back to where you last saw a full moon.

# Whenever the moon is full twice in one month, the second one is called a "blue moon." This 
# last happened in July of 2015 on the 1st and 31st. The next time is January of 2018 (same days). 
# You can research the timing, otherwise you can assume midnight. Write a program that determines 
# how many "blue moons" there will be in third milenia (2000-2999)?

# If you want to be really, really specific, the lunar month is actually 
# 29 days, 12 hours, and 44 minutes.

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

