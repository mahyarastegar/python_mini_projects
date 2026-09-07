# ==========================================
# Basics: User Input & Type Conversion
# ==========================================

# Greeting interactive input
user_name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(f"{user_name} likes {favorite_color}")

# Calculating age from birth year
birth_year = input("Birth year: ")
# Converting string input to integer
age = 2026 - int(birth_year)
print(f"You are {age} years old.")

# Weight conversion: Pounds to Kilograms
weight_lbs = input("Weight (lbs): ")
kilo_weight = int(weight_lbs) * 0.4536
print(f"Weight in Kilos: {kilo_weight:.2f}")