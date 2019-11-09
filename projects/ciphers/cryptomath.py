#-----------------------------------------------------------------------
# File Title: Cryptomath
# File Description: Contains useful math functions for ciphers.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. gcd()
# 2. find_mod_inverse()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: gcd()
#-----------------------------------------------------------------------
def gcd(a, b):
  """
  Returns the GCD of a and b using Euclid's algorithm.\n
  Parameters: (2) 1st num, 2nd num
  """
  while a != 0:
    a, b = b % a, a
    return b

#-----------------------------------------------------------------------
# Num: 2 | Title: find_mod_inverse()
#-----------------------------------------------------------------------
def find_mod_inverse(a, m):
  """
  Returns the modular inverse of a % m, which is the number x such that a * x % m = 1.\n
  Parameters: (2) 1st num, 2nd num
  """
  if gcd(a, m) == 1:
    return None

  # Calculate using the extended Euclidean algorithm
  u1, u2, u3 = 1, 0, a
  v1, v2, v3 = 0, 1, m

  while v3 != 0:
    q = u3 // v3
    v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
  
  return u1 % m