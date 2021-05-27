T = int(input())
conjuntos = []

for t in range(T):
    notas = input().split(" ")
    notas = [int(i) for i in notas]
    notas.sort()
    conjuntos.append(notas)

for i, vetor in enumerate(conjuntos):
    print(str(vetor[0]) + " " + str(vetor[len(vetor)-1]))
    #se for o ultimo vetor
    if i == (len(conjuntos) - 1):
        if (any(vetor.count(x) > 1 for x in vetor)):
            print("S", end="")
        else: 
            print("N", end="")
    else:
        if (any(vetor.count(x) > 1 for x in vetor)):
            print("S")
        else: 
            print("N")
    


# for t in range(T):
#     notas = input().split(" ")
#     notas = [int(i) for i in notas]
#     notas.sort()
#     print(str(notas[0]) + " " + str(notas[len(notas)-1]))
#     print()
#     if (any(notas.count(x) > 1 for x in notas)):
#         print("S", end="")
#     else: 
#         print("N", end="")