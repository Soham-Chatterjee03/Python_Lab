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

    

        




















        


















