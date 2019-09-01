#-----------------------------------------------------------------------
# File Title: Scraping Class
# File Description: Handles the web scraping functionality.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Scrap()
#    a. getUserInput()
#    b. getAllLinks()
#    c. sortData()
#-----------------------------------------------------------------------
import re, os, time, urllib.error, requests, shutil
from bs4 import BeautifulSoup
from gsearch import GSearch
from files import FileManage

#-----------------------------------------------------------------------
# Num: 1 | Title: Scrap()
#-----------------------------------------------------------------------
class Scrap():
  """
  Handles the web scraping functionality.\n
  Functions: (3) getUserInput(), getAllLinks(), sortData()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: getUserInput()
  #-----------------------------------------------------------------------
  def getUserInput(self):
    """
    Used to get the users url input. Returns the url if correct.
    """
    # Instructions for user
    print('-----------------------------------------------------------------------------------------------------------------')
    print('Input the url you would like to scrape. Format of the url must consist of the following:')
    print('   1. Protocol (http:// or https://)')
    print('   2. Website name')
    print('   3. Domain name (e.g. .com/, .co.uk/, .de/). Domain name MUST end with a /')
    print(" Format example: 'https://websitename.co.uk/' or 'https://subdomain.websitename.com/'")
    print('-----------------------------------------------------------------------------------------------------------------')
    print("Alternatively: input a search query to search Google! E.g. 'StackOverflow' or 'I'm not sure what to search'")
    print('-----------------------------------------------------------------------------------------------------------------')

    # Set variables
    gs = GSearch()
    clear = lambda: os.system('cls')
    urlCheck = re.compile(r"^((?:https)|(?:http)\w*://)" + # protocol - e.g. http://, https://
                          r"(\w*[a-z0-9\-])" + # website name - e.g. website.example, example.
                          r"((?:.*[a-z]/))" # domain name - e.g. .com/, .co.uk/
                         )
    # Get input
    while True:
      ui = input('=> ').lower()

      #---------------------------------------
      # Check input is a url
      #---------------------------------------
      if 'http' in ui:
        if not urlCheck.match(ui):
          print("Url invalid! Please check the formatting.")
        
        # Valid url
        else:
          # Set variables
          try:
            page = requests.get(ui)
            soup = BeautifulSoup(page.text, 'html.parser') # Convert page to readable format
            clear()

            # Get all links in page
            linkList = self.getAllLinks(soup, ui)

            # Scrape links data to HTML files
            pageDir = 'pages'
            self.sortData(linkList, ui, pageDir)
            print('Scraping complete. Program will exit in 10 seconds.')
            time.sleep(10) # 10 seconds
            break

          # Output error if there is one
          except requests.exceptions.RequestException as e:
            print(f"Unable to scrape website. Error: {e}")
            print("Please try a different URL or Google search query.")

      #---------------------------------------
      # Otherwise its a google search query
      #---------------------------------------
      else:
        clear()

        # Get all links
        linkList = gs.googleLink(ui)
        valueList = gs.getLinkNames(linkList)

        # Scrape links data to HTML files
        pageDir = 'search-results'
        gs.gSortData(linkList, valueList, pageDir)
        print('Scraping complete. Program will exit in 10 seconds.')
        time.sleep(10) # 10 seconds
        break

  #-----------------------------------------------------------------------
  # Num: 1b | Title: getAllLinks()
  #-----------------------------------------------------------------------
  def getAllLinks(self, root, url):
    """
    Utility function for getUserInput() that gets all links within the root page.\n
    Parameters: (2) root page content, users url input
    """
    # Set variables
    findAll = root.findAll('a', attrs={'href': re.compile("^https://")})
    linkList = set()
    limit = 10

    # Loop through page content
    for link in findAll:
      if url in str(link):
        linkList.add(link.get('href'))
        
        # If list is larger than limit
        if len(linkList) == limit:
          print('Page limit has been reached!')
          break
    
    # Display page total
    print(f'Page limit: {limit} | Total pages found: {len(linkList)}')

    # Convert set to dict
    linkList = list(linkList)
    return linkList

  #-----------------------------------------------------------------------
  # Num: 1c | Title: sortData()
  #-----------------------------------------------------------------------
  def sortData(self, linkList, url, pageDir):
    """
    Utility function for getUserInput() that sorts the data and creates HTML files based on the urls found.\n
    Parameters: (3) list of links, users url input, page directory
    """
    # Set variables
    f = FileManage()
    valuesList = []
    linkList.sort() # Sort list in order

    # Create a list of values
    for link in linkList:
      # If its the root, append with unique name
      if link == url:
        valuesList.append('root-page')
      # Otherwise, only get the page name
      else:
        fileName = re.sub(url, '', link) # Removes root url at front
        fileName = fileName[:-1] # Removes / at end
        valuesList.append(fileName.replace('/', '-')) # Replace any additional / with -

    # If directory exists, remove old one + files and recreate
    if os.path.exists(pageDir):
      shutil.rmtree(pageDir)
      os.mkdir(pageDir)
    
    # Create directory if doesn't exists
    if not os.path.exists(pageDir):
      os.mkdir(pageDir)

    # Loop through each file
    for link in range(len(linkList)):
      # Setup page
      page, htmlPage = f.pageSetup(linkList, link)
      
      # Output to file
      f.createHTML(pageDir, valuesList, page, htmlPage, link)
    
    # Output instruction to user
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print(f"Results for '{url}' completed. Please check the '{pageDir}' folder.")
    print('----------------------------------------------------------------------------------------------------------------------------------')