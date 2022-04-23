"Steps to convert multiple lists to nested dictionaries"

liste1=['S001', 'S002', 'S003', 'S004']
liste2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
liste3=[85, 98, 89, 92]

#Step-1:"Define a three parameter def function"
#Step-2:"Use zip function to access each iterator elements"
#Step-3:"List comprehension"
def nested_dictionary(liste1,liste2, liste3):
     result = [{x: {y: z}} for (x, y, z) in zip(liste1,lsite2, liste3)]
     return result

print(nested_dictionary(liste1,liste2, liste3))


"Output"
"""[{'S001': {'Adina Park': 85}}, 
{'S002': {'Leyton Marsh': 98}},
 {'S003': {'Duncan Boyle': 89}}, 
{'S004': {'Saim Richards': 92}}]"""
