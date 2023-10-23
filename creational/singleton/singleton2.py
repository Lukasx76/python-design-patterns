def singleton(cls):
    instances = {}

    def instance():
        if cls not in instances:
            instances[cls] = cls()

        return instances[cls]
    return instance


@singleton
class Government(object):

    def __init__(self) -> None:
        self.attr = None
