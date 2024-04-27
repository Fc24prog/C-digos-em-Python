soma = 0
for i in range (1,6):

    a=int(input("Entre com o numero: "))

    dv=a*i
    soma=soma+dv
    final= soma//11
    r= soma%11
if(r==0 or r==1):
        
        v=r*0
        print("O digito verificador é:",v)

        
if(r!=0 or r!=1):
        v=11-r
        print("O digito verificador é:",v)

    
print(" A soma eh: ",soma)
print("A divisao eh: ",final)
print("O resto eh: ",r)




