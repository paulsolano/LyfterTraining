import os

from actions import Student

CSV_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")

def save_students_to_csv(file_path, students):
    import csv
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['name', 'section', 'spanish_grade', 'english_grade', 'social_studies_grade', 'science_grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(vars(student))
    except Exception as e:
        print(f"An error occurred while saving the data to the CSV file: {e}")

def load_students_from_csv(file_path, students):
    import csv
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = Student(
                    row['name'],
                    row['section'],
                    float(row['spanish_grade']),
                    float(row['english_grade']),
                    float(row['social_studies_grade']),
                    float(row['science_grade'])
                )
                students.append(student)
    except FileNotFoundError:
        print(f"No existing data found at {file_path}. Starting with an empty student list.")
    except Exception as e:
        print(f"An error occurred while loading the data from the CSV file: {e}")