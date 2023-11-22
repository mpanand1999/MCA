#Find the sum of all items in a list using function
def sumList(list1):
    total = 0
    for i in list1:
        total += i
    return total

list1 = [1, 2, 3, 4, 5]
result = sumList(list1)
print("Sum of the list:", result)
