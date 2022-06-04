print('Welcome to the calculator!')

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num1 = int(input('Enter your first number here: '))
    num2 = int(input('Enter your second number here: '))

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

def again():
    calcagain = input('Would you like to use calculator again? (Y/N) ')
    if calcagain.upper() == 'Y':
        calculate()

    elif calcagain.upper() == 'N':
        print('See you later.')

    else:
        again()

calculate()