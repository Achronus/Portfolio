#-----------------------------------------------------------------------
# File Title: Create Directories Script
# File Description: This script is used to automate the creation ...
# ... of the starting directories and adding images to them.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. createDirectories()
# 2. readCSV()
# 3. main()
#-----------------------------------------------------------------------
import os, csv

#---------------------------------------------------------------------
# Num: 1
# Function Title: createDirectories()
# Description: Used to create empty directories for the images by ...
# ... reading the data from the CSV file.
# Parameters: (4) Directory, data & additional folder.
#---------------------------------------------------------------------
def createDirectories(directory, data, addFolder):
  # Get directory names & issue names from CSV file
  temp, fromDirList, folderNames = set(), [], []
  for item in range(len(data)):
    temp.add(data[item][0])
    folderNames.append(data[item][0])
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
        os.makedirs(os.path.join(newDirectory, newDirectory + issueFolder)) # issue directories
        
        # Return output to console
        print('  ' + folderNames[name]) # Print folder name
        print('     => ' + issueFolder.replace('\\', '')) # Print issue name

        # Go another step deeper and create the img directory
        if addFolder != 'none':
          imgFolder = newDirectory + issueFolder
          os.makedirs(os.path.join(imgFolder, imgFolder + '\\' + addFolder)) # img directory

#-----------------------------------------------------------------------
# Num: 2
# Function Title: readCSV()
# Description: Used to read the csv file 'text.csv' to get the data.
# Parameters: (1) Current directory.
# CSV Order: (7) Company, issue, link, heading 1, paragraph 1, ... 
# ... heading 2, paragraph 2.
#-----------------------------------------------------------------------
def readCSV(currentDir):
  # Get csv file
  csvFile = currentDir + '\\text.csv'

  # Put csv data into list of lists
  with open(csvFile, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
  
  # Remove headings
  data.pop(0)
  return data

#---------------------------------------------------------------------
# Num: 3
# Function Title: main()
# Description: Consists of the main functionality of the script.
# Parameters: (0) None.
#---------------------------------------------------------------------
def main():
  # Month & year variable (changes each month/year) - month must be 3 characters
  year, month, location, addFolder = input("Enter the year (4 digits), month (3 characters), folder location ([folder]\\[folder]) & extra folder name (Input 'none' if not applicable) - each separated by a space: ").lower().split()

  # Set file path variables
  currentDir = os.getcwd()
  folderLocation = f'D:\\[file_location]\\email-creatives\\{location}\\[company_name]'
  fromDir = f'{folderLocation}\\{year}\\{month}'
  
  # Create directories within from directory
  data = readCSV(currentDir)
  createDirectories(fromDir, data, addFolder)

  # Confirm script has finished running
  print('---------------------------------------------------------------------------------------------------------------------------')
  print(f"All directories have been made, please check the 'email-creatives\\[company_name]\\{year}\\{month}' folder.")
  print('---------------------------------------------------------------------------------------------------------------------------')

# Run main function
if __name__ == "__main__": main()