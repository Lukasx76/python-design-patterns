"""
    O Singleton é um padrão de projeto criacional que permite a você garantir que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância.

    fonte: https://refactoring.guru/pt-br/design-patterns/singleton
"""

"""
    Exemplo: O governo é um excelente exemplo de um padrão Singleton. Um país pode ter apenas um governo oficial. Independentemente das identidades pessoais dos indivíduos que formam governos, o título, “O Governo de X”, é um ponto de acesso global que identifica o grupo de pessoas no comando.

    fonte: https://refactoring.guru/pt-br/design-patterns/singleton
"""

class Government:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        
        return cls._instance
    
