"""
values=[]
for i in range(5):
    nvalue=int(input("Enter a number"))
    values+=[nvalue]
print("Creating a histogram from values")
print("%s %10s %10s"%("Elements","Value","Histogram"))
for i in range(len(values)):
    print("%7d %10d %s"%(i,values[i],"*"*values[i]))
"""

"""
table1=[[1,2,3],[4,5,6]]
print("Vaslues in table by row are")
for row in table1:
    for item in row:
        print(item,end="")
    print()
"""
def push(lis,val):
    if(top==(len(lis))):
        print("OverFlow")
    if(top==-1):
        top=top+1
        lis[top]=val
    else:
        top=top+1
        lis[top]=val

def pop(lis):
    if(top==-1):
        print("UnderFlow")
        return -1
    else:
        a=lis[top]
        top=top-1
        return top

while(n!=-1):
    n=int(input("Enter your choice"))
    if(n==1):
        val=int(input("Enter a number"))
        push(lis,val)
    elif(n==2):
        val=pop(lis)
    elif(n==3):
        val=lis[top]
        print(val)
    elif(n==4):
        for i in range(len(lis)):
            print(lis[i])











        
