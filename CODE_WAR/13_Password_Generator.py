"""How to generate random password from uppercase, 
   lowercase, numbers and symbols."""#13

import random
uppers=[chr(random.randint(65,90)) for i in range(3)] #Letters A-Z  between
lowers=[chr(random.randint(97,122)) for i in range(3)] #Letters a-z between
numbers=[chr(random.randint(48,57)) for i in range(3)]
chars=chr(random.randint(33,47))+chr(random.randint(58,64))

pasw="".join(numbers)+"".join(uppers)+"".join(lowers)+chars

#SHUFFLE

pass_list=list(pasw)
random.shuffle(pass_list)
"".join(pass_list)

#SAMPLE
pass_list=list(pasw)
random.sample(pass_list,k=4)
"".join(pass_list)