#6. Enter two list of integers. Check: a. Whether list are of the same length b. whetherlist sums to same value c. whether any value occurs in both


list1 = [8, 6, 7, 4, 5]
list2 = [5, 4, 3, 2, 1]
# a. Check if the lists have the same length
if len(list1) == len(list2):
    print("a. The lists have the same length.\n")
else:
    print("a. The lists have different lengths.\n")
    

# b. Check if the lists have the same sum
print(f"b. sum of list1: {sum(list1)} & sum of list2: {sum(list2)}")
if sum(list1) == sum(list2):
    print(" The lists sum to the same value.\n")
else:
    print(" The lists do not sum to the same value.\n")
    

# c. Check if there are any common values in both lists
common_values = set(list1) & set(list2)
if common_values:
    print(f"c. Common values in both lists: {common_values}\n")
else:
    print("c. There are no common values in both lists.\n")
