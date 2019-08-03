using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace assignment2
{
    class Data
    {
        #region Variables
        // Variables
        private readonly string filePath = Directory.GetCurrentDirectory() + @"\data\";        
        private string[] dir;
        private List<string> fileName = new List<string>();

        // High datasets
        private List<double> high2048 = new List<double>();
        private List<double> high256 = new List<double>();
        private List<double> high4096 = new List<double>();

        // Low datasets
        private List<double> low2048 = new List<double>();
        private List<double> low256 = new List<double>();
        private List<double> low4096 = new List<double>();
        
        // Mean datasets
        private List<double> mean2048 = new List<double>();
        private List<double> mean256 = new List<double>();
        private List<double> mean4096 = new List<double>();

        // Core dataset variables
        public string selectedDataset;
        public double[] activeDataset;
        public List<double> searchList;
        private List<double> mergedData;
        #endregion

        #region Constructor
        //---------------------------------------
        // CONSTRUCTOR: Handles data management
        //---------------------------------------
        public Data()
        {
            // Run GetDirectory() Method
            GetDirectory();

            // Create seperate lists of data
            ReadData(filePath + fileName[0] + ".txt", high2048);
            ReadData(filePath + fileName[1] + ".txt", high256);
            ReadData(filePath + fileName[2] + ".txt", high4096);
            ReadData(filePath + fileName[3] + ".txt", low2048);
            ReadData(filePath + fileName[4] + ".txt", low256);
            ReadData(filePath + fileName[5] + ".txt", low4096);
            ReadData(filePath + fileName[6] + ".txt", mean2048);
            ReadData(filePath + fileName[7] + ".txt", mean256);
            ReadData(filePath + fileName[8] + ".txt", mean4096);

            // Testing Purposes - checking file path & confirming files are being stored in list correctly
            /*Console.Write($"{filePath}{fileName[4]}.txt");
            foreach(double item in low256)
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine($"\nCount of low256 is: {low256.Count}");*/
        }
        #endregion

        #region Get Directory Method
        //----------------------------------------------
        // METHOD: GetDirectory - Get directory files
        //----------------------------------------------
        private void GetDirectory()
        {
            // Returns filenames in the directory
            dir = Directory.GetFiles(filePath, "*.*");

            // Add filenames into seperate list
            foreach(string name in dir)
            {
               fileName.Add(Path.GetFileName(name.Replace(".txt", "")));
            }

            // Testing Purposes - check how many files in directory
            //Console.WriteLine($"Total of {dir.Length} files in the directory.");
        }
        #endregion

        #region Read Data Method
        //------------------------------------------
        // METHOD: ReadData - Create lists of data
        //------------------------------------------
        private void ReadData(string dataFile, List<double> dataset)
        {
            // Read data from txt files & put into seperate arrays
            if (File.Exists(dataFile))
            {
                using (StreamReader sr = new StreamReader(dataFile))
                {
                    while (!sr.EndOfStream)
                    {
                        // Start loop to read data
                        double.TryParse(sr.ReadLine(), out double line);

                        // Add values to dataset & remove empty lines
                        dataset.Add(line);
                        dataset.Remove(0);
                    }

                    // Testing Purposes - Confirm file is read correctly
                    /*for (int i = 0; i < dataset.Count; i++)
                    {
                        Console.WriteLine($"{dataset[i]}");
                    }
                    Console.WriteLine($"Count total: {dataset.Count}");*/
                }
            }
            else
            {
                // File doesn't exist or isn't in right location
                Console.WriteLine($"Files cannot be located. Please make sure 'data folder' is in the current directory. \n{Directory.GetCurrentDirectory()}");
            }
        }
        #endregion

        #region Display File List Method
        //------------------------------------------------------------------------
        // METHOD: DisplayFileList - Displays the list of files in the directory
        //------------------------------------------------------------------------
        public void DisplayFileList()
        {
            // Return filenames
            for (int i = 0; i < dir.Length; i++)
            {
                Console.WriteLine($" {i + 1} | {fileName[i]}");
            }
        }
        #endregion

        #region Select Dataset Method
        //---------------------------------------------------------
        // METHOD: SelectDataset - Select a Dataset functionality
        //---------------------------------------------------------
        public void SelectDataset()
        {
            Regex pattern = new Regex(@"[1-9]");
            bool validInput = false;

            // Read users input
            while (!validInput) {
                string UserInput = Console.ReadLine();

                if (pattern.IsMatch(UserInput))
                {
                    Int32.TryParse(UserInput, out int dataUserInput);
                    
                    // If user number is too large, throw error
                    if (dataUserInput > dir.Length)
                    {
                        Console.Write("Index out of range! try again => ");
                    }
                    // Otherwise, continue as the input is correct
                    else
                    {
                        validInput = true;
                        Console.Clear();

                        // Get filename
                        selectedDataset = fileName[dataUserInput - 1];
                    }
                }
                else
                {
                    Console.Write("That's not a valid index! Try again => ");
                }
            }
        }
        #endregion

        #region Use Dataset Method (Merge Command)
        //----------------------------------------------------------------------------
        // METHOD: UseDataset - Get the user's chosen dataset for the merge command
        //----------------------------------------------------------------------------
        public void UseDataset(string dataset, ref List<double> dataList)
        {
            switch (dataset)
            {
                case "High_2048":
                    activeDataset = high2048.ToArray();
                    dataList = high2048;
                    break;
                case "High_256":
                    activeDataset = high256.ToArray();
                    dataList = high256;
                    break;
                case "High_4096":
                    activeDataset = high4096.ToArray();
                    dataList = high4096;
                    break;
                case "Low_2048":
                    activeDataset = low2048.ToArray();
                    dataList = low2048;
                    break;
                case "Low_256":
                    activeDataset = low256.ToArray();
                    dataList = low256;
                    break;
                case "Low_4096":
                    activeDataset = low4096.ToArray();
                    dataList = low4096;
                    break;
                case "Mean_2048":
                    activeDataset = mean2048.ToArray();
                    dataList = mean2048;
                    break;
                case "Mean_256":
                    activeDataset = mean256.ToArray();
                    dataList = mean256;
                    break;
                case "Mean_4096":
                    activeDataset = mean4096.ToArray();
                    dataList = mean4096;
                    break;
            }

            // Testing Purposes - checking activeDataset is set correctly
            /*Console.WriteLine($"Active Dataset is: {selectedDataset}");
            foreach(double item in activeDataset)
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine($"\nTotal items in list: {activeDataset.Length}");*/
        }
        #endregion

        #region Use Dataset Method (Sort Command)
        //-----------------------------------------------------------------------------------
        // OVERLOAD METHOD: UseDataset - Get the user's chosen dataset for the sort command
        //-----------------------------------------------------------------------------------
        public void UseDataset(string dataset)
        {
            switch (dataset)
            {
                case "High_2048":
                    activeDataset = high2048.ToArray();
                    searchList = high2048;
                    break;
                case "High_256":
                    activeDataset = high256.ToArray();
                    searchList = high256;
                    break;
                case "High_4096":
                    activeDataset = high4096.ToArray();
                    searchList = high4096;
                    break;
                case "Low_2048":
                    activeDataset = low2048.ToArray();
                    searchList = low2048;
                    break;
                case "Low_256":
                    activeDataset = low256.ToArray();
                    searchList = low256;
                    break;
                case "Low_4096":
                    activeDataset = low4096.ToArray();
                    searchList = low4096;
                    break;
                case "Mean_2048":
                    activeDataset = mean2048.ToArray();
                    searchList = mean2048;
                    break;
                case "Mean_256":
                    activeDataset = mean256.ToArray();
                    searchList = mean256;
                    break;
                case "Mean_4096":
                    activeDataset = mean4096.ToArray();
                    searchList = mean4096;
                    break;
            }

            // Testing Purposes - checking activeDataset is set correctly
            /*Console.WriteLine($"Active Dataset is: {selectedDataset}");
            foreach(double item in activeDataset)
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine($"\nTotal items in list: {activeDataset.Length}");*/
        }
        #endregion

        #region Display Data Method
        //-------------------------------------------------------
        // METHOD: DisplayData - Display the data after sorting
        //-------------------------------------------------------
        public void DisplayData(int counter)
        {
            IEnumerable<double> check = activeDataset.Where((num, index) => index % 10 == 0);
            int countCheck = 10;

            if (selectedDataset.Contains("2048"))
            {
                // Check to display every 50th value
                check = activeDataset.Where((num, index) => index % 50 == 0);
                countCheck = 50;
            }
            else if (selectedDataset.Contains("4096") || activeDataset.Length > 4096)
            {
                // Check to display every 80th value
                check = activeDataset.Where((num, index) => index % 80 == 0);
                countCheck = 80;
            }

            // Return output values
            Console.WriteLine("\nOutput of data is as follows:");

            // Run output loop
            foreach (double num in check)
            {
                Console.WriteLine(num);
            }
            // Output counter interations to console
            Console.WriteLine("-------------------------------------------------------------------------------------------------------------------");
            Console.Write($"    Sort iterations: {counter} | Volume of data on screen: {check.Count()} with every {countCheck}th value | Volume of data in list: {activeDataset.Length}\n");
            Console.WriteLine("-------------------------------------------------------------------------------------------------------------------");
        }
        #endregion

        #region Merge Data Method
        //--------------------------------------------------------------
        // METHOD: MergeData - Used for merging two datasets together
        //--------------------------------------------------------------
        public void MergeData(List<double> list1, List<double> list2, ref double[] activeDataset)
        {
            mergedData = new List<double>();

            // Merging Lists
            mergedData.AddRange(list1);
            mergedData.AddRange(list2);

            // Set datasets to the merged array
            activeDataset = mergedData.ToArray();
            searchList = mergedData;
        }
        #endregion
    }
}
