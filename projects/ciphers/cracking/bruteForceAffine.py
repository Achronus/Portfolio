#-----------------------------------------------------------------------
# File Title: Brute Forcing Affine Cipher
# File Description: Brute forcing the affine cipher.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. bf_affine()
# 2. main()
#-----------------------------------------------------------------------
import affine, cryptomath
import detectEnglish as de

#-----------------------------------------------------------------------
# Num: 1 | Title: bf_affine()
#-----------------------------------------------------------------------
def bf_affine(phrase):
  """
  A function used to brute-force crack the Affine cipher.\n
  Parameters: (1) phrase to crack
  """
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
  SILENT_MODE = True
  detect, ac = de.DetectEnglishText(), affine.AffineCipher()

  # Loop through each key
  for key in range(len(symbols) ** 2):
    key_a = ac.getKeyParts(key)[0]

    if cryptomath.gcd(key_a, len(symbols)) == 1:
      continue

    decoded_text = ac.decrypt(phrase, key)

    if not SILENT_MODE:
      print(f"Tried key #{key}... ({decoded_text[:40]})")

    # Check text is in English
    if detect.is_english(decoded_text):
      print(f"Possible encryption cracked:")
      print(f"Key: #{key} | Decrypted message: {decoded_text[:200]}\n")
      print("Enter D for done, or just press Enter to continue cracking:")
      response = input("> ")

      if response.strip().upper().startswith("D"):
        return decoded_text
  return None

#-----------------------------------------------------------------------
# Num: 2 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  phrase = "5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRGaQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RNQ-5!1RQP36ARu"
  text = bf_affine(phrase)

  if text != None:
    print(text)
  else:
    print("Failed to crack encryption.")

# Run main function
if __name__ == "__main__": main()