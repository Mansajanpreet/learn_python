#This program gets an items original price.
#and calculate the sale price, with 20% discount.

original_price = float(input("Enter the item original price: "))

#calculate the amount of discount.

discount = original_price * 0.2

#calculate the sale price.

sale_price = original_price - discount

print("the sale price is ", sale_price)