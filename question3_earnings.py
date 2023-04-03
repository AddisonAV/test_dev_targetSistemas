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
