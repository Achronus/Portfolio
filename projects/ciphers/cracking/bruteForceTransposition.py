#-----------------------------------------------------------------------
# File Title: Brute Forcing Transposition Cipher
# File Description: A method of cracking a transposition cipher.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. bfTransposition()
# 2. main()
#-----------------------------------------------------------------------
import sys, os
import detectEnglish as de
import transposition as tp

#-----------------------------------------------------------------------
# Num: 1 | Title: bfTransposition()
#-----------------------------------------------------------------------
def bfTransposition(phrase):
  """
  Runs through all instances of a transposition key until it finds the correct one and outputs it.\n
  Parameters: (1) phrase/data to crack
  """
  detect, tc = de.DetectEnglishText(), tp.TranspositionCipher()
  print("Cracking...")

  # Loop through each key
  for key in range(1, len(phrase)):
    print(f"Trying key #{key}...")

    # Store each key as a variable
    decText = tc.decrypt(phrase, key)

    # If the text is English
    if detect.isEnglish(decText):
      print("\nPossible encryption cracked:")
      print(f"Key {key}: {decText[:100]}\n")
      print("Enter D if done, anything else to continue cracking:")
      response = input("> ")

      # If response is correct, return and break loop
      if response.strip().upper().startswith("D"):
        return decText

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  message = "Cenoonommstmme oo snnio. s s c"
  phrase = bfTransposition(message)

  if phrase == None:
    print("Failed to crack encryption.")
  else:
    print(f"Cracked phrase: {phrase}")

# Run main function
if __name__ == "__main__": main()