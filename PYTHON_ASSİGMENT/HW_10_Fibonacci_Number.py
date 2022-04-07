

  

**The Fibonacci sequence is a sequence of numbers formed by adding each number with the previous one.**




fibo=[1,1]
for i in range(8):
  fibo.append(fibo[i]+fibo[i+1])
fibo
