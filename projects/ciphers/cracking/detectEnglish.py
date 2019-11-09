#-----------------------------------------------------------------------
# File Title: Detect English Words
# File Description: A class designed to detect English words.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. DetectEnglishText() 
#   a. load_dictionary()
#   b. get_english_count()
#   c. remove_non_letters()
#   d. is_english()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: DetectEnglishText()
#-----------------------------------------------------------------------
class DetectEnglishText():
	"""
	A class used to detect English words.\n
	Functions: (4) load_dictionary, get_english_count, remove_non_letters, is_english 
	"""
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	all_letters = letters + letters.lower() + ' \t\n' # Including spaces

	#-----------------------------------------------------------------------
	# Num: 1a | Title: load_dictionary()
	#-----------------------------------------------------------------------
	def load_dictionary(self):
		"""
		Opens the dictionary text file and stores all of the words within it into an English words dictonary. Returns the words dictionary.
		"""
		# Open file
		f = open('dictionary.txt')
		english_words = {}

		# Loop through each word in file
		for word in f.read().split('\n'):
				english_words[word] = None
		f.close()

		return english_words

	#-----------------------------------------------------------------------
	# Num: 1b | Title: get_english_count()
	#-----------------------------------------------------------------------
	def get_english_count(self, message):
		"""
		Gets the word count of a message provided.\n
		Parameters: (1) message to check
		"""
		# Set variables
		message = message.upper()
		message = self.remove_non_letters(message) # Remove punctuation
		possible_words = message.split() # Split words by spaces into list
		words = self.load_dictionary()

		# Check if there are english words
		if possible_words == []:
				return 0 # no words, so return 0

		count = 0
		# If there are words, add one to count
		for word in possible_words:
				if word in words:
						count += 1

		return float(count) / len(possible_words)

	#-----------------------------------------------------------------------
	# Num: 1c | Title: remove_non_letters()
	#-----------------------------------------------------------------------
	def remove_non_letters(self, message):
		"""
		Utility function for the get_english_count function, used to remove all punctuation (other than spaces).\n
		Parameters: (1) message to check
		"""
		letters_only = []
		# Loop through each letter
		for symbol in message:
			if symbol in self.all_letters:
				letters_only.append(symbol)

		return ''.join(letters_only)

	#-----------------------------------------------------------------------
	# Num: 1d | Title: is_english()
	#-----------------------------------------------------------------------
	def is_english(self, message, word_percent=20, letter_percent=85):
		"""
		Checks if a message contains English words. Requires a minimum of 20% of the words in the dictionary being being valid and 85% of all characters in the message must be letters or spaces (not punctuation or numbers).\n
		Parameters: (3) message to check, minimum word count that is English, letter percentage
		"""
		# Count the words
		words_match = self.get_english_count(message) * 100 >= word_percent
		num_letters = len(self.remove_non_letters(message))

		# Determine letters
		message_letters_percent = float(num_letters) / len(message) * 100
		letters_match = message_letters_percent >= letter_percent

		return words_match and letters_match