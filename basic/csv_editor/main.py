#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
from .utils.menu import Menu
from .utils.editor import Editor
import os

def main():
  """
  Consists of the main functionality of the script.
  """
  m, e = Menu(), Editor()
  clear = lambda: os.system('cls')

  # Set command list
  command_list = ['info', 'display', 'create', 'add', 'remove', 'update', 'exit']
  commands = [
    ("info", m.main_menu),
    ("display", e.display_data),
    ("create", e.create_file),
    ("add", e.add_data),
    ("remove", e.remove_data),
    ("update", e.update_data),
    ("exit", m.exit_program)
  ]

  # Display menu
  clear()
  m.main_menu([])

  # Get the users input
  while True:
    # Ask for user input, args as follows: 0, 1 = ['command', 'filename']
    user_input = input("=> ").lower().split(" ")
    clear()
    
    # Error handle if only one argument
    if len(user_input) < 2:
      filename = ''
    else:
      filename = f'{user_input[1]}.csv'
    
    # Loop through each command
    for command in commands:
      # Run function based on command
      if user_input[0] == command[0]:
        command[1](filename)

    # Error if invalid command
    if user_input[0] not in command_list:
      print("Invalid command. Type 'info' for a list of commands => ")

# Run main function
if __name__ == "__main__": main()