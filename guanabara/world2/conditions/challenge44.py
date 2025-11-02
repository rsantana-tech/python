# Python Exercise 44: Create a program that calculates the
# amount to be paid for a product, considering its normal
# price and the payment condition.

product_value = float(input('Enter product value ($): '))

form_payment = int(input("""
Select your payment method:
[0] Cash or Check
[1] Immediate payment by card
[2] Up to 2 installments on the card
[3] 3 or more installments on the card

Your choice: """))

# Calculate final price
if form_payment == 0:
    payment = product_value - (product_value * 0.10)
    form_payment_select = 'Cash or Check'
elif form_payment == 1:
    payment = product_value - (product_value * 0.05)
    form_payment_select = 'Immediate payment by card'
elif form_payment == 2:
    payment = product_value
    form_payment_select = 'Up to 2 installments on the card'
elif form_payment == 3:
    payment = product_value + (product_value * 0.20)
    form_payment_select = '3 or more installments on the card'
else:
    payment = None
    form_payment_select = 'Invalid option'

# Display result
if payment is not None:
    print(f"""
💰 Product value: ${product_value:.2f}
💳 Payment method: {form_payment_select}
✅ Final amount to pay: ${payment:.2f}
""")
else:
    print("❌ Invalid payment option. Please restart and choose between 0 and 3.")
