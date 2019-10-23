#-----------------------------------------------------------------------
# File Title: Columnar Transposition Cipher
# File Description: A cipher that reorganizes a phrase as a form of encryption.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. TranspositionCipher()
#   a. encrypt()
#   b. decrypt()
#   c. randomDataTest()
#   d. readFile()
# 2. main()
#-----------------------------------------------------------------------
import math, random, time, os

#-----------------------------------------------------------------------
# Num: 1 | Title: TranspositionCipher()
#-----------------------------------------------------------------------
class TranspositionCipher():
  """
  A class dedicated to the Transposition cipher that reorganizes a phrase as a form of encryption.\n
  Functions: (4) encrypt, decrypt, randomDataTest, readFile
  """

  #-----------------------------------------------------------------------
  # Num: 1a | Title: encrypt()
  #-----------------------------------------------------------------------
  def encrypt(self, phrase, key):
    """
    Used to reorganize a phrase based on a key value as a form of encryption. Splits the phrase into columns based on the key.\n
    Parameters: (2) phrase to encrypt, value to reorganize letters
    """
    # Each string in ciphertext, represents a column in a grid
    ciphertext = [''] * key

    # Loop through each column in ciphertext
    for col in range(key):
      cIdx = col # current index

      # Loop until past phrase length
      while cIdx < len(phrase):
        ciphertext[col] += phrase[cIdx]
        cIdx += key

    # Convert ciphertext list into a single string and return
    return ''.join(ciphertext)

  #-----------------------------------------------------------------------
  # Num: 1b | Title: decrypt()
  #-----------------------------------------------------------------------
  def decrypt(self, phrase, key):
    """
    Used to reorganize a phrase based on a key value to decrypt the encrypted version. Consists of 'columns' and 'rows'.\n
    Parameters: (2) phrase to decrypt, value to reorganize letters
    """
    numCols = int(math.ceil(len(phrase) / float(key)))
    numRows = key
    emptyCols = (numCols * numRows) - len(phrase)
    plaintext = [''] * numCols # Each column in a grid
    col, row = 0, 0

    for c in phrase:
      plaintext[col] += c
      col += 1 # Point to next column

      # If no columns (empty spaces), go back to first col & the next row
      if (col == numCols) or (col == numCols - 1 and row >= numRows - emptyCols):
        col = 0
        row += 1

    return ''.join(plaintext)

  #-----------------------------------------------------------------------
  # Num: 1c | Title: randomDataTest()
  #-----------------------------------------------------------------------
  def randomDataTest(self, seed, testCount):
    """
    Creates random seeds of data and then checks whether the cipher works correctly.\n
    Parameters: (2) random seed value, amount of tests to run
    """
    random.seed(seed)

    # Create tests
    for i in range(testCount):
      phrase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 20)

      # Convert to list
      phrase = list(phrase) # Put each character as a separate list
      random.shuffle(phrase) # Shuffle the list order
      phrase = ''.join(phrase) # Convert list back to a string

      # Print to console each test
      print(f'Test #{i + 1}: "{phrase[:50]}..."') # Only first 50 characters displayed

      # Check each key
      for key in range(1, int(len(phrase) / 2)):
        encrypted = self.encrypt(phrase, key)
        decrypted = self.decrypt(encrypted, key)

        # Error if decrypt doesn't match original message
        if phrase != decrypted:
          print(f"Mismatch with key: #{key} and phrase: {phrase[:50]}")
          print(f"Decrypted as {decrypted[:50]}")
      
      print("Transposition cipher test passed.")

  #-----------------------------------------------------------------------
  # Num: 1d | Title: readFile()
  #-----------------------------------------------------------------------
  def readFile(self, filename, key, mode):
    """
    Runs either encryption or decryption on a text file that is provided.\n
    Parameters: (1) txt filename, key value, mode of cryption
    """
    outFilename = filename + '.output.txt'
    filename += '.txt'

    # No file, program terminates
    if not os.path.exists(filename):
      print(f"The file {filename} does not exist.")

    # If output file exists, give the user chance to quit
    if os.path.exists(outFilename):
      print(f"This will overwrite the file {outFilename}. (C)ontinue or (Q)uit?")
      response = input('> ')
      if not response.lower().startswith('c'):
        exit()
    
    # Read messages from input file
    f = open(filename)
    data = f.read()
    f.close()

    print(f"{mode.title()}sing...")

    # Calculate time for encryption/decryption
    startTime = time.time()
    if mode == 'encrypt':
      result = self.encrypt(data, key)
    elif mode == 'decrypt':
      result = self.decrypt(data, key)
    totalTime = round(time.time() - startTime, 2)
    print(f"{mode.title()}sion time: {totalTime}")

    # Write results to output file
    of = open(outFilename, 'w')
    of.write(result)
    of.close()

    print(f"Done {mode.title()}ing {filename} ({len(data)} characters).")
    print(f"{mode.title()}ed file is {outFilename}.")

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "Common sense is not so common."
  key, seed, testCount = 8, 42, 20
  filename, mode = "test", "encrypt"
  tc = TranspositionCipher()

  # Encrypt example
  ciphertext = tc.encrypt(phrase, key)
  print(ciphertext)

  # Decrypt example
  plaintext = tc.decrypt(ciphertext, key)
  print(plaintext)

  # Test the cipher with random examples
  tc.randomDataTest(seed, testCount)

  # Testing with files
  tc.readFile(filename, key, mode)

# Run main function
if __name__ == "__main__": main()