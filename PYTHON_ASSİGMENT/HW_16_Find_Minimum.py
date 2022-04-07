

#FİND MİNUMUM
**Define a function named my_min to find the min of the inputted numbers.**

*1.DEF FONKSİYONUNU KULLANMA*

-MAP
-LAMBDA
-ARGS
-KWARGS
-MİN



# iterable=(1,2,3,4)
# fonksiyon=lambda x :min((x))
def my_min(*a):
    b=min(map(lambda x:x,a))
    return b

print(my_min(2,3,4,1,-1))
print(my_min(3,8,-9,0,12,1.2))
print(my_min(-100))

def my_min(*arg):
  if len(arg) == 1 :
    return min(arg)
  else :
    smallest_number = min(*arg)
    return smallest_numberdef my_min(*arg):
  if len(arg) == 1 :
    return min(arg)
  else :
    smallest_number = min(*arg)
    return smallest_number


