#-----------------------------------------------------------------------
# File Title: Search Class
# File Description: Handles the functions for the file searcher. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. File()
#    a. find_local_file()
#    b. find_other_drive_file()
#    c. check_type()
#    d. get_other_drives()
#    e. file_file()
#-----------------------------------------------------------------------
import os, re

#-----------------------------------------------------------------------
# Num: 1 | Title: Search()
#-----------------------------------------------------------------------
class Search():
  """
  Handles all functions for the file searcher application.\n
  Contains 5 functions: find_local_file(), find_other_drive_file(), check_type(), get_other_drives(), file_file().
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: find_local_file()
  #-----------------------------------------------------------------------
  def find_local_file(self, filename):
    """
    Used to find a file or folder on your local disk drive.\n
    Parameters: (1) file or folder name.
    """
    # Find the file
    local_drive = 'C:\\'
    self.check_type(filename, local_drive)
      
  #-----------------------------------------------------------------------
  # Num: 1b | Title: find_other_drive_file()
  #-----------------------------------------------------------------------
  def find_other_drive_file(self, filename):
    """
    Used to find a file or folder on another drive other than your local disk drive.\n
    Parameters: (1) file or folder name.
    """
    # Get list of other drives
    clear = lambda: os.system('cls')
    drive_list = self.get_other_drives()

    # Display list of other drives
    drive_dict = {}
    print('----------------------------------------------------------------------')
    print('Input the index of the drive you want to search through.')
    for idx, item in enumerate(drive_list, start=1):
      drive_dict.update({idx : item})
      print(f"  {idx}. {item}")
    print('---------------------------------------------------------------------')

    # Get user input
    while True:
      try:
        ui = input('=> ')
        
        # Check through dict and get drive option
        if int(ui) in drive_dict:
          clear()
          selected_drive = drive_dict.get(int(ui)) # Get drive name
        else:
          print("Index out of list, please input a valid index.")
        
        # Search for file/folder
        self.check_type(filename, selected_drive)
        break

      # Return error if not a number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1c | Title: check_type()
  #-----------------------------------------------------------------------
  def check_type(self, filename, drive_to_search):
    """
    Used to check if the file name is a file or folder.\n
    Parameters: (2) file name, drive to search through
    """
    # If its a file
    if os.path.isfile(filename):
      self.file_file(filename, drive_to_search, 'file')
    # Else if its a directory
    else:
      self.file_file(filename, drive_to_search, 'directory')

  #-----------------------------------------------------------------------
  # Num: 1d | Title: get_other_drives()
  #-----------------------------------------------------------------------
  def get_other_drives(self):
    """
    Used to get the other drive letters that are located on the machine.
    """
    # Get drive letters
    drive_list = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # iterate over drive letters
    drives = ['%s:\\' % d for d in drive_list if os.path.exists('%s:\\' % d)]
    return drives

  #-----------------------------------------------------------------------
  # Num: 1e | Title: file_file()
  #-----------------------------------------------------------------------
  def file_file(self, filename, drive_to_search, item_type):
    """
    Utility function for find_local_file() and find_other_drive_file() to search for the selected file or folder.\n
    Parameters: (3) file name, drive to search through, item type
    """
    # Set regex
    rex = re.compile(filename)
    result_list = []

    print(f'Searching for {item_type}, please wait...')
    print('------------------------------------------------------------------------------------------------------------------------')
    # Search through files
    for (root, dirs, files) in os.walk(drive_to_search):
      # Find dir
      if item_type == 'directory':
        for d in dirs:
          result = rex.match(d)
          if result:
            print(os.path.join(root, d))
            result_list.append(d)
      
      # Find file
      if item_type == 'file':
        for f in files:
          result = rex.match(f)
          if result:
            print(os.path.join(root, f))
            result_list.append(f)
    
    # Check that a result has been provided
    if len(result_list) == 0:
      print(f'No {item_type}s found with {filename} on {drive_to_search}.')
    else:
      print('------------------------------------------------------------------------------------------------------------------------')
      print(f"Searching complete. See all {item_type} locations above.")