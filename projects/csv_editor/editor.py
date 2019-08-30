#-----------------------------------------------------------------------
# File Title: Editor Class
# File Description: Used to add or remove data to and from a CSV file.
#-----------------------------------------------------------------------
# CONTENTS:
# 1. Editor()
#    a. displayData()
#    b. createFile()
#    c. selectData()
#    d. addData()
#    e. removeData()
#    f. updateData()
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
  Consists of 6 functions: displayData(), createFile(), selectData(), addData(), removeData(), updateData().
  """
  #-----------------------------------------------------------------------
  # Num: 1a | Title: displayData()
  #-----------------------------------------------------------------------
  def displayData(self, filename):
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
  # Num: 1b | Title: createFile()
  #-----------------------------------------------------------------------
  def createFile(self, filename):
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
  # Num: 1c | Title: selectData()
  #-----------------------------------------------------------------------
  def selectData(self, filename, optionList):
    """
    Used to select the data to add, remove or update from the selected CSV file.\n
    Parameters: (2) file name, option list.
    """
    # set variables
    m = Menu()
    printOutput = 'What information would you like to select?'

    # Get inital options
    options = m.optionList(optionList, printOutput)
    choice = m.singleUserInput(options)
    return choice

  #-----------------------------------------------------------------------
  # Num: 1d | Title: addData()
  #-----------------------------------------------------------------------
  def addData(self, filename):
    """
    Adds data to the file via users input.\n
    Parameters: (1) Filename.
    """
    # Set variables
    u = Utility()
    df = pd.read_csv(filename)
    df.to_csv(filename + '.bak', index=False) # Create file backup

    header = list(df.columns)
    optionsList = ['New column', 'Existing column', 'New row']

    # Select the data
    choice = self.selectData(filename, optionsList)

    #-------------------------
    # If new column
    #-------------------------
    if choice == optionsList[0]:
      # Get column name
      print(f"You selected '{choice}'. Input the name of the column to add.")
      newColName = input('=> ')
      header.append(newColName)

      # Get new data and add to dataset
      df = u.newColData(newColName, df, header)

    #-------------------------
    # If existing column
    #-------------------------
    if choice == optionsList[1]:
      # Get column name
      colPrint = f"You selected '{choice}'. Input the column index you want to add data to."
      selectedHeader = u.getColNames(colPrint, header)

      # Get new data and add to dataset
      df = u.newColData(selectedHeader, df, header)

    #-------------------------
    # If new row
    #-------------------------
    if choice == optionsList[2]:

      # Get users input
      optTwoPrint = f"You selected '{choice}'. Input the data to add. Separate by ', ' for next column. E.g. '1, 2, 3'"
      newRowData = u.fieldLengthCheck(optTwoPrint, header, 'column')
      
      # Add data to file
      newRowSubmission = pd.DataFrame([newRowData], columns=header)
      df = df.append(newRowSubmission, ignore_index=True)

    # Add the data to the CSV file
    df.to_csv(filename, index=False)
      
    # Display updated file
    self.displayData(filename)

  #-----------------------------------------------------------------------
  # Num: 1e | Title: removeData()
  #-----------------------------------------------------------------------
  def removeData(self, filename):
    """
    Removes data from the file via users input.\n
    Parameters: (1) Filename.
    """
    # Set variables
    m, u = Menu(), Utility()
    df = pd.read_csv(filename)
    df.to_csv(filename + '.bak', index=False) # Create file backup

    header = list(df.columns)
    optionsList = ['Whole column', 'Column data', 'Specific row']
    
    # Select the data
    choice = self.selectData(filename, optionsList)

    #-------------------------
    # If whole column
    #-------------------------
    if choice == optionsList[0]:
      # Get column name
      colPrint = f"You selected '{choice}'. Input the column index for the column you want to remove."
      selectedCol = u.getColNames(colPrint, header)

      # Remove column
      df = df.drop(columns=selectedCol)
    
    #-------------------------
    # If column data
    #-------------------------
    if choice == optionsList[1]:
      # Get column name
      colPrint = f"You selected '{choice}'. Input the column index for the column data you want to remove."
      selectedCol = u.getColNames(colPrint, header)

      # Get column data
      colDataPrint = f"You selected the column '{selectedCol}'. Input the indexes for the data to remove. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      colIdx = header.index(selectedCol)
      colDataOptions = m.optionList(df.loc[:, header[colIdx]].values, colDataPrint)
      selectedColData = m.multiUserInput(colDataOptions)

      # Remove selected data
      df = df.replace(selectedColData, '')

    #-------------------------
    # If specific row
    #-------------------------
    if choice == optionsList[2]:
      # Get each row in the file as a list
      rowList = u.getRowsAsList(df)
      
      # Get rows
      rowPrint = f"You selected '{choice}'. Input the indexes for the rows you want to remove. Separate by a ', ' for multiple rows. E.g. '1, 2, 3'"
      rowOptions = m.optionList(rowList, rowPrint)
      selectedRows = m.getRowUserInput(rowOptions)
            
      # Remove selected data
      df = df.drop(selectedRows)

    # Add the data to the CSV file
    df.to_csv(filename, index=False)
      
    # Display updated file
    self.displayData(filename)

  #-----------------------------------------------------------------------
  # Num: 1f | Title: updateData()
  #-----------------------------------------------------------------------
  def updateData(self, filename):
    """
    Updates data within the file via users input.\n
    Parameters: (1) Filename.
    """
    # Set variables
    m, u = Menu(), Utility()
    df = pd.read_csv(filename)
    df.to_csv(filename + '.bak', index=False) # Create file backup

    header = list(df.columns)
    optionsList = ['Column name', 'Column data', 'Specific row']

    # Select the data
    choice = self.selectData(filename, optionsList)

    #-------------------------
    # If column name
    #-------------------------
    if choice == optionsList[0]:
      # Select column names
      headerPrint = f"You selected '{choice}'. Input the column indexes for the column names you want to update. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      headerOptions = m.optionList(header, headerPrint)
      selectedHeaders = m.multiUserInput(headerOptions)

      # Get new column names 
      optZeroPrint = f"You selected the column names '{selectedHeaders}'. Input the new names for the columns. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      newColNames = u.fieldLengthCheck(optZeroPrint, selectedHeaders, 'selected column')
      
      # Update data
      for item in range(len(selectedHeaders)):
        df = df.rename(columns={selectedHeaders[item] : newColNames[item]})

    #-------------------------
    # If column data
    #-------------------------
    if choice == optionsList[1]:
      # Select column name
      colPrint = f"You selected '{choice}'. Input the column index for the column you want to update."
      selectedCol = u.getColNames(colPrint, header)

      # Select column data
      selColPrint = f"You selected the column '{selectedCol}'. Input the column indexes for the data to update. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      colIdx = header.index(selectedCol)
      colDataOptions = m.optionList(df.loc[:, header[colIdx]].values, selColPrint)
      selectedColData = m.multiUserInput(colDataOptions)

      # Select new column data names
      optOnePrint = f"You selected the column data '{selectedColData}'. Input the new names for the column data. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      newColNames = u.fieldLengthCheck(optOnePrint, selectedColData, 'selected column data field')

      # Update data
      df.replace(to_replace=selectedColData, value=newColNames, inplace=True)

    #-------------------------
    # If specific row
    #-------------------------
    if choice == optionsList[2]:
      # Get each row in the file as a list
      rowList = u.getRowsAsList(df)
      
      # Select rows
      rowPrint = f"You selected '{choice}'. Input the index for the row you want to update."
      rowOptions = m.optionList(rowList, rowPrint)
      selectedRow = m.getRowUserInput(rowOptions)
      selectedRowIdx = selectedRow[0]
      selRowList = rowOptions[selectedRowIdx + 1]

      # Select names in row
      selRowPrint = f"You selected '{selRowList}'. Input the indexes for the fields in the row you want to update. Separate by a ', ' for multiple fields. E.g. '1, 2, 3'"
      selRowItems = []
      for item in range(len(selRowList)):
        selRowItems.append(selRowList[item])
      selRowOptions = m.optionList(selRowItems, selRowPrint)
      selFieldNames = m.multiUserInput(selRowOptions)

      # Select new names
      optTwoPrint = f"You selected the row fields '{selFieldNames}'. Input the new names for the fields. Separate by a ', ' for multiple items. E.g. '1, 2, 3'"
      newRowNames = u.fieldLengthCheck(optTwoPrint, selFieldNames, 'selected row field')

      # Update data
      df.replace(to_replace=selFieldNames, value=newRowNames, inplace=True)

    # Add the data to the CSV file
    df.to_csv(filename, index=False)
      
    # Display updated file
    self.displayData(filename)