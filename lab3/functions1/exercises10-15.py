#10
def pal(x):
    for i in range(len(x)):
        if x[i]!=x[len(x)-i-1]:
            return False
    return True
x=input()
if pal(x):
    print("palindrome")
else:
    print("Not")
    
#11
def his(x):
    for i in x:
        j=1
        while j<=i:
            print("*", end=' ')  
            j+=1
        print()
his([4,9,7])

#12
import random
def fun(x, ran):
    if x==ran:
        return False
    return True
b=True
print("Hello ! What is your name?")
name=input()
print("Well," ,name ,", I am thinking of a number between 1 and 20.")
print("Take a guess")
ran=random.randint(1, 20)
print(ran)
n=0
while b:
    x=int(input())
    n+=1
    if x<ran:
        print("Your guess is too low")
    elif x>ran:
        print("Your guess is too high")
    if x!=ran:
        print("Take a guess")
    if fun(x, ran)==False:
        print("Good job,",name,"! You guesse my number in", n, "gueasses")
    b=fun(x, ran)