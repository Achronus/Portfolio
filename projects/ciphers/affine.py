#-----------------------------------------------------------------------
# File Title: Affine Cipher
# File Description: A combination of the multiplication and Caesar ciphers.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. AffineCiper()
#   a. encrypt()
#   b. decrypt()
#   c. getKeyParts()
#   d. checkKeys()
#   e. getRandomKey()
# 2. main()
#-----------------------------------------------------------------------
import cryptomath, random, sys

#-----------------------------------------------------------------------
# Num: 1 | Title: AffineCipher()
#-----------------------------------------------------------------------
class AffineCipher():
  """
  A class dedicated to the Affine ciper which is a combination of the multiplication and Caesar ciphers, used to encrypt and decrypt data.\n
  Functions: (5) encrypt, decrypt, getKeyParts, checkKeys, getRandomKey 
  """
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
  symbolLength = len(symbols)

  #-----------------------------------------------------------------------
  # Num: 1a | Title: encrypt()
  #-----------------------------------------------------------------------
  def encrypt(self, phrase, key):
    """
    A cipher that combines the multiplication and Caesar ciphers, resulting in a stronger and more reliable encryption method.\n
    Parameters: (2) phrase to encrypt, key to encrypt by
    """
    keyA, keyB = self.getKeyParts(key)
    self.checkKeys(keyA, keyB, "encrypt")
    ciphertext = ""

    for symbol in phrase:
      if symbol in self.symbols:
        # Encrypt the symbol
        sIdx = self.symbols.find(symbol)
        ciphertext += self.symbols[(sIdx * keyA + keyB) % self.symbolLength]
      else:
        ciphertext += symbol # append symbol without encrypting
    return ciphertext

  #-----------------------------------------------------------------------
  # Num: 1b | Title: decrypt()
  #-----------------------------------------------------------------------
  def decrypt(self, phrase, key):
    """
    Decryption method of affine cipher.\n
    Parameters: (2) phrase to decrypt, key to decrypt by
    """
    keyA, keyB = self.getKeyParts(key)
    self.checkKeys(keyA, keyB, "decrypt")
    plaintext = ""
    modInverseOfKeyA = cryptomath.findModInverse(keyA, self.symbolLength)

    for symbol in phrase:
      if symbol in self.symbols:
        # Decrypt the symbol
        sIdx = self.symbols.find(symbol)
        plaintext += self.symbols[(sIdx - keyB) * modInverseOfKeyA % self.symbolLength]
      else:
        plaintext += symbol # append symbol without decrypting
    return plaintext

  #-----------------------------------------------------------------------
  # Num: 1c | Title: getKeyParts()
  #-----------------------------------------------------------------------
  def getKeyParts(self, key):
    """
    Returns keys A and B after getting integer division and modulus.
    Parameters: (1) input key
    """
    keyA = key // self.symbolLength
    keyB = key % self.symbolLength
    return keyA, keyB

  #-----------------------------------------------------------------------
  # Num: 1d | Title: checkKeys()
  #-----------------------------------------------------------------------
  def checkKeys(self, keyA, keyB, mode):
    """
    Used to check the key lengths based on encryption mode.\n
    Parameters: (3) first key, second key, mode of cryption
    """
    if keyA == 1 and mode == "encrypt":
      sys.exit("Cipher is weak as key A is 1. Choose a different key.")
    if keyB == 0 and mode == "encrypt":
      sys.exit("Cipher is weak as key B is 0. Choose a different key.")
    if keyA < 0 or keyB < 0 or keyB > self.symbolLength - 1:
      sys.exit(f"Key A must be greater than 0 and Key B must be between 0 and {self.symbolLength - 1}")
    if cryptomath.gcd(keyA, self.symbolLength) == 1:
      sys.exit(f"Key A ({keyA}) and the symbol set size ({self.symbolLength}) are not relatively prime. Choose a different key.")

  #-----------------------------------------------------------------------
  # Num: 1e | Title: getRandomKey()
  #-----------------------------------------------------------------------
  def getRandomKey(self):
    """
    Generates a random key.
    """
    while True:
      keyA = random.randint(2, self.symbolLength)
      keyB = random.randint(2, self.symbolLength)

      if cryptomath.gcd(keyA, self.symbolLength) == 1:
        return keyA * self.symbolLength + keyB

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "A computer would deserve to be called intelligence if it could deceive a human into believing that it was human. -Alan Turing"
  enPhrase = "5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRGaQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RNQ-5!1RQP36ARu"
  key, mode = 2894, "decrypt"
  ac = AffineCipher()

  if mode == "encrypt":
    text = ac.encrypt(phrase, key)
  elif mode == "decrypt":
    text = ac.decrypt(enPhrase, key)
  
  print(f"Key used: {key} | {mode.title()}ed text:")
  print(text)

# Run main function
if __name__ == "__main__": main()