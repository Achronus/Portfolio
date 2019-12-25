# Project Catalog

### Description
Welcome! This repository is a collective of all the Python projects that I have completed. Whether the file is part of a larger project or a simple one page script, it will be located here! Here people can view and utilize pieces of code from my projects that they may find useful. 

Within this document I will go into detail on the projects that I have created. This includes: what the projects do, why I choose to create them and where you can find the coding files.

### Why Python?
Python is a beautiful language that allows for easy readability of code without the need for brackets. Also, it has the ability to do anything you need! Ranging from web development, to data science, to data mining or even automating small menial and tedious tasks - overall, it's a great language to have in your toolkit!

### Contents
  * [Projects](#projects)
  * [Mini Scripts](#mini-scripts)
  * [Personal](#personal)

## Projects
This folder is home to custom projects that I have created. These are primarily console run applications, where you can type in a few console commands to receive a specific output. These projects can be run within the relevant folder using the command `python3 main.py`. You **MUST** have a minimum of Python 3.7 installed to be able to use the programs. 

The project list is as follows:
  * [Conversion Exchanger](#conversion-exchanger)
  * [CSV Editor](#csv-editor)
  * [File Searcher](#file-searcher)
  * [Ciphers](#ciphers)
  * [Data Extraction Tool](#data-extraction-tool)
  * [Shape Coordinate System](#shape-coordinate-system) - _Coming soon!_

  ## [Conversion Exchanger](https://github.com/Achronus/Portfolio/tree/master/projects/conversion_exchanger)
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

  ## [CSV Editor](https://github.com/Achronus/Portfolio/tree/master/projects/csv_editor)
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

  ## [File Searcher](https://github.com/Achronus/Portfolio/tree/master/projects/file_searcher)
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

  ## [Ciphers](https://github.com/Achronus/Portfolio/tree/master/projects/ciphers)
  This folder consists of 4 common ciphers: the Caesar cipher, Transposition cipher, Substitution cipher and Affine cipher. Each cipher has their own unique class, with functions for encrypting and decrypting and an example for each one. 

  In addition to this, some of the ciphers have an example of being brute-forced. NOTE: I do not recommend using these ciphers for securing confidential information, these were fun little projects for me to understanding another means of problem solving.

  You can see the cipher specific files below:
  - [Caesar Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/caesar.py)
    - [Brute-forcing Caesar Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/cracking/bruteForceCaesar.py)
  - [Transposition Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/transposition.py)
    - [Brute-forcing Transposition Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/cracking/bruteForceTransposition.py)
  - [Affine Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/affine.py)
    - [Brute-forcing Affine Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/cracking/bruteForceAffine.py)
  - [Substitution Cipher](https://github.com/Achronus/Portfolio/blob/master/projects/ciphers/substitution.py)
  

  ## [Data Extraction Tool](https://github.com/Achronus/Portfolio/tree/master/projects/data_extraction_tool)
  The Data Extraction Tool uses the _BeautifulSoup_ and _pandas_ libraries to extract all the content you require from a local HTML file. You can select to extract: paragraphs, headings, links, image links, just links, just paragraphs and headings or all options in one!

  Firstly, input the name of the CSV file you want to create.
  ```
  Input the name of the CSV file you want to create.
  =>
  ```

  Secondly, select the index of the HTML file to extract data from (these files will need to be added to the data folder that is created after the program has been run once).
  ```
  Select the index of the HTML file to extract data from.
    1. projects-web-scraper.html
    2. root-page.html
  =>
  ```

  Lastly, select the index of the extraction option you would like to use.
  ```
  Select the index of the tag type you want to extract data from.
    1. Paragraphs
    2. Headings
    3. Links
    4. Img urls
    5. All text (no links)
    6. All links
    7. All content
  =>
  ```

  ## Shape Coordinate System
  _Coming soon!_

  This project involves creation of a two-dimensional virtual coordinate system, allowing you to store basic geometric shapes coordinate positions. 

## [Mini Scripts](https://github.com/Achronus/Portfolio/tree/master/mini)
Home to one page scripts and custom classes containing a variety of utility functions.

## Personal
This folder contains personal scripts that I use regularly.
