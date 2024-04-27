import math


a=int(input("Entre com o valor de a: "))

while a>0:
    b=int(input("Entre com o valor de b: "))
    c=int(input("Entre com o valor de C: "))
    d=math.sqrt((b**2)-4*a*c)
    print("O valor de deslta é: ",d)
    
    if (d<0):
        
        print("nao possui raizes reais: ")

    if(d==0):
        
        print("possui somente uma raiz real ")
        raiz1=(-b+d)/2*a
        raiz2=(-b-d)/2*a
        print("A raiz é: ",raiz1,raiz2)

    if(d>0):
        
        print("possui  duas raizes reais ")
        r1=(-b+d)/2*a
        r2=(-b-d)/2*a
        print("As raizes são: ",r1,r2)

    a=int(input("Entre com o valor de a: "))

    
'''
#12. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma: ax2 + bx + c
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário as
seguintes situações:
a) Se o usuário informar o valor de “a” igual a zero, a equação não é do segundo grau e
o programa não deve pedir os demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao
usuário e encerre o programa;

c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-
a ao usuário;

d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
