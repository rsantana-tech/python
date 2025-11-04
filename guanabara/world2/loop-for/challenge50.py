#Python Exercise 50: Develop a program that reads six integer
# numbers and displays the sum of only those that are even.
# If an entered value is odd, disregard it.
sum_total_even = 0
for c in range(1,7):
    number = int(input(f'Enter the {c}º integer number: '))
    if number % 2 == 0:
        sum_total_even += number
print(f"The sum total even is : {sum_total_even}")