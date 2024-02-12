#  menu list
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Create a dictionary for stock with initial values
stock = {"Coffee": 50, "Tea": 30, "Sandwich": 20, "Cake": 15}

# Create a dictionary for price with initial values
price = {"Coffee": 3.50, "Tea": 2.00, "Sandwich": 5.00, "Cake": 3.00}

# Calculate total stock worth
total_stock_worth = 0

for item in menu:
    total_stock_worth += stock[item] * price[item]

# Display the result
print(f"Total stock worth in the cafe: ${total_stock_worth:.2f}")
