#-----------------------------------------------------------------------
# File Title: Utility Class
# File Description: Contains utility functions for the Editor class.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Utility()
#    a. newColData()
#    b. fieldLengthCheck()
#    c. getColNames()
#    d. getRowsAsList()
#-----------------------------------------------------------------------
import pandas as pd
from menu import Menu

#-----------------------------------------------------------------------
# Num: 1 | Title: Utility()
#-----------------------------------------------------------------------
class Utility():
  """
  Manages the utility functions for the Editor class.\n
  Functions: (4) newColData(), fieldLengthCheck(), getColNames(), getRowsAsList()
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: newColData()
  #-----------------------------------------------------------------------
  def newColData(self, newColName, dataset, columnNames):
    """
    Used to get the column data for the addData() function.\n
    Parameters: (3) new column name, dataset, column names 
    """
    # Get new data to add to column
    print(f"The new column name is '{newColName}'. Input the data to add. Separate by ', ' for multiple items. E.g. '1, 2, 3'")
    newColData = input('=> ').split(', ')

    # Add data to file
    newSubmission = pd.DataFrame({newColName : newColData}, columns=columnNames)
    return dataset.append(newSubmission, ignore_index=True, sort=True)

  #-----------------------------------------------------------------------
  # Num: 1b | Title: fieldLengthCheck()
  #-----------------------------------------------------------------------
  def fieldLengthCheck(self, customPrint, compareField, item):
    """
    Used to check that the user inputs length is valid. Used in addData() and updateData().\n
    Parameters: (3) custom print statement, field to compare against, item selected
    """
    # Instructions to user
    print(customPrint)
    print(f"Total {item}s in file: {len(compareField)}. Please enter {len(compareField)} item(s).")

    # Loop through and check if invalid column size
    invalidLen = True
    while invalidLen:
      newData = input('=> ').split(', ')
      if len(newData) > len(compareField):
        print(f"Too many items! There are {len(compareField)} {item}(s). Please enter {len(compareField)} item(s).")
        invalidLen = True
      elif len(newData) < len(compareField):
        print(f"Not enough items! There are {len(compareField)} {item}(s). Please enter {len(compareField)} item(s).")
        invalidLen = True
      else:
        invalidLen = False

    return newData

  #-----------------------------------------------------------------------
  # Num: 1c | Title: getColNames()
  #-----------------------------------------------------------------------
  def getColNames(self, customPrint, columnNames):
    """
    Used to get the column names for multiple choices in the program. Used in addData(), removeData() and updateData().\n
    Parameters: (2) custom print statement, column names
    """
    m = Menu()
    options = m.optionList(columnNames, customPrint)
    return m.singleUserInput(options)

  #-----------------------------------------------------------------------
  # Num: 1d | Title: getRowsAsList()
  #-----------------------------------------------------------------------
  def getRowsAsList(self, dataset):
    """
    Used to get the csv files rows within a list format.\n
    Parameters: (1) dataset
    """
    rowList, rowIdx = [], dataset.index.values
    for row in range(len(rowIdx)):
      rowList.append(dataset.loc[rowIdx[row], :].values)
    return rowList
    