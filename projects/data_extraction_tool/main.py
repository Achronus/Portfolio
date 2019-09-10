#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. main()
#-----------------------------------------------------------------------
import os
from menu import Menu
from extract import Extraction
from files import FileManage

#-----------------------------------------------------------------------
# Num: 1 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  # Set variables
  clear = lambda: os.system('cls')
  m, e, f = Menu(), Extraction(), FileManage()

  # Create directory if doesn't exist
  dataFolder = f.checkDirectory()
  HTMLFileNames = f.getHTMLFileNames(dataFolder)

  # Get the CSV file name
  clear()
  print("Input the name of the CSV file you want to create.")
  csv = m.getFileName()

  # Get the HTML file to extract data from
  clear()
  print("Select the index of the HTML file to extract data from.")
  htmlOpts = m.displayMenu(HTMLFileNames)
  selHTML = 'data/' + m.getNumUserInput(htmlOpts)

  # Select information to extract
  print("Select the index of the tag type you want to extract data from.")
  tagList = ['Paragraphs', 'Headings', 'Links', 'Img urls', 'All text (no links)', 'All links', 'All content']
  tagOpts = m.displayMenu(tagList)
  selTag = m.getNumUserInput(tagOpts)

  # Get contents of HTML and adds to CSV file
  e.getContent(selHTML, selTag, csv)

# Run main function
if __name__ == "__main__": main()