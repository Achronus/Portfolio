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
#-----------------------------------------------------------------------
import os, csv
from shutil import copyfile

#-----------------------------------------------------------------------
# Num: 1 | Title: read_csv() 
#-----------------------------------------------------------------------
def read_csv(currentdir):
  """
  Used to read the csv file 'text.csv' to get the data.\n
  Parameters: (1) Current directory.\n
  CSV Order: (7) Company, issue, link, heading 1, paragraph 1, heading 2 & paragraph 2.
  """
  # Get csv file
  csv_file = currentdir + '\\text.csv'

  # Put csv data into list of lists
  with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter='|')
    data = list(reader)
  
  # Remove headings
  data.pop(0)
  return data

#-----------------------------------------------------------------------
# Num: 2 | Title: read_html()
#-----------------------------------------------------------------------
def read_html(directory, html_list, index):
  """
  Used to read the HTML email creatives.\n
  Parameters: (3) Directory, html list & index value.
  """
  # Read and output copied file
  filepath = directory + html_list[index]
  f = open(filepath, 'r')
  return f.read()

#-----------------------------------------------------------------------
# Num: 3 | Title: replace_html()
#-----------------------------------------------------------------------
def replace_html(html_file, destination, issueNum, link, headOne, paraOne, 
                headTwo, paraTwo, issueName, monthFormat):
  """
  Used to replace the HTML within each email creative.\n
  Parameters: (10) Html file, destination, issue number, url link, paragraphs 1 & 2, headings 1 & 2, issue name, img reformat.
  """
  # Variables for replace statements - easier readability
  issueReplace = '<td class="issue issue-number">Issue ' + issueNum + '</td>'
  linkReplace = ' class="issue-link" href="' + link + '">'
  headOneReplace = '<h1 class="heading-1">' + headOne
  headTwoReplace = '<h1 class="heading-2">' + headTwo
  paraOneReplace = '<p class="paragraph-1">' + paraOne
  paraTwoReplace = '<p class="paragraph-2">' + paraTwo
  imgReformat = '/2019/jun/' + issueName + '/'

  # Replace HTML elements
  with open(destination, 'w') as f:
    f.write(html_file.replace('<td class="issue issue-number"></td>', issueReplace)
            .replace(' class="issue-link" href="">', linkReplace)
            .replace('<h1 class="heading-1">', headOneReplace)
            .replace('<h1 class="heading-2">', headTwoReplace)
            .replace('<p class="paragraph-1">', paraOneReplace)
            .replace('<p class="paragraph-2">', paraTwoReplace)
            .replace(imgReformat, monthFormat))
  f.close()

#---------------------------------------------------------------------
# Num: 4 | Title: main()
#---------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  # Get variables from user input
  year, month = input('Enter the year (4 digits) & month (3 characters), separated by a space: ').lower().split()
  print('-----------------------------------------------------------------------------------')

  # Get filepath locations
  dirpath = os.getcwd()
  currentdir = dirpath
  htmldir = currentdir + '\\templates\\'
  newdir = currentdir + '\\updated\\'

  # Read CSV file
  data = read_csv(currentdir)

  # Get file names from CSV file
  html_list = []
  for item in data:
    html_list.append(item[0])
 
  # Create copies of HTML files, rename them and replace content
  count = 0
  for item, html_item in zip(data, html_list):
    # Check that file names are the same
    if item[0] == html_item:
      # Update filename
      filename = html_item + '-issue' + item[1] + '.html'

      # Copy file to new location
      src, dst = htmldir + html_item + '.html', newdir + filename
      copyfile(src, dst)

      # create monthFormat variable
      month_format = '/' + year + '/' + month + '/' + item[0] + '/issue' + item[1] + '/'
      
      # Read HTML files
      new_html_list = os.listdir(newdir)
      file_contents = read_html(newdir, new_html_list, count)
      count += 1

      # Replace HTML content
      replace_html(file_contents, dst, item[1], item[2], 
                  item[3], item[4], item[5],
                item[6], item[0], month_format)
  
      # Return file name to console
      print(f'File {filename} created and updated.')

  # Output completion message to console
  print('----------------------------------------------------------------------')
  print("Files finished copying and updating, please check 'updated' folder.")
  print('----------------------------------------------------------------------')

# Run main function
if __name__ == '__main__': main()