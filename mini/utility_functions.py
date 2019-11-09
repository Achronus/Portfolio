#-----------------------------------------------------------------------
# File Title: Utility Functions
# File Description: Place to store different utility functions.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. is_sorted()
# 2. countdown()
# 3. lists_to_tuple()
# 4. function_name()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: is_sorted()
#-----------------------------------------------------------------------
def is_sorted(data_list):
  """
  Checks if a list is sorted. Returns a bool.
  """
  if data_list == sorted(data_list):
    result = True
  else:
    result = False
  return result

#-----------------------------------------------------------------------
# Num: 2 | Title: countdown()
#-----------------------------------------------------------------------
def countdown(x):
  """
  Counts down from number input.
  """
  # If 0, end the countdown
  if x == 0:
    print("Done!")
  # Otherwise, recur down to 0
  else:
    print(x, "...")
    countdown(x-1)

#-----------------------------------------------------------------------
# Num: 3 | Title: lists_to_tuple()
#-----------------------------------------------------------------------
def lists_to_tuple(lists):
  """
  Converts a list of lists to a single tuple. Takes a list of lists as input.
  """
  size, result = [], []

  # Find largest list
  for opt in lists:
    size.append(len(opt))

  # set largest list length
  lg_list_len = max(size)

  # Add empty space until list length is correct
  for l in lists:
    while len(l) != lg_list_len:
      l.append('')

  # Add data to tuple
  for item in range(lg_list_len):
    new_data = [] # reset row each loop
    for l in lists:
      new_data.append(l[item])
    result.append(tuple(new_data)) # convert row to tuple and add to list
  return result

#-----------------------------------------------------------------------
# Num: 4 | Title: function_name()
#-----------------------------------------------------------------------
def function_name(self, func):
  """
  Gets function name of given function.\n
  Parameters: (1) function
  """
  return func.__name__