import math

def commaFormat(number):

    temp_num = number // 1
    if temp_num > 0:
        digits = int(math.log10(temp_num))+1
    elif temp_num == 0:
        digits = 1

    commas = (digits - 1) // 3

    char_list = list(str(number))

    decimal = False
    if char_list.count('.') > 0:
        decimal = True

    itr = len(char_list)-1
    comp_index = len(char_list)
    while commas > 0:

        if decimal:

            if char_list[itr] == '.':
                comp_index = itr
                decimal = False
                itr -= 1
                continue

            itr -= 1
            continue

        if comp_index - itr != 0 and (comp_index - itr) % 3 == 0:
            char_list.insert(itr, ',')
            commas -= 1

        itr -= 1


    returnStr = ''.join(char_list)

    return returnStr


assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'
