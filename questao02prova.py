pontuacao = 0
pgnt = ['Telefonou para a vítima?', 'Esteve no local do crime?','Mora perto da vítima?', 'Devia para a vítima?','Já trabalhou com a vítima?']

for pgnt in pgnt:
   print(pgnt)
   resposta = input('Informe sim ou não:  ').lower( ).replace( 'ã' , 'a' )
   if resposta == 'sim':
       pontuacao = pontuacao + 1

if pontuacao == 2:
 print('Essa pessoa é suspeita')

elif 3 <= pontuacao < 5:
 print('Essa pessoa é cúmplice.')

elif pontuacao == 5:
 print('Essa pessoa é assasino ou assassina.')

else:
 print('Essa pessoa é inocente.')
