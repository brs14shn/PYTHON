
"Converting two lists into a dictionary pairs with dict compheresion"

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

#zip(iterator1, iterator2, iterator3 ...)

myDict = {k: v for k, v in zip(keys, values)}
print("Dictionary Items  :  ",  myDict)

