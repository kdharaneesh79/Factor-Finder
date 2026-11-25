
import math
import sys

print('''Factor Finder, by Al Sweigart

A number's factors are two numbers that, when multiplied
with each other, produce the number.

For example:
2 x 13 = 26
1 x 26 = 26

The factors of 26 are 1, 2, 13, and 26.

If a number has only two factors (1 and itself),
it is called a prime number.
Otherwise, it is called a composite number.

Can you discover some prime numbers?
''')

while True:
    # Main program loop
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')

    # Exit the program
    if response.upper() == 'QUIT':
        print("Thank you for using Factor Finder!")
        sys.exit()

    # Validate input
    if not (response.isdecimal() and int(response) > 0):
        print("Please enter a valid positive whole number.")
        continue

    number = int(response)

    factors = []

    # Find the factors of the number
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    # Remove duplicate factors
    factors = list(set(factors))

    # Sort the factors
    factors.sort()

    # Display the results
    for i, factor in enumerate(factors):
        factors[i] = str(factor)

    print(', '.join(factors))

    # Identify prime or composite number
    if len(factors) == 2:
        print(number, "is a Prime Number.")
    else:
        print(number, "is a Composite Number.")
