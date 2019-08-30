#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. main()
#-----------------------------------------------------------------------
from menu import Menu
from calculations import Calculations

#-----------------------------------------------------------------------
# Num: 1 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  # Set variables
  optionList = ['Angle', 'Frequency', 'Length', 'Temperature', 'Volume', 'Weight']
  m = Menu()

  # Run the menu    
  conType = m.typeList(optionList) # Conversion type
  convertFrom, convertTo = m.convertList(conType)
  num = m.getValue(convertFrom, convertTo)

  # Run the calculations
  c = Calculations(num)
  data = c.readCSV('formulas.csv')
  c.runConversion(data, convertFrom, convertTo)

# Run main function
if __name__ == '__main__': main()