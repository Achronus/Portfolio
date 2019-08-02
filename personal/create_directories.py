#-----------------------------------------------------------------------
# File Title: Create Directories Script
# File Description: This script is used to automate the creation ...
# ... of the starting directories and adding images to them.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. createDirectories()
# 2. readCSV()
# 3. templateImgMove()
# 4. updatedImgMove()
# 5. main()
#-----------------------------------------------------------------------
import os, csv 
from shutil import copy

#---------------------------------------------------------------------
# Num: 1 | Title: createDirectories()
#---------------------------------------------------------------------
def createDirectories(directory, data, addFolder):
  """
  Used to create empty directories for the images by reading the data from the CSV file.\n
  Parameters: (3) From directory, CSV data & additional folder name.
  """
  # Get directory names & issue names from CSV file
  temp, fromDirList, folderNames, issueNamesList = set(), [], [], []
  for item in range(len(data)):
    temp.add(data[item][0]) # Unique names
    folderNames.append(data[item][0]) # Includes duplicate names
  fromDirList = list(temp) # change set back to list

  # If the directory doesn't exist, create it
  if not os.path.exists(directory):
    os.makedirs(directory) # month directory

    # Output title for directories to console
    print('---------------------------------------------')
    print(f"The following directories have been made:")
    print('---------------------------------------------')

    # Create each named directory
    for folder in fromDirList:
      os.makedirs(os.path.join(directory, folder)) # name directories

    # Sort folder names list in order
    folderNames.sort()

    # Go one step deeper and create each issue directory
    for name in range(len(data)):
      newDirectory = directory + '\\' + data[name][0]
      # Check directory names match
      if data[name][0] == folderNames[name]:
        # Add issue directory
        issueFolder = '\\issue' + data[name][1]
        issueNamesList.append(issueFolder.replace('\\', '')) # Add issue directory name to a list
        os.makedirs(os.path.join(newDirectory, newDirectory + issueFolder)) # issue directories
        
        # Return output to console
        print('  ' + folderNames[name]) # Print folder name
        print('     => ' + issueFolder.replace('\\', '')) # Print issue name

        # Go another step deeper and create the img directory
        if addFolder != 'none':
          imgFolder = newDirectory + issueFolder
          os.makedirs(os.path.join(imgFolder, imgFolder + '\\' + addFolder)) # img directory
  return folderNames, issueNamesList

#-----------------------------------------------------------------------
# Num: 2 | Title: readCSV()
#-----------------------------------------------------------------------
def readCSV(currentDir):
  """
  Used to read the csv file 'text.csv' to get the data.\n
  Parameters: (1) Current directory.\n
  CSV Order: (7) Company, issue, link, heading 1, paragraph 1, heading 2 & paragraph 2.
  """
  # Get csv file
  csvFile = currentDir + '\\text.csv'

  # Put csv data into list of lists
  with open(csvFile, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
  
  # Remove headings
  data.pop(0)
  return data

#-----------------------------------------------------------------------
# Num: 3 | Title: templateImgMove()
#-----------------------------------------------------------------------
def templateImgMove(currentDir, fromDir, folderNames, issueName):
  """
  Used to move the template images from one folder to another.\n
  Parameters: (4) Current directory, from directory, folder names list & issue name list.
  """
  # Set directory variable
  startDir = f'{currentDir}\\templates\\imgs'

  # Loop through each folder
  for folder in range(len(folderNames)):
    # Image file path
    imgFilePath = f'{startDir}\\{folderNames[folder]}\\'
    
    # Get the image names
    imgList = os.listdir(imgFilePath)

    # Copy images to new location
    for image in range(len(imgList)):
      src, dst = imgFilePath + imgList[image], f'{fromDir}\\{folderNames[folder]}\\{issueName[folder]}\\img\\'
      if not os.path.exists(imgList[image]):
        copy(src, dst)
    
  # Output image copy confirmation to console
  print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  print(f"Images finished copying from '{startDir}' to: '{fromDir}'")
  print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#-----------------------------------------------------------------------
# Num: 4 | Title: updatedImgMove()
#-----------------------------------------------------------------------
def updatedImgMove(currentDir, fromDir, filePath, folderNames, issueName):
  """
  Used to move the updated images from one folder to another.\n
  Parameters: (5) Current directory, from directory, folder file path, folder names list & issue name list.
  """
  # Set directory variable
  startDir = f'[file_path]\\email-creatives\\[comapany_name]\\{filePath}'

  # Loop through each folder
  for folder in range(len(folderNames)):
    # Image file path
    imgFilePath = f'{startDir}\\{folderNames[folder]}\\{issueName[folder]}\\img\\'
    
    # Get the image names
    imgList = os.listdir(imgFilePath)

    # Copy images to new location
    for image in range(len(imgList)):
      src, dst = imgFilePath + imgList[image], f'{fromDir}\\{folderNames[folder]}\\{issueName[folder]}'
      if not os.path.exists(imgList[image]):
        copy(src, dst)
  
  # Output image copy confirmation to console
  print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  print(f"Images finished copying from '{startDir}' to: '{fromDir}'")
  print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#-----------------------------------------------------------------------
# Num: 5 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  # Month & year variable (changes each month/year) - month must be 3 characters
  year, month, location, addFolder = input("Enter the year (4 digits), month (3 characters), folder location ([folder]\\[folder]) & extra folder name (Input 'none' if not applicable) - each separated by a space: ").lower().split()

  # Set file path variables
  currentDir = os.getcwd()
  folderLocation = f'[file_path]\\email-creatives\\{location}\\[company_name]'
  fromDir = f'{folderLocation}\\{year}\\{month}'
  folder = f'{year}\\{month}'
  
  # Create directories within from directory
  data = readCSV(currentDir)
  folderNames, issueNamesList = createDirectories(fromDir, data, addFolder)

  # Confirm directories have been created
  print('---------------------------------------------------------------------------------------------------------------------------')
  print(f"All directories have been made, please check the 'email-creatives\\[company_name]\\{year}\\{month}' folder.")
  print('---------------------------------------------------------------------------------------------------------------------------')

  # Check the location
  if location == '[company_name]':
    templateImgMove(currentDir, fromDir, folderNames, issueNamesList) # Move template images
  else:
    updatedImgMove(currentDir, fromDir, folder, folderNames, issueNamesList) # Move updated images

# Run main function
if __name__ == "__main__": main()