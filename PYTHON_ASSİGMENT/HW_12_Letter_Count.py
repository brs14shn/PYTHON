

### LETTER COUNT ###

*1.Count the number of each letter in a sentence.*

- The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.-
-Write a Python program that;-

**takes a sentence from the user,**

**counts the number of each letter/chars of the sentence,**

**collects the letters/chars as a key and the counted numbers as a value in a dictionary.**



word=input("Enter your a sentence :")
#liste=list(word)
dict1={}

for  i in word:
  dict1[i]=word.count(i)

print(dict1)

b=input("Enter your a word: ")

def word(a):
  dict1={}
  for  i in a:
    dict1[i]=a.count(i)
  return dict1

print(word(b))
