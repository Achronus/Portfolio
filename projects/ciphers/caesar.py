#-----------------------------------------------------------------------
# File Title: Caesar Cipher
# File Description: A very basic cipher.
#-----------------------------------------------------------------------
def caesar(phrase, pos, mode):
  """
  Substitute each letter of a message with a new letter by given number as input.\n
  Parameters: (3) phrase to encrypt, how many letters to change by, mode to encrypt or decrypt
  """
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
  result = ""

  for s in phrase:
    # Check if the symbol exists
    if s in symbols:
      sIdx = symbols.find(s) # Get symbols index

      # Perform encryption/decryption
      if mode == "encrypt":
        rIdx = sIdx + pos
      elif mode == "decrypt":
        rIdx = sIdx - pos
      
      # If index is too high or low, reset index
      if rIdx >= len(symbols):
        rIdx -= len(symbols)
      elif rIdx < 0:
        rIdx += len(symbols)
    
      # Set the result
      result += symbols[rIdx]
    else:
      # Append without encrypting/decrypting
      result += s
      
  print(result)
  return result

def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "This is my secret message"
  caesar(phrase, 5, "encrypt")
  caesar("1234567890", 6, "decrypt")


# Run main function
if __name__ == "__main__": main()