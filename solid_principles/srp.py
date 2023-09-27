# Single responsibility principle: a class should have a single responsibility

"""
    example of Bad practice
"""

class Worker:
    def paint(self):
        print("I am painting")
    def build(self):
        print("I am building")
    def drive(self):
        print("I am driving")

"""
   example Good practice
"""

class Painter:
    def paint(self):
        print("I am painting")
class Builder:
    def build(self):
        print("I am building")
class Driver:
    def drive(self):
        print("I am driving")