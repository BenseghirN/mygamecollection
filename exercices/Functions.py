# Write a function that take two params (price and discount)
# Calculate the final price after applying the discount
# Return the final price

def calculate_final_price(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

input_price = float(input("Enter the original price: "))
input_discount = float(input("Enter the discount percentage: "))
print(f"The final price after applying the discount is: {calculate_final_price(input_price, input_discount)} €")


