price = 19.99
quantity = 3
shipping_cost = 5.99
tax_rate = 0.07
tax_amount = price * quantity * tax_rate

total_price = (price * quantity + 
               shipping_cost + tax_amount)
print("Total price: $", total_price)

total_price = price * quantity + \
    shipping_cost + tax_amount
print("Total price: $", total_price)

PI = 3.14159