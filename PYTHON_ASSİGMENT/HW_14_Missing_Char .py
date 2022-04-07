



### Missing Char
*Given a non-empty string and an* **int n**, return a new string where the character at index n has been removed. The value of n will be a valid index of a character in the original string (i.e. n will be in the range **0....len(str)-1 inclusive).**




def missing_char(word, n):
  
    if 0<=n<=len(word)-1:
       change=word.replace(word[n],"")
       return change
      
    else:
     return "You must enter a value n between 0 and string length "
     
    


print(missing_char('kitchen', 1))
print(missing_char('kitchen', 0))
print(missing_char('kitchen', 3))
print(missing_char('kitchen', -1))

def missing_char(word, n):
     return (lambda x,y:x[:y]+x[y+1:])(word, n)


print(missing_char('kitchen', 1))
print(missing_char('kitchen', 0))
print(missing_char('kitchen', 4))

def missing_char(word, n):
  change=word.replace(word[n],"")
  return change

print(missing_char('kitchen', 1))
print(missing_char('kitchen', 0))
print(missing_char('kitchen', 4))

def missing_char(word, n):
      first_part = word[:n] 
      last_part = word[n+1:]
      return first_part + last_part

print(missing_char('kitchen', -1))

