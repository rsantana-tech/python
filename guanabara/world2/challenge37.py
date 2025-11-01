# Python Exercise 37: Write a Python program that reads
# any integer number and asks the user to choose the base
# for conversion: 1 for binary, 2 for octal, and 3 for
# hexadecimal.

number = int(input('Enter an integer number: '))
choice = int(input("""
Choose a number to convert the base...
[ 1 ] Binary
[ 2 ] Octal
[ 3 ] Hexadecimal

Your choice: """))

if choice == 1:
    converted = bin(number)[2:]
    base_name = "binary"
elif choice == 2:
    converted = oct(number)[2:]
    base_name = "octal"
elif choice == 3:
    converted = hex(number)[2:].upper()
    base_name = "hexadecimal"
else:
    converted = None

if converted:
    print(f"\nThe number {number} converted to {base_name} is {converted}.")
else:
    print("\nInvalid option. Please choose 1, 2, or 3.")
