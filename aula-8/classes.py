#Crie uma Classe Carro:

#Atributos: marca, modelo, ano.
#Método: exibir_informacoes (exibe os atributos do carro)

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_informacoes(self):
        print(F"O carro é da marca {self.marca}, modelo {self.modelo} e ano {self.ano}")

carro1 = Carro("Volkswagen", "Golf GTI", 2023)
carro2 = Carro("Tesla", "Model 3", 2024)
carro3 = Carro("Porche", "911 carrera S", 2022)
carro4 = Carro("Jeep", "Wrangles Rubicon", 2023)
carro5 = Carro("Toyota", "Corolla Cross Hybrid", 2023)

carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()


#Crie uma Classe Elétrica que herda de Carro:

#Atributo adicional: autonomia_bateria.

#Método adicional: mostrar_autonomia (exibe a autonomia da bateria).

class Eletrica(Carro):
    def __init__(self, marca, modelo, ano, autonomia_bateria):
        super().__init__(marca, modelo, ano)
        self.autonomia_bateria = autonomia_bateria

    def mostrar_autonomia(self):
         print(F"O carro é da marca {self.marca}, modelo {self.modelo} e ano {self.ano} com autonomia de bateria {self.autonomia_bateria}.")

carro1 = Eletrica("Volkswagen", "Golf GTI", 2023, 522)
carro2 = Eletrica("Tesla", "Model 3", 2024, 520)
carro3 = Eletrica("Porche", "911 carrera S", 2022, 422)
carro4 = Eletrica("Jeep", "Wrangles Rubicon", 2023, 483)
carro5 = Eletrica("Toyota", "Corolla Cross Hybrid", 2023, 481)


carro1.mostrar_autonomia()
carro2.mostrar_autonomia()
carro3.mostrar_autonomia()
carro4.mostrar_autonomia()
carro5.mostrar_autonomia()