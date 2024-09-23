#Crie um arquivo fundamentos.py e adicione os seguintes exercícios:
#Crie variáveis para seu nome, idade e altura, e exiba-os na tela.
Nome = "Thiago Henrique"
Idade = 34
Altura = 1.73
print(Nome)
print(type(Nome))
print(Idade)
print(type(Idade))
print(Altura)
print(type(Altura))
#Faça uma função que receba dois números e retorne a soma deles.
def soma(a,b):
    return a+b

print (soma(2,3))
#Crie um laço for que exiba os números de 1 a 10.
for i in range(11):
    print(i)
#Faça um laço while que pare quando uma variável contadora atingir 10.
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
#Teste os conceitos de estruturas condicionais:
if Idade >= 18:
    print("Voce é maior de idade!")
else:
    print("Você é menor de idade!")
#Escreva um código que verifique se um número é par ou ímpar e imprima o resultado.
numero = 4
if numero%2==0:
    print('Número par')
else:
    print('Número ímpar')