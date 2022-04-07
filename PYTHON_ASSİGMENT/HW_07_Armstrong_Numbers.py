#ARMSTRONG NUMBER"




A number is thought of as an Armstrong number if the sum of its own digits raised to the power
 number of digits gives the number itself. For example, 0, 1, 153, 370, 371, 407 are three-digit 
Armstrong numbers and, 1634, 8208, 9474 are four-digit Armstrong numbers and there are many more
"""

while True:
##isdigit(0-9) arasında karakter alır
  number=input("Enter a positive integer number :")
  digits=len(number)
  sum=0
  if not number.isdigit():
      print(number, "is invalid entry.Please enter valid input.")
  elif int(number)>=0 :
      for i in range(digits):
        sum+=int(number[i])**digits
      if sum==int(number):
        print(number, "is an Armsrong Number. ")
        breakpoint
      else:
        print(number,"is not an Armstong number")
        break

        
