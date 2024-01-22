
# K. M. Safin Kamal (2020-1-60-235)
# Mysha Maliha Priyanka (2020-1-60-230)
# Md. Adnan Morshed (2020-1-60-155)
# Nahida Hoque (2020-1-60-147)  (Sec- 2)
##############################################################

# from google.colab import drive
# drive.mount('/content/drive')
#
# cd /content/drive/MyDrive/CSE477Project

import time
num_of_trans = 0

def read_data(filename):
    global num_of_trans
    Transaction = []

    fptr = open(filename, "r")
    while True:
        line = fptr.readline()
        num_of_trans += 1

        if not line:
            break

        token = line.split()
        token.sort()
        #Transaction.append(set(token))
        Transaction.append(sorted(list(set(token))))
    fptr.close()

    DB = {}
    for trans in Transaction:
        trans_frozen = frozenset(sorted(trans))
        DB[trans_frozen] = DB.get(trans_frozen, 0) + 1

    return DB

class TreeNode:
    def __init__(self, Node_name, counter, parentNode):
        self.name = Node_name
        self.count = counter
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def increment_counter(self, counter):
        self.count += counter

def create_HTandFPTree(dataset, minSupport):
    HeaderTable = {}
    for transaction in dataset:
        for item in transaction:
            HeaderTable[item] = HeaderTable.get(item, 0) + dataset[transaction]
    for k in list(HeaderTable):
        if HeaderTable[k]*100/num_of_trans < minSupport:
        #if HeaderTable[k] < minSupport:
            del (HeaderTable[k])

    frequent_itemset = set(HeaderTable.keys())

    if len(frequent_itemset) == 0:
        return None, None

    for k in HeaderTable:
        HeaderTable[k] = [HeaderTable[k], None]

    root = TreeNode('ROOT', 1, None)

    for itemset, count in dataset.items():
        frequent_transaction = {}
        for item in itemset:
            if item in frequent_itemset:
                frequent_transaction[item] = HeaderTable[item][0]
        if len(frequent_transaction) > 0:
            ordered_itemset = [v[0] for v in sorted(frequent_transaction.items(), key=lambda p: p[1], reverse=True)]
            updateTree(ordered_itemset, root, HeaderTable, count)
    return root, HeaderTable


def updateTree(itemset, FPTree, HeaderTable, count):
    if itemset[0] in FPTree.children:
        FPTree.children[itemset[0]].increment_counter(count)
    else:
        FPTree.children[itemset[0]] = TreeNode(itemset[0], count, FPTree)

        if HeaderTable[itemset[0]][1] == None:
            HeaderTable[itemset[0]][1] = FPTree.children[itemset[0]]
        else:
            update_NodeLink(HeaderTable[itemset[0]][1], FPTree.children[itemset[0]])

    if len(itemset) > 1:
        updateTree(itemset[1::], FPTree.children[itemset[0]], HeaderTable, count)


def update_NodeLink(Test_Node, Target_Node):
    while (Test_Node.nodeLink != None):
        Test_Node = Test_Node.nodeLink

    Test_Node.nodeLink = Target_Node


def uptraverse(leaf_Node,  branch):
    if leaf_Node.parent != None:
        branch.append(leaf_Node.name)
        uptraverse(leaf_Node.parent,  branch)

def find_branches(pattern, TreeNode):
    Conditional_branches = {}

    while TreeNode != None:
        branch = []
        uptraverse(TreeNode,  branch)
        if len( branch) > 1:
            Conditional_branches[frozenset( branch[1:])] = TreeNode.count
        TreeNode = TreeNode.nodeLink

    return Conditional_branches


def Mine_Tree(FPTree, HeaderTable, minSupport, prefix, frequent_itemset):
    sorted_items = [v[0] for v in sorted(HeaderTable.items(), key=lambda p: p[1][0])]
    for pattern in sorted_items:
        new_frequentset = prefix.copy()
        new_frequentset.add(pattern)
        support = (HeaderTable[pattern][0] * 100) / len(processed_DB)

        frequent_itemset.append((new_frequentset,support))

        Conditional_branches = find_branches(pattern, HeaderTable[pattern][1])

        Conditional_FPTree, Conditional_header = create_HTandFPTree(Conditional_branches, minSupport)

        if Conditional_header != None:
            Mine_Tree(Conditional_FPTree, Conditional_header, minSupport, new_frequentset, frequent_itemset)

def print_FPTree(FPtree, depth=0):
    if FPtree is not None:
        print("  " * depth + f"{FPtree.name} ({FPtree.count})")
        for child in FPtree.children.values():
            print_FPTree(child, depth + 1)


#filename = r"D:\UNIVERSITY\Semester 11 (cse400B,350,477)\CSE477\Lab\apri\mydata.txt"
filename = r"D:\UNIVERSITY\Semester 11 (cse400B,350,477)\CSE477\Lab\apri\venv\mushroom.dat"
min_Support = 60
start = time.time()

processed_DB = read_data(filename)
FPtree, HeaderTable = create_HTandFPTree(processed_DB, min_Support)

frequent_itemset = []

Mine_Tree(FPtree, HeaderTable, min_Support, set([]), frequent_itemset)
end = time.time()

print("Time Taken is:")
print(end - start)
print("All frequent itemsets:")

print_FPTree(FPtree)
# #print(frequent_itemset)
for itemset, support in frequent_itemset:
     print(f"Itemset: {itemset} - Support: {support:.2f}%")

print(len(frequent_itemset))