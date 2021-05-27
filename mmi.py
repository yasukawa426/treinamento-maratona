T = int(input())
conjuntos = []

for t in range(T):
    notas = input().split(" ")
    notas = [int(i) for i in notas]
    notas.sort()
    conjuntos.append(notas)

for i, vetor in enumerate(conjuntos):
    menorNota = vetor[0]
    maiorNota = vetor[len(vetor)-1]
    print(str(menorNota) + " " + str(maiorNota))
    if menorNota == maiorNota:
        print("S", end="" if i == len(vetor)-1 else "\n")
    else:
        print("N", end="" if i == len(vetor)-1 else "\n")  