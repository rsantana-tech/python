# #Python Exercise 54: Create a program that reads the birth year of seven people.
# At the end, show how many of them have not yet reached legal adulthood and how many are already
from datetime import datetime

year_atual = datetime.now().year
adult = 0
lower = 0

for i in range(7):
    birth = int(input('Enter year you birth:'))
    age = year_atual - birth
    if age >= 18:
        adult += 1
    else:
        lower += 1
print(f"""
Adult: {adult}
lower:{lower}""")