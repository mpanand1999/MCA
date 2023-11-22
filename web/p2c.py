#c. Form a list of vowels selected from a given word (List comprehensions)
word=input("Enter a word: ")
listVowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are {listVowel}")
