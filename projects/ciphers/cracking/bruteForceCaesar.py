#-----------------------------------------------------------------------
# File Title: Brute Forcing Caesar Cipher
# File Description: A method of cracking a caesar cipher.
#-----------------------------------------------------------------------
def bf_caesar(phrase):
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
        symbol_idx = symbols.find(s) # Get symbol index
        result_idx = symbol_idx - key # Get result index

        # Reset index if out of range
        if result_idx < 0:
          result_idx += len(symbols)
        
        # Append decrypted symbols
        result += symbols[result_idx]

      else:
        # Append symbol without encrypting/decrypting
        result += s
  
    print(f"Key #{key}: {result}")

def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "guv6Jv6Jz!J6rp5r7Jzr66ntrM"
  bf_caesar(phrase)


# Run main function
if __name__ == "__main__": main()