

###FİZZ BUZZ NUMBERS ###

1.Print numbers from 1 to 100 inclusively following these instructions:
- if a number is multiple of 3, print "Fizz" instead of this number,-
-if a number is multiple of 5, print "Buzz" instead of this number,-
-for numbers that are multiples of both 3 and 5, print "FizzBuzz",-
print the rest of the numbers unchanged.
"""

def fizz_buzz(num):
  if num%3==0 and num%5==0:
    return "FizzBuzz"
  elif num%5==0:
    return "Buzz"
  elif num%3==0:
    return "Fizz"
  else:
    return str(num)
print(fizz_buzz(3))
print(fizz_buzz(13))
print(fizz_buzz(33))
print(fizz_buzz(35))
