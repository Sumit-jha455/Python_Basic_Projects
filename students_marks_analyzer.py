# Students Marks Analyzer

print("===== STUDENTS MARKS ANALYZER =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))

marks = [maths, python, english, science, computer]

# Calculate total and average
total = sum(marks)
average = total / len(marks)

# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Pass/Fail
if all(mark >= 33 for mark in marks):
    result = "PASS"
else:
    result = "FAIL"

# Display report
print("\n===== MARKS REPORT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", grade)
print("Result:", result)

# Performance message
if average >= 90:
    print("Performance: Excellent")
elif average >= 75:
    print("Performance: Very Good")
elif average >= 60:
    print("Performance: Good")
elif average >= 50:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")