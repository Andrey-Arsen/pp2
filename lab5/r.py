with open(r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab5\reg.txt', encoding='utf-8') as file:
    reg=file.read()
import re

#1
x=re.compile(r'^ab*$')
print(x.search("abbbbbs"))
print(x.search("abbbbb"))

#2
x=re.compile(r'ab{2,3}')
print(x.search("ab"))
print(x.search("abbb"))


#3
y=re.compile(r"[a-z_]+[_]{1}+[a-z_]+")
b=y.search("sadd,lalllpa_ml_kok")
print(b)

#4
x=re.compile(r"[A-Z]{1}+[a-z]+")
print(x.findall("OJOkok Akkk KMKs"))

#5
x=re.compile(r"^a.*b$")
print(x.search("amkmkb akmkknb"))

#6
x=re.compile(r"[ ,.]")
print(x.sub(":", "das.sadas,d a.d"))

#7
x=re.compile(r"_(.)")
s="asd_xvv_qwe"
c=x.sub(lambda match: match.group(1).upper(), s)
print(c)
#8
x=re.compile(r'[A-Z][^A-Z]*')
print(x.findall("AnnnAkmkonNnoj<Mkk"))


#9
x=re.compile(r'([a-z])([A-Z])')
print(x.sub(r'\1 \2',"ImmomKmkmlAnkk"))

#10
x=re.compile(r'([a-z])([A-Z])')
print(x.sub(r'\1_\2', "ArsenKbtuAdbe"))