# Python Exercise 38: Write a program that reads
# two integer numbers and compares them, displaying
# on the screen a message:
#
# – The first value is greater
# – The second value is greater
# – There is no greater value, both are equal

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

if number1 > number2:
    print('The first number is bigger.')
elif number2 > number1:
    print('The second number is bigger.')
else:
    print('There is no greater value — both numbers are equal.')
