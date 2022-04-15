

"""
Algorithm that combines the first letters 
of the fruits in the list and makes a string 
output='ABPAO'
"""
#SOLUTİON-1
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

for i in map(lambda x: x[0:1],fruit):
  print(i,end="")

#SOLUTİON-2
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

a=(map(lambda x: x[:1],fruit))

word="".join(a)
print(word)