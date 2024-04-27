t=int(input("Entre com a quantidade : "))
maior = 0
menor=888888
soma=0
cont=0

for i in range(0,t):
    tem=float(input("Entre com a temperatura: "))


    if (tem<menor):
        menor=tem
        
    if (tem>maior):
        maior =tem

    soma=soma+tem
    cont=cont+1
    md=soma/cont

print("O maior valor é: ",maior)
print("O menor valor é: ",menor)
print("A media desses valores é: ",md)

        





#O Departamento Estadual de Meteorologia lhe contratou para
#desenvolver um programa que leia  um conjunto indeterminado
#de temperaturas, e informe ao final a menor e a maior temperatura
#informada, bem como a média das temperaturas.
