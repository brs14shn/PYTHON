
"""Counting all letters,numbers,lower letters and upper letters in an entered sentence"""

s = input()
d={"DIGITS":0, "LETTERS":0, "LOWER":0,"UPPER":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    if c.isalpha():
        d["LETTERS"]+=1
    if c.islower():
        d["LOWER"]+=1
    if c.isupper():
        d["UPPER"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
print("LOWER", d["LOWER"])
print("UPPER", d["UPPER"])


#İNPUT(S)
"""6 Nisan 1453 - 29 Mayıs 1453 tarihleri arasında, 53 gün 
süren yoğun bir kuşatmanın sonucunda Osmanlı Devleti padişahı 
II. Mehmed komutasındaki Osmanlı ordusuBizans İmparatorluğu'nun
 başkenti olan İstanbul'u ele geçirmiştir."""

 #OUTPUT
 # LETTERS : 175
 # DIGITS  : 13
 # LOWER   : 164
 # UPPER   : 11