import datetime as dt
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        result = func(*args, **kwargs)
        args_str = ", ".join(str(arg) for arg in args)
        print(f"func:{func.__name__} - args: {args_str} - [{timestamp}] - Resultado: {result}")
        print(f"Resultado {result}")
        return result
    return wrapper

def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Argument {arg} is not a number.")
        return func(*args, **kwargs)
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

def main():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        try:
            result = multiply(a, b)
            print(f"Result of multiplying {a} and {b} is {result:.0f}")
        except ValueError as e:
            print(f"Error: {e}")

        break

if __name__ == "__main__":
    main()






