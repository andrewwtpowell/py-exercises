def getSmallest(numbers):

	if len(numbers) > 0:
		smallest = numbers[0]
	else:
		return None

	for i in range(1, len(numbers)):
		if numbers[i] < smallest:
			smallest = numbers[i]

	return smallest

def gitBiggest(numbers):

	if len(numbers) > 0:
		biggest = numbers[0]
	else:
		return None
		
	for i in range(1, len(numbers)):
		if numbers[i] > biggest:
			biggest = numbers[i]

	return biggest


assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None