#-----------------------------------------------------------------------
# File Title: Affine Cipher
# File Description: A combination of the multiplication and Caesar ciphers.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. AffineCiper()
#   a. encrypt()
#   b. decrypt()
#   c. get_key_parts()
#   d. check_keys()
#   e. get_random_key()
# 2. main()
#-----------------------------------------------------------------------
import cryptomath, random, sys

#-----------------------------------------------------------------------
# Num: 1 | Title: AffineCipher()
#-----------------------------------------------------------------------
class AffineCipher():
  """
  A class dedicated to the Affine ciper which is a combination of the multiplication and Caesar ciphers, used to encrypt and decrypt data.\n
  Functions: (5) encrypt, decrypt, get_key_parts, check_keys, get_random_key 
  """
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
  symbol_length = len(symbols)

  #-----------------------------------------------------------------------
  # Num: 1a | Title: encrypt()
  #-----------------------------------------------------------------------
  def encrypt(self, phrase, key):
    """
    A cipher that combines the multiplication and Caesar ciphers, resulting in a stronger and more reliable encryption method.\n
    Parameters: (2) phrase to encrypt, key to encrypt by
    """
    key_a, key_b = self.get_key_parts(key)
    self.check_keys(key_a, key_b, "encrypt")
    ciphertext = ""

    for symbol in phrase:
      if symbol in self.symbols:
        # Encrypt the symbol
        sIdx = self.symbols.find(symbol)
        ciphertext += self.symbols[(sIdx * key_a + key_b) % self.symbol_length]
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
    key_a, key_b = self.get_key_parts(key)
    self.check_keys(key_a, key_b, "decrypt")
    plaintext = ""
    mod_inverse_key_a = cryptomath.find_mod_inverse(key_a, self.symbol_length)

    for symbol in phrase:
      if symbol in self.symbols:
        # Decrypt the symbol
        sIdx = self.symbols.find(symbol)
        plaintext += self.symbols[(sIdx - key_b) * mod_inverse_key_a % self.symbol_length]
      else:
        plaintext += symbol # append symbol without decrypting
    return plaintext

  #-----------------------------------------------------------------------
  # Num: 1c | Title: get_key_parts()
  #-----------------------------------------------------------------------
  def get_key_parts(self, key):
    """
    Returns keys A and B after getting integer division and modulus.
    Parameters: (1) input key
    """
    key_a = key // self.symbol_length
    key_b = key % self.symbol_length
    return key_a, key_b

  #-----------------------------------------------------------------------
  # Num: 1d | Title: check_keys()
  #-----------------------------------------------------------------------
  def check_keys(self, key_a, key_b, mode):
    """
    Used to check the key lengths based on encryption mode.\n
    Parameters: (3) first key, second key, mode of cryption
    """
    if key_a == 1 and mode == "encrypt":
      sys.exit("Cipher is weak as key A is 1. Choose a different key.")
    if key_b == 0 and mode == "encrypt":
      sys.exit("Cipher is weak as key B is 0. Choose a different key.")
    if key_a < 0 or key_b < 0 or key_b > self.symbol_length - 1:
      sys.exit(f"Key A must be greater than 0 and Key B must be between 0 and {self.symbol_length - 1}")
    if cryptomath.gcd(key_a, self.symbol_length) == 1:
      sys.exit(f"Key A ({key_a}) and the symbol set size ({self.symbol_length}) are not relatively prime. Choose a different key.")

  #-----------------------------------------------------------------------
  # Num: 1e | Title: get_random_key()
  #-----------------------------------------------------------------------
  def get_random_key(self):
    """
    Generates a random key.
    """
    while True:
      key_a = random.randint(2, self.symbol_length)
      key_b = random.randint(2, self.symbol_length)

      if cryptomath.gcd(key_a, self.symbol_length) == 1:
        return key_a * self.symbol_length + key_b

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "A computer would deserve to be called intelligence if it could deceive a human into believing that it was human. -Alan Turing"
  encrypted_phrase = "5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRGaQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RNQ-5!1RQP36ARu"
  key, mode = 2894, "decrypt"
  ac = AffineCipher()

  if mode == "encrypt":
    text = ac.encrypt(phrase, key)
  elif mode == "decrypt":
    text = ac.decrypt(encrypted_phrase, key)
  
  print(f"Key used: {key} | {mode.title()}ed text:")
  print(text)

# Run main function
if __name__ == "__main__": main()