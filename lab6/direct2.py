#4
import os
l=[]
for i in range(4):
    x=input()
    l.append(x)
file=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories\lab6.txt'
with open(file, "w") as f:
    for i in l:
        f.write(i+'\n')
with open(file, 'r') as f:
    read=f.read()
print(read)

#5
import string
path=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories'
for i in string.ascii_letters:
    file=os.path.join(path, i+'.txt')
    with open(file,'w') as f:
        f.writelines(i)

#6
import shutil
file=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\directories\lab6.txt'
newfile=os.path.join(path, 'copyfile.txt')
shutil.copyfile(file, newfile)

builtin=r"C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab6\builtin.py"
shutil.copyfile(builtin,'abc.py')

#7
def fun(x):
    if os.access(x, os.F_OK):
        os.remove(x)
    else :
        print("error")

afile=r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\abc.py'
fun(afile)
nofile=r'C:\path\to\my\file.txt'

fun(nofile)