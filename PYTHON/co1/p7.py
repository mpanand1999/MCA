#Get a string from an input string where all occurrences of the first character are replaced with '$' except the first character. eg: onion - oni$n

s=input("Enter a word: ")
c=s[0] 
str1=s.replace(s[0],'$') 
print(c+str1[1:])

