

def ebob (x, y):
   ebob=1
   if x % y == 0:
       return y   
   for i in range(int(y / 2), 0, -1):
       if x % i == 0 and y % i == 0:
           ebob = i
           break 
   return ebob
   
print("GCD of 12 & 17 =",ebob(12, 17))
print("GCD of 4 & 8 =",ebob(4, 8))
print("GCD of 336 & 360 =",ebob(336, 360))
print("GCD of 336 & 360 =",ebob(100, 200))