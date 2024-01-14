def mergeTwoLists(list1, list2):

	while len(list1) > 0:
		
		num = list1.pop()
		inserted = False
		for i in range(len(list2)):

			if num <= list2[i]:
				list2.insert(i, num)
				inserted = True
				break

		if inserted == False:
			list2.append(num)	
	return list2

assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]

assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]

assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
