"""
    3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
        • O menor valor de faturamento ocorrido em um dia do mês;
        • O maior valor de faturamento ocorrido em um dia do mês;
        • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

    IMPORTANTE:
    a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
    b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""


import json

with open('dados.json', 'r') as f:
    data = json.load(f)

def main():
    lowest_earning = -1
    biggest_earning = -1
    average_earning = 0
    days_with_earning = 0
    for item in data:
        lowest_earning = item['valor'] if lowest_earning == -1 else lowest_earning
        biggest_earning = item['valor'] if biggest_earning == -1 else biggest_earning
        average_earning += item['valor']

        if item['valor'] < lowest_earning:
            lowest_earning = item['valor']
        if item['valor'] > biggest_earning:
            biggest_earning = item['valor']

    for item in data:
        if item['valor'] > (average_earning / len(data)):
            days_with_earning += 1
    
    print(f"Menor ganho: {lowest_earning}")
    print(f"Maior ganho: {biggest_earning}")
    print(f"Dias com ganho acima da média de ganho: {days_with_earning}")

main()
