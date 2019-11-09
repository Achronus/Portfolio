#-----------------------------------------------------------------------
# File Title: Extraction Class
# File Description: Extracts data from a directory of HTML files.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Extraction()
#    a. create_csv()
#    b. get_content()
#    c. content_loop()
#    d. set_column_length()
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
  Functions: (4) create_csv(), get_content(), content_loop(), set_column_length()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: create_csv()
  #-----------------------------------------------------------------------
  def create_csv(self, csv_name, data, headers):
    """
    Utility function for get_content(). Uses a pandas dataframe to output the data to a CSV file.\n
    Parameters: (3) CSV file name, data to add to file, list of headers
    """
    # Create dataframe
    df = pd.DataFrame(data, columns=headers)

    # Output to CSV file
    df.to_csv(csv_name, index=False, header=headers)
    print(f"File '{csv_name}' has been created and data has been successfully added.")
    print('Program will exit in 10 seconds.')
    time.sleep(10)

  #-----------------------------------------------------------------------
  # Num: 1b | Title: get_content()
  #-----------------------------------------------------------------------
  def get_content(self, html_path, option, csv_name):
    """
    Gets content within the selected HTML file based on the users selected option.\n
    Parameters: (3) selected HTML file path, users selected option, csv file name
    """
    # Get the HTML file as an object
    html_file = open(html_path)
    soup = BeautifulSoup(html_file, 'html.parser')
    html_file.close()
    
    # Perform different operations based on option selected
    #-------------------------------------------
    # Paragraphs
    #-------------------------------------------
    if option == 'Paragraphs':
      headers = ['Paragraphs']
      output = self.content_loop(soup, 'p')

    #-------------------------------------------
    # Headings
    #-------------------------------------------
    if option == 'Headings':
      headers = ['Headings']
      output = self.content_loop(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

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
      para = self.content_loop(soup, 'p')
      titles = self.content_loop(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

      # Resize data
      opt_list = [para, titles]
      output = self.set_column_length(opt_list)
    
    #-------------------------------------------
    # All Links
    #-------------------------------------------
    if option == 'All links':
      headers = ['Link Name', 'Link', 'Img Name', 'Url']
      links, link_names, img_names, urls = [], [], [], []
      # Loop through links and get the name + href
      for l in soup.find_all('a', href=True):
        link_names.append(l.contents[0].strip())
        links.append(l['href'])

      # Loop through images and the alt + src
      for img in soup.find_all('img', alt=True):
        img_names.append(img['alt'])
        urls.append(img['src'])

      # Resize data
      opt_list = [link_names, links, img_names, urls]
      output = self.set_column_length(opt_list)
    
    #-------------------------------------------
    # All Content
    #-------------------------------------------
    if option == 'All content':
      # Set headers
      headers = ['Paragraphs', 'Titles', 'Link Name', 'Link', 'Img Name', 'Url']
      links, link_names, img_names, urls = [], [], [], []

      # Get data
      para = self.content_loop(soup, 'p')
      titles = self.content_loop(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

      # Loop through links and get the name + href
      for l in soup.find_all('a', href=True):
        link_names.append(l.contents[0].strip())
        links.append(l['href'])

      # Loop through images and the alt + src
      for img in soup.find_all('img', alt=True):
        img_names.append(img['alt'])
        urls.append(img['src'])

      # Resize data
      opt_list = [para, titles, link_names, links, img_names, urls]
      output = self.set_column_length(opt_list)
      
    # Adds selected content to CSV file
    self.create_csv(csv_name, output, headers)

  #-----------------------------------------------------------------------
  # Num: 1c | Title: content_loop()
  #-----------------------------------------------------------------------
  def content_loop(self, soup, tag):
    """
    Utility function for get_content(). Gets all data based on tag provided. Returns a list.\n
    Parameters: (2) soup object of HTML file, tag to search for
    """
    text_list = []
    for item in range(len(soup.find_all(tag))):
      text = soup.find_all(tag)[item].contents[0].strip()
      text_list.append(text)

    # Remove empty list items
    text_list = list(filter(None, text_list))
    return text_list

  #-----------------------------------------------------------------------
  # Num: 1d | Title: set_column_length()
  #-----------------------------------------------------------------------
  def set_column_length(self, opt_list):
    """
    Utility function for get_content(). This adds any empty spaces needed to a list to create the correct column length.\n
    Parameters: (1) list of option variables
    """
    size, output = [], []

    # Find largest column
    for opt in opt_list:
      size.append(len(opt))

    # set column length
    col_len = max(size)

    # Add empty space until column length is correct
    for option in opt_list:
      while len(option) != col_len:
        option.append('')

    # Add data to tuple
    for item in range(col_len):
      row = [] # reset row each loop
      for opt in opt_list:
        row.append(opt[item]) # store items in row
      output.append(tuple(row)) # convert row to tuple and add to list
    return output
    