#Manipulação de Dicionários:

#Crie um dicionário representando um produto (com atributos como nome, preco e estoque).
copos = {
    "nome": "Super Feliz",
    "tamanho": "pequeno",
    "cor": "amarelo",
    "quantidade": 5
}
print(copos)
print(copos["cor"])
#Adicione uma chave categoria ao dicionário.
copos["preço"] = 50
#Remova a chave estoque e exiba o dicionário atualizado.
del copos["quantidade"]

print(copos)