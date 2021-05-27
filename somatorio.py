T = int (input())

soma = []

for t in range(T):
    valores = input().split(';')
    valores = [int(i) for i in valores]
    conta = sum([e for e in valores])
    soma.append(conta)

for i, valores in enumerate(soma):
    print(valores, end="" if i == len(soma)-1 else "\n")

