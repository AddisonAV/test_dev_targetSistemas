"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

    SP - R$67.836,43
    RJ - R$36.678,66
    MG - R$29.229,88
    ES - R$27.165,48
    Outros - R$19.849,53

    Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

"""

SP = float(67836.43)
RJ = float(36678.66)
MG = float(29229.88)
ES = float(27165.48)
Outros = float(19849.53)

def main():
    total = SP + RJ + MG + ES + Outros

    print(f"Representação percentual por estado:")
    print(f"SP: {round(SP / total * 100, 2)}%")
    print(f"RJ: {round(RJ / total * 100,2)}%")
    print(f"MG: {round(MG / total * 100,2)}%")
    print(f"ES: {round(ES / total * 100,2)}%")
    print(f"Outros: {round(Outros / total * 100, 2)}%")
    print(f"Total: R$ {total} ")

main()