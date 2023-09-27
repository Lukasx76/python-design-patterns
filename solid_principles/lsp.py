# liskov substitution principle, derivatives classes should be able to replace base classes entirely

"""
    example of bad practice
"""


class Sam:
    def bring_beverage(self):
        print("I am bringing you coffee")

class Eden(Sam):
    def bring_beverage(self):
        print("Sam is not here, so I am bringing you water")

# Eden should bring coffee

"""
    example of good practice
"""

class Peter:
    def make_sandwich(self):
        print("I am making you a fluffernutter")

class John(Peter):
    def make_sandwich(self):
        print("Peter is not here, but I can prepare a delicious fluffernutter to you")
