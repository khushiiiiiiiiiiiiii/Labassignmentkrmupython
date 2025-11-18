# ============================================================
# gradebook.py
# Author: Khushi Saini
# Date: 18-Nov-2025
# Title: GradeBook Analyzer
# ============================================================

import csv

print("===== Welcome to GradeBook Analyzer =====")
print("Choose input method:")
print("1. Manual Entry")
print("2. Load from CSV")

def get_data_manual():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks

def get_data_csv():
    marks = {}
    filename = input("Enter CSV file path: ")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) >= 2:
                marks[row[0]] = float(row[1])
    return marks

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    marks = get_data_manual()
elif choice == "2":
    marks = get_data_csv()
    print("\nData Loaded Successfully!")
    print(marks)
else:
    print("Wrong Input")

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    mid = n // 2
    if n % 2 == 0:
        return (scores[mid - 1] + scores[mid]) / 2
    else:
        return scores[mid]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

print("\n--- Statistics ---")
print(f"Average: {calculate_average(marks):.2f}")
print(f"Median: {calculate_median(marks):.2f}")
print(f"Highest: {find_max_score(marks)}")
print(f"Lowest: {find_min_score(marks)}")

def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

grades = assign_grades(marks)

distribution = {g: list(grades.values()).count(g) for g in ['A','B','C','D','F']}

print("\n--- Grade Distribution ---")
for grade, count in distribution.items():
    print(f"{grade}: {count} student(s)")

passed_students = [name for name, score in marks.items() if score >= 40]
failed_students = [name for name, score in marks.items() if score < 40]

print("\n--- Pass/Fail Summary ---")
print(f"Passed ({len(passed_students)}): {passed_students}")
print(f"Failed ({len(failed_students)}): {failed_students}")

def show_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    for name, marks in marks_dict.items():
        print(f"{name:<10}\t{marks:<6}\t{grades_dict[name]}")

while True:
    show_table(marks, grades)
    again = input("\nDo you want to analyze again? (y/n): ").lower()
    if again != 'y':
        print("Exiting GradeBook Analyzer. Goodbye!")
        break