
from random import choice

seçenekler=["rock", "paper","scissors"]
scorePC,scoreMe=0,0

while True:
  pc=choice(seçenekler)
  me=input("rock-paper-scissors :")

  if me=="rock":
    if pc=="paper":
      scorePC+=1
    elif pc=="scissors":
      scoreMe+=1
  elif me=="paper":
    if pc=="scissors":
      scorePC+=1
    elif pc=="rock":
      scoreMe+=1
  elif me=="scissors":
    if pc=="rock":
      scorePC+=1
    elif pc=="paper":
      scoreMe+=1
  if  scoreMe== 2:
      print("Congrats.... You deserved a chocolate...")
      break
  elif scorePC == 2:
      print("Sorry.. You lost the game...")
      break
  else:
    print("Score",scoreMe,"-",scorePC)
    
  print("Computer choice:", pc)

  