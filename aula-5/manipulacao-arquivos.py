#Ler um arquivo de texto:
#Crie um arquivo de texto no seu sistema com algumas linhas de conteúdo e escreva um código Python para abri-lo e exibir seu conteúdo.
arquivo = open("texto.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
#Escrever em um arquivo:
#Escreva um código Python para criar (ou sobrescrever) um arquivo de texto e inserir uma mensagem de sua escolha.
with open ("texto.txt","w")as arquivo:
    conteudo = arquivo.write("Paranguaricotirimiruaro. \n" "Não contavam com minha astúcia \n"  "Sigam-me os bons")

    
#Ler linha por linha:
#Modifique o código de leitura para ler o arquivo linha por linha.
with open ("texto.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    print(conteudo)

#Anexar conteúdo a um arquivo:
#Escreva um código que anexe uma nova linha de texto a um arquivo já existente.
with open ("texto.txt", "a") as arquivo:
    conteudo = arquivo.write("\n O rato roeu a roupa do rei de roma")

with open("texto.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)