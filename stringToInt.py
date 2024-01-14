def convertStrToInt(word):

    num_dict = { '0':0,
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9 }

    char_list = list(word) 
    number = 0
    negative = False
    for i in range(len(char_list)):
        if char_list[i] == '-':
            negative = True
            continue

        number += num_dict[char_list[i]] * 10**(len(char_list)-1-i)

    if negative:
        number = -number

    return number


for i in range(-10000, 10000):

    assert convertStrToInt(str(i)) == i
