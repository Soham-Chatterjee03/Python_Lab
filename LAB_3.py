"""
rate=int(input("Rate"))
hour=int(input("Hours"))
if (hour<=40):
    pay=hour*rate
else:
    pay=40*rate+1.5*rate*(hour-40)
print("Pay :",pay)
"""

"""
try:
    print("x")
except:
    print("An exception occoured")
"""

"""print(x)"""

"""
try:
    print(x)
except NameError:
    print("variablke is not defined")
except:
    print("Something else occoured")
"""
"""
try:
    print("x")
except:
    print("Something went wrong")
else:
    print("Huulaa")
"""

"""
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try except is finshed")
"""
#RAISE EXCEPTION
"""
x=-1
if(x<0):
    raise Exception("Sorry,no numbers below zero")
"""

"""
x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

"""
"""
try:
    x=int(input("Enyer a number"))
except:
    x="qwe"
if x is "qwe":
    pass
    
elif(x%2==0):
    print("Even")
else:
    print("Odd")
"""

#assignment 3
#1
"""
a=int(input("Enter a number"))
b=int(input("Enter another Number"))
if(a>b):
    print("The first number is greater")
elif(a<b):
    print("The second numner is greater ")
else:
    print("The numbers are equal")
"""
#2
"""
rate=int(input("Rate"))
hour=int(input("Hours"))
if (hour<=40):
    pay=hour*rate
else:
    pay=40*rate+1.5*rate*(hour-40)
print("Pay :",pay)
"""
#3
"""
score=float(input("Enter the score between the reange 0.0-1.0 :"))
if((score>0.0) and (score<1.0)):
        if(score>=0.9):
            print("A")
        elif(score>=0.8):
            print("B")
        elif(score>=0.7):
            print("C")
        elif(score>=0.6):
            print("D")
        else:
            print("F")
else:
    raise Exception("Enter the value in the given range")    
"""

#4
"""
choice=int(input(""1.For Farhenite to Celcious
2.For Celcious to farhenite""))
if(choice==1):
        F=float(input("Enter the temperature in farhenite:"))
        C=(F-32)*(5/9)
        print("THe temp in Celcious is",C)
elif(choice==2):
        C=float(input("Enter the temperature in celcious:"))
        F=(C*(9/5))+32
        print("THe temp in Farhenite is",F)
else:
        print("Wrong input")
"""

#5
"""
num=int(input("Enter a number"))
if(num>=0):
        print("+ve")
else:
        print("-ve")
"""
#6
"""
num=int(input("Enter a number"))
if(num%2==0):
        print("even")
else:
        print("Odd")
"""
#7
"""

a=int(input("Enter A "))
b=int(input("Enter B "))
c=int(input("Enter C "))
if(a>b and a>c):
        print("A is largest")
elif(b>a and b>c):
        print("B is largest")
else:
        print("C is largest")

"""
#8
"""
try:
        rate=int(input("Rate"))
        hour=int(input("Hours"))
except:
        print("Error,Please enter numeric form")
        x="a"
if x is "a":
        pass
elif(hour<=40):
        pay=hour*rate
        print("Pay :",pay)
else:
        pay=40*rate+1.5*rate*(hour-40)
        print("Pay :",pay)
        
"""
        




















        


















