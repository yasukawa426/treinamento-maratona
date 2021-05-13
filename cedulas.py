valor = int(input())
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

while valor >= 100:
    nota100 = nota100 + 1
    valor = valor - 100
while valor >= 50:
    nota50 = nota50 + 1
    valor = valor - 50
while valor >= 20:
    nota20 = nota20 + 1
    valor = valor - 20
while valor >= 10:
    nota10 = nota10 + 1
    valor = valor - 10
while valor >= 5:
    nota5 = nota5 + 1
    valor = valor - 5
while valor >= 2:
    nota2 = nota2 + 1
    valor = valor - 2
while valor >= 1:
    nota1 = nota1 + 1
    valor = valor - 1

print(str(nota100) + " nota(s) de R$ 100")
print(str(nota50) + " nota(s) de R$ 50")
print(str(nota20) + " nota(s) de R$ 20")
print(str(nota10) + " nota(s) de R$ 10")
print(str(nota5) + " nota(s) de R$ 5")
print(str(nota2) + " nota(s) de R$ 2")
print(str(nota1) + " nota(s) de R$ 1", end="")