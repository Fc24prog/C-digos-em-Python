import math

s=0

n=int(input("Entre com o valor de n: "))

for i in range(1,n):

    if(i%2==0):
        s=s-(1/i**2)
    else:
        s=s+(1/i**2)
        
res=math.sqrt(12*s)
print(res)








#Faça um programa que calcule o valor de PI pela soma dos n primeiros termos da
#série abaixo: raiz (12*1-1/4+1/9-1/16+1/25-1/36)
