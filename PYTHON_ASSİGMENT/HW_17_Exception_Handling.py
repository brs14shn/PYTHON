fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
num = 3
while num > 0:
    try:
        print("You have {} right.".format(num))
        index = int(input("Please enter index number :"))
        print("My favorite fruit is", fruits[index])

    except IndexError:
        num -= 1
        print("Index Error raised.You have {} right left. Try again!".format(num))

    except ValueError:
        num -= 1
        print("Value Error raised.You have {} right left. Try again!".format(num))

    else:
        print("Congrats! You've entered a valid input")
        break

    finally:
        print("Our fruits are always fresh!")