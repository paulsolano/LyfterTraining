def number_validator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Argument {arg} is not a number.")
        return func(*args, **kwargs)
    return wrapper

@number_validator
def add(a, b):
    return a + b

@number_validator
def multiply(a, b):
    return a * b

def main():
    print(add(1, 2))
    print(multiply(3, 4))

    try:
        print(add(1, "two"))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
