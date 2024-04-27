res=input("Entre com a res do usuário: ")

cs=cn=cres=0

while (res!= 'f'):

    if (res=='s'):

        cs=cs+1

    if (res=='n'):

        cn=cn+1

    cres=cres+1
    
    cts=cs/cres

    ctn=cn/cres
    res=input("Entre com a res do usuário: ")

    
ps=(cts*100)
pn=(ctn*100)

print("a porcentagem dos que disseram sim é: ", ps)
print("a porcentagem dos que disseram não é: ", pn)

'''
13. Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber
se os consumidores estavam satisfeitos, para isso eles deveriam
responder sim “S” ou não “N”.
Crie um algoritmo que leia a resposta de todas as pessoas
e escreva a porcentagem dos que disseram sim e dos que disseram não.
Obs.: O final da leitura de dados é marcado pela resposta “F”.

'''
