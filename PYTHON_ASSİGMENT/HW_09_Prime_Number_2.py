"""
SOLUTION-1
"""
liste=[]
for i in range(2, 101):
        for j in range(2, i):
            if (i % j) == 0:
              break
        else:
            liste.append(i)

print(liste)
"""
SOLUTON-2
"""          
liste=[]
for i in range(2, 101):
        for j in range(2, i):
            if (i % j) == 0:
              print(i, "is not a prime number")
              break
        else:
            print(i,"is a prime number")
