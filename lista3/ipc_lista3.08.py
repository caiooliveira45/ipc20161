#professor Jucimar junior
#Ana Jessye 1615310046, 
#Franklin Yuri 1615310033,
#Kylciane Freitas 1615310032 
#Madson Lemos 1615310037
#IPC_Lista3.8

valida = 0

while (valida ==0 ):
    num1 = float(input("Informe o primeiro numero: \n"))
    num2 = float(input("Informe o segundo numero: \n"))
    num3 = float(input("Informe o terceiro numero: \n"))
    num4 = float(input("Informe o quarto numero: \n"))
    num5 = float(input("Informe o quinto numero: \n"))
    
    
    soma = (num1+num2+num3+num4+num5)
    media = (soma/5)
    
    print ("Soma: ",soma)
    print ("Media",media)
    valida = int(input("Quer tentar de novo? 0-Sim - 1-Nao: \n"))
