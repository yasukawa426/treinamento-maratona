import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv
}

x = int(input())
op1 = input()
y = int(input())
op2 = input()
z = int(input())
resultado = 0

if op1 == "*" or op1 == "/":
    #print("x e y primeiro")

    if y == 0 and op1 == "/":
        print("erro",end="")
    elif z == 0 and op2 == "/":
        print("erro", end="")
    else:
        resultado = ops[op1](x,y)
        resultado = ops[op2](resultado,z)
        print(resultado, end="")


elif op2 == "*" or op2 == "/":
    #print ("y e z primeiro")
    
    if z == 0 and op2 == "/":
        print("erro", end="")
    else:
        resultado = ops[op2](y,z)
        resultado = ops[op1](x,resultado)
        print(resultado, end="")
        
    

#os dois operadores são mais ou menos
else:
    resultado = ops[op1](x,y)
    resultado = ops[op2](resultado,z)
    print(resultado, end="")