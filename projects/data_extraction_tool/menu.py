#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Handles the menu functionality.
#-----------------------------------------------------------------------
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Handles all menu functionality that the user sees.\n
  Functions: (3) get_filename(), get_num_user_input(), display_menu()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: get_filename()
  #-----------------------------------------------------------------------
  def get_filename(self):
    """
    Used to receive the users file name input. Checks if the file exists, if it does error is displayed. Otherwise, returns the file name with .csv extension added.
    """
    # Get users input
    while True:
      ui = input('=> ').strip('.csv')

      if len(ui) == 0:
        print('Cannot be blank!')
      else:
        csv_name = ui + '.csv'
        
        # If file exists, display error
        if os.path.exists(csv_name):
          print(f"File '{csv_name}' already exists! Please choose a different name.")
        else:
          return csv_name

  #-----------------------------------------------------------------------
  # Num: 1b | Title: get_num_user_input()
  #-----------------------------------------------------------------------
  def get_num_user_input(self, options_dict):
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
        if int(ui) in options_dict:
          clear()
          return options_dict.get(int(ui))
        else:
          print("Number is invalid, please try again.")
      
      # Return error if not number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1c | Title: display_menu()
  #-----------------------------------------------------------------------
  def display_menu(self, item_list):
    """
    Displays the menu of instructions to the user. Returns a dictionary of values.\n
    Parameters: (1) item list
    """
    item_dict = {}
    # Loop through items and display to user
    for idx, item in enumerate(item_list, start=1):
      item_dict.update({idx : item})
      print(f'  {idx}. {item}')
    return item_dict