from prettytable import PrettyTable

def multipleTable():

	table = PrettyTable(['','1','2','3','4','5','6','7','8','9','10'])

	for row in range(1,11):
		table.add_row([str(row),str(row),str(2*row),str(3*row),str(4*row),str(5*row),str(6*row),str(7*row),str(8*row),str(9*row),str(10*row)])

	print(table)

multipleTable()

def betterMultipleTable(upperBound):

	fields = [' ']
	for i in range(1, upperBound+1):
		fields.append(str(i))

	table = PrettyTable(fields)

	for row in range(1, upperBound+1):

		entry = [str(row)]
		for col in range(1, upperBound+1):
			entry.append(str(row*col))

		table.add_row(entry)

	print(table)

betterMultipleTable(30)

