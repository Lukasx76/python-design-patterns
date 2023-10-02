"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código
"""

"""caso para exemplo: Uber tem vários tipos de veículo, criarei uma classe veículo que possui um método abstrato(dessa forma todas as especializações precisarão definir esse método) para buscar o cliente, depois vou criar mais 4 classes (especializações de veículo) e por fim vou criar uma factory que retorna qual especialização vai ser chamada"""
"""Essa é outra forma de projetar uma simple factory. Ao invés de retornar o objeto das classes especializadas nós retornamos a própria factory"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_customer(self) -> None:
        pass

class UberX(Vehicle):
    def get_customer(self) -> None:
        print("UberX is getting the client")

class UberXL(Vehicle):
    def get_customer(self) -> None:
        print("UberXL is getting the client")

class UberGreen(Vehicle):
    def get_customer(self) -> None:
        print("UberGreen is getting the client")

class UberSelect(Vehicle):
    def get_customer(self) -> None:
        print("UberSelect is getting the client")

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type : str) -> Vehicle:
        if vehicle_type == "uberx":
            return UberX()
        if vehicle_type == "uberxl":
            return UberXL()
        if vehicle_type == "ubergreen":
            return UberGreen()
        if vehicle_type == "uberselect":
            return UberSelect()
        assert 0, "Vehicle doesn't exist"
        
if __name__ == "__main__":
    from random import choice
    vehicle_categories = ["uberx", "uberxl", "ubergreen", "uberselect"]

    """ Irei instânciar a factory aleatoriamente 10 vezes"""
    for i in range(10):
        vehicle = VehicleFactory.get_vehicle(choice(vehicle_categories))
        vehicle.get_customer()


