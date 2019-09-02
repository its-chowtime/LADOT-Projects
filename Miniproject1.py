# function and loops project
message = "\n\nClick anywhere and press enter to continue..."
print("""
This program is to show my understanding of what I learned in the last week
Pt 1: Comments | Print | String | Variables
Pt 2: Functions | Whitespace | Parameters(Multiple) | Returns(Multiple)
Pt 3: Boolean | If Elif Else Statements | Boolean Operators""")  # used """ to write a multiline string

input(message)
print("\n\n\n\n\nWhat would you like to calculate? \n")  # \n used to create an extra space

print("Options: [sum(add)], [average(mean)], [multiply(times)], [divide], [loops] \n")

print("Type in below what function you want to use.")
x = str(input())

if x == "loops" or x == "loop":
    print("Choose a range")
    print("Choose the first number:")
    y = int(input())
    print("\nChoose the second number:")
    z = int(input())
else:

    print("\nChoose the first number")
    y = int(input())
    print("\nChoose the second number")
    z = int(input())


def calculate_numbers(y, z):
    add = y + z
    average = (y + z) / 2
    multiply = y * z
    divide = y / z
# using if elif else with boolean operators
    if (x == "sum") or (x == "add"):
        return add
    elif (x == "average") or (x == "mean"):
        return average
    elif (x == "multiply") or (x == "times"):
        return multiply
    elif x == "divide":
        return divide
    elif x == "loops" or x == "loop":
        for num in range(y, z):
            print(num)
    else:
        return "You did not pick an option."


def choose_function(x):
    if (x == "loops") or (x == "loop"):
        return calculate_numbers(y, z)
    else:
        text2 = " and the result is:"
        print(
                "\n" + "You are %sing your inputs" % x  # not sure what the % is and how it works
                + text2)  # combining strings by adding a variable
        return calculate_numbers(y, z)


print(choose_function(x))

print(input("Press enter to exit."))