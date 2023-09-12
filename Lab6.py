#Tuple
"""
num=[10,20,30,(10,20),40]
ctr=0
for n in num:
    if isinstance(n,tuple):
        break
    ctr=ctr+1
print(ctr)
"""
"""
tup=tuple("index tuple")
print(tup)
index=tup.index("p")
print(index)
index=tup.index("p",5)
print(index)
index=tup.index("e",3,6)
print(index)
#ValueError Exception
#index=tup.index("y")
t=(2,4,6,5,8,6,3,1,6,4,9)
slice=t[3:5]
print(slice)
slice=t[:6]
print(slice)
"""
#Dictionary
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
thisdict['School']="DPS School"
print(thisdict)
thisdict['Name']="Soham"
print(thisdict)
thisdict['brand']="Suzuki"
print(thisdict)
person={'name':'Phil','age':22}
print(person)
person.clear()
print(person)
person={1:'Soham',2:'Sanjana',3:'Srinjay'}
print(person)
dic={1:1,2:2,3:3}
print(dic)
"""
"""
d={i:i**3 for i in range(1,15,2)}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(len(d))
"""
"""
d1={1:100,2:200,3:300}
d2={4:400,5:500}
d1.update(d2)
print(d1)
sales={'apple':2,'orange':3,'grapes':4}
print(sales)
element=sales.pop('guava','banana')
print(element)
print(sales)
dict={'a':100,'b':120,'c',150}
"""

"""
statesAndCapitals={'Gujrat':'Gandhinagar','Mharashtra':'Mumbai','Rjasthan':'Jaipur','Bihar':'Patna'}
for state in statesAndCapitals:
    print(state)
keys=['red','green','blue']
values=['#FF0000','#HEHEHE','#kjhhgssd']
dict1=dict(zip(keys,values))
print(dict1)
my_dict={'x':500,'y':5874,'z':560}
key_max=max(my_dict.keys(),key=(lambda k:my_dict[k]))
print(0my_dict)
d={'data1':100,'data2':-54,'data3':247}
"""
#set
"""
a=set((1,2,3,4,5,7,9))
b=set((1,3,5,7,9))
print(a|b)
print(a&b)
print(a-b)
print(a^b)
"""
def compn(n):
    for i in range(2,n):
        if(n%i)==0:
            return True
        return False
a={x for x in range(1,11)if (x%2)==0}
b=[x for x in range(1,21)]
b=set(list(filter(compn,b)))
print(a)
print(b)
a.add(0)
print(a)
print(a.issuperset(b))
print(len(a))
