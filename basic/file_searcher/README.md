# File Searcher

This project is used to locate a file or directory in minutes. Simply input one of two commands `local [filename/folder name]` or `other [filename/folder name]` and the program will search the disk drive of your choice. This also works with USB sticks and external hard drives connected to your machine.

```Psuedocode
-----------------------------------------------------------------------------------------------------------------
Please choose an option:
- info - displays a list of commands that can be used
- local [filename] - finds a file on the local disk drive
- other [filename] - finds a file on another drive on your machine
- exit - exits the program
-----------------------------------------------------------------------------------------------------------------
=> local menu.py
```

Above is an example of the main menu and below is an example of the command `local menu.py` being run. This command searches the local disk drive (C:) for any files named `menu.py`.

```Psuedocode
Searching for file, please wait...
-----------------------------------------------------------------------------------------------------------------
C:\Users\[name]\Documents\GitHub\Portfolio\projects\conversion_exchanger\menu.py
C:\Users\[name]\Documents\GitHub\Portfolio\projects\csv_editor\menu.py
C:\Users\[name]\Documents\GitHub\Portfolio\projects\file_searcher\menu.py
-----------------------------------------------------------------------------------------------------------------
Searching complete. See all file locations above.
=>
```
