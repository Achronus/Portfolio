#-----------------------------------------------------------------------
# File Title: Brute Forcing Affine Cipher
# File Description: Brute forcing the affine cipher.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. bfAffine()
# 2. main()
#-----------------------------------------------------------------------
import affine, cryptomath
import detectEnglish as de

#-----------------------------------------------------------------------
# Num: 1 | Title: bfAffine()
#-----------------------------------------------------------------------
def bfAffine(phrase):
  """
  A function used to brute-force crack the Affine cipher.\n
  Parameters: (1) phrase to crack
  """
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
  silentMode = True
  detect, ac = de.DetectEnglishText(), affine.AffineCipher()

  # Loop through each key
  for key in range(len(symbols) ** 2):
    keyA = ac.getKeyParts(key)[0]

    if cryptomath.gcd(keyA, len(symbols)) == 1:
      continue

    decText = ac.decrypt(phrase, key)

    if not silentMode:
      print(f"Tried key #{key}... ({decText[:40]})")

    # Check text is in English
    if detect.isEnglish(decText):
      print(f"Possible encryption cracked:")
      print(f"Key: #{key} | Decrypted message: {decText[:200]}\n")
      print("Enter D for done, or just press Enter to continue cracking:")
      response = input("> ")

      if response.strip().upper().startswith("D"):
        return decText
  return None

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRGaQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RNQ-5!1RQP36ARu"
  text = bfAffine(phrase)

  if text != None:
    print(text)
  else:
    print("Failed to crack encryption.")

# Run main function
if __name__ == "__main__": main()