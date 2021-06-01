#-----------------------------------------------------------------------
# File Title: Substitution Cipher
# File Description: A cipher that is very difficult to brute force attack.
#-----------------------------------------------------------------------
import random
import sys

class SubstitutionCipher():
  """
  A class dedicated to the Substitution cipher, this cipher is very difficult to 
  crack using brute force. This is a more reliable method for encryption.\n
  Functions: (5) key_is_valid, encrypt, decrypt, translate_message, get_random_key
  """
  def __init__(self):
    self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def key_is_valid(self, key):
    """
    Checks if the key is valid.\n
    Parameters: (1) key to check
    """
    key_list = list(key)
    letters_list = list(self.letters)
    key_list.sort()
    letters_list.sort()

    return key_list == letters_list

  def encrypt(self, key, message):
    """
    Used to encrypt a message using the substitution cipher.\n
    Parameters: (2) key, message to encrypt
    """
    return self.translate_message(key, message, "encrypt")

  def decrypt(self, key, message):
    """
    Used to decrypt a message using the substitution cipher.\n
    Parameters: (2) key, message to decrypt
    """
    return self.translate_message(key, message, "decrypt")

  def translate_message(self, key, message, mode):
    """
    Utility function to encrypt or decrypt a given message.\n
    Parameters: (4) key, message to encrypt/decrypt, mode of cryption
    """
    translated = ""
    chars_a, chars_b = self.letters, key

    # Method is same as encrypting, except, keys and letters are swapped
    if mode == "decrypt":
      chars_a, chars_b = chars_b, chars_a

    # Loop through each symbol
    for s in message:
      if s.upper() in chars_a:
        # Encrypt/decrypt the symbol
        sIdx = chars_a.find(s.upper())
        if s.isupper():
          translated += chars_b[sIdx].upper()
        else:
          translated += chars_b[sIdx].lower()
      else:
        # Symbol isn't in letters, just add it
        translated += s
    
    return translated

  def get_random_key(self):
    """
    Generate a random key.
    """
    key = list(self.letters)
    random.shuffle(key)
    return ''.join(key)

def main():
  """
  Consists of the main functionality of the script.
  """
  sc = SubstitutionCipher()
  key, mode = sc.get_random_key(), "encrypt"
  message = "If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell"
  
  # Check key is valid
  if not sc.key_is_valid(key):
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