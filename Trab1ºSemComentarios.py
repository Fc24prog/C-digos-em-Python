import math


t1 = [1.1, 7.5, 0.8, 1.8, 1.5, 1.9, 10.0, 10.0, 9.3, 10.0, 7.7, 0.6, 0.5,
8.7, 5.6, 7.0, 8.3, 7.0, 9.1, 7.4, 8.1, 7.0, 6.3, 0.6, 7.4, 2.8, 5.0, 1.4, 1.5, 0.5,
8.3, 7.0, 2.9, 7.6, 10.0, 3.3, 1.9, 5.1, 7.0]

# (Turma 1)

ct1= 0 
sm1=0 
max1= -8 
min1 = 99999999 
smdv1=0


for i in range (0,len(t1)):

    sm1=sm1+t1[i] 
    ct1=ct1+1 
    md1=(sm1/ct1) 

    if t1[i]>max1:

        max1=t1[i]
        
    if t1[i]<min1 :

        min1=t1[i]
        


for i in range (0,len(t1)):
    
      c1=(t1[i]-md1)**2  
      smdv1 = smdv1 + c1  
      dv1=math.sqrt(smdv1/ct1) 
        
print("A media da turma 1 eh", md1)
print("O valor maximo da tirma 1 eh", max1)
print("O valor minimo da turma 1 eh", min1)
print("O valor do desvio padrao da turma 1 eh", dv1)

# Turma 2:

t2 = [10.0, 8.2, 8.7, 5.5, 6.8, 8.6, 8.5, 6.1, 6.2, 8.5, 7.7, 10.0, 10.0,
6.1, 8.4, 5.4, 5.6, 9.8, 2.1, 8.5, 3.3, 8.7, 8.5, 9.1, 9.7]



ct2= 0 
sm2=0 
max2= -8 
min2 = 99999999 
smdv2=0


for i in range (0,len(t2)):

    sm2=sm2+t2[i] 
    ct2=ct2+1 
    md2=(sm2/ct2) 

    if t2[i]>max2:

        max2=t2[i]
        
    if t2[i]<min2 :

        min2=t2[i]
        


for i in range (0,len(t2)):
    
      c2=(t2[i]-md2)**2  
      smdv2 = smdv2 + c2  
      dv2=math.sqrt(smdv2/ct2) 
        
print("A media da turma 2 eh", md2)
print("O valor maximo da turma 2  eh", max2)
print("O valor minimo da turma 2 eh", min2)
print("O valor do desvio padrao da turma 2 eh", dv2)

