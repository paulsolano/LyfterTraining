import menu
from data import students

def get_valid_grade(subject):
    while True:
        raw_grade = input(f"Enter the student's {subject} grade: ")
        try:
            grade = float(raw_grade)
        except ValueError:
            print("Invalid grade. Please enter a number.")
            continue
        if grade < 0 or grade > 100:
            print("Invalid grade. Please enter a number between 0 and 100.")
            continue
        return grade

def valid_name(name):
    if not name.strip() or any(char.isdigit() for char in name):
        print("Invalid name. Please enter a non-empty name without numbers.")
        return False
    if any(student['name'].strip().lower() == name.strip().lower() for student in students):
        print("Invalid name. A student with this name already exists.")
        return False
    return True

def valid_section(section):
    if section not in ["10A", "10B", "10C"]:
        print("Invalid section. Please enter 10A, 10B, or 10C.")
        return False
    return True

def add_student():
    while True:
        name = input("Enter the student's complete name: ")
        if valid_name(name):
            break

    while True:
        section = input("Enter the student's section: ")
        if valid_section(section):
            break
    spanish_grade = get_valid_grade("Spanish")
    english_grade = get_valid_grade("English")
    social_studies_grade = get_valid_grade("Social Studies")
    science_grade = get_valid_grade("Science")
    student = {"name": name, "section": section, "spanish_grade": spanish_grade, "english_grade": english_grade, "social_studies_grade": social_studies_grade, "science_grade": science_grade}

    students.append(student)
    print(f"Student {name} from {section} added successfully.")


def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"Name: {student['name']}, Section: {student['section']}, Spanish: {student['spanish_grade']}, English: {student['english_grade']}, Social Studies: {student['social_studies_grade']}, Science: {student['science_grade']}")
        print("--------------------------------------------------")
    print("Students listed successfully.")

def top_three_students():
    if not students:
        print("No students found.")
        return

    sorted_students = sorted(students, key=lambda x: (x['spanish_grade'] + x['english_grade'] + x['social_studies_grade'] + x['science_grade']) / 4, reverse=True)
    top_students = sorted_students[:3]

    print("Top 3 Students:")
    for student in top_students:
        average_grade = (student['spanish_grade'] + student['english_grade'] + student['social_studies_grade'] + student['science_grade']) / 4
        print(f"Name: {student['name']}, Section: {student['section']}, Average Grade: {average_grade:.2f}")

def average_grade_per_student():
    if not students:
        print("No students found.")
        return

    total_grade = 0
    for student in students:
        average_grade = (student['spanish_grade'] + student['english_grade'] + student['social_studies_grade'] + student['science_grade']) / 4
        print(f"Name: {student['name']}, Section: {student['section']}, Average Grade: {average_grade:.2f}")
        total_grade += average_grade
    average = total_grade / len(students)
    
    print(f"Average Grade of All Students: {average:.2f}")

def underage_grade_per_student():
    if not students:
        print("No students found.")
        return

    for student in students:
        average_grade = (student['spanish_grade'] + student['english_grade'] + student['social_studies_grade'] + student['science_grade']) / 4
        if average_grade < 60:
            print(f"Name: {student['name']}, Section: {student['section']}, Average Grade: {average_grade:.2f} - Below Passing Grade")

def delete_student():
    name = input("Enter the complete name of the student AND the section to delete: ")
    section = input("Enter the section of the student to delete: ")
    for student in students:
        if student["name"] == name and student["section"] == section:
            while True:
                print(f"Do you want to delete {student['name']} from {student['section']}? (yes/no)")
                answer = input("Answer: ").lower()
                if answer == "yes":
                    students.remove(student)
                    print(f"Student {name} from {section} deleted successfully.")
                    return
                elif answer == "no":
                    print("Deletion canceled.")
                    return
    print(f"Student {name} from {section} not found.")

