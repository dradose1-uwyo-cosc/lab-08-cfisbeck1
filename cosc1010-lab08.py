# Connor Fisbeck
# UWYO COSC 1010
# 11/10/2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# got help from jhett


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def check_convert_str(string):
    # check if string is an int or a float and converts the string to that type
    # returns "null" if string wasnt converted
    given = string
    is_float = False
    decimals = 0
    for i in string:
        if i == ".":
            decimals += 1
            if decimals == 1:
                is_float = True
            elif decimals > 1:
                return False
    if is_float == True:
        str_float = float(string)
        if type(str_float) == float:
            return str_float
        else:
            return False
    else:
        str_int = int(string)
        if type(str_int) == int:
            return str_int
        else:
            return False




print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope_intercept(m,b,xlower,xupper):
    # calculate y values using point-slope formula
    m = check_convert_str(m)
    b = check_convert_str(b)
    xlower = check_convert_str(xlower)
    xupper = check_convert_str(xupper)
    if xlower < xupper and type(xupper) == int and type(xlower) == int:
        x = []
        y = []
        while xlower <= xupper:
            x.append(xlower)
            y.append(m * xlower + b)
            xlower += 1
        return f"x = {x}",f"y = {y}"
    else:
        return False



# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
user_exit = False
while user_exit == False:
    m = input("Enter your slope m: ").lower()
    if m == "exit":
        user_exit = True
        break
    b = input ("Enter your y-intercept b: ").lower()
    if b == "exit":
        user_exit = True
        break
    xlower = input ("Enter your lower x bound as an integer: ").lower()
    if xlower == "exit":
        user_exit = True
        break
    xupper = input ("Enter your upper x bound as an integer: ").lower()
    if xupper == "exit":
        user_exit = True
        break
    print(slope_intercept(m,b,xlower,xupper))


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def sqrt(a,b,c):
   # function to calculate square root portion of quadratic formula
    a = check_convert_str(a)
    b = check_convert_str(b)
    c = check_convert_str(c)
    result = (b**2 - 4*a*c)**(1/2)
    if a == False or b == False or c == False:
        return False
    if result < 0:
        return False
    else:
        return result



def quadratic(a,b,c):
    #calculate the quadratic formula
    s = sqrt(a,b,c)
    a = check_convert_str(a)
    b = check_convert_str(b)
    c = check_convert_str(c)
    if s != False:
        result1 = (-b + s)/(2*a)
        result2 = (-b - s)/(2*a)
        return f"x = {result1} and x = {result2}"
    else:
        return False

user_exit = False
while user_exit == False:
    a = input("Enter a for quadratic formula: ").lower()
    if a == "exit":
        user_exit = True
        break
    b = input ("Enter b for quadratic formula: ").lower()
    if b == "exit":
        user_exit = True
        break
    c = input ("Enter c for quadratic formula: ").lower()
    if c == "exit":
        user_exit = True
        break
    print(quadratic(a,b,c))
