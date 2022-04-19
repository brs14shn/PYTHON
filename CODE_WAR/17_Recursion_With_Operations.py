

"Use recursion to calculate the sum of all items in the list"
def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0] + calc(list[1:]) 

list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)

#Output==>15



"""All items in the list using recursion to calculate the sum of their squares"""
def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0]**2 + calc(list[1:]) 

list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)
