using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace assignment2
{
    #region Binary Search Tree Class
    class BinarySearchTree
    {
        public int counter = 0;

        #region BST Sort (ASC) Method
        //-----------------------------------------------------------------
        // METHOD: BSTSortAsc - Sorts array of values in ascending order
        //-----------------------------------------------------------------
        public void BSTSortASC(double[] dataset)
        {
            // Set Variables & Objects
            Node node = null;
            BinaryTree bst = new BinaryTree();
            counter = 0;

            // Insert the nodes to the tree
            for (int i = 0; i < dataset.Length; i++)
            {
                node = bst.InsertNode(ref node, dataset[i]);
                counter++;
            }

            // Traverse the data in ascending order
            bst.InOrderTraversalASC(node);
        }
        #endregion

        #region BST Sort (DESC) Method
        //-------------------------------------------------------------------
        // METHOD: BSTSortDESC - Sorts array of values in descending order
        //-------------------------------------------------------------------
        public void BSTSortDESC(double[] dataset)
        {
            // Set Variables & Objects
            Node node = null;
            BinaryTree bst = new BinaryTree();
            counter = 0;

            // Insert the nodes to the tree
            for (int i = 0; i < dataset.Length; i++)
            {
                node = bst.InsertNode(ref node, dataset[i]);
                counter++;
            }

            // Traverse the data in descending order
            bst.InOrderTraversalDESC(node);
        }
        #endregion

    }
    #endregion

    #region Node Class
    //-------------------------------------------
    // CLASS: Node - template for node elements
    //-------------------------------------------
    class Node
    {
        // Variables
        public double key; // Key value
        public Node left, right; // Left, Right & Parent nodes

        #region Constructor
        //------------------------------
        // CONSTRUCTOR: Declares nodes
        //------------------------------
        public Node (double value)
        {
            key = value;
            left = right = null;
        }
        #endregion        
    }
    #endregion

    #region Tree Class
    //--------------------------------------------
    // CLASS: BinaryTree - Functionality of Nodes
    //--------------------------------------------
    class BinaryTree
    {
        // Variables
        public Node node;

        #region Constructor
        //----------------------------------
        // CONSTRUCTOR: Sets nodes to null
        //----------------------------------
        public BinaryTree()
        {
            node = null;
        }
        #endregion

        #region Insert Node Method
        //---------------------------------------
        // METHOD: InsertNode - Create the Nodes
        //---------------------------------------
        public Node InsertNode(ref Node node, double key)
        {
            // If node = null, create a new node & set the key value
            if (node == null)
            {
                node = new Node(key);
            }
            // If key is less than the node key value, set it to the left child node
            else if (key < node.key)
            {
                node.left = InsertNode(ref node.left, key);
            }
            // Otherwise, set it to the right child node
            else
            {
                node.right = InsertNode(ref node.right, key);
            }
            // Return the node
            return node;
        }
        #endregion

        #region In-order Traversal (ASC) Method
        //---------------------------------------------------------
        // METHOD: InOrderTraversalASC - sort in ascending order
        //--------------------------------------------------------
        // Run in order - left child; node; right child
        public void InOrderTraversalASC(Node node)
        {
            // If there isn't a node, don't return anything
            if (node == null)
            {
                return;
            }
            // Recur on left child
            InOrderTraversalASC(node.left);

            // Testing Purposes - Print data of node (Returns all data)
            //Console.WriteLine(node.key);

            // Recur on right child
            InOrderTraversalASC(node.right);
        }
        #endregion

        #region In-order Traversal (DESC) Method
        //----------------------------------------------------------
        // METHOD: InOrderTraversalDESC - sort in descending order
        //----------------------------------------------------------
        // Run in order - left child; node; right child
        public void InOrderTraversalDESC(Node node)
        {
            // If there isn't a node, don't return anything
            if (node == null)
            {
                return;
            }

            // Recur on right child
            InOrderTraversalDESC(node.right);

            // Testing Purposes - Print data of node (Returns all data)
            //Console.WriteLine(node.key);

            // Recur on left child
            InOrderTraversalDESC(node.left);
        }
        #endregion
    }
    #endregion
}
