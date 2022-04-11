

"""
How do we test whether there are identical digits in a number sequence?
"""

liste=[1,2,3,4,5,6]

for k in liste:
  if liste.count(k)>=2:
    print("There are repeating elements",k)
    break
  else:
   print("There aren't repeating elements")
   break
   

