print("Students Control System\n")

def main():
    import menu
    import data

    students = []
    data.load_students_from_csv(data.CSV_FILE_PATH, students)

    while menu.menu(students):
        pass

    data.save_students_to_csv(data.CSV_FILE_PATH, students)


main()