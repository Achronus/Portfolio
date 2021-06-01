#-----------------------------------------------------------------------
# File Title: Menu Class
# File Description: Handles all menu functionality.
#-----------------------------------------------------------------------
import os
from circle import Circle
from rectangle import Rectangle
from square import Square
from movable import Movable

#-----------------------------------------------------------------------
# Num: 1 | Title: Menu()
#-----------------------------------------------------------------------
class Menu():
  """
  Used to handle all menu functionality and user input controls.\n
  Functions: (6) main_menu(), add_menu(), shift_menu(), get_command(*args), run_command(input_list), exit_program()
  """
  _shapes = {}
  _idx = 1 # shape index

  #-----------------------------------------------------------------------
  # Num: a | Title: main_menu()
  #-----------------------------------------------------------------------
  def main_menu(self):
    """
    Displays the programs main menu and command list.
    """
    print("-------------------------------------------------------------------------------------------------------")
    print(" Main command menu")
    print("-------------------------------------------------------------------------------------------------------")
    print(" - add - Create a new shape")
    print(" - shift - Move or scale an existing shape")
    print(" - menu - Displays the list of user commands")
    print(" - display - Displays a list of shapes created")
    print(" - exit - Exits the program")
    print("-------------------------------------------------------------------------------------------------------")

  #-----------------------------------------------------------------------
  # Num: b | Title: add_menu()
  #-----------------------------------------------------------------------
  def add_menu(self):
    """
    Displays the add menu command list.
    """
    print("-------------------------------------------------------------------------------------------------------")
    print(" Input the command for the shape you would like to create")
    print("-------------------------------------------------------------------------------------------------------")
    print(" - rectangle [x_coordinate] [y_coordinate] [height] [width] - Creates a rectangle")
    print(" - square [x_coordinate] [y_coordinate] [edge_length] - Creates a square")
    print(" - circle [x_coordinate] [y_coordinate] [radius] - Creates a circle")
    print("-------------------------------------------------------------------------------------------------------")

  #-----------------------------------------------------------------------
  # Num: c | Title: shift_menu()
  #-----------------------------------------------------------------------
  def shift_menu(self):
    """
    Displays the shift menu command list.
    """
    print("-------------------------------------------------------------------------------------------------------")
    print(" Input the command to change a shape")
    print("-------------------------------------------------------------------------------------------------------")
    print(" - move [shape_index] [x_coordinate] [y_coordinate] - Moves a created shape")
    print(" - scale [shape_index] [x_scale_amount] [y_scale_amount] - Scales a created shape")
    print("-------------------------------------------------------------------------------------------------------")

  #-----------------------------------------------------------------------
  # Num: d | Title: get_command()
  #-----------------------------------------------------------------------
  def get_command(self, *args):
    """
    Gets the user input and performs checks to action the required command.\n
    Parameters: (1) one, four or five arguments
    """
    # Get the users commands and split into a list
    user_input = input("Enter the command: ")
    input_list = user_input.split(' ')
    
    # Check parameters length
    if len(input_list) >= 2 and len(input_list) < 4:
      print(f"Not enough arguments provided! Check command was input correctly. Length provided: {len(input_list)}")
    elif len(input_list) > 5:
      print(f"Too many arguments provided! Remove additional arguments. Length provided: {len(input_list)}")
    else:
      self.run_command(input_list)

  #-----------------------------------------------------------------------
  # Num: e | Title: run_command()
  #-----------------------------------------------------------------------
  def run_command(self, input_list):
    """
    Checks the arguments of the input list are within the command list and run the associated command.\n
    Parameters: (1) user input parameters
    """
    # Create clear console function
    clear_console = lambda: os.system('cls')

    # Create command list
    command_list = ["rectangle", "square", "circle", "add", "shift", "move", "scale", "menu", "display", "exit"]

    # Create parameters list
    parameters = list(input_list)
    parameters.pop(0) # remove first element
    parameters = [int(i) for i in parameters]

    # Check if command is in command list
    if input_list[0] not in command_list:
      print("First argument is invalid, check correct spelling provided!")

    #---------------------------
    # Create Rectangle
    #---------------------------
    elif input_list[0] == "rectangle" and len(input_list) == 5:

      # Set Rectangle object, store shape and return output
      r = Rectangle(parameters[0], parameters[1], parameters[2], parameters[3])
      self._shapes[self._idx] = r
      r.display_stats()

      # Update shape index
      self._idx += 1

      print()
      print("Input the command 'menu' for the list of commands.")

    #---------------------------
    # Create Square
    #---------------------------
    elif input_list[0] == "square" and len(input_list) == 4:
      
      # Set Square object, store shape and return output
      s = Square(parameters[0], parameters[1], parameters[2])
      self._shapes[self._idx] = s
      s.display_stats()

      # Update shape index
      self._idx += 1

      print()
      print("Input the command 'menu' for the list of commands.")

    #---------------------------
    # Create Circle
    #---------------------------
    elif input_list[0] == "circle" and len(input_list) == 4:
      
      # Set Circle object, store shape and return output
      c = Circle(parameters[0], parameters[1], parameters[2])
      self._shapes[self._idx] = c
      c.display_stats()

      # Update shape index
      self._idx += 1

      print()
      print("Input the command 'menu' for the list of commands.")

    #---------------------------
    # Move or scale a shape
    #---------------------------
    elif (input_list[0] == "move" or input_list[0] == "scale") and len(input_list) == 4:

      # Check shape parameter is correct
      if parameters[0] not in self._shapes:
        print("Shape doesn't exist! Try a different index.")
      else:
        print("---------------------------------")
        print(f"Shape Number: {parameters[0]} updated")
        print("---------------------------------")

        # Move the selected shape
        if input_list[0] == "move":
          self._shapes[parameters[0]].move(parameters[1], parameters[2])

        # Scale the selected shape
        elif input_list[0] == "scale":
          self._shapes[parameters[0]].scale(parameters[1], parameters[2])
        
        # Display shape statistics
        self._shapes[parameters[0]].display_stats()

        print()
        print("Input the command 'menu' for the list of commands.")

    #---------------------------
    # Display add menu
    #---------------------------
    elif input_list[0] == "add":
      clear_console()
      self.add_menu()
    
    #-------------------------------
    # Display shift menu or shapes
    #-------------------------------
    elif input_list[0] == "shift" or input_list[0] == "display":
      
      # Check shape size
      if len(self._shapes) == 0:
        print("No shapes have been created! Create a shape first.")
      else:
        clear_console()

        # Show shift menu
        if input_list[0] == "shift":
          self.shift_menu()

        # Display shape list
        for key, shape in self._shapes.items():
          print("------------------------------")
          print(f"Shape Number: {key}")
          print("------------------------------")
          shape.display_stats()
          print()
        
        # Show additional print
        if input_list[0] == "display":
          print("Input the command 'menu' for the list of commands.")

    #---------------------------
    # Display menu
    #---------------------------
    elif input_list[0] == "menu":
      clear_console()
      self.main_menu()

    #---------------------------
    # Exit the program
    #---------------------------
    elif input_list[0] == "exit":
      self.exit_program()
    
    # Check arguments length
    else:
      print(f"Incorrect argument length. Length provided: {len(input_list)}")

    # Create extra space
    print()

  #-----------------------------------------------------------------------
  # Num: f | Title: exit_program()
  #-----------------------------------------------------------------------
  def exit_program(self):
    """
    Exits the program.
    """
    print("Program exited.")
    exit()