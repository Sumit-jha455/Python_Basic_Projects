# Scholarship Eligibility System 🎓

A simple Python-based program that checks whether a student is eligible for a scholarship based on predefined eligibility criteria.

## 📌 Project Overview

The Scholarship Eligibility System takes student details as input and evaluates them against multiple scholarship requirements.

If all criteria are satisfied, the student is marked as **Eligible**. Otherwise, the program displays the reasons for ineligibility.

## ✨ Features

- Takes student name as input
- Checks student's age
- Checks family income
- Checks academic percentage
- Checks attendance percentage
- Displays scholarship eligibility status
- Shows specific reasons when the student is not eligible

## 🧠 Eligibility Criteria

A student is eligible when all of the following conditions are satisfied:

| Criteria | Requirement |
|---|---|
| Age | 25 years or below |
| Percentage | 75% or above |
| Attendance | 75% or above |
| Family Income | ₹3,00,000 or below |

## 🛠️ Technologies Used

- **Python 3**
- `input()`
- Conditional Statements (`if`, `else`)
- Lists
- `append()`
- `len()`
- f-strings
- Type Conversion

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:

```bash
git clone https://github.com/Sumit-jha455/Python_Basic_Projects.git

Navigate to the project directory:
cd Python_Basic_Projects
Run the program:
python scholarship_eligibility.py
💻 Sample Output
Eligible Student
Enter student name: Rahul
Enter age: 20
Enter family income: 200000
Enter percentage: 85
Enter attendance: 90

================================
SCHOLARSHIP ELIGIBILITY REPORT
================================
Student: Rahul
Status: ELIGIBLE
Reason: All criteria satisfied.
Not Eligible Student
Enter student name: Aman
Enter age: 27
Enter family income: 400000
Enter percentage: 68
Enter attendance: 70

================================
SCHOLARSHIP ELIGIBILITY REPORT
================================
Student: Aman
Status: NOT ELIGIBLE
Reasons:
- Age is above 25.
- Percentage below 75%.
- Attendance below 75%.
- Family income above ₹3,00,000.
📚 Concepts Practiced

This project was created to practice:

User Input
Variables
Data Types
Type Casting
Conditional Statements
Lists
if-else
Multiple Conditions
Basic Problem Solving
🚀 Future Improvements

Possible improvements for this project:

Add a graphical user interface (GUI)
Store student records
Add multiple scholarship categories
Add more eligibility criteria
Use functions for better code organization
Add database support

👨‍💻 Author

Sumit Kumar Jha