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