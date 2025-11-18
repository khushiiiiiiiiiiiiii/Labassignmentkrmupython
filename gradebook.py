## ============================================================
# Name          : Khushi Saini
# Project Title : Daily Calorie Tracker
# Date          : 18 October 2025
# ============================================================

print("===============================================")
print("   Welcome to the Daily Calorie Tracker CLI    ")
print("===============================================\n")

# Data Collection

meal_names = []
calorie_values = []

try:
    num_meals = int(input("Enter the amount of meals you want to enter "))
except ValueError:
    print("Invalid input, defaulting to 1 meal")
    num_meals = 1

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ").strip()
    try:
        calories = float(input("Enter calorie amount: "))
    except ValueError:
        print("Invalid calorie input, defaulting to 0 calories")
        calories = 0.0

    meal_names.append(meal)
    calorie_values.append(calories)

total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

try:
    daily_limit = float(input("\nEnter your daily calorie limit: "))
except ValueError:
    print("Invalid input, defaulting daily limit to 2000 calories.")
    daily_limit = 2000.0


if total_calories > daily_limit:
    status = "You have exceeded your daily calorie limit!"
else:
    status = "You are within your daily calorie limit."

# Printing

print("\n\n================= Daily Summary =================")
print(f"{'Meal Name':<20}{'Calories'}")
print("-------------------------------------------------")
for i in range(len(meal_names)):
    print(f"{meal_names[i]}\t\t{calorie_values[i]}")
print("-------------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("-------------------------------------------------")
print(status)
print("=================================================\n")