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
min1 = 99999999 # o minimo da turma 1
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
    
      c1=(t1[i]-md1)**2 # c1= calculo 1 = vetor da turma 1 (menos) a media. 
      smdv1 = smdv1 + c1  # o somatorio do desvio padrao para ficar organizado
      dv1=math.sqrt(smdv1/ct1) # o calculo do desvio padrao dA turma 1
        
print("A media eh", md1)
print("O valor maximo eh", max1)
print("O valor minimo eh", min1)
print("O valor do desvio padrao da turma 1 eh", dv1)


# Turma 2:

t2 = [10.0, 8.2, 8.7, 5.5, 6.8, 8.6, 8.5, 6.1, 6.2, 8.5, 7.7, 10.0, 10.0,
6.1, 8.4, 5.4, 5.6, 9.8, 2.1, 8.5, 3.3, 8.7, 8.5, 9.1, 9.7]



ct2= 0   #cont turma 2.
sm2=0 # o somatorio turma 2
max2= -8  # o maxímo da turma 2
min2 = 99999999 # o minimo da turma 2
smdv2=0  #soma do desvio padrão da turma 2 


for i in range (0,len(t2)):

    sm2=sm2+t2[i]  # somatorio da turma 2
    ct2=ct2+1 # vai contar quantidade das notas que foram entradas
    md2=(sm2/ct2) # media da turma 2

    
# a maior e a menor nota da turma 2: 


    if t2[i]>max2:

        max2=t2[i]
        
    if t2[i]<min2 :

        min2=t2[i]
        
# desvio padrão da turma 2:

for i in range (0,len(t2)):
    
      c2=(t2[i]-md2)**2  # c2= calculo 2 = vetor da turma 2 (menos) a media. 
      smdv2 = smdv2 + c2  # vai contar quantidade das notas que foram entradas
      dv2=math.sqrt(smdv2/ct2) # desvio padrão da turma 2
      
print("A media da turma 2 eh", md2) 
print("O valor maximo da turma 2  eh", max2)
print("O valor minimo da turma 2 eh", min2)
print("O valor do desvio padrao da turma 2 eh", dv2)

#Obs.: coloquei (**2) porque não estou conseguindo usar a função pow, toda vez que uso ela o
#meu programa trava (ah,eu importei bonitinho, mas não rolou)

    
    
