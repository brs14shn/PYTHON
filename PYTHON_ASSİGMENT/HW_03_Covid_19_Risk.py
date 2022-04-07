#COVİD-19 RİSK ESTİMATE

"""Estimating the risk of death from coronavirus  
Consider the following questions in terms of True/False regarding anyone else. 
Are you a cigarette addict older than 75 years old? Variable → age
Do you have a severe chronic disease? Variable → chronic
Is your immune system too weak? Variable → immune
Set a logical algorithm using boolean logic operators (and/or) and the given variables
 in order to give us True (there is a risk of death) or False (there is not a risk of death) as a result.
"""

age=input("Are you a cigarette addict older than 75 years old?: ")
chronic=input("Do you have a severe chronic disease?: ")
immune=input("Is your immune system too weak?: ")
risk=age and chronic and immune
print(risk) # True(ölüm riski var)),False(ölüm riski yok)

age=input("Are you a cigarette addict older than 75 years old?: ")
chronic=input("Do you have a severe chronic disease?: ")
immune=input("Is your immune system too weak?: ")
risk =(age and chronic and immune)
if risk==True:
   print("You have a risk a death")
else:
   print("No risk")
