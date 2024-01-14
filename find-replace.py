def findAndReplace(text, oldText, newText):
	oldCount = text.count(oldText)

	for i in range(oldCount):
		oldItr = text.index(oldText)
		text = text[:oldItr] + newText + text[oldItr + len(oldText):]

	return text

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

assert findAndReplace('foxfoxdogdofoxfodogfox', 'fox', 'dog') == 'dogdogdogdodogfodogdog'