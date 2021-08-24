"""
Title: 
  Notes App

Description: 
  Provides a clean user interface to create and delete notes. Uses authentication to store notes and some user information within a database.
"""
from website import SNLTool

def main():
  """Runs the program."""
  snl = SNLTool()
  snl.app.run(debug=False)

# Runs main function
if __name__ == "__main__":
  main()
