def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Parámetros: {args}")
        print(f"Retorno: {result}")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

@my_decorator
def add(a, b):
    return a + b

def main():
    say_hello()
    add(3, 5)

if __name__ == "__main__":
    main()