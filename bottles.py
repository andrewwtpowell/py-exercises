def bottles():

	numBottles = 99
	while numBottles >= 0:
		if numBottles > 1:
			print(str(numBottles) + ' bottles of beer on the wall,')
			print(str(numBottles) + ' bottles of beer,')
			print('Take one down,')
			print('Pass it around')
		elif numBottles == 1:
			print(str(numBottles) + ' bottle of beer on the wall,')
			print(str(numBottles) + ' bottle of beer,')
			print('Take one down,')
			print('Pass it around')
		else:
			print('No more bottles of beer on the wall!')

		numBottles -= 1

bottles()