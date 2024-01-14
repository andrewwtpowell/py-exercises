def makeChange(amount):

    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    return_dict = {}

    while amount >= 25:
        num_quarters += 1
        amount -= 25

    while amount >= 10:
        num_dimes += 1
        amount -= 10

    while amount >= 5:
        num_nickels += 1
        amount -= 5

    while amount >= 1:
        num_pennies += 1
        amount -= 1

    if num_quarters > 0:
        return_dict.update({'quarters': num_quarters})

    if num_dimes > 0:
        return_dict.update({'dimes': num_dimes})

    if num_nickels > 0:
        return_dict.update({'nickels': num_nickels})

    if num_pennies > 0:
        return_dict.update({'pennies': num_pennies})

    return return_dict


assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}
