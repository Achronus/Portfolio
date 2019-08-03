using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace assignment2
{
    class Menu
    {
        #region Variables
        // Variables
        private string command;
        private bool quit = false;
        private string activeSearch;
        private string sortOption;
        private bool vFInput = false;
        private string[] mergedDatasets;
        private string sortMethod;
        private string[] sortMethods = new string[] { "Bubble Sort", "Merge Sort", "Heapsort", "Binary Search Tree" };
        private string[] sortFormatOptions = new string[] { "Ascending", "Descending" };
        private string[] searchOptions = new string[] { "Linear Search", "Binary Search" };

        // Set objects
        Data data = new Data();
        Sort sort = new Sort();
        BinarySearchTree bst = new BinarySearchTree();
        Search search = new Search();
        #endregion

        #region Constructor
        //-------------------------------------
        // CONSTRUCTOR: First load of program
        //-------------------------------------
        public Menu()
        {
            // Displays main menu
            MainMenu();

            // Allows user input
            CommandOptions();
        }
        #endregion

        #region Main Menu Method
        //---------------------------------------------
        // METHOD: MainMenu - Displays the main menu
        //---------------------------------------------
        public void MainMenu()
        {
            // Assignment Title
            Console.WriteLine("\n----------------------------------------------------------------------------");
            Console.WriteLine("      Ryan Partridge | CMP1124M: Algorithms & Complexity - Assessment 2      ");
            Console.WriteLine("----------------------------------------------------------------------------\n");

            // Menu options
            Console.WriteLine("------------------------------------------------------------------------------------------");
            Console.WriteLine("|                          Welcome to the Weather Data Analyzer!                         |");
            Console.WriteLine("------------------------------------------------------------------------------------------");
            Console.WriteLine("| This application consists of multiple datasets and allows you to do the following:     |");
            Console.WriteLine("|                                                                                        |");
            Console.WriteLine("|  - sort - Choose the dataset you want to sort and search through                       |");
            Console.WriteLine("|  - merge - Merge two datasets before sorting and searching through them                |");
            Console.WriteLine("|  - exit - Exit the application                                                         |");
            Console.WriteLine("|                                                                                        |");
            Console.WriteLine("|  NOTE: You must sort through a dataset before being able to search it                  |");
            Console.WriteLine("------------------------------------------------------------------------------------------\n");
            Console.Write("What would you like to do? => ");
        }
        #endregion

        #region Sort Menu Method
        //---------------------------------------------------------------------------
        // METHOD: SortMenu - Displays the sort menu and manages its functionality
        //---------------------------------------------------------------------------
        public void SortMenu()
        {
            // Set local variables
            string ui;
            string input;
            bool vInput = false;

            // Display list of sort methods
            ListOptions(sortMethods);

            while (!vFInput)
            {
                input = Console.ReadLine();

                switch (input)
                {
                    #region Bubble Sort Switch
                    // Bubble Sort
                    case "1":
                        // Output format options to console
                        vFInput = true;
                        Console.Clear();
                        Console.WriteLine($"You have selected '{sortMethods[0]}' - which format would you like?");
                        ListOptions(sortFormatOptions);

                        // Check Sorting type
                        while (!vInput)
                        {
                            ui = Console.ReadLine();

                            if (ui == "1")
                            {
                                vInput = true;
                                sortOption = "bubbleASC";
                                sort.BubbleASC(data.activeDataset);
                                data.DisplayData(sort.counter);
                            }
                            else if (ui == "2")
                            {
                                vInput = true;
                                sortOption = "bubbleDESC";
                                sort.BubbleDESC(data.activeDataset);
                                data.DisplayData(sort.counter);
                            }
                            else
                            {
                                Console.Write("Index is invalid, please try again => ");
                            }
                        }
                        break;
                    #endregion

                    #region Merge Sort Switch
                    // Merge Sort
                    case "2":
                        // Output format options to console
                        vFInput = true;
                        Console.Clear();
                        Console.WriteLine($"You have selected '{sortMethods[1]}' - which format would you like?");
                        ListOptions(sortFormatOptions);

                        // Check Sorting type
                        while (!vInput)
                        {
                            ui = Console.ReadLine();

                            if (ui == "1")
                            {
                                vInput = true;
                                sortOption = "mergeASC";
                                sort.MergeSortASC(data.activeDataset);
                                data.DisplayData(sort.counter);
                            }
                            else if (ui == "2")
                            {
                                vInput = true;
                                sortOption = "mergeDESC";
                                sort.MergeSortDESC(data.activeDataset);
                                data.DisplayData(sort.counter);
                            }
                            else
                            {
                                Console.Write("Index is invalid, please try again => ");
                            }
                        }
                        break;
                    #endregion

                    #region Heapsort Switch
                    // Heapsort
                    case "3":
                        // Output format options to console
                        vFInput = true;
                        Console.Clear();
                        Console.WriteLine($"You have selected '{sortMethods[2]}' - which format would you like?");
                        ListOptions(sortFormatOptions);

                        // Check Sorting type
                        while (!vInput)
                        {
                            ui = Console.ReadLine();

                            if (ui == "1")
                            {
                                vInput = true;
                                sortOption = "heapASC";
                                sort.HeapsortASC(data.activeDataset);
                                data.DisplayData(sort.counter);
                            }
                            else if (ui == "2")
                            {
                                vInput = true;
                                sortOption = "heapDESC";
                                sort.HeapsortDESC(data.activeDataset);
                                data.DisplayData(sort.counter);
                            }
                            else
                            {
                                Console.Write("Index is invalid, please try again => ");
                            }
                        }
                        break;
                    #endregion

                    #region Binary Search Tree Switch
                    // Binary Search Tree
                    case "4":
                        // Output format options to console
                        vFInput = true;
                        Console.Clear();
                        Console.WriteLine($"You have selected '{sortMethods[3]}' - which format would you like?");
                        ListOptions(sortFormatOptions);
                        sortMethod = "BST";

                        // Check Sorting type
                        while (!vInput)
                        {
                            ui = Console.ReadLine();

                            if (ui == "1")
                            {
                                vInput = true;
                                sortOption = "binaryASC";
                                bst.BSTSortASC(data.activeDataset);
                                data.DisplayData(bst.counter);
                            }
                            else if (ui == "2")
                            {
                                vInput = true;
                                sortOption = "binaryDESC";
                                bst.BSTSortDESC(data.activeDataset);
                                data.DisplayData(bst.counter);
                            }
                            else
                            {
                                Console.Write("Index is invalid, please try again => ");
                            }
                        }
                        break;
                    #endregion

                    // Throw error if invalid input
                    default:
                        Console.Write("Invalid index, try again => ");
                        break;
                }
            }
        }
        #endregion

        #region List Options Method
        //-----------------------------------------------
        // METHOD: ListOptions - Displays list options
        //-----------------------------------------------
        public void ListOptions(string[] listOptions)
        {
            // Display options
            for (int i = 0; i < listOptions.Length; i++)
            {
                Console.WriteLine(" {0} | {1}", i + 1, listOptions[i]);
            }
            Console.Write("\nPlease input the index => ");
        }
        #endregion

        #region Search Menu Method
        //------------------------------------------------------------------------
        // METHOD: SearchMenu - Displays search menu and manages it's interface
        //------------------------------------------------------------------------
        public void SearchMenu()
        {
            #region Local Variables
            // Set local variables
            string ui;
            string iCheck;
            bool vInput = false;
            bool vInputCheck = false;
            bool custValCheck = false;
            double customValue;
            #endregion

            Console.Write("\nWould you like to search for a value? (Y/N) => ");

            while (!vInputCheck)
            {
                iCheck = Console.ReadLine().ToUpper();

                #region Quit Program if N
                // No, so quit the program
                if (iCheck == "N")
                {
                    vInputCheck = true;
                    End();
                }
                #endregion

                #region Output options if Y
                // Yes, so output the options
                else if (iCheck == "Y")
                {
                    vInputCheck = true;
                    Console.Clear();

                    // User input for value
                    Console.Write("Please input the value you would like to search for => ");

                    while (!custValCheck)
                    {
                        bool isDouble = Double.TryParse(Console.ReadLine(), out customValue);

                        // Check if customValue is a double
                        if (isDouble)
                        {
                            custValCheck = true;

                            #region Search Options
                            Console.WriteLine("\nWhat method would you like to search with?");

                            // Display list of search methods
                            ListOptions(searchOptions);
                            #endregion

                            #region Performing Search
                            // Check Searching type
                            while (!vInput)
                            {
                                ui = Console.ReadLine();
                                if (ui == "1")
                                {
                                    // Perform Linear Search
                                    vInput = true;
                                    activeSearch = "Linear";
                                    double result = search.LinearSearch(customValue, data.activeDataset);
                                    search.SearchForValue(result, customValue, activeSearch, sortOption, data.searchList, data.activeDataset);
                                    SearchMenu();
                                }
                                else if (ui == "2")
                                {
                                    // Conduct Binary Search
                                    vInput = true;
                                    activeSearch = "Binary";
                                    double result = search.BinarySearch(customValue, data.activeDataset);
                                    search.SearchForValue(result, customValue, activeSearch, sortOption, data.searchList, data.activeDataset);
                                    SearchMenu();
                                }
                                else
                                {
                                    Console.Write("Invalid index, please try again => ");
                                }
                            }
                            #endregion
                        }
                        else
                        {
                            Console.Write("Number is invalid. Please input a valid decimal number => ");
                        }
                    }
                }
                #endregion

                // Invalid console input
                else
                {
                    Console.Write("Invalid input, please enter the letter: Y or N => ");
                }
            }
        }
        #endregion

        #region Merge Menu Method
        //----------------------------------------------------------------------------
        // METHOD: MergeMenu - Displays the merge menu and manages its functionality
        //----------------------------------------------------------------------------
        private void MergeMenu()
        {
            List<double> list1 = new List<double>();
            List<double> list2 = new List<double>();

            // Select 1st dataset
            Console.WriteLine("\nPlease select the 1st dataset you want to merge:");
            data.DisplayFileList();
            Console.Write("\nInput the index => ");
            data.SelectDataset();
            string firstDataset = data.selectedDataset; // String of dataset name

            // Select 2nd dataset
            Console.WriteLine("Please select the 2nd dataset you want to merge:");
            data.DisplayFileList();
            Console.Write("\nInput the index => ");
            data.SelectDataset();
            string secondDataset = data.selectedDataset; // String of dataset name

            // Check if datasets are the same
            if (firstDataset == secondDataset)
            {
                // If so, return an error and re-run
                Console.WriteLine($"Sorry, you cannot use the same dataset! The first dataset you have selected to merge is '{firstDataset}'.");
                data.DisplayFileList();
                Console.Write("\nPlease input a different datasets index => ");
                data.SelectDataset();
                secondDataset = data.selectedDataset;
            }

            // Assign the datasets to the right set of data
            data.UseDataset(firstDataset, ref list1);
            data.UseDataset(secondDataset, ref list2);

            // Merge the datasets together
            data.MergeData(list1, list2, ref data.activeDataset);
            mergedDatasets = new string[] { firstDataset, secondDataset };
        }
        #endregion

        #region Command Options Method
        //----------------------------------------------------------
        // METHOD: CommandOptions - Functionality of the main menu
        //----------------------------------------------------------
        public void CommandOptions()
        {
            while (!quit)
            {
                // Get user command input
                command = Console.ReadLine().ToLower();
                switch (command)
                {
                    #region Sort command
                    // Choose a dataset
                    case "sort":
                        Console.WriteLine("\nPlease select the dataset you want to sort:");
                        data.DisplayFileList();
                        Console.Write("\nInput the index => ");
                        data.SelectDataset();

                        // Return dataset of users input
                        Console.WriteLine($"You have selected '{data.selectedDataset}' - what sorting method would you like to use?");
                        data.UseDataset(data.selectedDataset);

                        // Continue with sorting
                        SortMenu();

                        // Start searching if not BST
                        if (sortMethod != "BST")
                        {
                            SearchMenu();
                        }
                        // Otherwise, end the program
                        else
                        {
                            End();
                        }
                        
                        break;
                    #endregion

                    #region Merge command
                    // Merge two datasets
                    case "merge":
                        // Merge the datasets together
                        MergeMenu();

                        // Start the sort
                        Console.WriteLine($"You have merged '{mergedDatasets[0]}' & '{mergedDatasets[1]}' together - what sorting method would you like to use?");
                        SortMenu();

                        // Start searching if not BST
                        if (sortMethod != "BST")
                        {
                            SearchMenu();
                        }
                        // Otherwise, end the program
                        else
                        {
                            End();
                        }
                        break;
                    #endregion

                    // Exit program
                    case "exit":
                        End();
                        break;
                    
                    // If other command is input, throw error
                    default:
                        Console.Write("Unknown command, try again => ");
                        break;
                }
            }
        }
        #endregion

        #region End Method
        //------------------------------------------
        // METHOD: End - Used to end the program
        //------------------------------------------
        public void End()
        {
            quit = true;
            Console.WriteLine("\nPress the enter key to exit...");
            Console.ReadLine();
        }
        #endregion

        #region Test Method - Outputs Data of sorted array
        //---------------------------------------------
        // METHOD: OutputData - Used for testing only
        //---------------------------------------------
        public void OutputData()
        {
            foreach (double item in data.activeDataset)
            {
                Console.WriteLine(item);
            }
        }
        #endregion
    }
}
