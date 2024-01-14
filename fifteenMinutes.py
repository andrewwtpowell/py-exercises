HOURS = [12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11]
MINUTES = ['00','15','30','45']


def fifteenMinutes():

	for h in range(0,24):

		for m in range(0, 4):

			print(str(HOURS[h]) + ':' + MINUTES[m])


fifteenMinutes()
