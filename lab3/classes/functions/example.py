#1
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#2
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Osapanov", "Dias")

#3
def function(*kids):
    print("he youngest child is " + kids[2])
function("Emil", "Tobias", "Linus")

#4
def function(**kid):
    print("His last name is " + kid["lname"])
function(fname="Tobias", lname="Refsnes")

#5
def function(food):
    for x in food:
        print(x)
fruits=["apple", "banana", "cherry"]
function(fruits)

#6
def func(x):
    return 5*x
print(func(3))
print(func(9))

#7
def recursion(x):
    if(x>0):
        result=x+recursion(x-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion Example Results")
recursion(6)

        
