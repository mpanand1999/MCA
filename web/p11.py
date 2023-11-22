#11. Accept a filename from the user and print an extension of that

filename=input("Enter the filename:")
extension=filename.split(".")
print("The extension of the file is:", extension[-1])
