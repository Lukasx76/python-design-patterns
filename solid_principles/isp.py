# Interface segregation principle: clients should not be forced to depend on methods they do not use

""" 
    example of bad practice, this is bad practice because older printer doesn't support the scan or fax methods
"""

from abc import ABC, abstractmethod

# class Printer(ABC):
#     @abstractmethod
#     def print(self, document):
#         pass

#     @abstractmethod
#     def fax(self, document):
#         pass

#     @abstractmethod
#     def scan(self, document):
#         pass

# class OldPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in black and white...")

#     def fax(self, document):
#         raise NotImplementedError("Fax functionality not supported")

#     def scan(self, document):
#         raise NotImplementedError("Scan functionality not supported")

# class ModernPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in color...")

#     def fax(self, document):
#         print(f"Faxing {document}...")

#     def scan(self, document):
#         print(f"Scanning {document}...")

"""
    example of good practice: to fix this we can separate the mandatory methods into individual classes with its due mandatory method
"""

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class ModernPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")