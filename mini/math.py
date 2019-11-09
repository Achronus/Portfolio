#-----------------------------------------------------------------------
# File Title: Math Functions
# File Description: Place to store different mathematic functions.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. mean()
# 2. median()
# 3. mode()
# 4. factorial()
# 5. sum_positive_nums()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: mean()
#-----------------------------------------------------------------------
def mean(data_list):
  """
  Finds the mean of a list of data. The mean is the average of all numbers, this is calculated by adding all numbers together and dividing by the size of the list. Takes a list as input.
  """
  length, total = len(data_list), sum(data_list)
  mean = total / length
  return mean

#-----------------------------------------------------------------------
# Num: 2 | Title: median()
#-----------------------------------------------------------------------
def median(data_list):
  """
  Finds the median of a list of data. The median is the middle number in a list of numbers. Takes a list as input.
  """
  length = len(data_list)
  data_list.sort()
  
  if length % 2 == 0:
    median = (data_list[length // 2] + data_list[length //2 - 1]) / 2
  else:
    median = data_list[length // 2]
  return median

#-----------------------------------------------------------------------
# Num: 3 | Title: mode()
#-----------------------------------------------------------------------
def mode(data_list):
  """
  Finds the mode of a list of data. The mode is the number that occurs the most in a list of numbers. Takes a list as input.
  """
  from collections import Counter
  
  length = len(data_list)
  data = dict(Counter(data_list))
  mode = [key for key, val in data.items() if val == max(list(data.values()))]
  
  if len(mode) == length:
    return None
  else:
    return mode

#-----------------------------------------------------------------------
# Num: 4 | Title: factorial()
#-----------------------------------------------------------------------
def factorial(num):
  """
  Denoted as !n, is the product of all positive integers less than or equal to n. Uses recursion.
  """
  if num == 0:
    return 1 # 0!
  else:
    return num * factorial(num-1)

#-----------------------------------------------------------------------
# Num: 5 | Title: sum_positive_nums()
#-----------------------------------------------------------------------
def sum_positive_nums(num_list):
  """
  Uses recursion to add a list of positive numbers together.
  """
  if len(num_list) == 1:
    return num_list[0]
  else:
    return num_list[0] + sum_positive_nums(num_list[1:])