def getUppercase(text):

    char_list = list(text)

    for i in range(len(char_list)):

        if ord(char_list[i]) in range(97, 123):
            char_list[i] = chr( ord(char_list[i]) - 32 )

    return ''.join(char_list)


assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''
    
