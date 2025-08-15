"""
FizzBuzz game implementation.
Prints numbers from 1 to 50, replacing multiples of 3 with 'Fizz',
multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'.
"""

def fizzbuzz():
    """
    Función que implementa el juego FizzBuzz:
    - Si el número es divisible por 3, imprime "Fizz"
    - Si el número es divisible por 5, imprime "Buzz"
    - Si el número es divisible por ambos (3 y 5), imprime "FizzBuzz"
    - En caso contrario, imprime el número
    """
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()
