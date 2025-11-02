# Python Exercise 41: The National Swimming Confederation needs a
# program that reads an athlete’s year of birth and shows their
# category according to their age.

# – Up to 9 years old: CHILD (MIRIM)
# – Up to 14 years old: YOUTH (INFANTIL)
# – Up to 19 years old: JUNIOR
# – Up to 25 years old: SENIOR
# – Above 25 years old: MASTER

from datetime import date

birth = date.fromisoformat(input('Enter your birth date (YYYY-MM-DD): '))
today = date.today()

age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1

if age <= 9:
    category = 'CHILD (MIRIM)'
elif age <= 14:
    category = 'YOUTH (INFANTIL)'
elif age <= 19:
    category = 'JUNIOR'
elif age <= 25:
    category = 'SENIOR'
else:
    category = 'MASTER'

print(f"""
🏊 Athlete's age: {age} year(s)
📘 Category: {category}
""")
