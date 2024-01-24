class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj))

def myfunction():
    return True
print(myfunction())

def function():
    return True
if function():
    print("YES")
else:print("NO")

x=200
print(isinstance(x, int))

