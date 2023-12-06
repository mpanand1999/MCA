#write a python program to read each row from a given csv file and print a list of strings
import csv
with open('employee.csv','r') as file1:
    reader=csv.reader(file1)
    for row in reader:
        print(row)
