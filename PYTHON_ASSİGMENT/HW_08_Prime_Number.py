

A prime number is a whole number greater than 1 whose only factors are 1 and itself. 
A factor is a whole number that can be divided evenly into another number. 
The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29. 
Numbers that have more than two factors are called composite numbers.
"""

n=int(input("Enter a positive number: "))
count=0

for i in range(1,n+1):
  if n%i==0:
    count+=1
if (n==0) or (n==1) or (count>=3):
  print(n, "is a not prime number")
else:
  print(n, "is a prime number")
