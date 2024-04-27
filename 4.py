base=int(input("Entre com a base: "))
expo= int(input("Entre com o expoente: "))

# Nosso resultado vai ficar armazenado na variável potencia, que deve iniciar com valor 1.

pot= 1

#Temos que multiplicar a variável potencia por base, várias vezes.  Quantas vezes? expoente vezes!

for i in range (0,expo):

    pot=pot*base

print("a base e",base, "o expoente e",expo,"=",pot)


#4. Faça um programa que peça dois números, base e expoente, calcule o primeiro número elevado
#ao segundo número. Não utilize a função de potência (pow) nem o operando **.
