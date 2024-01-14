def bubbleSort(numbers):

	for i in range(len(numbers)-1):
		
		for j in range(i+1, len(numbers)):
		
			if numbers[i] > numbers[j]:
				temp = numbers[i]
				numbers[i] = numbers[j]
				numbers[j] = temp

	return numbers


assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]

assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
