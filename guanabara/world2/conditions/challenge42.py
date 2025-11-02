# Python Exercise 42: Redo challenge 35 (the triangle problem),
# adding the feature to show what type of triangle will be formed:
#
# – EQUILATERAL: all sides are equal
# – ISOSCELES: two sides are equal, one is different
# – SCALENE: all sides are different

a = float(input('Enter the first side of the triangle (cm): '))
b = float(input('Enter the second side of the triangle (cm): '))
c = float(input('Enter the third side of the triangle (cm): '))

if (a < b + c) and (b < c + a) and (c < a + b):
    print(f'\n✅ The line segments {a:.1f}, {b:.1f}, and {c:.1f} can form a triangle.')

    if a == b == c:
        print("It's an EQUILATERAL triangle.")
    elif a == b or a == c or b == c:
        print("It's an ISOSCELES triangle.")
    else:
        print("It's a SCALENE triangle.")
else:
    print(f"\n❌ The line segments {a:.1f}, {b:.1f}, and {c:.1f} cannot form a triangle.")
