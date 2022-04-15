

calculator={"+":lambda x,y:x+y,
            "-":lambda x,y:x-y,
            "*":lambda x,y:x*y,
            "/":lambda x,y:x/y
            }
print(calculator["+"](15,5))
print(calculator["-"](15,5))
print(calculator["*"](15,5))
print(calculator["/"](15,5))