# Python Exercise 43: Develop a program that reads a person's
# weight and height, calculates their Body Mass Index (BMI),
# and shows their status according to the table below:
#
# – BMI below 18.5: Underweight
# – Between 18.5 and 24.9: Ideal weight
# – From 25 up to 30: Overweight

weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = 'Underweight'
elif 18.5 <= bmi < 25:
    category = 'Ideal weight'
elif 25 <= bmi < 30:
    category = 'Overweight'
else:
    category = 'Obese'

print(f"""
📊 Body Mass Index (BMI) Report
-------------------------------
Your weight is: {weight:.2f} kg
Your height is: {height:.2f} m
Your BMI is: {bmi:.2f}

🏷️ Category: {category}
""")
