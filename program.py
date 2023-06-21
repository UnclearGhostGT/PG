

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')


def add_num():
    sum = float(num1) + float(num2)
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

cal = input('Calculate the sum? [Y/n]: ')
if cal == 'Y':
    add_num()
elif cal == 'n':
    print('Calculation will not run.')
else:
    print('No option or invalid option selected.')