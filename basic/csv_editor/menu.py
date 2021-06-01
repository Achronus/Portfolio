#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Class commited to the menu functionality.
#-----------------------------------------------------------------------
import os

class Menu():
  """
  Used to manage the menu functionality.\n
  Contains 6 functions: main_menu(), exit_program(), multi_user_input(), single_user_input(), option_list(), get_row_user_input().
  """
  def main_menu(self):
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

  def exit_program(self):
    """
    Exits the program.
    """
    print("Program exited.")
    exit()

  def multi_user_input(self, options_dict):
    """
    Used to get multiple user inputs.\n
    Parameters: (1) options dictionary from option_list()
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ').split(", ")
        ui = list(map(int, ui)) # convert to list of ints

        # Check through dict and get input option
        ui_list = []
        for item in range(len(options_dict)):
          try:
            # Check that the item is in the list
            if ui[item] in options_dict:
              clear()
              ui_list.append(options_dict.get(ui[item]))
            # Not a number within the list
            else:
              print("Number is invalid, please try again.")
          
          # Ignore Length error
          except IndexError:
            break

        return ui_list # Return the user input list

      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  def single_user_input(self, options_dict):
    """
    Used to get one user input.\n
    Parameters: (1) options dictionary from option_list()
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        ui = input('=> ')

        # Check through dict and get input option
        if int(ui) in options_dict:
          clear()
          return options_dict.get(int(ui)) # returns name
        else:
          print("Number is invalid, please try again.")

      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  def option_list(self, option_list, print_output):
    """
    Used to get a list of different options per command. Takes in a list and returns a dictionary.\n
    Parameters: (2) options list, print output statement
    """
    # Get list of relevant options and items
    item_dict = {}
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    print(print_output)
    for idx, item in enumerate(option_list, start=1):
      item_dict.update({idx : item})
      print(f"  {idx}. {item}")
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    return item_dict

  def get_row_user_input(self, options_dict):
    """
    Used to get multiple row user inputs.\n
    Parameters: (1) options dictionary from option_list()
    """
    clear = lambda: os.system('cls')
    # Get users input
    while True:
      try:
        inv_len = True
        while inv_len:
          ui = input('=> ').split(", ")
          if len(ui) > 1:
            inv_len = True
            print("You can only select one option!")
          else:
            inv_len = False
            ui = list(map(int, ui)) # convert to list of ints

        # Check through dict and get input option
        ui_list = []
        for item in range(len(options_dict)):
          try:
            # Check that the item is in the list
            if ui[item] in options_dict:
              clear()
              ui_list.append(ui[item] - 1)
            # Not a number within the list
            else:
              print("Number is invalid, please try again.")
          
          # Ignore Length error
          except IndexError:
            break

        return ui_list # Return the user input list

      # Return error if not number
      except ValueError:
        print("That isn't a number!")