def hotel_cost(num_nights):
    # Assuming a price of $100 per night for the hotel
    return num_nights * 100

def plane_cost(city_flight):
    # Assigning flight costs based on the chosen city
    if city_flight == "New York":
        return 300
    elif city_flight == "Paris":
        return 500
    elif city_flight == "Tokyo":
        return 700
    else:
        return 0  # Return 0 if city is not recognized

def car_rental(rental_days):
    # Assuming a daily rental cost of $50 for the car
    return rental_days * 50

def holiday_cost(city_flight, num_nights, rental_days):
    # Calling each function to get individual costs
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    rental = car_rental(rental_days)
    
    # Calculating total cost
    total_cost = hotel + flight + rental
    return total_cost

# Get user inputs
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate and print the total holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)
print("Your total holiday cost is:", total_cost)

