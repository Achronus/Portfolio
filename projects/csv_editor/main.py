#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. main()
#-----------------------------------------------------------------------
from menu import Menu
from editor import Editor
import pandas as pd
import os

#-----------------------------------------------------------------------
# Num: 1 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  m, e = Menu(), Editor()
  clear = lambda: os.system('cls')

  # Set command list
  commandList = ['info', 'display', 'create', 'add', 'remove', 'update', 'exit']
  commands = [
    ("info", m.mainMenu),
    ("display", e.displayData),
    ("create", e.createFile),
    ("add", e.addData),
    ("remove", e.removeData),
    ("update", e.updateData),
    ("exit", m.exitProgram)
  ]

  # Display menu
  clear()
  m.mainMenu([])

  # Get the users input
  while True:
    # Ask for user input, args as follows: 0, 1 = ['command', 'filename']
    userInput = input("=> ").lower().split(" ")
    clear()
    
    # Error handle if only one argument
    if len(userInput) < 2:
      filename = ''
    else:
      filename = f'{userInput[1]}.csv'
    
    # Loop through each command
    for command in commands:
      # Run function based on command
      if userInput[0] == command[0]:
        command[1](filename)

    # Error if invalid command
    if userInput[0] not in commandList:
      print("Invalid command. Type 'info' for a list of commands => ")

# Run main function
if __name__ == "__main__": main()