#-----------------------------------------------------------------------
# File Title: Editor Class
# File Description: Used to add or remove data to and from a CSV file.
#-----------------------------------------------------------------------
import os, csv
import numpy as np
import pandas as pd
from menu import Menu
from utility import Utility

#-----------------------------------------------------------------------
# Num: 1 | Title: Editor()
#-----------------------------------------------------------------------
class Editor():
  """
  Manages the editor functionality.\n 
  Consists of 6 functions: display_data(), create_file(), select_data(), add_data(), remove_data(), update_data().
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: display_data()
  #-----------------------------------------------------------------------
  def display_data(self, filename):
    """
    Takes a filename as input and outputs its data into the console.\n
    Parameters: (1) Filename.
    """
    try:
      print("--------------------------------------------------------------------------------------------------")
      print("Data in file:")
      print("--------------------------------------------------------------------------------------------------")
      print(pd.read_csv(filename))
    except pd.errors.EmptyDataError:
      print('File is empty!')
    except FileNotFoundError:
      print("This file doesn't exist. You must create it first!")

  #-----------------------------------------------------------------------
  # Num: 1b | Title: create_file()
  #-----------------------------------------------------------------------
  def create_file(self, filename):
    """
    Used to create files that do not exist.\n
    Parameters: (1) Filename.
    """
    if os.path.exists(filename):
      print(f"File with the name '{filename}' already exists!")
    else:
      open(filename, 'w')
      print(f"File with the name '{filename}' has been created.")

  #-----------------------------------------------------------------------
  # Num: 1c | Title: select_data()
  #-----------------------------------------------------------------------
  def select_data(self, filename, option_list):
    """
    Used to select the data to add, remove or update from the selected CSV file.\n
    Parameters: (2) file name, option list.
    """
    # set variables
    m = Menu()
    print_output = 'What information would you like to select?'

    # Get inital options
    options = m.option_list(option_list, print_output)
    choice = m.single_user_input(options)
    return choice

  #-----------------------------------------------------------------------
  # Num: 1d | Title: add_data()
  #-----------------------------------------------------------------------
  def add_data(self, filename):
    """
    Adds data to the file via users input.\n
    Parameters: (1) Filename.
    """
    # Set variables
    u = Utility()
    df = pd.read_csv(filename)
    df.to_csv(filename + '.bak', index=False) # Create file backup

    header = list(df.columns)
    options_list = ['New column', 'Existing column', 'New row']

    # Select the data
    choice = self.select_data(filename, options_list)

    #-------------------------
    # If new column
    #-------------------------
    if choice == options_list[0]:
      # Get column name
      print(f"You selected '{choice}'. Input the name of the column to add.")
      new_col_name = input('=> ')
      header.append(new_col_name)

      # Get new data and add to dataset
      df = u.new_data(new_col_name, df, header)

    #-------------------------
    # If existing column
    #-------------------------
    if choice == options_list[1]:
      # Get column name
      col_print = f"You selected '{choice}'. Input the column index you want to add data to."
      selected_header = u.get_col_names(col_print, header)

      # Get new data and add to dataset
      df = u.new_data(selected_header, df, header)

    #-------------------------
    # If new row
    #-------------------------
    if choice == options_list[2]:

      # Get users input
      opt_two_print = f"You selected '{choice}'. Input the data to add. Separate by ', ' for next column. E.g. '1, 2, 3'"
      new_row_data = u.field_length_check(opt_two_print, header, 'column')
      
      # Add data to file
      new_row_submission = pd.DataFrame([new_row_data], columns=header)
      df = df.append(new_row_submission, ignore_index=True)

    # Add the data to the CSV file
    df.to_csv(filename, index=False)
      
    # Display updated file
    self.display_data(filename)

  #-----------------------------------------------------------------------
  # Num: 1e | Title: remove_data()
  #-----------------------------------------------------------------------
  def remove_data(self, filename):
    """
    Removes data from the file via users input.\n
    Parameters: (1) Filename.
    """
    # Set variables
    m, u = Menu(), Utility()
    df = pd.read_csv(filename)
    df.to_csv(filename + '.bak', index=False) # Create file backup

    header = list(df.columns)
    options_list = ['Whole column', 'Column data', 'Specific row']
    
    # Select the data
    choice = self.select_data(filename, options_list)

    #-------------------------
    # If whole column
    #-------------------------
    if choice == options_list[0]:
      # Get column name
      col_print = f"You selected '{choice}'. Input the column index for the column you want to remove."
      selected_col = u.get_col_names(col_print, header)

      # Remove column
      df = df.drop(columns=selected_col)
    
    #-------------------------
    # If column data
    #-------------------------
    if choice == options_list[1]:
      # Get column name
      col_print = f"You selected '{choice}'. Input the column index for the column data you want to remove."
      selected_col = u.get_col_names(col_print, header)

      # Get column data
      col_data_print = f"You selected the column '{selected_col}'. Input the indexes for the data to remove. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      col_idx = header.index(selected_col)
      col_data_options = m.option_list(df.loc[:, header[col_idx]].values, col_data_print)
      selected_col_data = m.multi_user_input(col_data_options)

      # Remove selected data
      df = df.replace(selected_col_data, '')

    #-------------------------
    # If specific row
    #-------------------------
    if choice == options_list[2]:
      # Get each row in the file as a list
      row_list = u.get_rows_as_list(df)
      
      # Get rows
      row_print = f"You selected '{choice}'. Input the indexes for the rows you want to remove. Separate by a ', ' for multiple rows. E.g. '1, 2, 3'"
      row_options = m.option_list(row_list, row_print)
      selected_rows = m.get_row_user_input(row_options)
            
      # Remove selected data
      df = df.drop(selected_rows)

    # Add the data to the CSV file
    df.to_csv(filename, index=False)
      
    # Display updated file
    self.display_data(filename)

  #-----------------------------------------------------------------------
  # Num: 1f | Title: update_data()
  #-----------------------------------------------------------------------
  def update_data(self, filename):
    """
    Updates data within the file via users input.\n
    Parameters: (1) Filename.
    """
    # Set variables
    m, u = Menu(), Utility()
    df = pd.read_csv(filename)
    df.to_csv(filename + '.bak', index=False) # Create file backup

    header = list(df.columns)
    options_list = ['Column name', 'Column data', 'Specific row']

    # Select the data
    choice = self.select_data(filename, options_list)

    #-------------------------
    # If column name
    #-------------------------
    if choice == options_list[0]:
      # Select column names
      header_print = f"You selected '{choice}'. Input the column indexes for the column names you want to update. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      header_options = m.option_list(header, header_print)
      selected_headers = m.multi_user_input(header_options)

      # Get new column names 
      opt_zero_print = f"You selected the column names '{selected_headers}'. Input the new names for the columns. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      new_col_names = u.field_length_check(opt_zero_print, selected_headers, 'selected column')
      
      # Update data
      for item in range(len(selected_headers)):
        df = df.rename(columns={selected_headers[item] : new_col_names[item]})

    #-------------------------
    # If column data
    #-------------------------
    if choice == options_list[1]:
      # Select column name
      col_print = f"You selected '{choice}'. Input the column index for the column you want to update."
      selected_col = u.get_col_names(col_print, header)

      # Select column data
      sel_col_print = f"You selected the column '{selected_col}'. Input the column indexes for the data to update. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      col_idx = header.index(selected_col)
      col_data_options = m.option_list(df.loc[:, header[col_idx]].values, sel_col_print)
      selected_col_data = m.multi_user_input(col_data_options)

      # Select new column data names
      opt_one_print = f"You selected the column data '{selected_col_data}'. Input the new names for the column data. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      new_col_names = u.field_length_check(opt_one_print, selected_col_data, 'selected column data field')

      # Update data
      df.replace(to_replace=selected_col_data, value=new_col_names, inplace=True)

    #-------------------------
    # If specific row
    #-------------------------
    if choice == options_list[2]:
      # Get each row in the file as a list
      row_list = u.get_rows_as_list(df)
      
      # Select rows
      row_print = f"You selected '{choice}'. Input the index for the row you want to update."
      row_options = m.option_list(row_list, row_print)
      selected_row = m.get_row_user_input(row_options)
      selected_row_idx = selected_row[0]
      sel_row_list = row_options[selected_row_idx + 1]

      # Select names in row
      sel_row_print = f"You selected '{sel_row_list}'. Input the indexes for the fields in the row you want to update. Separate by a ', ' for multiple fields. E.g. '1, 2, 3'"
      sel_row_items = []
      for item in range(len(sel_row_list)):
        sel_row_items.append(sel_row_list[item])
      sel_row_options = m.option_list(sel_row_items, sel_row_print)
      sel_field_names = m.multi_user_input(sel_row_options)

      # Select new names
      opt_two_print = f"You selected the row fields '{sel_field_names}'. Input the new names for the fields. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      new_row_names = u.field_length_check(opt_two_print, sel_field_names, 'selected row field')

      # Update data
      df.replace(to_replace=sel_field_names, value=new_row_names, inplace=True)

    # Add the data to the CSV file
    df.to_csv(filename, index=False)
      
    # Display updated file
    self.display_data(filename)