num=int(input("Entre com o numero: "))

primo=True

for i in range (2,num):
    if num%i==0:
        primo=False

if primo:

        print("O numero é primo: ")

else:

        print ("O numero nao é primo: ")




#5. Os números primos possuem várias aplicações dentro da Computação, por exemplo na
#Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um
#programa que peça um número inteiro e determine se ele é ou não um número primo.
