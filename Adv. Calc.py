import sys
for i in sys.path:
    print(i)

def ask_input(text_prompt):
    # Divine local variable
    converted_num = math.nan

    # Wait for valid numerical input
    while True:
        num = input(text_prompt)
        try:
            # Try to typecast the input to a float
            float(num)
        except ValueError:
            # Catch the exception if it is not a number
            print("ERROR: Syn: Invalid Num")
        else:
            # Typecasting
            converted_num = float(num)
            break
    return converted_num

# Help List

def abilitiesList():
    print("+...      Addition")
    print("-...      Subtraction")
    print("*...      Multiplication")
    print("/...      Division")
    print("^...      Exponentiation")
    print("/-...     Square Roots ")
    print("!...      Factorials (Input Cannot Be Negative)")
    print("Abs...    Absolute Value")
    print("d/r...    Degrees To Radians")
    print("r/d...    Radians To Degrees")
    print("f...      Celsius to Fahrenheit")
    print('kg...     Pound to Kilograms')
    print('lb...     Kilograms to Pound')
    print("pi...     Returns PI")
    print("e...      Returns 'e'")
    print("tau...    Returns TAU (2xPI)")
    print("M+...     Save input to memory")
    print("MR...     Recall Memory")
    print("M-...     Clear Memory")
    print("sin...    Sine")
    print("cos...    Cosine")
    print("tan...    Tangent")
    print("asin...   Arc Sine")
    print("acos...   Arc Cosine")
    print("atan...   Arc Tangent")
    print("log10...  Log(10) of Input")
    print("log...    Returns The Appropriate Log of the Input (input1 is the log power)")
    print("rand...   Returns A Random Number Between 0 and 1")
    print("randint...Returns A Random Number Between The Two Inputs")
    print("//////////////////////////////////////////////////////////////////////////")

print("//////////////////////////////////////////////////////////////////////////")
print("Type 'help' for a list of abilities")

# Import 'math' and 'random' Libraries
import math
import random

# Loop for getting operation
while True:
    operator = input("What operation do you want to perform?\n")
    # Is operator == to any of out constants or predefine?
    if operator in {'help', '?'}:
        abilitiesList()
    elif operator == "pi":
        print(math.pi)
    elif operator == "e":
        print(math.e)
    elif operator == "tau":
        print(math.pi*2)
    elif operator == "MR":
        print(str(memStore))
    elif operator == "M-":
        memStore = "Empty"
        print("Memory Cleared")
    elif operator == "rand":
        print(random.random())
    # Has the user entered in a valid operator?
    elif operator in {'+', '-', '*', '/', '^', '/-', '!', 'Abs', 'd/r', 'r/d', 'M+', 'M-', 'MR', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log10', 'log', 'randint', 'f', 'kg', 'lb',}:
        break
    else:
        print("ERROR: Invalid Operator")

# Loop for 1st number input
while True:
    num1 = ask_input("First Number? ")
    # Catch asin and acos out of bounds error case
    if operator in {'asin', 'acos'} and (num1 > 1 or num1 < -1):
        print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
    elif operator == "!" and num1 < 0:
        print("ERROR: Math: Factorials only accept inputs > 0")
    else:
        break

# Does the operation require a 2nd input?
if not operator in {'/-', '!', 'Abs', 'd/r', 'r/d', 'M+', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log10', 'f', 'kg', 'lb'}:
    # Loop for 2nd number input
    while True:
        num2 = ask_input("Second Number? ")
        # Catch x/0 error case
        if operator == "/" and num2 == 0.0:
            print("ERROR: Math: Cannot divide by 0!")
        # Catch randInt Num1 = x, Num2 =< Num1
        elif operator.lower() == 'randint' and num2 == (num1>=num2):
            print("ERROR: Random: Can't generate a number if num1 >= num2")
        else:
            break

# Calculations
if operator == "+":
    output = num1 + num2
    print("Your Answer: "+str(output))
elif operator == "-":
    output = num1 - num2
    print("Your Answer: "+str(output))
elif operator == "*":
    output = num1 * num2
    print("Your Answer: "+str(output))
elif operator == "/":
    output = num1 / num2
    print("Your Answer: "+str(output))
elif operator == "^":
    output = math.pow(num1, num2)
    print("Your Answer: "+str(output))
elif operator == "/-":
    output = math.sqrt(num1)
    print("Your Answer: "+str(output))
elif operator == "!":
    output = math.factorial(num1)
    print("Your Answer: "+str(output))
elif operator == "Abs":
    output = math.fabs(num1)
    print("Your Answer: "+str(output))
elif operator == "d/r":
    output = math.radians(num1)
    print("Your Answer: "+str(output))
elif operator == "r/d":
    output = math.degrees(num1)
    print("Your Answer: "+str(output))
elif operator == "M+":
    memStore = num1
    print("Number Stored")
elif operator == "sin":
    output = math.sin(num1)
    print("Your Answer: "+str(output))
elif operator == "cos":
    output = math.cos(num1)
    print("Your Answer: "+str(output))
elif operator == "tan":
    output = math.tan(num1)
    print("Your Answer: "+str(output))
elif operator == "asin":
    output = math.asin(num1)
    print("Your Answer: "+str(output))
elif operator == "acos":
    output = math.acos(num1)
    print("Your Answer: "+str(output))
elif operator == "atan":
    output = math.atan(num1)
    print("Your Answer: "+str(output))
elif operator == "log10":
    output = math.log10(num1)
    print("Your Answer: "+str(output))
elif operator == "log":
    output = math.log(num2, num1)
    print("Your Answer: "+str(output))
elif operator == "randint":
    output = random.randint(num1, num2)
    print("Your Answer: "+str(output))
elif operator.lower() == 'f':
    output = (num1 * 9 / 5) + 32
    print(f'{num1} Celsius is equivalent to {(num1 * 9 / 5) + 32} fahrenheit')
elif operator == 'kg':
    output = (num1 / 2.2046)
    print(f'{num1} pounds is equivalent to {round(num1 / 2.2046, 2)} kg')
elif operator == 'lb':
    output = (num1 * 2.2046)
    print(f'{num1} kilogram is equivalent to {round(num1 * 2.2046, 2)} pounds')
