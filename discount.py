print()
from datetime import datetime 

current_date = datetime.now()
weekday = current_date.weekday()

subtotal = float(input('Enter your subtotal: '))


if weekday == 1 or weekday == 2:
    if subtotal >= 50:
        discount = (subtotal * .10) 
        new_subtotal = subtotal - discount
        tax = (new_subtotal * .06)
        total = new_subtotal + tax 
        
        print(f'Discount amount: ${discount: 0.2f}')
        print(f'Sales tax amount: ${tax: 0.2f}')
        print(f'Total: ${total: 0.2f}')
    elif subtotal < 50:
        difference = 50 - subtotal
        tax = (subtotal * .06)
        total = subtotal + tax
        print(f'Aditional amount needed to recieve discount: ${difference: 0.2f}')
        print(f'Sales tax amount: ${tax: 0.2f}')
        print(f'Total: ${total: 0.2f}')
else: 
    tax = (subtotal * .06)
    total = subtotal + tax
    print(f'Sales tax amount: ${tax: 0.2f}')
    print(f'Total: ${total: 0.2f}')

print()