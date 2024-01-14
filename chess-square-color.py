def getChessSquareColor(column, row):
	if column > 7 or row > 7:
		return ''
	elif (column + row) % 2 == 0:
		return 'white'
	elif (column + row) % 2 == 1:
		return 'black'

	return ''

assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''