import time

class pattern:
  itemset = []
  support = 0

def join(item1, item2):
    y = item1.copy()
    z = item2.copy()
    y.pop()
    z.pop()
    if (len(item1) == 1 or y == z ):
        joined = sorted(set(item1 + item2))
        return joined
    else:
        return None

def downward_closure(itemset, frequent_itemsets):
    for i in range(len(itemset)):
        subset = itemset[:i] + itemset[i + 1:]
        if subset not in frequent_itemsets:
            return False
    return True


C = []
L = []
itemlist = []
database = []
count = []
total = 0
minsup = 99

path = r"D:\UNIVERSITY\Semester 11 (cse400B,350,477)\CSE477\Lab\apri\venv\chess.dat"
fptr = open(path, "r")
n = 0

start_time = time.time()

while True:
    line = fptr.readline()

    if not line:
        break
    n += 1

    token = line.split()
    token.sort()
    itemlist.extend(set(token))
    database.append(set(token))

print(n)
fptr.close()

temp = list(set(itemlist))
temp.sort()

print(len(temp))

# Generate C1
C1 = []
for item in temp:
    #s = itemlist.count(item)*100/n
    s = sum(item in transaction for transaction in database) * 100 / n
    p = pattern()
    p.itemset= [item]
    p.support = s
    C1.append(p)



L1 = []
for i in C1:
    if i.support >= minsup:
      L1.append(i)
      total += 1

L.append(L1)
count.append(total)

L1_items = []
print("L 1 :")
for pa in L1:
    L1_items.append(pa.itemset)
    print("  ",pa.itemset," :", round(pa.support,2))


# Generate other C and L
C2 = []
L2 = []
Ln = 1
for LX in L:
    for i in range(len(LX)):
        for j in range(i + 1, len(LX)):
            itemset1 = LX[i].itemset
            itemset2 = LX[j].itemset
            joined_itemset = join(itemset1, itemset2)
            if joined_itemset is not None:
                if downward_closure(joined_itemset, L1_items):
                    support = sum(
                        set(joined_itemset).issubset(transaction) for transaction in database
                    ) * 100 / n
                    p = pattern()
                    p.itemset= sorted(joined_itemset)
                    p.support = support
                    C2.append(p)


    L1_items.clear()
    L2.clear()
    total = 0

    # if len(C2) == 0:
    #   break


    for m in C2:
        if m.support >= minsup:
            L2.append(m)
            total += 1

    if len(L2) != 0:
      L.append(L2)
      count.append(total)

      Ln += 1
      print("L",Ln," :")
      for pa in L2:
          L1_items.append(pa.itemset)
          print("  ",pa.itemset," :", round(pa.support,2))


    C2.clear()

end_time = time.time()

elapsed_time = end_time - start_time

print()
print("Total Frequent patters in each L :  ",count)

print(f"Elapsed time: {elapsed_time:.4f} seconds")