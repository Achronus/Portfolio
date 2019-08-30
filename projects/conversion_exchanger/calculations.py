#-----------------------------------------------------------------------
# File Title: Calculations Class
# File Description: Used to run all conversion calculations. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Calculations()
#    a. readCSV()
#    b. runConversion()
#-----------------------------------------------------------------------
import csv

#-----------------------------------------------------------------------
# Num: 1 | Title: Calculations()
#-----------------------------------------------------------------------
class Calculations():
  """
  Used to run all 6 conversion type metric calculations. Takes in a number as input.
  """
  def __init__(self, num):
    self.num = num
  
  #-----------------------------------------------------------------------
  # Num: 1a | Title: readCSV()
  #-----------------------------------------------------------------------
  def readCSV(self, filename):
    """
    Reads the formula CSV file, gets the formula needed and outputs it. Takes a filename as input.
    """
    # Read the file and get the right formula
    with open(filename) as f:
      reader = csv.reader(f)
      data = list(reader)
      return data

  #-----------------------------------------------------------------------
  # Num: 1b | Title: runConversion()
  #-----------------------------------------------------------------------
  def runConversion(self, data, convertFrom, convertTo):
    """
    Reads the data from the CSV and gets the formula related to the users input.\n
    Parameters: (3) dataset, convert from name, convert to name.
    """
    # Get formula for conversion
    for item in range(len(data)):
      if data[item][0] == f'{convertFrom} to {convertTo}':
        formula = data[item][1]
    
    # Display the conversion results
    result = eval(formula)
    print(f"{self.num} {convertFrom} -> {result:g} {convertTo}")
      
    

