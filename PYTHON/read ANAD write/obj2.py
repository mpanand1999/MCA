class student:
    def __init__(self,rlno,name):
        self.rlno=rlno
        self.name=name
    def display(self):
        print("Roll No:",self.rlno)
        print("Name",self.name)
#main
stud1=student(26,"ANAND")
stud2=student(25,"JITH")
stud3=student(27,"MANYA")
stud1.display()
stud2.display()
stud3.display()
