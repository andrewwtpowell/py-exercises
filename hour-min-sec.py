def getHoursMinutesSeconds(totalSeconds):

	hours = totalSeconds//3600
	totalSeconds -= hours*3600
	minutes = totalSeconds//60
	totalSeconds -= minutes*60
	seconds = totalSeconds
	if hours and minutes and seconds:
		output = str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's'
	elif hours and minutes:
		output = str(hours) + 'h ' + str(minutes) + 'm'
	elif hours and seconds:
		output = str(hours) + 'h ' + str(seconds) + 's'
	elif minutes and seconds:
		output = str(minutes) + 'm ' + str(seconds) + 's'
	elif hours:
		output = str(hours) + 'h'
	elif minutes:
		output = str(minutes) + 'm'
	elif seconds:
		output = str(seconds) + 's'
	else:
		output = str(seconds) + 's'

	return output

assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'