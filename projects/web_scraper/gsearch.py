#--------------------------------------------------------------------------
# File Title: GSearch Class
# File Description: Handles the scraping functionality for Google queries.
#--------------------------------------------------------------------------
# CONTENTS:
# 1. GSearch()
#    a. googleLink()
#    b. getLinkNames()
#    c. gSortData()
#--------------------------------------------------------------------------
import re, os, time, urllib.error, requests, shutil
from googleapiclient.discovery import build
from files import FileManage

#-----------------------------------------------------------------------
# Num: 1 | Title: GSearch()
#-----------------------------------------------------------------------
class GSearch():
  """
  Handles the searching and web scraping functionality for Google queries.\n
  Functions: (3) googleLink(), getLinkNames(), gSortData()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: googleLink()
  #-----------------------------------------------------------------------
  def googleLink(self, searchTerm):
    """
    Function that takes a google search query, get's the webpages results and scrapes those page links. Uses Google's search API.\n
    Parameters: (1) takes in user search result
    """
    # Set variables
    APIKey = 'Your_API_Key'
    CSEID = 'Custom_Search_Engine_ID'

    # Create search 
    print(f"Finding first 10 pages for search query: '{searchTerm}'")
    search = build("customsearch", "v1", developerKey=APIKey)
    result = search.cse().list(q=searchTerm, cx=CSEID).execute() # pylint: disable=maybe-no-member

    # Get item results
    fTen = result['items'] # First 10
    linkList = [fTen[item]['link'] for item in range(len(fTen))]
    print(f'Total links found: {len(linkList)}')
    return linkList
  
  #-----------------------------------------------------------------------
  # Num: 1b | Title: getLinkNames()
  #-----------------------------------------------------------------------
  def getLinkNames(self, linkList):
    """
    Function that gets all the Google search page results link names as a list.\n
    Parameters: (1) Google search page link list 
    """
    # Set variables
    valueList = []
    for item in range(len(linkList)):
      valueList.append(f'result-{item+1}')
    return valueList

  #-----------------------------------------------------------------------
  # Num: 1c | Title: gSortData()
  #-----------------------------------------------------------------------
  def gSortData(self, linkList, valuesList, pageDir):
    """
    Function that sorts the Google data and creates HTML files based on the urls found within the Google search query.\n
    Parameters: (3) list of links, list of HTML page names, page directory
    """
    f = FileManage()

    # If directory exists, remove old one + files and recreate
    if os.path.exists(pageDir):
      shutil.rmtree(pageDir)
      os.mkdir(pageDir)
    
    # Create directory if doesn't exists
    if not os.path.exists(pageDir):
      os.mkdir(pageDir)

    # Loop through each file
    for link in range(len(linkList)):
      try:
        # Setup page
        page, htmlPage = f.pageSetup(linkList, link)

        # Create and add reference tag to file
        referenceTag = htmlPage.new_tag('meta')
        referenceTag.attrs['name'] = 'google-search ' + valuesList[link]
        referenceTag.attrs['content'] = linkList[link]
        htmlPage.head.insert(1, referenceTag)

        # Output to file
        f.createHTML(pageDir, valuesList, page, htmlPage, link)
      
      # Ignore errors
      except (UnicodeEncodeError, requests.exceptions.RequestException) as e:
        print(f'Page cannot be scraped. Error: {e}')
        pass
    
    # Output instructions to user
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print("A reference tag has been added to each HTMLs 'head' section. Look for the meta tag with 'google-search' to locate it.")
    print(f"Please check the '{pageDir}' folder.")
    print('----------------------------------------------------------------------------------------------------------------------------------')