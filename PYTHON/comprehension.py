list1=[2,4,-6,-8,9]
list2=[i for i in list1 if(i>0)];
print(f'positive list ={list2}')






n=[1,2,3,4,5]
sq=[i**2 for i in n]
print(f'the squre of the number : {sq}')


word=input("Enter a String:")
vowel=[i for i in word if i in 'aeiouAEIOU']
print(f"Vowels in the Word are:{vowel}")


w=input("Enter any Characters:")
ordinals=[ord(i) for i in w]
print(ordinals)
