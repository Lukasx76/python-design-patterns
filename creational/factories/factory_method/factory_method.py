"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

"""
Problema: A simple factory permite instânciar classes sem que o cliente precise chamar as classes diretamente, ao invés disso uma fábrica lida com o processo de criação de objetos. No entanto, ao criar objetos, é provável que nem todos os clientes tenham acesso as mesmas funcionalidades por exemplo: a Uber nos estados unidos oferece mais variedades de carros como o Green e o XL, que não existem no Brasil. Para resolver isso é necessário permitir que as subclasses decidam como a interface se comportará."""

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

# Ao tornar a VehicleFactory uma classe abstrata com o método get_vehicle sendo abstrato as subclasses terão mais flexibilidade ao implementar suas próprias funcionalidades
class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_vehicle(vehicle_type : str) -> Vehicle:
        pass

class VehicleFactoryUsa(ABC):
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

class VehicleFactoryBrazil(ABC):
    @staticmethod
    def get_vehicle(vehicle_type : str) -> Vehicle:
        if vehicle_type == "uberx":
            return UberX()
        assert 0, "Vehicle doesn't exist"        

if __name__ == "__main__":
    from random import choice
    vehicle_categories_usa = ["uberx", "uberxl", "ubergreen", "uberselect"]
    vehicle_categories_brazil = ["uberx"]

    print("Uber USA: \n")

    """ Irei instânciar a factory aleatoriamente 10 vezes"""
    for i in range(10):
        vehicle = VehicleFactoryUsa.get_vehicle(choice(vehicle_categories_usa))
        vehicle.get_customer()
    
    print()
    print("Uber Brazil: \n")

    for i in range(10):
        vehicle = VehicleFactoryBrazil.get_vehicle(choice(vehicle_categories_brazil))
        vehicle.get_customer()
