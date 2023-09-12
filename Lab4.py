"""
list=["apple","orande","mango"]
for i in range (0,3):
    print(list[i])
"""
"""
for i in range(1,5):
    for j in range(i):
        print("*",end=' ')
    print()
"""
"""
var1="HEllo World"
var2="Python Programming"
print(var1[0])
print(var2[1:5])
"""
"""
var1="Soham"
var2="Chatterjee"
print(var1+var2)
print(var1*3)
print("S" in var1)
print("S" not in var1)
print(R"Soh\nv qadsfa\tasdf")
print("asdasd %s asdasd"%var1)
"""
"""
sampleStr="Hello!!"
print("****Iterate over string using for loop****")
for element in sampleStr:
    print(element)

sampleStr="Hello!!"
count=0
print("****Iterate over string using for loop****")
for element in sampleStr:
    if(element=="l"):
        count=count+1
print(count)
"""
"""
st="python is a language"
print(st[-3:])
print('J'+st[1:])
print(st[0:2]+st[-2:])
print(st[::3])
print(st[::-2])
print(st[::-1])
list=['hello','welcome','bye']
print("<.>".join(list))
s="="*5
print(s*5)
s='hello'
print(s.center(10,' '))
print(s.count('l'))
s="Welcome to the world of Python Jython"
x1="ld"
print(s.find(x1,0,len(s)))
x2="ython"
print(s.partition(x2))
t="on"
u="xxyy"
print(s.replace(t,u))
print(s.split(x2))
s="Welcome to the world of Python Jython"
x='0'
u=''
print(s.rsplit(x,3))
"""




#1
"""
n=int(input(" Enter a number "))
s=0
for i in range (n+1):
    s=s+i
print(s)
"""

#2
"""
n=int(input(" Enter a number "))
c=0
for i in range (2,n//2):
    if(n%i==0):
        c=c+1
        break
if (c==1):
    print("Not prime")
else:
    print("Prime")

"""
#3
"""
n=3
for i in range(100,1000):
    m=i
    s=0
    while(m!=0):
       digit=m%10
       s=s+digit**n
       m=m//10
    if i==s:
        print(i)
"""
n=101
num1=0
num2=1
for i in range(2,n):
        c=num1+num2
        print(c)
        num1=num2
        num2=c
print()

    
        


























