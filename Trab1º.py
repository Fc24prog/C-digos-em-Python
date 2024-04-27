import math
#Calcule as seguintes estatísticas para o conjunto de notas de uma
#determinada turma: máximo, mínimo, média e desvio padrão

t1 = [1.1, 7.5, 0.8, 1.8, 1.5, 1.9, 10.0, 10.0, 9.3, 10.0, 7.7, 0.6, 0.5,
8.7, 5.6, 7.0, 8.3, 7.0, 9.1, 7.4, 8.1, 7.0, 6.3, 0.6, 7.4, 2.8, 5.0, 1.4, 1.5, 0.5,
8.3, 7.0, 2.9, 7.6, 10.0, 3.3, 1.9, 5.1, 7.0]

# (Turma 1)

ct1= 0 #cont turma 1.
sm1=0 # o somatorio turma 1
max1= -8 # o maxímo da turma 1
min1 = 99999999 # o minimo da turma
smdv1=0  #soma do desvio padrão da turma 1 


for i in range (0,len(t1)):

    sm1=sm1+t1[i] # somatorio da turma 1
    ct1=ct1+1 # vai contar quantidade das notas que foram entradas
    md1=(sm1/ct1) # media da turma 1

# a maior e a menor nota:

    if t1[i]>max1:

        max1=t1[i]
        
    if t1[i]<min1 :

        min1=t1[i]
        
# desvio padrão 1 = raiz quadrada(somatorio(o valor do elemneto,logo o t1[i] - md1) elevado ao quadrado)

for i in range (0,len(t1)):
    
      c1=pow(sm1-md1) # c1= calculo 1 = vetor da turma 1 (menos) a media. 
      smdv1 = smdv1 + c1  # o somatorio do desvio padrao para ficar organizado
      dv1=math.sqrt(smdv1/ct1) # o calculo do desvio padrao 
        
print("A media eh", md1)
print("O valor maximo eh", max1)
print("O valor minimo eh", min1)
print("O valor do desvio padrao da turma 1 eh", dv1)


#Obs.: coloquei (**2) porque não estou conseguindo usar a função pow, toda vez que uso ela o meu programa trava (ah,eu importei bonitinho, mas não rolou)

    
    
