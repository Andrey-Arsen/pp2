#1
import os
path=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories'
d=[]
l=[]
al=[]
for name in os.listdir(path):
    direct=os.path.join(path, name)
    if os.path.isdir(direct):
        d.append(name)
    if not os.path.isdir(direct):
        l.append(name)
    al.append(name)
print(d)
print(l)
print(al)

#2
file=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories\lab6.txt'
d = {
    "exist": False,
    "read": False,
    "write": False,
    "execute": False
}
d["exist"]=os.access(file, os.F_OK)
d["read"]=os.access(file, os.R_OK)
d["write"]=os.access(file, os.W_OK)
d["execute"]=os.access(file, os.X_OK)
print(d)

#3
path=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories\lab6.txt'
if os.access(path, os.F_OK):  #if os.path.exists(path):
    print("exists")
    direc, fname=os.path.split(path)
    print(direc)
    print(fname)
print(os.path.dirname(path))
print(os.path.basename(path))

#4
path=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories\lab6.txt'
n=0
with open(path) as txt:
    for k in enumerate(txt):
        n+=1
print(n)