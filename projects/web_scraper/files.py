#--------------------------------------------------------------------------
# File Title: FileManage Class
# File Description: Handles file management functionality.
#--------------------------------------------------------------------------
# CONTENTS:
# 1. FileManage()
#    a. createHTML()
#    b. pageSetup()
#--------------------------------------------------------------------------
import os, requests
from bs4 import BeautifulSoup, Comment

#-----------------------------------------------------------------------
# Num: 1 | Title: FileManage()
#-----------------------------------------------------------------------
class FileManage():
  """
  Handles file management functionality.\n
  Functions: (2) createHTML(), pageSetup()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: createHTML()
  #-----------------------------------------------------------------------
  def createHTML(self, pageDir, valuesList, page, htmlPage, link):
    """
    Creates the HTML files.\n
    Parameters: (5) page directory, values name list, page url, html page, loop index
    """
    # Check if page can be accessed
    if page.status_code != 200:
      print(f'Webpage cannot be scraped. Error: {page.status_code}')
    else:
      # Amend formatting
      p = str(htmlPage.encode()).replace("b'<", "<").replace("\\n", "").replace("</html>'", "</html>")
      page = BeautifulSoup(p, 'html.parser')

      # Put HTML into files
      with open(pageDir + '/' + valuesList[link] + '.html', 'w') as f:
        f.write(page.prettify())
        print(f"New file has been created called '{valuesList[link]}'.")
        f.close()

  #-----------------------------------------------------------------------
  # Num: 1b | Title: pageSetup()
  #-----------------------------------------------------------------------
  def pageSetup(self, linkList, link):
    """
    Setups the pages and removes all unneeded data.\n
    Parameters: (2) list list, link index
    """
    # Set page variables
    page = requests.get(linkList[link])
    htmlPage = BeautifulSoup(page.text, 'html.parser')

    # Remove unneeded elements
    comments = htmlPage.find_all(text=lambda text: isinstance(text, Comment))
    js = htmlPage.find_all('script')
    css = htmlPage.find_all('style')
    for comment in comments:
      comment.extract()
    for script in js:
      script.extract()
    for style in css:
      style.extract()

    return page, htmlPage