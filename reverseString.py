def reverseString(text):

    char_list = list(text)

    for i in range(len(char_list) // 2):

        swap_char = char_list[i]
        char_list[i] = char_list[len(char_list) - 1 - i]
        char_list[len(char_list) - 1 - i] = swap_char

    return ''.join(char_list)


assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'
