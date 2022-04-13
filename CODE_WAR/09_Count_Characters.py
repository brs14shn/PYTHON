

"""How do you find the number of characters specified in a text file"""

def count_char(text, char):
  count = 0
  for i in text:
    if i == char:
      count += 1
  return count

  #filename==>>istiklal marşı.txt
  #İlk iki kıta 

with open("istiklal marşı.txt","r") as f:
  text = f.read()

print(count_char(text, "O"))
print(count_char(text, "a"))
print(count_char(text, "e"))

#Output==>>2,25,21

"""All Characters Number"""

def word(text):
  dict1={}
  for  i in text:
    dict1[i]=text.count(i)
  return dict1


with open("istiklal marşı.txt","r") as f:
  text= f.read()
print(word(text))

#Output==>>{'K': 2, 'o': 7, 'r': 15, 'k': 15, 'm': 19, 'a': 35, 
# ',': 7, ' ': 44, 's': 6, 'ö': 3, 'n': 27, 'e': 21, 'z': 6, 'b': 8, 
# 'u': 7, 'ş': 2, 'f': 1, 'l': 24, 'd': 12, 'y': 6, 'ü': 6, 'c': 5,
#  ';': 2, '\n': 7, 'S': 2, 't': 10, '.': 3, 'O': 2, 'i': 20, 
# 'ı': 12, 'p': 2, 'Ç': 1, 'ç': 1, 'h': 4, 'â': 4, '!': 1, 'g': 1,
#  '…': 1, '?': 1, 'H': 2, "'": 1}









