# My Name: [Your Name Here]
# Date: November 18, 2025
# Project Title: Daily Calorie Tracker CLI

# Task 1: Setup & Introduction [cite: 21]
print("=========================================")
print("👋 Welcome to the Simple Calorie Tracker!")
print("This tool helps you quickly log your meals and total up your daily calories. [cite: 11]")
print("=========================================")

# --- Setting up our data structures ---
meal_names = []  # List to hold meal names (like "Breakfast") 
calorie_amounts = [] # List to hold calorie numbers (like 350) 

# --- Get the Daily Limit ---
# We'll ask for this first so we can use it later
while True:
    try:
        daily_limit = float(input("\nWhat is your daily calorie limit? (e.g., 2000): "))
        if daily_limit <= 0:
            print("Please enter a positive limit.")
            continue
        break
    except ValueError:
        print("Oops! Please enter a valid number for your limit.")


# Task 2: Input & Data Collection [cite: 27]
while True:
    try:
        num_meals = int(input(f"\nHow many meals are you tracking today?  "))
        if num_meals < 1:
            print("Please enter at least 1 meal.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")

print(f"\n--- Entering {num_meals} Meals ---")

# Loop to collect meal data
for i in range(num_meals):
    # 1. Get the meal name
    name = input(f"Meal #{i+1} Name (e.g., Lunch): [cite: 30] ")
    meal_names.append(name)

    # 2. Get the calorie amount (and convert it to a number!) 
    while True:
        try:
            calories = float(input(f"Calories for {name}:  "))
            if calories < 0:
                print("Calories must be 0 or more.")
                continue
            calorie_amounts.append(calories) # Store the number
            break
        except ValueError:
            print("Invalid input. Please enter a number for calories.")


# Task 3: Calorie Calculations (Initial Setup) [cite: 35]

# Calculate Total Calories 
total_calories = sum(calorie_amounts)

# Calculate Average Calories 
# We must check the number of meals to avoid dividing by zero
if num_meals > 0:
    average_calories = total_calories / num_meals
else:
    average_calories = 0.0

# --- The remaining tasks (Task 4 & 5) will go here! ---