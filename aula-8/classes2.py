#Polimorfismo com classes de animais:

#Crie uma classe base Animal com um método fazer_som().
class Animal:
    def fazer_som(self):
        print("O animal está fazendo um som")

cachorro = Animal()

cachorro.fazer_som()


#Crie as subclasses Cachorro, Gato e Pássaro, cada uma sobrescrevendo o método fazer_som() para emitir um som específico.
class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro está latindo!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato está miando!")

class Passaro(Animal):
    def fazer_som(self):
        print("O pássaro está cantando!")

cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

cachorro.fazer_som()
gato.fazer_som()
passaro.fazer_som()

#Sobrescrever um método de exibição:

#Use a classe Carro do exercício anterior e sobrescreva o método exibir_informacoes na classe Eletrica, para incluir a autonomia da bateria ao exibir as informações.
from classes import Carro

class Eletrica(Carro):
    def __init__(self, marca, modelo, ano, autonomia_bateria):
        super().__init__(marca, modelo, ano)
        self.autonomia_bateria = autonomia_bateria

    def exibir_informacoes(self):
         print(f"O carro é da marca {self.marca}, modelo {self.modelo}, ano {self.ano}, com autonomia de {self.autonomia_bateria} km de bateria.")

carro1 = Eletrica("Volkswagen", "Golf GTI", 2023, 522)
carro2 = Eletrica("Tesla", "Model 3", 2024, 520)
carro3 = Eletrica("Porche", "911 carrera S", 2022, 422)
carro4 = Eletrica("Jeep", "Wrangles Rubicon", 2023, 483)
carro5 = Eletrica("Toyota", "Corolla Cross Hybrid", 2023, 481)


carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()