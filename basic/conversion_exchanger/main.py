#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
from utils.menu import Menu
from utils.calculations import Calculations

def main():
  """
  Consists of the main functionality of the script.
  """
  # Set variables
  option_list = ['Angle', 'Frequency', 'Length', 'Temperature', 'Volume', 'Weight']
  m = Menu()

  # Run the menu    
  conversion_type = m.type_list(option_list) # Conversion type
  convert_from, convert_to = m.convert_list(conversion_type)
  num = m.get_value(convert_from, convert_to)

  # Run the calculations
  c = Calculations(num)
  data = c.read_csv('utils/formulas.csv')
  c.run_conversion(data, convert_from, convert_to)

# Run main function
if __name__ == '__main__': main()