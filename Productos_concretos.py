from Producto import IDeportista

# Productos concretos
class Futbolista(IDeportista):
    def descripcion(self) -> str:
        return "Soy un futbolista."

class Tenista(IDeportista):
    def descripcion(self) -> str:
        return "Soy un tenista."

class Basquetbolista(IDeportista):
    def descripcion(self) -> str:
        return "Soy un basquetbolista."

class Voleybolista(IDeportista):
    def descripcion(self) -> str:
        return "Soy un voleybolista."