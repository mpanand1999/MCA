class time:
    def __init__(self):
        self.hours=int(input("enter the hours:"))
        self.minutes=int(input("enter the minutes:"))
        self.second=int(input("enter the second:"))
    def __add__(self,t2):
        hours=self.hours+t2.hours
        minutes=self.minutes+t2.minutes
        second=self.second+t2.second
        total=hours*60*60+minutes*60+second
        return self.convert(total)
    def convert(self,second):
        second=second%(24*3600)
        hours=second//3600
        second%=3600
        minutes=second//60
        second%=60
        return hours,minutes,second

t1=time()
t2=time()
print("total time:",t1+t2)
