#write a python program to read a file line by line and store it into a list
file=open('file1.txt','w')
file.write("This attribute returns the raw bytes of the response content. text : The text attribute returns the content as a normal UTF-8 encoded Python string. json() : You can use the json() method to get the response content in JSON format.")
list1=[]
with open('file1.txt','r') as file:
    for line in file:
        list1.append(line.split())
print(list1)
