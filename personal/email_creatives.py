#-----------------------------------------------------------------------
# File Title: Email Creative Updater
# File Description: This script is used to automate updating email ...
# ... creatives by reading a CSV files data and inputting it into ...
# ... the correct locations within the HTML file. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. readCSV()
# 2. readHTML()
# 3. replaceHTML()
# 4. main()
#    - Contains month variable which must be amended each month
#-----------------------------------------------------------------------
import os, csv
from shutil import copyfile

#-----------------------------------------------------------------------
# Num: 1
# Function Title: readCSV()
# Description: Used to read the csv file 'text.csv' to get the data.
# Parameters: (1) Current directory.
# CSV Order: (7) Company, issue, link, heading 1, paragraph 1, ... 
# ... heading 2, paragraph 2.
#-----------------------------------------------------------------------
def readCSV(currentdir):
  # Get csv file
  csvFile = currentdir + '\\text.csv'

  # Put csv data into list of lists
  with open(csvFile, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
  
  # Remove headings
  data.pop(0)
  return data

#-----------------------------------------------------------------------
# Num: 2
# Function Title: readHTML()
# Description: Used to read the HTML email creatives.
# Parameters: (3) Directory, html list, index value.
#-----------------------------------------------------------------------
def readHTML(directory, htmlList, index):
  # Read and output copied file
  filepath = directory + htmlList[index]
  f = open(filepath, 'r')
  return f.read()

#-----------------------------------------------------------------------
# Num: 3
# Function Title: replaceHTML()
# Description: Used to replace the HTML within each email creative.
# Parameters: (10) Html file, destination, issue number, url link, ...
# ... paragraphs 1 & 2, headings 1 & 2, issue name, img reformat.
#-----------------------------------------------------------------------
def replaceHTML(htmlFile, destination, issueNum, link, headOne, paraOne, 
                headTwo, paraTwo, issueName, monthFormat):
  # Variables for replace statements - easier readability
  issueReplace = '<td class="issue issue-number">Issue ' + issueNum + '</td>'
  linkReplace = '<a class="issue-link" href="' + link + '">'
  headOneReplace = '<h1 class="heading-1">' + headOne
  headTwoReplace = '<h1 class="heading-2">' + headTwo
  paraOneReplace = '<p class="paragraph-1">' + paraOne
  paraTwoReplace = '<p class="paragraph-2">' + paraTwo
  imgReformat = '/2019/jun/' + issueName + '/'

  # Replace HTML elements
  with open(destination, 'w') as f:
    f.write(htmlFile.replace('<td class="issue issue-number"></td>', issueReplace)
            .replace('<a class="issue-link" href="">', linkReplace)
            .replace('<h1 class="heading-1">', headOneReplace)
            .replace('<h1 class="heading-2">', headTwoReplace)
            .replace('<p class="paragraph-1">', paraOneReplace)
            .replace('<p class="paragraph-2">', paraTwoReplace)
            .replace(imgReformat, monthFormat))
  f.close()

#---------------------------------------------------------------------
# Num: 4
# Function Title: main()
# Description: Consists of the main functionality of the script.
# Parameters: (0) None.
#---------------------------------------------------------------------
def main():
  # Month variable (changes each month) - must be 3 characters
  month = 'jun'

  # Get filepath locations
  dirpath = os.getcwd()
  currentdir = dirpath + '\\scripts\\'
  htmldir = currentdir + '\\templates\\'
  newdir = currentdir + '\\updated\\'

  # Get file names inside template folder
  htmlList = os.listdir(htmldir)

  # Remove .html from file names
  upHtmlList = []
  for i in range(len(htmlList)):
    upHtmlList.append(htmlList[i].replace('.html', ''))
  
  # Read CSV file
  data = readCSV(currentdir)

  # Create copies of HTML files, rename them and replace content
  for item in range(len(data)):
      for index in range(item, len(data)):
        try:
          # Check that file names are the same
          if data[index][0] in upHtmlList[item]:
            # Update filename
            fileName = upHtmlList[item] + '-issue' + data[index][1] + '.html'

            # Copy file to new location
            src, dst = htmldir + upHtmlList[item] + '.html', newdir + fileName
            copyfile(src, dst)

            # create monthFormat variable
            monthFormat = '/2019/' + month + '/' + data[index][0] + '/issue' + data[index][1] + '/'
            
            # Read HTML files
            newHtmlList = os.listdir(newdir)
            fileContents = readHTML(newdir, newHtmlList, item)

            # Replace HTML content
            replaceHTML(fileContents, dst, data[index][1], data[index][2], 
                        data[index][3], data[index][4], data[index][5], 
                        data[index][6], data[index][0], monthFormat)
        
        # Error handle to say completed
        except IndexError:
          print('Files finished copying and updating, please check updated folder.')

# Run main function
if __name__ == '__main__': main()