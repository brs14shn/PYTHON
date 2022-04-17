

  

**The Fibonacci sequence is a sequence of numbers formed by adding each number with the previous one.**
#SOLUTİON-1

num = int(input())
n1,n2 = 0,1
count = 0

if num == 1:
    print(n1)

while count < num:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

#SOLUTİON-2
n=int(input()) 
def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return fibonacci(n-1)+fibonacci(n-2)
for n in range(n):
   print(fibonacci(n))

