#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gon�alves dos Santos - 1615310033

#Um vetor real X com n elementos � apresentado como resultado de um sistema de equa��es lineares Ax = B cujos coeficientes s�o representados em uma matriz real Amxn e os lados direitos das equa��es em um vetor real B de m elementos. Verificar se o vetor X � realmente solu��o do sistema dado.
 
from matriz import*  

matriz = []  
m = int(input("Digite o numero de linhas da matriz"))
n = int(input("Digite o numero de colunas da matriz"))
gerar_matriz(m,n)
mostrar_matriz(matriz, linhas)

print ("Vetor de resultados: ")
X = []
gerar_vetor(n)
print (X)

print ("Vetor de termos independentes: ")
B = []
gerar_vetor(n)
print(B)

print ("Multiplicacao do sistema")
R = []
multiplicacaovetor(matriz, X, B, R)
print(R)

print ("Verificacao de resultado")
verificar(matriz, R)