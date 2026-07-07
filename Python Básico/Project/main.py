print("Students Control System\n")

def main():
    import menu
    import data
    data.load_students_from_csv(data.CSV_FILE_PATH)
    while menu.menu():
        pass
    data.save_students_to_csv(data.CSV_FILE_PATH)

main()