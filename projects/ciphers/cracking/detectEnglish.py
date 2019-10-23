#-----------------------------------------------------------------------
# File Title: Detect English Words
# File Description: A class designed to detect English words.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. DetectEnglishText() 
#   a. loadDictionary()
#   b. getEnglishCount()
#   c. removeNonLetters()
#   d. isEnglish()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: DetectEnglishText()
#-----------------------------------------------------------------------
class DetectEnglishText():
	"""
	A class used to detect English words.\n
	Functions: (4) loadDictionary, getEnglishCount, removeNonLetters, isEnglish 
	"""
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	allLetters = letters + letters.lower() + ' \t\n' # Including spaces

	#-----------------------------------------------------------------------
	# Num: 1a | Title: loadDictionary()
	#-----------------------------------------------------------------------
	def loadDictionary(self):
		"""
		Opens the dictionary text file and stores all of the words within it into an English words dictonary. Returns the words dictionary.
		"""
		# Open file
		f = open('dictionary.txt')
		englishWords = {}

		# Loop through each word in file
		for word in f.read().split('\n'):
				englishWords[word] = None
		f.close()

		return englishWords

	#-----------------------------------------------------------------------
	# Num: 1b | Title: getEnglishCount()
	#-----------------------------------------------------------------------
	def getEnglishCount(self, message):
		"""
		Gets the word count of a message provided.\n
		Parameters: (1) message to check
		"""
		# Set variables
		message = message.upper()
		message = self.removeNonLetters(message) # Remove punctuation
		possibleWords = message.split() # Split words by spaces into list
		words = self.loadDictionary()

		# Check if there are english words
		if possibleWords == []:
				return 0 # no words, so return 0

		count = 0
		# If there are words, add one to count
		for word in possibleWords:
				if word in words:
						count += 1

		return float(count) / len(possibleWords)

	#-----------------------------------------------------------------------
	# Num: 1c | Title: removeNonLetters()
	#-----------------------------------------------------------------------
	def removeNonLetters(self, message):
		"""
		Utility function for the getEnglishCount function, used to remove all punctuation (other than spaces).\n
		Parameters: (1) message to check
		"""
		lettersOnly = []
		# Loop through each letter
		for symbol in message:
			if symbol in self.allLetters:
				lettersOnly.append(symbol)

		return ''.join(lettersOnly)

	#-----------------------------------------------------------------------
	# Num: 1d | Title: isEnglish()
	#-----------------------------------------------------------------------
	def isEnglish(self, message, wordPercentage=20, letterPercentage=85):
		"""
		Checks if a message contains English words. Requires a minimum of 20% of the words in the dictionary being being valid and 85% of all characters in the message must be letters or spaces (not punctuation or numbers).\n
		Parameters: (3) message to check, minimum word count that is English, letter percentage
		"""
		# Count the words
		wordsMatch = self.getEnglishCount(message) * 100 >= wordPercentage
		numLetters = len(self.removeNonLetters(message))

		# Determine letters
		messageLettersPercentage = float(numLetters) / len(message) * 100
		lettersMatch = messageLettersPercentage >= letterPercentage

		return wordsMatch and lettersMatch