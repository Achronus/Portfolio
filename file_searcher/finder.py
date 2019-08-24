#-----------------------------------------------------------------------
# File Title: Search Class
# File Description: Handles the functions for the file searcher. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. File()
#    a. findLocalFile()
#    b. findOtherDriveFile()
#    c. checkType()
#    d. getOtherDrives()
#    e. findFile()
#-----------------------------------------------------------------------
import os, re

#-----------------------------------------------------------------------
# Num: 1 | Title: Search()
#-----------------------------------------------------------------------
class Search():
  """
  Handles all functions for the file searcher application.\n
  Contains 5 functions: findLocalFile(), findOtherDriveFile(), checkType(), getOtherDrives(), findFile().
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: findLocalFile()
  #-----------------------------------------------------------------------
  def findLocalFile(self, filename):
    """
    Used to find a file or folder on your local disk drive.\n
    Parameters: (1) file or folder name.
    """
    # Find the file
    localDrive = 'C:\\'
    self.checkType(filename, localDrive)
      
  #-----------------------------------------------------------------------
  # Num: 1b | Title: findOtherDriveFile()
  #-----------------------------------------------------------------------
  def findOtherDriveFile(self, filename):
    """
    Used to find a file or folder on another drive other than your local disk drive.\n
    Parameters: (1) file or folder name.
    """
    # Get list of other drives
    clear = lambda: os.system('cls')
    driveList = self.getOtherDrives()

    # Display list of other drives
    driveDict = {}
    print('----------------------------------------------------------------------')
    print('Input the index of the drive you want to search through.')
    for idx, item in enumerate(driveList, start=1):
      driveDict.update({idx : item})
      print(f"  {idx}. {item}")
    print('---------------------------------------------------------------------')

    # Get user input
    while True:
      try:
        ui = input('=> ')
        
        # Check through dict and get drive option
        if int(ui) in driveDict:
          clear()
          selectedDrive = driveDict.get(int(ui)) # Get drive name
        else:
          print("Index out of list, please input a valid index.")
        
        # Search for file/folder
        self.checkType(filename, selectedDrive)
        break

      # Return error if not a number
      except ValueError:
        print("That isn't a number!")

  #-----------------------------------------------------------------------
  # Num: 1c | Title: checkType()
  #-----------------------------------------------------------------------
  def checkType(self, filename, driveToSearch):
    """
    Used to check if the file name is a file or folder.\n
    Parameters: (2) file name, drive to search through
    """
    # If its a file
    if os.path.isfile(filename):
      self.findFile(filename, driveToSearch, 'file')
    # Else if its a directory
    else:
      self.findFile(filename, driveToSearch, 'directory')

  #-----------------------------------------------------------------------
  # Num: 1d | Title: getOtherDrives()
  #-----------------------------------------------------------------------
  def getOtherDrives(self):
    """
    Used to get the other drive letters that are located on the machine.
    """
    # Get drive letters
    driveList = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # iterate over drive letters
    drives = ['%s:\\' % d for d in driveList if os.path.exists('%s:\\' % d)]
    return drives

  #-----------------------------------------------------------------------
  # Num: 1e | Title: findFile()
  #-----------------------------------------------------------------------
  def findFile(self, filename, driveToSearch, itemType):
    """
    Utility function for findLocalFile() and findOtherDriveFile() to search for the selected file or folder.\n
    Parameters: (3) file name, drive to search through, item type
    """
    # Set regex
    rex = re.compile(filename)
    resultList = []

    print(f'Searching for {itemType}, please wait...')
    print('------------------------------------------------------------------------------------------------------------------------')
    # Search through files
    for (root, dirs, files) in os.walk(driveToSearch):
      # Find dir
      if itemType == 'directory':
        for d in dirs:
          result = rex.match(d)
          if result:
            print(os.path.join(root, d))
            resultList.append(d)
      
      # Find file
      if itemType == 'file':
        for f in files:
          result = rex.match(f)
          if result:
            print(os.path.join(root, f))
            resultList.append(f)
    
    # Check that a result has been provided
    if len(resultList) == 0:
      print(f'No {itemType}s found with {filename} on {driveToSearch}.')
    else:
      print('------------------------------------------------------------------------------------------------------------------------')
      print(f"Searching complete. See all {itemType} locations above.")