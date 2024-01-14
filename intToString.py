import math

def convertIntToStr(number):

    addDash = False

    num_dict = { 0:'0', 
                1:'1',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'6',
                7:'7',
                8:'8',
                9:'9' }
    
    if number > 0:
        digits = int(math.log10(number))+1
    elif number == 0:
        digits = 1
    else:
        digits = int(math.log10(-number))+1
        number = -number
        addDash = True

    returnStr = ''
    
    for i in range(digits):
        digit = num_dict[(number % 10**(i+1)) // 10**i]
        returnStr = digit + returnStr
        
    if addDash:
        returnStr = '-' + returnStr

    return returnStr

for i in range(-10000, 10000):

    assert convertIntToStr(i) == str(i)
