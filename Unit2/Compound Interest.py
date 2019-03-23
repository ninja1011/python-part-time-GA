# initialize variables that will be used with input from the user
principle_amount = float(input("Please enter principle"))
compound = float(input("Please enter compound"))
rate = float(input("Please enter rate"))/100
time = float(input("Please enter time"))

# create formulas
a = principle_amount*(1.0 + rate/compound)**(compound*time)
interest_amount = (1.0 + rate/compound)**(compound*time)

print("Compound Interest is", round(a, 2))
print("Compound Interest = Principle Amount + Interest Amount where")
print("Principle amount = ", principle_amount)
print("Interest Amount = ", round(interest_amount, 2))