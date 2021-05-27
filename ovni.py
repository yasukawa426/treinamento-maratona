T = int (input())

for t in range(T):
    raios = input().split(" ")
    raios = [int(i) for i in raios]
    ovni1 = raios[0]
    ovni2 = raios[1]
    base = raios[2]

    if ((ovni1 * 2) + (ovni2 * 2)) <= base * 2:
        print("CABE!", end="" if t == T-1 else "\n")
    else:
        print("NAO CABE!", end="" if t == T-1 else "\n")