# Python Exercise 36: Write a program to approve a bank loan
# for the purchase of a house. Ask for the value of the house,
# the buyer’s salary, and how many years they will take to pay it off.
# The monthly installment cannot exceed 30% of the salary;
# otherwise, the loan will be denied.

house_value = float(input("Enter the house value ($): "))
salary = float(input("Enter your salary ($): "))
years = int(input("Enter how many years the payment will take: "))

monthly_installment = house_value / (years * 12)
salary_limit = salary * 0.30

print(f"\nMonthly installment: ${monthly_installment:.2f}")
print(f"Salary limit (30%): ${salary_limit:.2f}")

if monthly_installment <= salary_limit:
    print("\n✅ Credit approved!")
else:
    print("\n❌ Credit denied!")
