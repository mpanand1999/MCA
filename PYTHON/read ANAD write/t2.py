f1=open('test1.txt','r')
f2=open('text2.txt','w')
content=f1.readlines()
print('content\n',content)
for i in range(0,len(content)):
    if(1%2==0):
        f2.write(content[1])
    else:
        pass
f2.close()
f2=open('text2.txt','r')
content1=f2.read()
print("\nodd lines\n\n",content1)
f2.close()
