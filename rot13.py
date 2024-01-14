def rot13(text):

	new_text = ''
	for letter in text:
		
		ascii_val = ord(letter)		
		if ascii_val >= 65 and ascii_val <= 90:
			new_ascii = ascii_val + 13
			if new_ascii > 90:
				new_ascii = new_ascii - 91 + 65
			new_text += chr(new_ascii)

		elif ascii_val >= 97 and ascii_val <= 122:
			new_ascii = ascii_val + 13
			if new_ascii > 122:
				new_ascii = new_ascii - 123 + 97	
			new_text += chr(new_ascii)

		else:
			new_text += letter 
	
	return new_text

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'

assert rot13('Uryyb, jbeyq!') == 'Hello, world!'

assert rot13(rot13('Hello, world!')) == 'Hello, world!'

assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'

assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
