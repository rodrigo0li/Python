def lanchonete(cod):
    cardapio = [(100,'Cachorro quente',8.50), (101,'Bauru', 9.90), (102, 'Hamburguer', 11.50), (103,'X-burguer', 13.00),(104, 'X-tudo', 15.00), (105, 'Refrigerante', 4.50)] 
    for l, lan, pr in cardapio:
        if l == cod:
           return lan, pr 
    return '',0.0
def imprimenota(ped):
    total = 0
    totalg = 0
    print('Sanduiche            Quantidade        VUnico       Total') 
    for (lan,qntda,pr) in pedido:
        total = qntda * pr 
        print(lan, (24 - len(lan))*' ', qntda, '           ', pr, '        ', total)
        totalg += total
    print('                                    total da Nota: ', totalg)         
pedido = []
cod = int(input('Informe aqui o código do cardápio ou -0 para fechar o pedido:'))
while cod != -0:
     lan, pr = lanchonete(cod)
     if lan != '':
        qntda = int(input('Informe aqui a quantidade:'))
        pedido.append((lan,qntda,pr)) 
     cod = int(input('Informe aqui o código do cardápio ou -0 para fechar o seu pedido:'))
imprimenota(pedido) 
