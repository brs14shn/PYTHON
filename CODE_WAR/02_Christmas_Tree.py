
"""SOLUTION-1"""
count=1
width=20

for i in range(10):
  print(("*"*count).center(width))
  count+=2
print("| |".center(width))


"""SOLUTION-2"""
count=1
width=20
for i in range(10):
  print(f'{"*"*count:^20}')
  count+=2
print(f'{"| |":^20}')