
"""

Python program that asks the user to enter Celsius temperature (it can be a decimal number),\
 converts the entered temperature into Fahrenheit degree and prints the result.
"""

celsisus=input("lütfen sıcaklığı C giriniz:")
fahrenheit=(1.8*float(celsisus))+32
print("Oda sıcaklığı {} F".format(fahrenheit))

"""Python program that asks the user to enter a distance (it can be a decimal number)\
 in kilometers, converts the entered distance into miles and prints the result."""

km=input("lütfen km giriniz:")
mil=(float(km)*0.62137)
print("50 km {0} mil eder".format(mil))
