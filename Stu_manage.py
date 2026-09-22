# Student Management System with Mark Analyzer

students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    marks = {}
    subjects = ["FSD", "ADT", "C&DS", "COD", "PYTHON"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def calculate_result(marks):
    total = sum(marks.values())
    average = total / len(marks)

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

    return total, average, grade


def display_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!")
        return

    student = students[roll_no]

    print("\n--- Student Details ---")
    print("Roll Number:", roll_no)
    print("Name:", student["name"])

    print("\nMarks:")
    for subject, mark in student["marks"].items():
        print(subject, ":", mark)

    total, average, grade = calculate_result(student["marks"])

    print("\nTotal:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


def display_all_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- All Students ---")

    for roll_no, student in students.items():
        total, average, grade = calculate_result(student["marks"])

        print(
            f"Roll No: {roll_no} | "
            f"Name: {student['name']} | "
            f"Total: {total} | "
            f"Average: {average:.2f} | "
            f"Grade: {grade}"
        )


def mark_analyser():
    if not students:
        print("No student records available.")
        return

    all_marks = []

    for student in students.values():
        all_marks.extend(student["marks"].values())

    highest = max(all_marks)
    lowest = min(all_marks)
    average = sum(all_marks) / len(all_marks)

    print("\n--- Mark Analysis ---")
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)
    print("Class Average:", round(average, 2))

    # Subject-wise analysis
    subjects = list(next(iter(students.values()))["marks"].keys())

    print("\nSubject-wise Average:")

    for subject in subjects:
        subject_marks = []

        for student in students.values():
            subject_marks.append(student["marks"][subject])

        subject_average = sum(subject_marks) / len(subject_marks)

        print(f"{subject}: {subject_average:.2f}")


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("\nStudent Found!")
        print("Name:", students[roll_no]["name"])
        print("Marks:", students[roll_no]["marks"])
    else:
        print("Student not found!")


# Main program
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Display All Students")
    print("4. Search Student")
    print("5. Mark Analyzer")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_student()

    elif choice == "3":
        display_all_students()

    elif choice == "4":
        search_student()

    elif choice == "5":
        mark_analyser()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
