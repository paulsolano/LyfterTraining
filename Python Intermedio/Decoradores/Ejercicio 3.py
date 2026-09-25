from datetime import date, datetime

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = datetime.now().date()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

def require_adult(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User must be at least 18 years old.")
        return func(user, *args, **kwargs)
    return wrapper

@require_adult
def greet(user):
    return f"Welcome! You are {user.age} years old."

def main():
    user1 = User(date_of_birth=date(2015, 5, 15))
    user2 = User(date_of_birth=date(2000, 12, 18))

    try:
        print(greet(user1))
    except ValueError as e:
        print(f"Error for user1: {e}")

    try:
        print(greet(user2))
    except ValueError as e:
        print(f"Error for user2: {e}")

if __name__ == "__main__":
    main()


