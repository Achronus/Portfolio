#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program.
#-----------------------------------------------------------------------
import os
from utils.menu import Menu
from utils.extract import Extraction
from utils.files import FileManage

def main():
  """
  Consists of the main functionality of the script.
  """
  # Set variables
  clear = lambda: os.system('cls')
  m, e, f = Menu(), Extraction(), FileManage()

  # Create directory if doesn't exist
  data_folder = f.check_directory()
  html_filenames = f.get_html_filenames(data_folder)

  # Get the CSV file name
  clear()
  print("Input the name of the CSV file you want to create.")
  csv = m.get_filename()

  # Get the HTML file to extract data from
  clear()
  print("Select the index of the HTML file to extract data from.")
  html_opts = m.display_menu(html_filenames)
  sel_html = 'data/' + m.get_num_user_input(html_opts)

  # Select information to extract
  print("Select the index of the tag type you want to extract data from.")
  tag_list = ['Paragraphs', 'Headings', 'Links', 'Img urls', 'All text (no links)', 'All links', 'All content']
  tag_opts = m.display_menu(tag_list)
  sel_tag = m.get_num_user_input(tag_opts)

  # Get contents of HTML and adds to CSV file
  e.get_content(sel_html, sel_tag, csv)

# Run main function
if __name__ == "__main__": main()