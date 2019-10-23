#-----------------------------------------------------------------------
# File Title: Brute Forcing Caesar Cipher
# File Description: A method of cracking a caesar cipher.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. bfCaesar()
# 2. main()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: bfCesar()
#-----------------------------------------------------------------------
def bfCaesar(phrase):
  """
  Brute force approach to breaking the caesar cipher encryption.\n
  Parameters: (1) phrase to crack
  """
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

  # Loop through every possible key
  for key in range(len(symbols)):
    result = ""
    # Loop through each symbol in the given phrase
    for s in phrase:
      # If symbol is in symbols
      if s in symbols:
        sIdx = symbols.find(s) # Get symbol index
        rIdx = sIdx - key # Get result index

        # Reset index if out of range
        if rIdx < 0:
          rIdx += len(symbols)
        
        # Append decrypted symbols
        result += symbols[rIdx]

      else:
        # Append symbol without encrypting/decrypting
        result += s
  
    print(f"Key #{key}: {result}")

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "guv6Jv6Jz!J6rp5r7Jzr66ntrM"
  bfCaesar(phrase)


# Run main function
if __name__ == "__main__": main()