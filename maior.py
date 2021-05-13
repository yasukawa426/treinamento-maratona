numeros = input().split(' ')

num1 = int(numeros[0])
num2 = int(numeros[1])
num3 = int(numeros[2])

maior1 = (num1 + num2 + abs(num1 - num2))// 2
maior2 = (num3 + maior1 + abs(maior1 - num3)) //2
print(maior2, end="")