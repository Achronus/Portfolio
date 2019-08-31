# Project Catalog

### Description
Welcome! This repository is a collective of all the Python projects that I have completed. Whether the file is part of a larger project or a simple one page script, it will be located here! Here people can view and utilize pieces of code from my projects that they may find useful. 

Within this document I will go into detail on the projects that I have created. This includes: what the projects do, why I choose to create them and where you can find the coding files.

### Why Python?
Python is a beautiful language that allows for easy readability of code without the need for brackets. Also, it has the ability to do anything you need! Ranging from web development, to data science, to data mining or even automating small menial and tedious tasks - overall, it's a great language to have in your toolkit!

### Contents
  * [Projects](#projects)
  * [Mini Scripts](#mini-scripts) - _Coming soon!_
  * [Personal](#personal)

### Projects
  * [Conversion Exchanger](#conversion-exchanger)
  * [CSV Editor](#csv-editor)
  * [File Searcher](#file-searcher)
  * [Web Scraper](#web-scraper)
  * [Data Extraction Tool](#data-extraction-tool) - _Coming soon!_
  * [Graph Plotter](#graph-plotter) - _Coming soon!_

  #### Description
  This area is dedicated to all the large projects I have completed. These projects can be run within the relevant folder using the command `python3 main.py`. You **MUST** have a minimum of Python 3.7 installed to be able to use the programs.

  #### Conversion Exchanger | [Check out the code files here ->](https://github.com/Achronus/Portfolio/tree/master/projects/conversion_exchanger)
  
  ##### What It Does
  This is designed to convert core metrics from one to another. Inputting the index of your choice allows you to select the conversion type and then go through the metric options relevant to that type. It reads from a CSV of formulas to get the correct conversion, based on the users input. 
  
  In total the program has 6 conversion types that consist of 42 different metrics. That's a total of 328 conversions! These metrics include:
  1. Temperature (3) – Celsius, fahrenheit, kelvin.
  2. Frequency (4) – Hertz, kilohertz, megahertz, gigahertz.
  3. Angle (4) – Degrees, radians, gradians, milligradians.
  4. Weight (8) – Kilogram, gram, milligram, ton, microgram, stone, pound, ounce.
  5. Length (11) – Kilometre, metre, centimetre, millimetre, micrometre, nanometre, mile, yard, foot, inch, nautical mile.
  6. Volume (12) – Cubic metre, litre, millilitre, gallon, quart, pint, cup, fluid ounce, tablespoon, teaspoon, cubic foot, cubic inch.

  ```
  ---------------------------------------------------------------------------------
  Select the conversion type (input the index):
    1. Angle
    2. Frequency
    3. Length
    4. Temperature
    5. Volume
    6. Weight
  ---------------------------------------------------------------------------------
  =>
  ```

  Above is as example of the main menu and below is an example of the _temperature_ menu.

  ```
  ---------------------------------------------------------------------------------
  You selected the 'Temperature' conversion type, what would you like to convert as?
    1. Celsius
    2. Fahrenheit
    3. Kelvin
  ---------------------------------------------------------------------------------
  =>
  ```

  #### CSV Editor | [Check out the code files here ->](https://github.com/Achronus/Portfolio/tree/master/projects/csv_editor)

  ##### What It Does
  This project is a console based application that allows you to create new CSV files that you can add data to, remove data from or update existing data inside of it. This program uses the _pandas_ library to allow editing the CSV data as a dataframe that then updates the file name of the users choice.

  Below is an example of what the main menu looks like:

  ```
  -----------------------------------------------------------------------------------------------------------------
  Please choose an option:
  - info - displays a list of commands that can be used
  - display [filename] - displays the data within a CSV file
  - create [filename] - creates a CSV file
  - add [filename] - adds data to a chosen CSV file
  - remove [filename] - removes data from a chosen CSV file
  - update [filename] - allows you to update the data within a chosen CSV file
  - exit - exits the program
  -----------------------------------------------------------------------------------------------------------------
  =>
  ```

  #### File Searcher | [Check out the code files here ->](https://github.com/Achronus/Portfolio/tree/master/projects/file_searcher)

  ##### What It Does
  This project is used to locate a file or directory in minutes. Simply input one of two commands `local [filename/folder name]` or `other [filename/folder name]` and the program will search the disk drive of your choice. This also works with USB sticks and external hard drives connected to your machine.

  ```
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

  ```
  Searching for file, please wait...
  -----------------------------------------------------------------------------------------------------------------
  C:\Users\[name]\Documents\GitHub\Portfolio\projects\conversion_exchanger\menu.py
  C:\Users\[name]\Documents\GitHub\Portfolio\projects\csv_editor\menu.py
  C:\Users\[name]\Documents\GitHub\Portfolio\projects\file_searcher\menu.py
  -----------------------------------------------------------------------------------------------------------------
  Searching complete. See all file locations above.
  =>
  ```

  #### Web Scraper | [Check out the code files here ->](https://github.com/Achronus/Portfolio/tree/master/projects/web_scraper)
  **PLEASE NOTE:** This project is still being developed. 

  ##### What It Does
  This uses the _urllib_ and _BeautifulSoup_ libraries to crawl a user provided URL. It scans the provided URL for any links that connect to other pages on the website. Collating those URLs, it opens the URLs and scrapes their HTML contents into separate files into a directory on your local machine. This allows you to view the files and extract specific data from them that you require. 
  
  A tool that compliments this web scraper is the ['Data Extraction Tool'](#data-extraction-tool).

  ```
  -----------------------------------------------------------------------------------------------------------------
  Input the url you would like to scrape. Format of the url must consist of the following:
    1. Protocol (http:// or https://)
    2. Website name
    3. Domain name (e.g. .com/, .co.uk/, .de/). Domain name MUST end with a /
  Format example: 'https://websitename.co.uk/' or 'https://subdomain.websitename.com/'
  -----------------------------------------------------------------------------------------------------------------
  => https://acius.co.uk/
  ```

  Above is an example of the Web Scraper menu, using my website as an example you can see the output below.

  ```
  Page limit: 20 | Total pages found: 8
  New file has been created called 'root-page'.
  New file has been created called 'cookies-policy'.
  New file has been created called 'projects-conversion-exchanger'.
  New file has been created called 'projects-csv-editor'.
  New file has been created called 'projects-data-extraction-tool'.
  New file has been created called 'projects-file-searcher'.
  New file has been created called 'projects-graph-plotter'.
  New file has been created called 'projects-web-scraper'.
  -----------------------------------------------------------------------------------------------------------------
  Please check the 'pages' folder.
  -----------------------------------------------------------------------------------------------------------------
  Scraping complete. Program will exit in 10 seconds.
  ```

  #### Data Extraction Tool
  _Coming soon!_

  #### Graph Plotter
  _Coming soon!_

### Mini Scripts
_Coming soon!_
Home to one page scripts and custom classes containing a variety of utility functions.

### Personal
This folder contains personal scripts that I use regularly. Sometimes I will get fed up of repeating menial tasks, what better way then to write up a quick script to help speed things up!
