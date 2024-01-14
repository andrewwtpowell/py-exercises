def writeToFile(filename, text):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write(text)

def appendToFile(filename, text):
	curr_text = readFromFile(filename)
	writeToFile(filename, curr_text + text)

def readFromFile(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		read_text = f.read()
	
	return read_text

writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'