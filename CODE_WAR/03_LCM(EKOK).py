

"""1-"""
###MATH MODÜLÜNÜ İLE EKOK BULMA 

from math import gcd as ebob

def ekok(x,y):  ###ebob(a,b)*ekok(a,b)=a*b====>>>>ekok(a,b)=a*b/ebob(a,b) dir
  return int((x*y)/ebob(x,y))

print(ekok(3,25))
print(ekok(12,18))
print(ekok(16,20))
print(ekok(50,26))
print(ekok(18,20))

"""2-"""
a=int(input("sayı 1: "))
b=int(input("sayı2: "))

listea=[]
listeb=[]

for i in range(a,100000):
  if i%a==0:
    listea.append(i)

for i in range(a,1000000):
  if i%b==0:
    listeb.append(i)


set1=set(listea)
set2=set(listeb)

ekok=(set1.intersection(set2))

print(min(ekok))