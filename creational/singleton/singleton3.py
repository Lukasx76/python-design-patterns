# criar um singleton com uma metaclasse

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Government(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        self.president = None


if __name__ == "__main__":
    france = Government()
    andorra = Government()

    andorra.president = "Some random guy"
    france.president = "Emanuel macron"

    print(france.president, andorra.president)
