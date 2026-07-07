import actions

def menu():
    user_input = input("\nWelcome to the Student Control System\nPlease select an option:\n1. Add student\n2. Show students\n3. Delete student\n4. Reports\n5. Exit\nSelect an option: ")
    if user_input == "1":
        actions.add_student()
    elif user_input == "2":
        actions.show_students()
    elif user_input == "3":
        actions.delete_student()
    elif user_input == "4":
        sub_menu()
    elif user_input == "5":
        print("Exiting the program...")
        return False
    else:
        print("Invalid option. Please try again.")
    return True

def sub_menu():
    user_input = input("\nPlease select an option:\n1. Show all students data\n2. Show top 3 students\n3. Show average grade per student\n4. Show all underage students\n5. Back to main menu\nSelect an option: ")
    if user_input == "1":
        actions.show_students()
    elif user_input == "2":
        actions.top_three_students()
    elif user_input == "3":
        actions.average_grade_per_student()
    elif user_input == "4":
        actions.underage_grade_per_student()
    elif user_input == "5":
        menu()
    else:
        print("Invalid option. Please try again.")

