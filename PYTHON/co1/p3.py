#Write a program to count the occurrences of each word in a line of text
s=input ("Enter a sentence: ");
print(s)
wordsList =s.split()
print(wordsList)
for i in wordsList:
    print (f"{i} occurs {wordsList.count(i)} times")
