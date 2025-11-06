# Python Exercise 51: Develop a program that reads the first term
# and the common difference of an arithmetic progression (A.P.).
# At the end, display the first 10 terms of this progression.

a1 = int(input('Enter a first term (a1): '))
r = int(input('Enter a difference (r): '))
terms = int(input('Enter how many terms: '))

for number in range(a1, a1 + (terms * r), r):
    print(number)