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
def helpList():
    print(f'''{74 * '/'}
    +...      Addition
    -...      Subtraction
    *...      Multiplication
    /...      Division
    ^...      Exponentiation
    /-...     Square Roots 
    !...      Factorials (Input Cannot Be Negative)
    Abs...    Absolute Value
    d/r...    Degrees To Radians
    r/d...    Radians To Degrees
    f...      Celsius to Fahrenheit
    kg...     Pound to Kilograms
    lb...     Kilograms to Pound
    pi...     Returns PI
    e...      Returns "e"
    tau...    Returns TAU (2xPI)
    M+...     Save input to memory
    MR...     Recall Memory
    M-...     Clear Memory
    sin...    Sine
    cos...    Cosine
    tan...    Tangent
    asin...   Arc Sine
    acos...   Arc Cosine
    atan...   Arc Tangent
    log10...  Log(10) of Input
    log...    Returns The Appropriate Log of the Input (input1 is the log power)
    rand...   Returns A Random Number Between 0 and 1
    randint...Returns A Random Number Between The Two Inputs''')
    print(74 * '/')


print(74 * '/')
print('Type "help" for a list of abilities')

# Import 'math' and 'random' Libraries
import math
import random

# Loop for getting operation
while True:
    operator = input('What operation do you want to perform?\n')
    # Is operator == to any of out constants or predefine?
    if operator in {'help', '?'}:
        helpList()
    elif operator == 'pi':
        print(math.pi)
    elif operator == 'e':
        print(math.e)
    elif operator == 'tau':
        print(math.pi * 2)
    elif operator == 'MR':
        print(str(memStore))
    elif operator == 'M-':
        memStore = 'Empty'
        print('Memory Cleared')
    elif operator == 'rand':
        print(random.random())
    # Has the user entered in a valid operator?
    elif operator in {'+', '-', '*', '/', '^', '/-', '!', 'Abs', 'd/r', 'r/d', 'M+', 'M-', 'MR', 'sin', 'cos', 'tan',
                      'asin', 'acos', 'atan', 'log10', 'log', 'randint', 'f', 'kg', 'lb', }:
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
if operator not in {'/-', '!', 'Abs', 'd/r', 'r/d', 'M+', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log10', 'f',
                    'kg', 'lb'}:
    # Loop for 2nd number input
    while True:
        num2 = ask_input("Second Number? ")
        # Catch x/0 error case
        if operator == "/" and num2 == 0.0:
            print("ERROR: Math: Cannot divide by 0!")
        # Catch randInt Num1 = x, Num2 =< Num1
        elif operator.lower() == 'randint' and num2 == (num1 >= num2):
            print("ERROR: Random: Can't generate a number if num1 >= num2")
        else:
            break

# Calculations
if operator == '+':
    output = num1 + num2
    print(f'Your answer: {output}')
elif operator == '-':
    output = num1 - num2
    print(f'Your answer: {output}')
elif operator == '*':
    output = num1 * num2
    print(f'Your answer: {output}')
elif operator == '/':
    output = num1 / num2
    print(f'Your answer: {output}')
elif operator == '^':
    output = math.pow(num1, num2)
    print(f'Your answer: {output}')
elif operator == '/-':
    output = math.sqrt(num1)
    print(f'Your answer: {output}')
elif operator == '!':
    output = math.factorial(num1)
    print(f'Your answer: {output}')
elif operator == 'Abs':
    output = math.fabs(num1)
    print(f'Your answer: {output}')
elif operator == 'd/r':
    output = math.radians(num1)
    print(f'Your answer: {output}')
elif operator == 'r/d':
    output = math.degrees(num1)
    print(f'Your answer: {output}')
elif operator == 'M+':
    memStore = num1
    print('Number Stored')
elif operator == 'sin':
    output = math.sin(num1)
    print(f'Your answer: {output}')
elif operator == 'cos':
    output = math.cos(num1)
    print(f'Your answer: {output}')
elif operator == 'tan':
    output = math.tan(num1)
    print(f'Your answer: {output}')
elif operator == 'asin':
    output = math.asin(num1)
    print(f'Your answer: {output}')
elif operator == 'acos':
    output = math.acos(num1)
    print(f'Your answer: {output}')
elif operator == 'atan':
    output = math.atan(num1)
    print(f'Your answer: {output}')
elif operator == 'log10':
    output = math.log10(num1)
    print(f'Your answer: {output}')
elif operator == 'log':
    output = math.log(num2, num1)
    print(f'Your answer: {output}')
elif operator == 'randint':
    output = random.randint(num1, num2)
    print(f'Your answer: {output}')
elif operator.lower() == 'f':
    output = (num1 * 9 / 5) + 32
    print(f'{num1} Celsius is equivalent to {output} fahrenheit')
elif operator == 'kg':
    output = round(num1 / 2.2046, 2)
    print(f'{num1} pounds is equivalent to {output} kg')
elif operator == 'lb':
    output = round(num1 * 2.2046, 2)
    print(f'{num1} kilogram is equivalent to {output} pounds')
