#-----------------------------------------------------------------------
# File Title: Create Start Directories Script
# File Description: This script is used to automate the creation ...
# ... of the starting directories before adding images to them.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. createDirectories()
# 2. readCSV()
# 3. main()
#    - Contains month & year variable which must be amended
#-----------------------------------------------------------------------
import os, csv

#---------------------------------------------------------------------
# Num: 1
# Function Title: createDirectories()
# Description: Used to create empty directories for the images by ...
# ... reading the data from the CSV file.
# Parameters: (2) Directory, data.
#---------------------------------------------------------------------
def createDirectories(directory, data):
  # Get directory names & issue names from CSV file
  temp, fromDirList, folderNames = set(), [], []
  for item in range(len(data)):
    temp.add(data[item][0])
    folderNames.append(data[item][0])
  fromDirList = list(temp) # change set back to list

  # If the directory doesn't exist, create it
  if not os.path.exists(directory):
    os.makedirs(directory) # month directory
    for folder in fromDirList:
      os.makedirs(os.path.join(directory, folder)) # name directories

    # Sort folder names list in order
    folderNames.sort()

    # Loop through each directory
    for name in range(len(data)):
      newDirectory = directory + '\\' + data[name][0]
      # Check directory names match
      if data[name][0] == folderNames[name]:
        # Add issue directory
        issueFolder = '\\issue' + data[name][1]
        os.makedirs(os.path.join(newDirectory, issueFolder)) # issue directories
        
        # Add image directory
        imgFolder = newDirectory + issueFolder
        os.makedirs(os.path.join(imgFolder, 'img')) # img directory

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
  csvFile = currentDir + '\\scripts\\text.csv'

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
  year, month = '2019', 'aug'

  # Set file path variables
  currentDir = os.getcwd()
  fromDir = currentDir + '\\[company_name]\\' + year + '\\' + month
  
  # Create directories within from directory
  data = readCSV(currentDir)
  createDirectories(fromDir, data)

# Run main function
if __name__ == "__main__": main()