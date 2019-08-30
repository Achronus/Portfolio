#-----------------------------------------------------------------------
# File Title: Scraping Class
# File Description: Handles the web scraping functionality.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Scrap()
#    a. getUserInput()
#    b. getAllLinks()
#    c. createHTMLFiles()
#    d. googleLink()
#-----------------------------------------------------------------------
import re, os, time, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup

#-----------------------------------------------------------------------
# Num: 1 | Title: Scrap()
#-----------------------------------------------------------------------
class Scrap():
  """
  Handles the web scraping functionality.\n
  Functions: (3) getUserInput(), getAllLinks(), createHTMLFiles()
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
    print('Input the url you would like to scrape. Format of the url must contain the following:')
    print('   1. Protocol (http:// or https://)')
    print('   2. Website name')
    print('   3. Domain name (e.g. .com/, .co.uk/, .de/). Domain name MUST end with a /')
    print(" Format example: 'https://websitename.co.uk/' or 'https://subdomain.websitename.com/'")
    print('-----------------------------------------------------------------------------------------------------------------')

    # Set variables
    clear = lambda: os.system('cls')
    urlCheck = re.compile(r"^((?:https)|(?:http)\w*://)" + # protocol - e.g. http://, https://
                          r"(\w*[a-z0-9\-])" + # website name - e.g. website.example, example.
                          r"((?:.*[a-z]/))" # domain name - e.g. .com/, .co.uk/
                         )
    # Get input
    while True:
      ui = input('=> ').lower()

      # Check input is a valid url
      if not urlCheck.match(ui):
        print("Url invalid! Please check the formatting.")
      
      # Check if the website exists
      else:
        try:
          page = urlopen(ui)
          # Doesn't exist if status code != 200
          if page.getcode() != 200:
            print("Website does not exist!")
          # Website exists
          else:
            clear()
            # Convert page to readable format
            soup = BeautifulSoup(page, 'html.parser')

            # Get all links in page
            linkList = self.getAllLinks(soup, ui)

            # Scrape links HTML
            self.createHTMLFiles(linkList, ui)
            print('Scraping complete. Program will exit in 10 seconds.')
            time.sleep(10) # 10 seconds
            break
        
        # Output error if there is one
        except urllib.error.HTTPError as e:
          print(f"Website unable to scrape. Error: {e}")

  #-----------------------------------------------------------------------
  # Num: 1b | Title: getAllLinks()
  #-----------------------------------------------------------------------
  def getAllLinks(self, root, url):
    """
    Utility function for getUserInput() that gets all links within the root page.\n
    Parameters: (2) root page content, users url input
    """
    # set variables
    findAll = root.findAll('a', attrs={'href': re.compile("^https://")})
    linkList = set()
    limit = 20

    # Loop through page content
    for link in findAll:
      if url in str(link):
        linkList.add(link.get('href'))
        
        # If list is larger than limit
        if len(linkList) == limit:
          print('Page limit has been reached!')
          break
    print(f'Page limit: {limit} | Total pages found: {len(linkList)}')

    # Convert set to dict
    linkList = list(linkList)
    return linkList

  #-----------------------------------------------------------------------
  # Num: 1c | Title: createHTMLFiles()
  #-----------------------------------------------------------------------
  def createHTMLFiles(self, linkList, url):
    """
    Utility function for getUserInput() that creates HTML files based on the urls found.\n
    Parameters: (2) list of links, users url input
    """
    # Set variables
    valuesList, pageDir = [], 'pages'
    linkList.sort()

    # Create a list of values
    for link in linkList:
      # If its the root, append with the name homepage
      if link == url:
        valuesList.append('homepage')
      # Otherwise, only get the page name
      else:
        fileName = re.sub(url, '', link) # Removes url at front
        fileName = fileName[:-1] # Removes / at end
        valuesList.append(fileName.replace('/', '-')) # Replace any additional / with -

    # Create pages directory
    if not os.path.exists(pageDir):
      os.mkdir(pageDir)

    # Loop through each file
    for link in range(len(linkList)):
      # Set page variables
      page = urlopen(linkList[link])
      htmlPage = BeautifulSoup(page, 'html.parser')
      
      # Output to file
      with open('pages/' + valuesList[link] + '.html', 'w') as f:
        f.write(str(htmlPage.prettify()))
        print(f"New file has been created called '{valuesList[link]}'.")
    
    # Output instruction to user
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print("Please check the 'pages' folder.")
    print('----------------------------------------------------------------------------------------------------------------------------------')

  #-----------------------------------------------------------------------
  # Num: 1d | Title: googleLink()
  #-----------------------------------------------------------------------
  def googleLink(self, url):
    """
    Utility function for getUserInput() that handles the root links functionality if it's a google link.\n
    Parameters: () users url link
    """
    pass