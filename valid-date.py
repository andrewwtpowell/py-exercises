import leapyear

def isValidDate(year, month, day):
	if year < 0 or month < 1 or day < 1:
		return False

	if month > 12:
		return False

	if month == 2:
		if leapyear.isLeapYear(year) and day == 29:
			return True
		elif day < 29:
			return True
		else:
			return False

	short_months = [4,6,9,11]
	long_months = [1,3,5,7,8,10,12]

	if short_months.count(month) > 0:
		if day < 31:
			return True
		else:
			return False

	if long_months.count(month) > 0:
		if day < 32:
			return True
		else:
			return False

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay
