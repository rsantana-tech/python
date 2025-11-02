# Python Exercise 40: Create a program that reads two student
# grades and calculates their average, displaying a message at
# the end according to the average achieved:
#
# – Average below 5.0: FAILED
# – Average between 5.0 and 6.9: RECOVERY
# – Average 7.0 or higher: PASSED

first_grade = float(input('Enter your first grade: '))
second_grade = float(input('Enter your second grade: '))
avg_grade = (first_grade + second_grade) / 2

if avg_grade < 5.0:
    msg = 'FAILED'
elif 5.0 <= avg_grade < 7.0:
    msg = 'RECOVERY'
else:
    msg = 'PASSED'

print(f"""
Your average grade is {avg_grade:.2f}.
You have {msg}.
""")
