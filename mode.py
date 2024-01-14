def mode(numbers):

	if len(numbers) == 0:
		return None

	count = {0 : 0}
	for i in range(0, len(numbers)):
		if numbers[i] not in count:
			count[numbers[i]] = 1
		else:
			count[numbers[i]] += 1

	maxFreq = 0
	for key, value in count.items():
		if value > maxFreq:
			mode = key
			maxFreq = value

	return mode

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

