#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Handles the menu functionality.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Menu()
#    a. getFileName()
#    b. getNumUserInput()
#    c. displayMenu()
#-----------------------------------------------------------------------
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Handles all menu functionality that the user sees.\n
  Functions: (3) getFileName(), getNumUserInput(), displayMenu()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: getFileName()
  #-----------------------------------------------------------------------
  def getFileName(self):
    """
    Used to receive the users file name input. Checks if the file exists, if it does error is displayed. Otherwise, returns the file name with .csv extension added.
    """
    # Get users input
    while True:
      ui = input('=> ').strip('.csv')

      if len(ui) == 0:
        print('Cannot be blank!')
      else:
        csvName = ui + '.csv'
        
        # If file exists, display error
        if os.path.exists(csvName):
          print(f"File '{csvName}' already exists! Please choose a different name.")
        else:
          return csvName

  #-----------------------------------------------------------------------
  # Num: 1b | Title: getNumUserInput()
  #-----------------------------------------------------------------------
  def getNumUserInput(self, optionsDict):
    """
    Used to receive the users index input. Returns the index input.\n
    Parameters: (1) dictionary of menu items
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ')

        # Check through dict and get input option
        if int(ui) in optionsDict:
          clear()
          return optionsDict.get(int(ui))
        else:
          print("Number is invalid, please try again.")
      
      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1c | Title: displayMenu()
  #-----------------------------------------------------------------------
  def displayMenu(self, itemList):
    """
    Displays the menu of instructions to the user. Returns a dictionary of values.\n
    Parameters: (1) item list
    """
    itemDict = {}
    # Loop through items and display to user
    for idx, item in enumerate(itemList, start=1):
      itemDict.update({idx : item})
      print(f'  {idx}. {item}')
    return itemDict