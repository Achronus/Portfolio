#-----------------------------------------------------------------------
# File Title: Substitution Cipher
# File Description: A cipher that is very difficult to brute force attack.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. SubstitutionCipher()
#   a. keyIsValid()
#   b. encrypt()
#   c. decrypt()
#   d. translateMessage()
#   e. getRandomKey()
# 2. main()
#-----------------------------------------------------------------------
import random, sys

#-----------------------------------------------------------------------
# Num: 1 | Title: SubstitutionCipher()
#-----------------------------------------------------------------------
class SubstitutionCipher():
  """
  A class dedicated to the Substitution cipher, this cipher is very difficult to crack using brute force. This is a more reliable method for encryption.\n
  Functions: (5) keyIsValid, encrypt, decrypt, translateMessage, getRandomKey
  """
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  #-----------------------------------------------------------------------
  # Num: 1a | Title: keyIsValid()
  #-----------------------------------------------------------------------
  def keyIsValid(self, key):
    """
    Checks if the key is valid.\n
    Parameters: (1) key to check
    """
    keyList = list(key)
    lettersList = list(self.letters)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList

  #-----------------------------------------------------------------------
  # Num: 1b | Title: encrypt()
  #-----------------------------------------------------------------------
  def encrypt(self, key, message):
    """
    Used to encrypt a message using the substitution cipher.\n
    Parameters: (2) key, message to encrypt
    """
    return self.translateMessage(key, message, "encrypt")

  #-----------------------------------------------------------------------
  # Num: 1c | Title: decrypt()
  #-----------------------------------------------------------------------
  def decrypt(self, key, message):
    """
    Used to decrypt a message using the substitution cipher.\n
    Parameters: (2) key, message to decrypt
    """
    return self.translateMessage(key, message, "decrypt")

  #-----------------------------------------------------------------------
  # Num: 1d | Title: translateMessage()
  #-----------------------------------------------------------------------
  def translateMessage(self, key, message, mode):
    """
    Utility function to encrypt or decrypt a given message.\n
    Parameters: (4) key, message to encrypt/decrypt, mode of cryption
    """
    translated = ""
    charsA, charsB = self.letters, key

    # Method is same as encrypting, except, keys and letters are swapped
    if mode == "decrypt":
      charsA, charsB = charsB, charsA

    # Loop through each symbol
    for s in message:
      if s.upper() in charsA:
        # Encrypt/decrypt the symbol
        sIdx = charsA.find(s.upper())
        if s.isupper():
          translated += charsB[sIdx].upper()
        else:
          translated += charsB[sIdx].lower()
      else:
        # Symbol isn't in letters, just add it
        translated += s
    
    return translated

  #-----------------------------------------------------------------------
  # Num: 1e | Title: getRandomKey()
  #-----------------------------------------------------------------------
  def getRandomKey(self):
    """
    Generate a random key.
    """
    key = list(self.letters)
    random.shuffle(key)
    return ''.join(key)

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  sc = SubstitutionCipher()
  key, mode = sc.getRandomKey(), "encrypt"
  message = "If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell"
  
  # Check key is valid
  if not sc.keyIsValid(key):
    sys.exit("There is an error in the key or symbol set.")
  
  # Encrypt or decrypt
  if mode == "encrypt":
    text = sc.encrypt(key, message)
  elif mode == "decrypt":
    text = sc.decrypt(key, message)
  
  # Output text to screen
  print(f"Using key '{key}' | The {mode}ed message is:")
  print(text)

# Run main function
if __name__ == "__main__": main()