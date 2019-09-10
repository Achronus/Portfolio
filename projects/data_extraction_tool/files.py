#-----------------------------------------------------------------------
# File Title: FileManage Class
# File Description: Handles the file management functionality.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. FileManage()
#    a. checkDirectory()
#    b. getHTMLFileNames()
#-----------------------------------------------------------------------
import os, time

#-----------------------------------------------------------------------
# Num: 1 | Title: FileManage()
#-----------------------------------------------------------------------
class FileManage():
  """
  Handles all file management functionality. These are mainly utility functions.\n
  Functions: (2) checkDirectory(), getHTMLFileNames()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: checkDirectory()
  #-----------------------------------------------------------------------
  def checkDirectory(self):
    """
    Checks that there are files within the relevant directory. If no files, display an error and close program. Returns dataFolder location.
    """
    folderName = 'data'
    dataFolder = os.getcwd() + '\\' + folderName

    # Create folder if doesn't exist
    if not os.path.exists(folderName):
      os.makedirs(folderName)
      print('Data directory has been created. Please add the HTML files you want to use for data extraction into the data directory.')
      print('Program will exit in 10 seconds. Re-run once files have been added.')
      time.sleep(10)
      exit()
    else:
      # Check there are files in the directory
      folderSize = os.listdir(dataFolder)

      # If no files, display error
      if len(folderSize) == 0:
        print('Data directory exists. Please add the relevant HTML files you want to extract data from into the data directory.')
        print('Program will exit in 10 seconds. Re-run once files have been added.')
        time.sleep(10)
        exit()
      else:
        return dataFolder

  #-----------------------------------------------------------------------
  # Num: 1b | Title: getHTMLFileNames()
  #-----------------------------------------------------------------------
  def getHTMLFileNames(self, dataFolder):
    """
    Checks through the data directory and gets all HTML file names as a list. Returns the list of names.\n
    Parameters: (1) data folder file path
    """
    fileNames = []
    # Look through data directory
    for _, _, files in os.walk(dataFolder):
      for f in files:
        fileNames.append(f)
    return fileNames