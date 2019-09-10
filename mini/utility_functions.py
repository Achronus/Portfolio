#-----------------------------------------------------------------------
# File Title: Utility Functions
# File Description: Place to store different utility functions.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. isSorted()
# 2. countdown()
# 3. listsToTuple()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Num: 1 | Title: isSorted()
#-----------------------------------------------------------------------
def isSorted(dataList):
  """
  Checks if a list is sorted. Returns a bool.
  """
  if dataList == sorted(dataList):
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
# Num: 3 | Title: listsToTuple()
#-----------------------------------------------------------------------
def listsToTuple(lists):
  """
  Converts a list of lists to a single tuple. Takes a list of lists as input.
  """
  size, result = [], []

  # Find largest list
  for opt in lists:
    size.append(len(opt))

  # set largest list length
  lgList = max(size)

  # Add empty space until list length is correct
  for l in lists:
    while len(l) != lgList:
      l.append('')

  # Add data to tuple
  for item in range(lgList):
    newData = [] # reset row each loop
    for l in lists:
      newData.append(l[item])
    result.append(tuple(newData)) # convert row to tuple and add to list
  return result