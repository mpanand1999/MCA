  if str1.endswith("ing"):
        return str1 + "ly"
    else:
        return str1 + "ing"
str1=input("enter a string:")
result=modifystr(str1)
print(result)
