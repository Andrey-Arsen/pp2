#1
import datetime
x=datetime.datetime.now()
y=datetime.timedelta(days=5)
print(x-y)

#2
n=datetime.datetime.now()
y=n-datetime.timedelta(days=1)
t=n+datetime.timedelta(days=1)
print("now",x)
print("yesterday",y)
print("tomorrow",t)

#3
x=datetime.datetime.now()
y=x.replace(microsecond=0)
print(y)
print(x.strftime("%f"))

#4
import datetime

a=input()
b=input()
x = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
y = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S")
z = abs((x - y).total_seconds())
print(z)
