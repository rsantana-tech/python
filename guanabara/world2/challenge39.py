# Python Exercise 39:
# Write a program that reads a young person’s year of birth and, according to their age,
# informs whether they still have to enlist for military service, if it is the exact time
# to enlist, or if the enlistment period has already passed. The program should also show
# how much time is left or how long it has been since the deadline.

from datetime import date
from dateutil.relativedelta import relativedelta

# 🎯 Input
birth = date.fromisoformat(input("Enter your birth date (YYYY-MM-DD): "))
today = date.today()

# 📅 Calculations
age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1

enlist_date = birth.replace(year=birth.year + 18)

print(f"\n📆 Today: {today.isoformat()}")
print(f"🎂 Birth date: {birth.isoformat()}")
print(f"🧮 You are {age} year(s) old.")

# ⚖️ Conditional logic
if today < enlist_date:
    diff = relativedelta(enlist_date, today)
    print(f"\n⚠️ You still have {diff.years} year(s), {diff.months} month(s), and {diff.days} day(s) left until enlistment.")
    print(f"📅 Your enlistment date will be: {enlist_date.isoformat()}")
elif today == enlist_date:
    print("\n🎯 It's the exact day to enlist! Go to the recruitment center today.")
else:
    diff = relativedelta(today, enlist_date)
    print(f"\n⏰ You are {diff.years} year(s), {diff.months} month(s), and {diff.days} day(s) late for enlistment.")
    print(f"📅 Your enlistment date was: {enlist_date.isoformat()}")
