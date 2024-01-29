list1 =["apple", "banana" ,"cherry"]
list1.remove("banana")
print(list1)

mylist=["apple", "banana", "cherry", "banana", "kiwi"]
mylist.remove("banana")
print(mylist)

list2=["apple", "banana", "cherry"]
list2.pop(1)
print(list2)

thislist=["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

list3=["apple", "banana", "cherry"]
del list3[0:2]
print(list3)
"""
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)"""

list4= ["apple", "banana", "cherry"]
list4.clear()
print(list4)