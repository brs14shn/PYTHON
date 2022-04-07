
"""How do we get the output that moves the 
robot to 0 on the x-axis and -10 on the y-axis?"""

command=["right 20","right 30","left 50","up 10","down 20"]
command
#Coordinate to be reached output [x=0,y=-10]

command[0].split() #===>>output====>>["right",20] 

command[0].split()[1] ##=====>> "20" 

command=["right 20","right 30","left 50","up 10","down 20"]
x=y=0
for i in range(len(command)):
  if command[i].startswith("r"):x=x+int(command[i].split()[1])
  elif command[i].startswith("l"):x=x-int(command[i].split()[1])
  elif command[i].startswith("d"):y=y-int(command[i].split()[1])
  elif command[i].startswith("u"):y=y+int(command[i].split()[1])
[x,y]