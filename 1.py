n=int(input("Entre com a quantidade: "))
soma=0
maior =0
menor = 999999


for i in range (0,n):
    num=int(input("Entre com os numeros: "))


    if (num<menor):
        menor=num
        
    if (num>maior):
        maior=num

    soma = soma + i
print("O maior valor é: ",maior)
print("O menor valor é: ",menor)
print("A soma desses valores é: ",soma)

# Faça um programa que, dado um conjunto de N números,
#determine o menor valor, o maior valor e a soma dos valores.
