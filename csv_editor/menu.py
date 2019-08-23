#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Class commited to the menu functionality.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Menu()
#    a. mainMenu()
#    b. exitProgram()
#    c. multiUserInput()
#    d. singleUserInput()
#    e. optionList()
#    f. getRowUserInput()
#-----------------------------------------------------------------------
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Used to manage the menu functionality.\n
  Contains 6 functions: mainMenu(), exitProgram(), multiUserInput(), singleUserInput(), optionList(), getRowUserInput().
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: mainMenu()
  #-----------------------------------------------------------------------
  def mainMenu(self, *args):
    """
    Displays a list of commands to utilise the choosen CSV file.
    """
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    print(" Please choose an option:") 
    print("- info - displays a list of commands that can be used")
    print("- display [filename] - displays the data within a CSV file")
    print("- create [filename] - creates a CSV file")
    print("- add [filename] - adds data to a chosen CSV file")
    print("- remove [filename] - removes data from a chosen CSV file")
    print("- update [filename] - allows you to update the data within a chosen CSV file")
    print("- exit - exits the program")
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')

  #-----------------------------------------------------------------------
  # Num: 1b | Title: exitProgram()
  #-----------------------------------------------------------------------
  def exitProgram(self, *args):
    """
    Exits the program.
    """
    print("Program exited.")
    exit()

  #-----------------------------------------------------------------------
  # Num: 1c | Title: multiUserInput()
  #-----------------------------------------------------------------------
  def multiUserInput(self, optionsDict):
    """
    Used to get multiple user inputs.\n
    Parameters: (1) options dictionary from optionList()
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ').split(", ")
        ui = list(map(int, ui)) # convert to list of ints

        # Check through dict and get input option
        uiList = []
        for item in range(len(optionsDict)):
          try:
            # Check that the item is in the list
            if ui[item] in optionsDict:
              clear()
              uiList.append(optionsDict.get(ui[item]))
            # Not a number within the list
            else:
              print("Number is invalid, please try again.")
          
          # Ignore Length error
          except IndexError:
            break

        return uiList # Return the user input list

      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1d | Title: singleUserInput()
  #-----------------------------------------------------------------------
  def singleUserInput(self, optionsDict):
    """
    Used to get one user input.\n
    Parameters: (1) options dictionary from optionList()
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ')

        # Check through dict and get input option
        if int(ui) in optionsDict:
          clear()
          return optionsDict.get(int(ui)) # returns name
        else:
          print("Number is invalid, please try again.")

      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1e | Title: optionList()
  #-----------------------------------------------------------------------
  def optionList(self, optionList, printOutput):
    """
    Used to get a list of different options per command. Takes in a list and returns a dictionary.\n
    Parameters: (2) options list, print output statement
    """
    # Get list of relevant options and items
    itemDict = {}
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    print(printOutput)
    for idx, item in enumerate(optionList, start=1):
      itemDict.update({idx : item})
      print(f"  {idx}. {item}")
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    return itemDict

  #-----------------------------------------------------------------------
  # Num: 1f | Title: getRowUserInput()
  #-----------------------------------------------------------------------
  def getRowUserInput(self, optionsDict):
    """
    Used to get multiple row user inputs.\n
    Parameters: (1) options dictionary from optionList()
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        invalidLen = True
        while invalidLen:
          ui = input('=> ').split(", ")
          if len(ui) > 1:
            invalidLen = True
            print("You can only select one option!")
          else:
            invalidLen = False
            ui = list(map(int, ui)) # convert to list of ints

        # Check through dict and get input option
        uiList = []
        for item in range(len(optionsDict)):
          try:
            # Check that the item is in the list
            if ui[item] in optionsDict:
              clear()
              uiList.append(ui[item] - 1)
            # Not a number within the list
            else:
              print("Number is invalid, please try again.")
          
          # Ignore Length error
          except IndexError:
            break

        return uiList # Return the user input list

      # Return error if not number
      except ValueError:
        print("That isn't a number!")