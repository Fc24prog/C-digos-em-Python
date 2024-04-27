a=input("Telefonou para vitima? ")
b=input("Esteve no local do crime?  ")
c=input("Mora perto da vitima? ")
d=input("Devia para a vitima? ")
e=input("Já trabalhou com a vitima? ")

for pergunta in perguntas:

   print(pergunta)

   resposta = input('Responda sim ou não:  ')

   if resposta == 'sim':

       pontos +=1

if pontos == 2:

   print('Esta pessoa é suspeita...')

elif 3 <= pontos < 5:

   print('Esta pessoa é cúmplice!')

elif pontos == 5:

   print('Esta pessoa é a(o) assassina(o)!')

else:

   print('Esta pessoa é inocente.')

