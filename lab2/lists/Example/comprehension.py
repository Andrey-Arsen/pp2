fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

list1=["apple", "banana", "cherry", "kiwi", "mango"]
list1=[x for x in list1 if "a" in x]
print(list1)

newlist=[x for x in fruits if x!="apple"]
print(newlist)

list2=[x for x in list1]
print(list2)

mylist=[x for x in range (10)]
print(mylist)

li=[x for x in range(10) if x<5]
print(li)

newlist=[x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)