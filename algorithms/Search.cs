using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace assignment2
{
    class Search
    {
        private int counter = 0;

        #region Linear Search Method
        //----------------------------------------------------------------------------------------
        // METHOD: LinearSearch - Searches through every item in the array until result is found
        //----------------------------------------------------------------------------------------
        public double LinearSearch(double value, double[] dataset)
        {
            counter = 0;

            for(int i = 0; i < dataset.Length; i++)
            {
                // Check each value in the dataset till found
                if(dataset[i] == value)
                {
                    counter++;
                    return i;
                }
                counter++;
            }
            // If cannot be found
            counter++;
            return -1;
        }
        #endregion

        #region Binary Search Method
        //----------------------------------------------------------------------------------------------
        // METHOD: BinarySearch - Searches through an array halving it until it finds the right value
        //----------------------------------------------------------------------------------------------
        public double BinarySearch(double target, double[] dataset)
        {
            int l = 0;
            int r = dataset.Length - 1;
            counter = 0;

            // while left is less than the right
            while (l <= r)
            {
                int mid = (l + r) / 2;

                // If the middle value is less than the search value, move to the left
                if (dataset[mid] < target)
                {
                    l = mid + 1;
                    counter++;
                }
                // If the middle value is greater than the search value, move to the right
                else if (dataset[mid] > target)
                {
                    r = mid - 1;
                    counter++;
                }
                // Otherwise, return the middle value
                else
                {
                    counter++;
                    return mid;
                }
                counter++;
            }
            // Return -1 if not found
            counter++;
            return -1;
        }
        #endregion

        #region Search For Value Method
        //-------------------------------------------------------------
        // METHOD: SearchForValue - Deals with Searching Functionality
        //-------------------------------------------------------------
        public void SearchForValue(double result, double customValue, string activeSearch, string sortOption, List<double> searchList, double[] dataset)
        {
            // Define local objects
            Sort sort = new Sort();
            BinarySearchTree bst = new BinarySearchTree();

            // If value cannot be found
            if (result == -1)
            {
                // Add the value to the array
                searchList.Add(customValue);
                dataset = searchList.ToArray();

                // Re-sort the data
                sort.ReSort(sortOption, dataset);

                // Search for newly added value
                switch (activeSearch)
                {
                    case "Linear":
                        result = LinearSearch(customValue, dataset);
                        break;
                    case "Binary":
                        result = BinarySearch(customValue, dataset);
                        break;
                }

                // Return the search results
                SearchOutput(result, customValue, searchList, dataset);

                // Delete the value from the array
                searchList.Remove(customValue);
                dataset = searchList.ToArray();
            }
            // Else value is found
            else
            {
                Console.WriteLine($"{customValue} can be found at index: {result}");
            }
        }
        #endregion

        #region Search Output Method
        //-------------------------------------------------------------------
        // METHOD: SearchOutput - Displays the search output to the console
        //-------------------------------------------------------------------
        public void SearchOutput(double result, double value, List<double> searchList, double[] dataset)
        {
            // Testing Purposes - return output of data & display index
            /*Console.WriteLine("Output of data is as follows:");
            // Run output loop
            foreach (double num in dataset)
            {
                Console.WriteLine(num);
            }
            Console.WriteLine($"{value} can be found at index: {result}");*/

            // Check if newly added value is at front. If so, only return 1 index value
            if (result == 0)
            {
                double closest = dataset[1];

                // Output search iteration
                Console.WriteLine($"Total search iterations: {counter}");

                Console.WriteLine($"Sorry, {value} is not within the dataset. The closest value is: {closest}");
                Console.WriteLine($"{closest} can be found at index: {result}"); // result will be first value
            }
            // Check if newly added value is at back. If so, only return 1 index value
            else if (result + 1 == dataset.Length)
            {
                double closest = dataset[dataset.Length - 2];

                // Output search iteration
                Console.WriteLine($"Total search iterations: {counter}");

                Console.WriteLine($"Sorry, {value} is not within the dataset. The closest value is: {closest}");
                Console.WriteLine($"{closest} can be found at index: {result}"); // result will be last value
            }
            // Else, return both next to it
            else
            {
                int frontIndex = Convert.ToInt32(result - 1);
                int backIndex = Convert.ToInt32(result + 1);
                double infront = dataset[frontIndex];
                double behind = dataset[backIndex];

                // Output search iteration
                Console.WriteLine($"Total search iterations: {counter}");

                // Find values and indexes next to newly added value
                Console.WriteLine("Sorry, {0} is not within the dataset. The closest values are: {1}, {2}", value, infront, behind);
                Console.Write($"{infront} can be found at index: {frontIndex + 1} | "); // value infront
                Console.Write($"{behind} can be found at index: {backIndex}"); // value behind
            }
        }
        #endregion
    }
}
