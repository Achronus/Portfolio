#-----------------------------------------------------------------------
# File Title: Calculations Class
# File Description: Used to run all conversion calculations. 
#-----------------------------------------------------------------------
import csv
import time
import math

class Calculations():
  """
  Used to run all 6 conversion type metric calculations. Takes in a number as input.
  """
  def __init__(self, num):
    self.num = num

  def read_csv(self, filename):
    """
    Reads the formula CSV file, gets the formula needed and outputs it. Takes a filename as input.
    """
    # Read the file and get the right formula
    with open(filename) as f:
      reader = csv.reader(f)
      data = list(reader)
      return data

  def run_conversion(self, data, convert_from, convert_to):
    """
    Reads the data from the CSV and gets the formula related to the users input.\n
    Parameters: (3) dataset, convert from name, convert to name.
    """
    # Get formula for conversion
    for item in range(len(data)):
      if data[item][0] == f'{convert_from} to {convert_to}':
        formula = data[item][1]
    
    # Display the conversion results
    result = eval(formula)
    print(f"{self.num} {convert_from} -> {result:g} {convert_to}")
    print('Program will exit in 3 seconds.')
    time.sleep(3) # 10 seconds
    

