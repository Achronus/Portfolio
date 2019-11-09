#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Contains all functionality related to the menu.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Menu()
#   a. type_list()
#   b. convert_list()
#   c. convert_list_output()
#   d. get_user_input()
#   e. get_value()
#-----------------------------------------------------------------------
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Parent class to all other conversion metrics.\n
  Parameters: (1) Number.\n
  Functions available (3): result(convert_from, convert_to, result), type_list(option_list), convert_list(conversion_type)
  """  
  #-----------------------------------------------------------------------
  # Num: 1a | Title: type_list()
  #-----------------------------------------------------------------------
  def type_list(self, option_list):
    """
    Displays a list of all the conversion type options. Takes an option list as input.\n
    Options: (6) Temperature, frequency, weight, volume, angle, length.
    """
    # Output conversion type options list
    print_output = "Select the conversion type (input the index):"
    options_dict = self.convert_list_output(option_list, print_output)
    conversion_type = self.get_user_input(options_dict)
    return conversion_type

  #-----------------------------------------------------------------------
  # Num: 1b | Title: convert_list()
  #-----------------------------------------------------------------------
  def convert_list(self, conversion_type):
    """
    Displays a list of all the conversion options within the selected converion type for from and to.\n
    Takes a conversion type as input and uses the utility function 'convert_list_output()'.\n
    Options are broken down into relevant types below:\n
      1. Angle (4) - Degrees, radians, gradians, milligradians.
      2. Frequency (4) - Hertz, kilohertz, megahertz, gigahertz.
      3. Length (11) - Kilometre, metre, centimetre, millimetre, micrometre, nanometre, mile, yard, foot, inch, nautical mile.
      4. Volume (12) - Cubic metre, litre, millilitre, gallon, quart, pint, cup, fluid ounce, tablespoon, teaspoon, cubic foot, cubic inch.
      5. Temperature (3) - Celsius, fahrenheit, kelvin.
      6. Weight (8) - Kilogram, gram, milligram, ton, microgram, stone, pound, ounce.
    """
    # Set Metrics
    if conversion_type == 'Angle':
      metrics = ['Degrees', 'Gradians', 'Milligradians', 'Radians']

    if conversion_type == 'Frequency':
      metrics = ['Gigahertz', 'Hertz', 'Kilohertz', 'Megahertz']

    if conversion_type == 'Length':
      metrics = ['Centimetre', 'Foot', 'Inch', 'Kilometre', 'Metre', 'Micrometre', 'Mile', 'Millimetre', 'Nanometre', 'Nautical Mile', 'Yard']
    
    if conversion_type == 'Volume':
      metrics = ['Cubic Foot', 'Cubic Inch', 'Cubic Metre', 'Cup', 'Fluid Ounce', 'Gallon', 'Litre', 'Millilitre', 'Pint', 'Tablespoon', 'Teaspoon', 'Quart']
    
    if conversion_type == 'Temperature':
      metrics = ['Celsius', 'Fahrenheit', 'Kelvin']
    
    if conversion_type == 'Weight':
      metrics = ['Gram', 'Kilogram', 'Microgram', 'Milligram', 'Ounce', 'Pound', 'Stone', 'Ton']
    
    # Output metric list and get conversion metric
    print_output1 = f"You selected the '{conversion_type}' conversion type, what would you like to convert as?"
    metric_dict = self.convert_list_output(metrics, print_output1)
    convert_from = self.get_user_input(metric_dict)

    # Remove selected metric
    if convert_from in metrics:
      metrics.remove(convert_from)

    # Output new metric list and get conversion metric
    print_output2 = f"You selected the '{convert_from}' conversion metric to convert to:"
    updated_metric_dict = self.convert_list_output(metrics, print_output2)
    convert_to = self.get_user_input(updated_metric_dict)
    return convert_from, convert_to 
  
  #-----------------------------------------------------------------------
  # Num: 1c | Title: convert_list_output()
  #-----------------------------------------------------------------------
  def convert_list_output(self, option_list, print_output):
    """
    Utility function for convert_list. Takes in a list and returns a dictionary.\n
    Parameters: (2) options list, print output statement
    """
    # Get list of relevant options and items
    item_dict = {}
    print('---------------------------------------------------------------------------------')
    print(print_output)
    for idx, item in enumerate(option_list, start=1):
      item_dict.update({idx : item})
      print(f"  {idx}. {item}")
    print('---------------------------------------------------------------------------------')
    return item_dict

  #-----------------------------------------------------------------------
  # Num: 1d | Title: get_user_input()
  #-----------------------------------------------------------------------
  def get_user_input(self, options_dict):
    """
    Utility function used to get the users input.
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ')

        # Check through dict and get input option
        if int(ui) in options_dict:
          clear()
          return options_dict.get(int(ui)) # returns a type or metric name
        else:
          print("Number is invalid, please try again.")
      
      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1e | Title: get_value()
  #-----------------------------------------------------------------------
  def get_value(self, convert_from, convert_to):
    """
    Used to get the value for converting to a different metric.
    """
    # Get users input
    print(f"Input a number to convert from '{convert_from}' to '{convert_to}':")
    while True:
      try:
        value = int(input('=> '))
        return value
      
      # Return error if not number
      except ValueError:
        print("That isn't a number!")