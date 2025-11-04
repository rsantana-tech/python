#Python Exercise 49: Redo challenge 9, displaying the multiplication
# table of a number chosen by the user, but this time using a for loop.

number = int(input('Enter a number: '))
print(f" Multiplication table of {number}")
for mult in range(11):
    print(f"""{number:>2} x  {mult} = {number * mult:>3}""")
