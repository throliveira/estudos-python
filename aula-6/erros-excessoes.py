#Tratamento de exceções ao dividir por zero:
#Escreva um código que peça dois números ao usuário e exiba o resultado da divisão. Trate a exceção de divisão por zero.
def divisao(x,y):
    if y==0:
        raise ZeroDivisionError("Divisão por zero não dá queridinha!!!!!!")
    return x/y

try:
    resposta = divisao(10,0)
    print(resposta)
except ZeroDivisionError as z:
    print(z)

#Tratamento de exceções com leitura de arquivos:
#Modifique o código anterior de leitura de arquivos para tratar a exceção de arquivo não encontrado.
try:
    with open ("texto.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo não tá aqui mona. Se liga!")
else:
    print("Arrasou bicha! Arquivo babado lido com sucesso!")
finally:
    print("Hora de dar tchau!")
#Exceção personalizada:
#Crie uma função que simule a compra de um item, levantando uma exceção se o saldo for insuficiente.
class SaldoInsuficienteError(Exception):
    pass
def comprar_item(nome_item, preco_item, saldo_atual):
    if saldo_atual < preco_item:
        raise SaldoInsuficienteError("Saldo insuficiente para comprar o item!")
    else:
        print(f"Compra de {nome_item} realizada com sucesso!")
        print(f"Saldo atual: {saldo_atual - preco_item:.2f}")

try:
    comprar_item("laptop", 2000.0, 3000.0)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")