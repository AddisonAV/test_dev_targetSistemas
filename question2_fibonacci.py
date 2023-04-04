"""
    2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
    escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence
    ou não a sequência.

        IMPORTANTE:
        Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""


number = int(input("Enter a number: "))

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

def main():
    fibonacci_index = 0
    fibonacci_number = fibonacci(fibonacci_index)
    while number > fibonacci_number or number == fibonacci_number:
        fibonacci_number = fibonacci(fibonacci_index)
        if number == fibonacci_number:
            print(f"The number {number} is part of the fibonacci sequence")
            return
        fibonacci_index += 1
    print(f"The number {number} is not part of the fibonacci sequence")

main()