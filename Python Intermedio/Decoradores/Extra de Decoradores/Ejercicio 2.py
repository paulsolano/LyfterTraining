def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("User must be logged in to access this function.")
        return func(*args, **kwargs)
    return wrapper

@requires_login
def protected_function():
    print("This is a protected function that requires login.")

@requires_login
def send_message(message):
    print(f"Sending message: {message}")

@requires_login
def change_settings(setting):
    print(f"Changing setting: {setting}")

def main():
    global user_logged_in
    user_logged_in = False

    while True:
        user_input = input("Enter 'login' to log in, or 'exit' to quit: ")
        if user_input == "login":
            user_logged_in = True
            print("You are now logged in.")
        elif user_input == "exit":
            break
        else:
            print("Invalid input. Please try again.")

    try:
        protected_function()
        send_message("Hello!")
        change_settings("dark mode")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()