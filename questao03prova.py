numero = int(input("Digite aqui o número: "))
A = []
for i in range(numero):
    lado = []
    for b in range(numero):
        lado.append(int(input('Informe o valor aqui[' + str(i) + ',' + str(b) + ']:')))
    A.append(lado)
magic=0
for i in range(numero):
    magic =+ A[i][i]
soma=0
for i in range(numero):
    soma =+ A[i][numero-1-i]
if (soma != magic):
    print("Não é mágico!")
    exit()
for i in range(numero):
    soma=0
    for a in range(numero):
        soma=+A[i][b]
    if (soma != magic):
        print("Não é magico!")
        exit()
for b in range(numero):
    soma=0
    for i in range(numero):
        soma=+A[i][b]
    if (soma != magic):
        print("Não é magico!")
        exit()       
print("É magico!")
