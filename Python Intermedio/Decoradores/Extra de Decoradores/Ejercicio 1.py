def repeat_twice(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_twice(2)
def say_hello(name):
    print(f"Hola, {name}")

def main():
    say_hello("Reaper")

if __name__ == "__main__":
    main()
