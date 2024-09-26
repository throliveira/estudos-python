#Função de saudação:
#Crie uma função que receba o nome de uma pessoa e exiba uma saudação personalizada.
def saudacao(nome):
    print(f"Olá {nome}!")

saudacao("Thiago")

#Função de soma:
#Defina uma função que receba dois números e retorne a soma deles.
def soma(a,b):
    return a + b

print(soma(10,16))
#Função de contagem:
#Crie uma função que receba um número e exiba a contagem de 0 até o número fornecido.
def contagem(x):
    for i in range (x + 1):
        print(i)

contagem(10)

#Escopo Global e Local:
#Crie duas variáveis globais e use-as em uma função, mas dentro da função, defina variáveis locais com o mesmo nome e exiba a diferença entre os dois escopos.
a = 10
b = 11

def imprimir():
    a = 2
    b = 3
    print(a,b)

imprimir()
print(a,b)
