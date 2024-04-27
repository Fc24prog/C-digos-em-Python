#Fazer um algoritmo para ler a idade de uma pessoa
#e imprimir sua situação de acordo com os critérios
#abaixo:
#Idade <= 0 ➔ ERRO
#1 <= idade <= 3 ➔ BEBE
#4 <= idade <= 11 ➔ CRIANÇA
#12 <= idade <= 17 ➔ TEEN
#18 <= idade <= 30 ➔ JOVEM
#31 <= idade <= 64 ➔ ADULTO
#idade >= 65 ➔ SENIOr

id= int(input("Entre com a idade: "))

if id<=0:
    print("Erro")
else:

    if (1<=id<=3):
          print("Bebe")
    else:
        if (4<=id<=11):
            print("Criaça")

        else:
            if (12<=id<=17):
                print("Teen")

            else:
                     if (18<=id<=30):
                            print("Jovem")

                     else:
                               if (31<=id<=64):
                                     print("Adulto")

                               else :
                                           print("Senior")
