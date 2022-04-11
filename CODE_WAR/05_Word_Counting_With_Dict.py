

"""Find the numbers of an entered word with the dictionary"""


word=input("Enter your a word: ")
#I scream, you scream, we all scream for ice cream.

liste=[]

liste=word.split()
frequency=[liste.count(i) for i in liste]

myDict=dict(zip(liste,frequency))
print("Word_Number: ",myDict)

#Output==> Word_Number:  {'I': 1, 'scream,': 2, 'you': 1, 'we': 1, 'all': 1, 'scream': 1, 'for': 1, 'ice': 1, 'cream.': 1}



