def getTitleCase(text):

    char_list = list(text)
    next_upper = True

    for i in range(len(char_list)):

        curr_ascii = ord(char_list[i])
        if curr_ascii in range(97,123):

            if next_upper:
                char_list[i] = chr( ord(char_list[i]) - 32 )

            next_upper = False


        elif curr_ascii in range(65, 91):

            if next_upper is False:
                char_list[i] = chr( ord(char_list[i]) + 32 )

            next_upper = False

        else:

            next_upper = True

    return ''.join(char_list)


assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

