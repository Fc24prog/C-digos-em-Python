somah=0
conth=0

nm=input("Entre com o nome: ")

while (nm!= 'fim'):

    sx=input ("Entre com o sexo da pessoa: ")
    n1=float(input("Entre com a nota 1: "))
    n2=float(input("Entre com a nota 2: "))

    md = (n1+n2)/2

    if (sx== "f"):
        print ("A media é: ",md)
        
    else:
        somah=somah+md
        conth=+1
        mdh = (somah/conth)
        
    nm=input("Entre com o nome: ")

print ("A media dos homens sao: ",mdh)

# Fazer um programa em PYTHON para ler o nome, 
#sexo e duas notas dos alunos de uma turma até que 
#seja digitado o nome FIM. Imprimir a média pessoal
#APENAS das alunas. Imprimir também a média
#aritmética dos homen
