This mini project focuses on implementing the FP-Growth algorithm in Python for frequent pattern 
mining. FP-growth is a fast way to find frequent patterns in big datasets. This method doesn't 
require candidate generation and can be much faster than the Apriori algorithm. The goal of this 
project is to develop a Python program that takes a transactional dataset as input and mines the 
frequent patterns using the FP-Growth algorithm.
This project has a few important steps:
1. Data Loading and Preprocessing: The ‘read data’ function reads transaction data from a 
file. It then prepares the data by splitting each file line into separate parts, called tokens. A 
dictionary is made where each entry represents a transaction and its frequency and then it 
is used for further processing.
2. FP-tree Construction: The function ‘create_HTandFPTree’ makes a Header Table and an 
FP-Tree. The Header Table has information about how often each item appears. The FP 
tree is a type of tree where each node represents an item. The nodes are connected to show 
the order and frequency of items in transactions.
3. FP tree growth: The 'updateTree' function updates the FP tree with a transaction in a 
repetitive manner. The 'update_NodeLink' function changes the links between nodes for 
items in the HeaderTable. These actions help create the FP-Tree in a more efficient way.
4. Mining Frequent Patterns: The 'uptraverse' and 'find_branches' functions are used to find 
conditional pattern bases for a given item. The function 'Mine_Tree' mines frequent 
patterns by creating special trees for each item. The frequent itemsets are kept in the 
‘frequent_itemset’ list.
5. Result Generation and Analysis: Finally, the program shows how long the process took 
and shows the frequent patterns with their support values. It also calculates the support in 
percentages (relative support).
The main goal of this project is to efficiently mine frequent itemsets from transaction data using 
the FP-growth algorithm and provide a clear analysis of the discovered patterns. After finding 
these patterns, the project will analyze them, and we can gain a deeper understanding of frequent 
pattern mining techniques and their applications in real-world scenarios
