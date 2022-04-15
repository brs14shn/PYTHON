
"""Create A Calendar"""-11

import calendar
y = int(input("Input the year : ")) 
m = int(input("Input the month : "))
d = int(input("Input the day : "))
print(calendar.month(y, m))


#Output
# Input the year : 2022
# Input the month : 4
# Input the day : 12
#      April 2022
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30