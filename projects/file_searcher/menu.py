#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Class commited to the menu functionality.
#-----------------------------------------------------------------------
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Used to manage the menu functionality.\n
  Contains 2 functions: main_menu(), exit_program().
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: main_menu()
  #-----------------------------------------------------------------------
  def main_menu(self, *args):
    """
    Displays a list of commands to utilise the choosen CSV file.
    """
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    print(" Please choose an option:") 
    print("- info - displays a list of commands that can be used")
    print("- local [filename] - finds a file on the local disk drive")
    print("- other [filename] - finds a file on another drive on your machine")
    print("- exit - exits the program")
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')

  #-----------------------------------------------------------------------
  # Num: 1b | Title: exit_program()
  #-----------------------------------------------------------------------
  def exit_program(self, *args):
    """
    Exits the program.
    """
    print("Program exited.")
    exit()