#mulheres
somaF=0
contF=0
maiorF=0
menorF=88888
#homens
somaH=0
contH=0
maiorH=0
menorH=999909999

for i in range (0,5):

    sx=input("Entre com o sexo: ")
    idade=int(input("Entre com a idade: "))


    if (sx=='f'):
        somaF=somaF+idade
        contF=contF+1

        if (idade<menorF):
            
            menorF=idade

        if (idade>maiorF):

            maiorF=idade

    if(sx=='m'): # não pode ser else aqui, porque vai pedir para ser embaixo do if  e vai mandar indentar tudo
                 # e como é outro sexo precisamos especificar ;;   
        
        somaH=somaH+idade
        contH=contH+1
        
        if (idade<menorH):
            
            menorH=idade

        if (idade>maiorH):

            maiorH=idade
            
mdF=(somaF/contF)
mdH=(somaH/contH)


print("A media das mulheres eh: ",mdF)
print("A media dos homens eh: ",mdH)
print("A idade da pessoa mais NOVA DAS mulheres eh: ",menorF)
print("A idade da pessoa mais velha DAS mulheres eh: ",maiorF)
print("A idade da pessoa mais NOVA dos homens eh: ",menorH)
print("A idade da pessoa mais velha dos homens eh: ",maiorH)



#Exercício (estatísticas):
#▪ Fazer um programa para ler o sexo ('M' ou 'F') e a idade de 20 pessoas.
#▪ Escrever a média de idades das mulheres e dos homens.
#▪ Escrever as idades da mulher e do homem mais velhos.
#▪ Escrever as idades da mulher e do homem mais novos.


        
        
        

        
    
