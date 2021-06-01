#-----------------------------------------------------------------------
# File Title: FileManage Class
# File Description: Handles the file management functionality.
#-----------------------------------------------------------------------
import os
import time

class FileManage():
  """
  Handles all file management functionality. These are mainly utility functions.\n
  Functions: (2) check_directory(), get_html_filenames()
  """
  def check_directory(self):
    """
    Checks that there are files within the relevant directory. If no files, 
    display an error and close program. Returns data_folder location.
    """
    folder_name = 'data'
    data_folder = os.getcwd() + '\\' + folder_name

    # Create folder if doesn't exist
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
      print('Data directory has been created. Please add the HTML files you want to use for data extraction into the data directory.')
      print('Program will exit in 10 seconds. Re-run once files have been added.')
      time.sleep(10)
      exit()
    else:
      # Check there are files in the directory
      folder_size = os.listdir(data_folder)

      # If no files, display error
      if len(folder_size) == 0:
        print('Data directory exists. Please add the relevant HTML files you want to extract data from into the data directory.')
        print('Program will exit in 10 seconds. Re-run once files have been added.')
        time.sleep(10)
        exit()
      else:
        return data_folder

  def get_html_filenames(self, data_folder):
    """
    Checks through the data directory and gets all HTML file names as a list. 
    Returns the list of names.\n
    Parameters: (1) data folder file path
    """
    filenames = []
    # Look through data directory
    for _, _, files in os.walk(data_folder):
      for f in files:
        filenames.append(f)
    return filenames