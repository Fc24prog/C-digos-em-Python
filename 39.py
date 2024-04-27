import math
e=0
x=float(input("Entre com o valor de x: "))
y=float(input("Entre com o valor de y: "))

for i in range (1,51):

    e= e+(x+math.sqrt(y+2))/3 + (i)**2 - (y)**5

print ("A equação e ",e )
