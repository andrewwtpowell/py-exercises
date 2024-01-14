def calculateSum(numbers):

	sum = 0
	for i in range(0,len(numbers)):
		sum += numbers[i]

	return sum

def calculateProduct(numbers):

	product = 1
	for i in range(0,len(numbers)):
		product *= numbers[i]

	return product

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840