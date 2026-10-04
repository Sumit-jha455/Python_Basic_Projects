# Student Management System

print("===== STUDENT MANAGEMENT SYSTEM =====")

students = {}


def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    students[roll_number] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("Student added successfully.")


def view_students():
    if len(students) == 0:
        print("No students found.")

    else:
        print("\n----- STUDENT LIST -----")

        for roll_number, student in students.items():
            print("Roll Number:", roll_number)
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("------------------------")


def search_student():
    roll_number = input("Enter roll number to search: ")

    if roll_number in students:
        student = students[roll_number]

        print("\n----- STUDENT DETAILS -----")
        print("Roll Number:", roll_number)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])

    else:
        print("Student not found.")


def update_student():
    roll_number = input("Enter roll number to update: ")

    if roll_number in students:
        student = students[roll_number]

        student["name"] = input("Enter new name: ")
        student["age"] = int(input("Enter new age: "))
        student["course"] = input("Enter new course: ")

        print("Student updated successfully.")

    else:
        print("Student not found.")


def delete_student():
    roll_number = input("Enter roll number to delete: ")

    if roll_number in students:
        del students[roll_number]
        print("Student deleted successfully.")

    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice. Please try again.")