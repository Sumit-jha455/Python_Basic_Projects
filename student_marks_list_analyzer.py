# Student Marks List Analyzer

print("===== STUDENT MARKS LIST ANALYZER =====")

marks = []

number_of_students = int(input("Enter number of students: "))

if number_of_students <= 0:
    print("Number of students must be greater than 0.")

else:
    for i in range(number_of_students):
        mark = float(input(f"Enter marks for student {i + 1}: "))

        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print("Marks must be between 0 and 100.")
            break

    if len(marks) == number_of_students:
        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)

        passed_students = 0

        for mark in marks:
            if mark >= 40:
                passed_students += 1

        failed_students = len(marks) - passed_students

        print("\n----- MARKS ANALYSIS -----")
        print("Marks:", marks)
        print("Total Marks:", total)
        print("Average Marks:", round(average, 2))
        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)
        print("Passed Students:", passed_students)
        print("Failed Students:", failed_students)