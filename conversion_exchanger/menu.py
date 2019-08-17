#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Contains all functionality related to the menu.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Menu()
#   a. typeList()
#   b. convertList()
#   c. convertListOutputFormat()
#   d. getUserInput()
#   e. getValue()
#-----------------------------------------------------------------------
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Parent class to all other conversion metrics.\n
  Parameters: (1) Number.\n
  Functions available (3): result(convertFrom, convertTo, result), typeList(optionList), convertList(conType)
  """  
  #-----------------------------------------------------------------------
  # Num: 1a | Title: typeList()
  #-----------------------------------------------------------------------
  def typeList(self, optionList):
    """
    Displays a list of all the conversion type options. Takes an option list as input.\n
    Options: (6) Temperature, frequency, weight, volume, angle, length.
    """
    # Output conversion type options list
    printOutput = "Select the conversion type (input the index):"
    optionsDict = self.convertListOutputFormat(optionList, printOutput)
    conType = self.getUserInput(optionsDict)
    return conType

  #-----------------------------------------------------------------------
  # Num: 1b | Title: convertList()
  #-----------------------------------------------------------------------
  def convertList(self, conType):
    """
    Displays a list of all the conversion options within the selected converion type for from and to.\n
    Takes a conversion type as input and uses the utility function 'convertListOutputFormat()'.\n
    Options are broken down into relevant types below:\n
      1. Angle (4) - Degrees, radians, gradians, milligradians.
      2. Frequency (4) - Hertz, kilohertz, megahertz, gigahertz.
      3. Length (11) - Kilometre, metre, centimetre, millimetre, micrometre, nanometre, mile, yard, foot, inch, nautical mile.
      4. Volume (12) - Cubic metre, litre, millilitre, gallon, quart, pint, cup, fluid ounce, tablespoon, teaspoon, cubic foot, cubic inch.
      5. Temperature (3) - Celsius, fahrenheit, kelvin.
      6. Weight (8) - Kilogram, gram, milligram, ton, microgram, stone, pound, ounce.
    """
    # Set Metrics
    if conType == 'Angle':
      metrics = ['Degrees', 'Gradians', 'Milligradians', 'Radians']

    if conType == 'Frequency':
      metrics = ['Gigahertz', 'Hertz', 'Kilohertz', 'Megahertz']

    if conType == 'Length':
      metrics = ['Centimetre', 'Foot', 'Inch', 'Kilometre', 'Metre', 'Micrometre', 'Mile', 'Millimetre', 'Nanometre', 'Nautical Mile', 'Yard']
    
    if conType == 'Volume':
      metrics = ['Cubic Foot', 'Cubic Inch', 'Cubic Metre', 'Cup', 'Fluid Ounce', 'Gallon', 'Litre', 'Millilitre', 'Pint', 'Tablespoon', 'Teaspoon', 'Quart']
    
    if conType == 'Temperature':
      metrics = ['Celsius', 'Fahrenheit', 'Kelvin']
    
    if conType == 'Weight':
      metrics = ['Gram', 'Kilogram', 'Microgram', 'Milligram', 'Ounce', 'Pound', 'Stone', 'Ton']
    
    # Output metric list and get conversion metric
    printOutput1 = f"You selected the '{conType}' conversion type, what would you like to convert as?"
    metricDict = self.convertListOutputFormat(metrics, printOutput1)
    convertFrom = self.getUserInput(metricDict)

    # Remove selected metric
    if convertFrom in metrics:
      metrics.remove(convertFrom)

    # Output new metric list and get conversion metric
    printOutput2 = f"You selected the '{convertFrom}' conversion metric to convert to:"
    updatedMetricDict = self.convertListOutputFormat(metrics, printOutput2)
    convertTo = self.getUserInput(updatedMetricDict)
    return convertFrom, convertTo 
  
  #-----------------------------------------------------------------------
  # Num: 1c | Title: convertListOutputFormat()
  #-----------------------------------------------------------------------
  def convertListOutputFormat(self, optionList, printOutput):
    """
    Utility function for convertList. Takes in a list and returns a dictionary.\n
    Parameters: (3) conversion type name, options list, print output statement
    """
    # Get list of relevant options and items
    itemDict = {}
    print('---------------------------------------------------------------------------------')
    print(printOutput)
    for idx, item in enumerate(optionList, start=1):
      itemDict.update({idx : item})
      print(f"  {idx}. {item}")
    print('---------------------------------------------------------------------------------')
    return itemDict

  #-----------------------------------------------------------------------
  # Num: 1d | Title: getUserInput()
  #-----------------------------------------------------------------------
  def getUserInput(self, optionsDict):
    """
    Utility function used to get the users input.
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ')

        # Check through dict and get input option
        if int(ui) in optionsDict:
          clear()
          return optionsDict.get(int(ui)) # returns a type or metric name
        else:
          print("Number is invalid, please try again.")
      
      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1e | Title: getValue()
  #-----------------------------------------------------------------------
  def getValue(self, convertFrom, convertTo):
    """
    Used to get the value for converting to a different metric.
    """
    # Get users input
    print(f"Input a number to convert from '{convertFrom}' to '{convertTo}':")
    while True:
      try:
        value = int(input('=> '))
        return value
      
      # Return error if not number
      except ValueError:
        print("That isn't a number!")