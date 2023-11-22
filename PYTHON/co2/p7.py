#Add ‘ing’ at the end of a given string.
#If it already ends with ‘ing’, then add ‘ly’

def modifyStr(str1):
    if str1.endswith("ing"):
        return str1 + "ly"
    else:
        return str1 + "ing"
str1 = input("Enter a string: ")
result = modifyStr(str1)
print(result)
