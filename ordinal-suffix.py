def ordinalSuffix1(num):
	s = str(num)
	
	if s[-2:] == '11' or s[-2:] == '12' or s[-2:] == '13':
		return s + 'th'
	else:
		match s[-1:]:
			case '1':
				return s + 'st'
			case '2':
				return s + 'nd'
			case '3':
				return s + 'rd'
			case _:
				return s + 'th'

def ordinalSuffix(num):
	if num % 100 == 11 or num % 100 == 12 or num % 100 == 13:
		return str(num) + 'th'
	else:
		match num % 10:
			case 1:
				return str(num) + 'st'
			case 2:
				return str(num) + 'nd'
			case 3:
				return str(num) + 'rd'
			case _:
				return str(num) + 'th'


assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'