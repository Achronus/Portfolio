#-----------------------------------------------------------------------
# File Title: Extraction Class
# File Description: Extracts data from a directory of HTML files.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Extraction()
#    a. createCSV()
#    b. getContent()
#    c. contentLoop()
#    d. setColumnLength()
#-----------------------------------------------------------------------
import re, time
from bs4 import BeautifulSoup
import pandas as pd

#-----------------------------------------------------------------------
# Num: 1 | Title: Extraction()
#-----------------------------------------------------------------------
class Extraction():
  """
  Used to extract data from a directory of HTML files based on users input.\n
  Functions: (4) createCSV(), getContent(), contentLoop(), setColumnLength()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: createCSV()
  #-----------------------------------------------------------------------
  def createCSV(self, csvName, data, headers):
    """
    Utility function for getContent(). Uses a pandas dataframe to output the data to a CSV file.\n
    Parameters: (3) CSV file name, data to add to file, list of headers
    """
    # Create dataframe
    df = pd.DataFrame(data, columns=headers)

    # Output to CSV file
    df.to_csv(csvName, index=False, header=headers)
    print(f"File '{csvName}' has been created and data has been successfully added.")
    print('Program will exit in 10 seconds.')
    time.sleep(10)

  #-----------------------------------------------------------------------
  # Num: 1b | Title: getContent()
  #-----------------------------------------------------------------------
  def getContent(self, htmlPath, option, csvName):
    """
    Gets content within the selected HTML file based on the users selected option.\n
    Parameters: (3) selected HTML file path, users selected option, csv file name
    """
    # Get the HTML file as an object
    htmlFile = open(htmlPath)
    soup = BeautifulSoup(htmlFile, 'html.parser')
    htmlFile.close()
    
    # Perform different operations based on option selected
    #-------------------------------------------
    # Paragraphs
    #-------------------------------------------
    if option == 'Paragraphs':
      headers = ['Paragraphs']
      output = self.contentLoop(soup, 'p')

    #-------------------------------------------
    # Headings
    #-------------------------------------------
    if option == 'Headings':
      headers = ['Headings']
      output = self.contentLoop(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    #-------------------------------------------
    # Links
    #-------------------------------------------
    if option == 'Links':
      headers, output = ['Link Name', 'Link'], []
      # Loop through links and get the name + href
      for l in soup.find_all('a', href=True):
        link = l.contents[0].strip(), l['href']
        output.append(link)

    #-------------------------------------------
    # Img Urls
    #-------------------------------------------
    if option == 'Img urls':
      headers, output = ['Img Name', 'Url'], []
      # Loop through images and the alt + src
      for img in soup.find_all('img', alt=True):
        item = img['alt'], img['src']
        output.append(item)

    #-------------------------------------------
    # All text (no links)
    #-------------------------------------------
    if option == 'All text (no links)':
      # Set headers
      headers = ['Paragraphs', 'Titles']
      
      # Get data
      para = self.contentLoop(soup, 'p')
      titles = self.contentLoop(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

      # Resize data
      optList = [para, titles]
      output = self.setColumnLength(optList)
    
    #-------------------------------------------
    # All Links
    #-------------------------------------------
    if option == 'All links':
      headers = ['Link Name', 'Link', 'Img Name', 'Url']
      links, linkNames, imgNames, urls = [], [], [], []
      # Loop through links and get the name + href
      for l in soup.find_all('a', href=True):
        linkNames.append(l.contents[0].strip())
        links.append(l['href'])

      # Loop through images and the alt + src
      for img in soup.find_all('img', alt=True):
        imgNames.append(img['alt'])
        urls.append(img['src'])

      # Resize data
      optList = [linkNames, links, imgNames, urls]
      output = self.setColumnLength(optList)
    
    #-------------------------------------------
    # All Content
    #-------------------------------------------
    if option == 'All content':
      # Set headers
      headers = ['Paragraphs', 'Titles', 'Link Name', 'Link', 'Img Name', 'Url']
      links, linkNames, imgNames, urls = [], [], [], []

      # Get data
      para = self.contentLoop(soup, 'p')
      titles = self.contentLoop(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

      # Loop through links and get the name + href
      for l in soup.find_all('a', href=True):
        linkNames.append(l.contents[0].strip())
        links.append(l['href'])

      # Loop through images and the alt + src
      for img in soup.find_all('img', alt=True):
        imgNames.append(img['alt'])
        urls.append(img['src'])

      # Resize data
      optList = [para, titles, linkNames, links, imgNames, urls]
      output = self.setColumnLength(optList)
      
    # Adds selected content to CSV file
    self.createCSV(csvName, output, headers)

  #-----------------------------------------------------------------------
  # Num: 1c | Title: contentLoop()
  #-----------------------------------------------------------------------
  def contentLoop(self, soup, tag):
    """
    Utility function for getContent(). Gets all data based on tag provided. Returns a list.\n
    Parameters: (2) soup object of HTML file, tag to search for
    """
    textList = []
    for item in range(len(soup.find_all(tag))):
      text = soup.find_all(tag)[item].contents[0].strip()
      textList.append(text)

    # Remove empty list items
    textList = list(filter(None, textList))
    return textList

  #-----------------------------------------------------------------------
  # Num: 1d | Title: setColumnLength()
  #-----------------------------------------------------------------------
  def setColumnLength(self, optList):
    """
    Utility function for getContent(). This adds any empty spaces needed to a list to create the correct column length.\n
    Parameters: (1) list of option variables
    """
    size, output = [], []

    # Find largest column
    for opt in optList:
      size.append(len(opt))

    # set column length
    colLength = max(size)

    # Add empty space until column length is correct
    for option in optList:
      while len(option) != colLength:
        option.append('')

    # Add data to tuple
    for item in range(colLength):
      row = [] # reset row each loop
      for opt in optList:
        row.append(opt[item]) # store items in row
      output.append(tuple(row)) # convert row to tuple and add to list
    return output
    