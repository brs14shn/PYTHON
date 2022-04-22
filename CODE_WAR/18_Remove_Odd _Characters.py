
# Remove Odd Characters in a String

str1 = input("Please Enter your Own String : ")

# input==>>The grass is always greener on the other side of the fence.

str2 = ''

for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
        
print("Original String :  ", str1)
print("Final String :     ", str2)

#Output==>> "h rs sawy ree nteohrsd ftefne"
