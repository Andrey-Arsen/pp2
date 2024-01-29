class account:
    def __init__(owner, balance=3000):
        owner.bal=balance
    def deposit(owner):
        x=int(input())
        owner.bal+=x
        print(owner.bal)
    def withdraw(owner):
        y=int(input())
        if owner.bal<0:
            print("ERROR")
            print(owner.bal)
        else:
            owner.bal-=y
            print(owner.bal)
    
owner=account()
a=int(input())
for i in range(a):
    x=str(input())
    if x=='b':
        owner.deposit()
    else:
        owner.withdraw()