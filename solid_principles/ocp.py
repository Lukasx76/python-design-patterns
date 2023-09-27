# Open/closed principle: a class should be open to extension but closed to modification

"""
    example of bad practice
"""

class Worker:
    def __init__(self):
        ...
    def paint(self):
        print("I am painting")


class AnotherWorker(Worker):
    def __init__(self):
        ...
    def paint(self):
        print("Now I am cutting")

"""
    example of good practice
"""

class GoodWorker(Worker):
    def __init__(self):
        ...
    def cut(self):
        print("I am cutting, but I also can paint")

worker = GoodWorker()