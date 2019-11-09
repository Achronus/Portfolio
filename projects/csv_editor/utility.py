#-----------------------------------------------------------------------
# File Title: Utility Class
# File Description: Contains utility functions for the Editor class.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Utility()
#    a. new_data()
#    b. field_length_check()
#    c. get_col_names()
#    d. get_rows_as_list()
#-----------------------------------------------------------------------
import pandas as pd
from menu import Menu

#-----------------------------------------------------------------------
# Num: 1 | Title: Utility()
#-----------------------------------------------------------------------
class Utility():
  """
  Manages the utility functions for the Editor class.\n
  Functions: (4) new_data(), field_length_check(), get_col_names(), get_rows_as_list()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: new_data()
  #-----------------------------------------------------------------------
  def new_data(self, new_col_name, dataset, column_names):
    """
    Used to get the column data for the addData() function.\n
    Parameters: (3) new column name, dataset, column names 
    """
    # Get new data to add to column
    print(f"The new column name is '{new_col_name}'. Input the data to add. Separate by ', ' for multiple items. E.g. '1, 2, 3'")
    new_data = input('=> ').split(', ')

    # Add data to file
    new_submission = pd.DataFrame({new_col_name : new_data}, columns=column_names)
    return dataset.append(new_submission, ignore_index=True, sort=True)

  #-----------------------------------------------------------------------
  # Num: 1b | Title: field_length_check()
  #-----------------------------------------------------------------------
  def field_length_check(self, custom_print, compare_field, item):
    """
    Used to check that the user inputs length is valid. Used in addData() and updateData().\n
    Parameters: (3) custom print statement, field to compare against, item selected
    """
    # Instructions to user
    print(custom_print)
    print(f"Total {item}s in file: {len(compare_field)}. Please enter {len(compare_field)} item(s).")

    # Loop through and check if invalid column size
    inv_len = True
    while inv_len:
      new_data = input('=> ').split(', ')
      if len(new_data) > len(compare_field):
        print(f"Too many items! There are {len(compare_field)} {item}(s). Please enter {len(compare_field)} item(s).")
        inv_len = True
      elif len(new_data) < len(compare_field):
        print(f"Not enough items! There are {len(compare_field)} {item}(s). Please enter {len(compare_field)} item(s).")
        inv_len = True
      else:
        inv_len = False

    return new_data

  #-----------------------------------------------------------------------
  # Num: 1c | Title: get_col_names()
  #-----------------------------------------------------------------------
  def get_col_names(self, custom_print, column_names):
    """
    Used to get the column names for multiple choices in the program. Used in addData(), removeData() and updateData().\n
    Parameters: (2) custom print statement, column names
    """
    m = Menu()
    options = m.option_list(column_names, custom_print)
    return m.single_user_input(options)

  #-----------------------------------------------------------------------
  # Num: 1d | Title: get_rows_as_list()
  #-----------------------------------------------------------------------
  def get_rows_as_list(self, dataset):
    """
    Used to get the csv files rows within a list format.\n
    Parameters: (1) dataset
    """
    row_list, row_idx = [], dataset.index.values
    for row in range(len(row_idx)):
      row_list.append(dataset.loc[row_idx[row], :].values)
    return row_list
    