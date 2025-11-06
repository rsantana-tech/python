# Python Exercise 52: Write a program that reads
# an integer and tells whether or not it is a prime number.


number = int(input('Enter an integer number: '))
divisible_count = 0

for c in range(1, number + 1 ):
    if number % c == 0 :
        divisible_count += 1

if divisible_count == 2 :
    print(f"The number {number} is a prime number")
else:
    print(f"The number {number} is not a prime number ")