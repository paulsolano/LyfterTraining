print("Ejercicio 7 - Funciones")

def detect_prime_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False

        return True
    
number = int(input("Cuantos numeros quieres ingresar: "))

primes = []

for i in range(number):
    num = int(input("Ingresa un numero: "))
    if detect_prime_number(num):
        primes.append(num)
    
print("La lista de los numeros primos que ingresaste son: ", primes)

