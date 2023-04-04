"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

"""

string_input = input("Enter a string: ")

def main():
    reversed_string = string_input[::-1]
    print(reversed_string)
    return

main()