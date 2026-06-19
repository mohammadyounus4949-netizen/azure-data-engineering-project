import csv
from datetime import date

EMPLOYEE_FILE = "employees.csv"
ATTENDANCE_FILE = "attendance.csv"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")

    with open(EMPLOYEE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name])

    print("Employee added successfully!")

def mark_attendance():
    emp_id = input("Enter Employee ID: ")

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, date.today(), "Present"])

    print("Attendance marked successfully!")

while True:
    print("\n1. Add Employee")
    print("2. Mark Attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
