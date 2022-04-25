"""
How to listify the list of given strings individually using Python map.
"""
color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print("Original list: ")
print(color) 
print("\nAfter listify the list of strings are:") 
result = list(map(list, color)) #map(function,iterable) list is a built-function.
print(result)

#Output=>[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

