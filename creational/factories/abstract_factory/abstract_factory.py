"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""

from abc import ABC, abstractmethod

class XVehicle(ABC):
    @abstractmethod
    def get_customer(self) -> None:
        pass

class OtherVehicle(ABC):
    @abstractmethod
    def get_customer(self) -> None:
        pass

class UberXUSA(XVehicle):
    def get_customer(self) -> None:
        print("UberX USA is getting the client")

class UberXLUSA(XVehicle):
    def get_customer(self) -> None:
        print("UberXL USA is getting the client")

class UberGreenUSA(OtherVehicle):
    def get_customer(self) -> None:
        print("UberGreen USA is getting the client")

class UberSelectUSA(OtherVehicle):
    def get_customer(self) -> None:
        print("UberSelect USA is getting the client")
class UberXBrazil(XVehicle):
    def get_customer(self) -> None:
        print("UberX Brazil is getting the client")

class UberXLBrazil(XVehicle):
    def get_customer(self) -> None:
        print("UberXL Brazil is getting the client")

class UberGreenBrazil(OtherVehicle):
    def get_customer(self) -> None:
        print("UberGreen Brazil is getting the client")

class UberSelectBrazil(OtherVehicle):
    def get_customer(self) -> None:
        print("UberSelect Brazil is getting the client")

# Ao tornar a VehicleFactory uma classe abstrata com o método get_vehicle sendo abstrato as subclasses terão mais flexibilidade ao implementar suas próprias funcionalidades
class VehicleFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_xvehicle(vehicle_type : str) -> XVehicle:
        pass
    
    @staticmethod
    @abstractmethod
    def get_xlvehicle(vehicle_type : str) -> XVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_greenvehicle(vehicle_type : str) -> OtherVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_selectvehicle(vehicle_type : str) -> OtherVehicle:
        pass


class VehicleFactoryUsa(VehicleFactory):
    @staticmethod
    def get_xvehicle() -> XVehicle:
        return UberXUSA()
    
    @staticmethod
    def get_xlvehicle() -> XVehicle:
        return UberXLUSA()

    @staticmethod
    def get_greenvehicle() -> OtherVehicle:
        return UberGreenUSA()

    @staticmethod
    def get_selectvehicle() -> OtherVehicle:
        return UberSelectUSA()
    

class VehicleFactoryBrazil(ABC):
    @staticmethod
    def get_xvehicle() -> XVehicle:
        return UberXBrazil()
    
    @staticmethod
    def get_xlvehicle() -> XVehicle:
        return UberXLBrazil()

    @staticmethod
    def get_greenvehicle() -> OtherVehicle:
        return UberGreenBrazil()

    @staticmethod
    def get_selectvehicle() -> OtherVehicle:
        return UberSelectBrazil()   

class Client:
    def get_clients(self) -> None:
        for factory in [VehicleFactoryUsa(), VehicleFactoryBrazil()]:
            uberX = factory.get_xvehicle()
            uberX.get_customer()

            uberXl = factory.get_xlvehicle()
            uberXl.get_customer()
            
            uberGreen = factory.get_greenvehicle()
            uberGreen.get_customer()

            uberSelect = factory.get_selectvehicle()
            uberSelect.get_customer()   

if __name__ == "__main__":
    client = Client()
    client.get_clients()