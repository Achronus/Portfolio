#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
# CONTENTS:
# 1. main()
#-----------------------------------------------------------------------
from scraping import Scrap

#-----------------------------------------------------------------------
# Num: 1 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  # Set variables
  s = Scrap()

  # Get the users input url as a html file
  s.getUserInput()

# Run main function
if __name__ == "__main__": main()