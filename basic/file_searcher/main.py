#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
import os
from .menu import Menu
from .finder import Search

def main():
  """
  Consists of the main functionality of the script.
  """
  m, s = Menu(), Search()
  clear = lambda: os.system('cls')

  # Set command list
  command_list = ['info', 'local', 'other', 'exit']
  commands = [
    ("info", m.main_menu),
    ("local", s.find_local_file),
    ("other", s.find_other_drive_file),
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
      filename = user_input[1]
    
    # Loop through each command
    for command in commands:
      # Run function based on command
      if user_input[0] == command[0]:
        command[1](filename)

    # Error if invalid command
    if user_input[0] not in command_list:
      print("Invalid command. Type 'info' for a list of commands => ")
    
# Run main function
if __name__ == '__main__': main()