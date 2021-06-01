#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Class commited to the menu functionality.
#-----------------------------------------------------------------------
class Menu():
  """
  Used to manage the menu functionality.\n
  Contains 2 functions: main_menu(), exit_program().
  """
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

  def exit_program(self, *args):
    """
    Exits the program.
    """
    print("Program exited.")
    exit()