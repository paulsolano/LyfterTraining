def detect_prime_number(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

def test_detect_prime_number_with_small_prime():
    assert detect_prime_number(2) == True
    assert detect_prime_number(3) == True
    assert detect_prime_number(5) == True


def test_detect_prime_number_with_large_prime():
    assert detect_prime_number(13) == True
    assert detect_prime_number(19) == True
    assert detect_prime_number(97) == True


def test_detect_prime_number_with_non_prime():
    assert detect_prime_number(4) == False
    assert detect_prime_number(9) == False
    assert detect_prime_number(20) == False

def test_detect_prime_number_with_negative_numbers():
    assert detect_prime_number(-1) == False
    assert detect_prime_number(-2) == False
    assert detect_prime_number(-3) == False
    assert detect_prime_number(-4) == False
    assert detect_prime_number(-5) == False

def test_detect_prime_number_with_zero_and_one():
    assert detect_prime_number(0) == False
    assert detect_prime_number(1) == False

if __name__ == "__main__":
    print("Ejercicio 7 - Funciones")
    number = int(input("Cuantos numeros quieres ingresar: "))

    primes = []

    for i in range(number):
        num = int(input("Ingresa un numero: "))
        if detect_prime_number(num):
            primes.append(num)

    print("La lista de los numeros primos que ingresaste son: ", primes)
