using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace assignment2
{
    class Sort
    {
        // Variables
        public int counter = 0;

        #region Bubble Sort ASC Method
        //---------------------------
        // METHOD: Bubble Sort (ASC)
        //---------------------------
        public void BubbleASC(double[] data)
        {
            int n = data.Length - 1;
            counter = 0;

            for (int i = 0; i < n; i++)
            {
                counter++;
                for (int j = 0; j < n - i; j++)
                {
                    counter++;
                    if (data[j + 1] < data[j])
                    {
                        double temp = data[j];
                        data[j] = data[j + 1];
                        data[j + 1] = temp;
                        counter++;
                    }
                }
            }
        }
        #endregion

        #region Bubble Sort DESC Method
        //----------------------------
        // METHOD: Bubble Sort (DESC)
        //----------------------------
        public void BubbleDESC(double[] data)
        {
            int n = data.Length - 1;
            counter = 0;

            for (int i = 0; i < n; i++)
            {
                counter++;
                for (int j = 0; j < n - i; j++)
                {
                    counter++;
                    if (data[j + 1] > data[j])
                    {
                        double temp = data[j];
                        data[j] = data[j + 1];
                        data[j + 1] = temp;
                        counter++;
                    }
                }
            }
        }
        #endregion

        #region Merge Sort ASC Methods
        //---------------------------
        // METHOD: Merge Sort (ASC)
        //---------------------------
        // Consists of two lists, 'data' is used for sorting; 'temp' is used as moving
        private void MergeASC(double[] data, double[] temp, int low, int middle, int high)
        {
            int ri = low; // result index
            int ti = low; // temp index
            int di = middle; // destination index

            // While the two lists are not empty, merge the smaller value
            while (ti < middle && di <= high)
            {
                if (data[di] < temp[ti])
                {
                    data[ri++] = data[di++]; // Smaller value is in data
                    counter++;
                }
                else
                {
                    data[ri++] = temp[ti++]; // Smaller value is in the temp
                    counter++;
                }
                counter++;
            }
            // Move leftover values out of the temp array to the main array
            while (ti < middle)
            {
                data[ri++] = temp[ti++];
                counter++;
            }
        }

        //-------------------------------------
        // METHOD: Merge Sort Recursive (ASC)
        //-------------------------------------
        private void MergeRecASC(double[] data, double[] temp, int low, int high)
        {
            int n = high - low + 1;
            int middle = low + n / 2;
            int i;

            if (n < 2)
            {
                return; // Ignore n
            }

            // Move the lower half of the data into temp
            for (i = low; i < middle; i++)
            {
                temp[i] = data[i];
                counter++;
            }
            // Sort the lower half of the list
            MergeRecASC(temp, data, low, middle - 1);

            // Sort the upper half of the list
            MergeRecASC(data, temp, middle, high);

            // Merge the halves together
            MergeASC(data, temp, low, middle, high);
        }

        //--------------------------
        // METHOD: Merge Sort (ASC)
        //--------------------------
        public void MergeSortASC(double[] data)
        {
            // Create a temporary array to allow merge of the two halves
            double[] temp = new double[data.Length];

            // Merge the two halves
            MergeRecASC(data, temp, 0, data.Length - 1);
        }
        #endregion

        #region Merge Sort DESC Methods
        //----------------------
        // METHOD: Merge (DESC)
        //----------------------
        private void MergeDESC(double[] data, double[] temp, int low, int middle, int high)
        {
            int ri = low; // result index
            int ti = low; // temp index
            int di = middle; // destination index

            // While the two lists are not empty, merge the smaller value
            while (ti < middle && di <= high)
            {
                if (data[di] > temp[ti]) // symbol has been flipped here to achieve DESC
                {
                    data[ri++] = data[di++]; // Smaller value is in data
                    counter++;
                }
                else
                {
                    data[ri++] = temp[ti++]; // Smaller value is in the temp
                    counter++;
                }
                counter++;
            }
            // Move leftover values out of the temp array to the main array
            while (ti < middle)
            {
                data[ri++] = temp[ti++];
                counter++;
            }
        }

        //-------------------------------------
        // METHOD: Merge Sort Recursive (DESC)
        //-------------------------------------
        private void MergeRecDESC(double[] data, double[] temp, int low, int high)
        {
            int n = high - low + 1;
            int middle = low + n / 2;
            int i;

            if (n < 2)
            {
                return; // Ignore n
            }

            // Move the lower half of the data into temp
            for (i = low; i < middle; i++)
            {
                temp[i] = data[i];
                counter++;
            }
            // Sort the lower half of the list
            MergeRecDESC(temp, data, low, middle - 1);

            // Sort the upper half of the list
            MergeRecDESC(data, temp, middle, high);

            // Merge the halves together
            MergeDESC(data, temp, low, middle, high);
        }

        //---------------------------
        // METHOD: Merge Sort (DESC)
        //---------------------------
        public void MergeSortDESC(double[] data)
        {
            double[] temp = new double[data.Length];
            MergeRecDESC(data, temp, 0, data.Length - 1);
        }
        #endregion

        #region Heapsort ASC Method
        //------------------------------
        // METHOD: Heapsort (ASC)
        //------------------------------
        // Divides an array of data into a sorted & unsorted region using a 'heap'
        public void HeapsortASC(double[] data)
        {
            counter = 0;

            BuildHeapASC(data);

            // Extract the values from the heap
            for (int i = data.Length - 1; i >= 0; i--)
            {
                // Largest value (root) is stored in a temp variable
                double temp = data[0];

                // Other values are swapped with the root moving it to the end
                data[0] = data[i];
                data[i] = temp;

                // Reestablish nodes to heap
                HeapifyASC(data, i, 0); // data = dataset; n = other data value index; i = largest value
                counter++;
            }
        }

        //------------------------
        // METHOD: Heapify (ASC)
        //------------------------
        public void HeapifyASC(double[] data, int n, int i)
        {
            int lg = i; // largest (root)
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            // If left child larger than current root, set root to left
            if (left < n && data[left] > data[lg])
            {
                lg = left;
                counter++;
            }

            // If right child is larger than current root, set root to right
            if (right < n && data[right] > data[lg])
            {
                lg = right;
                counter++;
            }

            // If largest isn't the root
            if (lg != i)
            {
                // Swap the values
                double swap = data[i];
                data[i] = data[lg];
                data[lg] = swap;

                // Put values back on heap
                HeapifyASC(data, n, lg);
                counter++;
            }
        }

        #region BuildHeap Method
        //--------------------------
        // METHOD: BuildHeap (ASC)
        //--------------------------
        public void BuildHeapASC(double[] data)
        {
            // Split data into two sections - thus building the heap
            for (int i = data.Length / 2 - 1; i >= 0; i--)
            {
                // Turn data into heap
                HeapifyASC(data, data.Length, i); // data = dataset; n = the size of the data; i = the index
                counter++;
            }
        }
        #endregion

        #endregion

        #region Heapsort DESC Method
        //-------------------------------
        // METHOD: Heapsort (DESC)
        //-------------------------------
        public void HeapsortDESC(double[] data)
        {
            counter = 0;

            BuildHeapDESC(data);

            for (int i = data.Length - 1; i >= 0; i--)
            {
                double temp = data[0];
                data[0] = data[i];
                data[i] = temp;
                HeapifyDESC(data, i, 0);
                counter++;
            }
        }

        //-------------------------
        // METHOD: Heapify (DESC)
        //-------------------------
        public void HeapifyDESC(double[] data, int n, int i)
        {
            int sm = i; // Smallest
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            if (left < n && data[left] < data[sm]) // Symbols inverted
            {
                sm = left;
                counter++;
            }
            if (right < n && data[right] < data[sm]) // Symbols inverted
            {
                sm = right;
                counter++;
            }
            if (sm != i)
            {
                double swap = data[i];
                data[i] = data[sm];
                data[sm] = swap;
                HeapifyDESC(data, n, sm);
                counter++;
            }
        }

        //----------------------------
        // METHOD: BuildHeap (DESC)
        //----------------------------
        public void BuildHeapDESC(double[] data)
        {
            for (int i = data.Length / 2 - 1; i >= 0; i--)
            {
                HeapifyDESC(data, data.Length, i);
                counter++;
            }
        }
        #endregion

        #region Re-sort Method
        //------------------------------------------------------------------------------
        // METHOD: Resort - Decides which sort to use based on user previous responses
        //------------------------------------------------------------------------------
        public void ReSort(string sortOption, double[] dataset)
        {
            BinarySearchTree bst = new BinarySearchTree();

            // Check what sort option to use and resort data in order
            switch (sortOption)
            {
                case "bubbleASC":
                    BubbleASC(dataset);
                    break;
                case "bubbleDESC":
                    BubbleDESC(dataset);
                    break;
                case "mergeASC":
                    MergeSortASC(dataset);
                    break;
                case "mergeDESC":
                    MergeSortDESC(dataset);
                    break;
                case "heapASC":
                    HeapsortASC(dataset);
                    break;
                case "heapDESC":
                    HeapsortDESC(dataset);
                    break;
            }
        }
        #endregion
    }
}
