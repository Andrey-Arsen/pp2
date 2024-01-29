list1=["apple", "banana", "cherry"]
for x in list1:
    print(x)

for i in range(len(list1)):
    print(list1[i])
    
list2=["Arsen", "Sayat", "Marat"]
i=0
while i<len(list2):
    print(list2[i])
    i+=1
    
thislist=["apple", "banana", "cherry"]
[print(x) for x in thislist]