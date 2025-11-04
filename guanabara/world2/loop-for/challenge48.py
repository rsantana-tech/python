# Python Exercise 48: Write a program that calculates the sum of
# all numbers that are multiples of three and are found
# in the range from 1 to 500.

sum_total = 0

for c in range(1, 501):
    if c % 3 == 0:
        sum_total += c

print(sum_total)
